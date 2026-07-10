#!/usr/bin/env python3
import argparse
import datetime as dt
import re
import subprocess
import sys
from dataclasses import dataclass
from typing import Dict, List, Optional, Set, Tuple

import requests
from packaging.version import Version, InvalidVersion

PYPI_JSON = "https://pypi.org/pypi/{project}/json"


@dataclass(frozen=True)
class ReleaseInfo:
    version_str: str
    version_obj: Version
    files: List[dict]
    newest_upload: dt.datetime


def parse_args():
    p = argparse.ArgumentParser(
        description=(
            "Purge PyPI releases while keeping only the latest stable patch "
            "for each major.minor series."
        )
    )
    p.add_argument("--project", required=True, help="PyPI project name")
    p.add_argument(
        "--older-than-days",
        type=int,
        default=None,
        help=(
            "Only purge releases whose newest uploaded file is older than this many days"
        ),
    )
    p.add_argument(
        "--delete-prereleases",
        action="store_true",
        help="Also purge all prereleases (still honoring --older-than-days)",
    )
    p.add_argument(
        "--delete-stable-subreleases",
        action="store_true",
        help=(
            "Delete non-latest stable patch releases within each major.minor line. "
            "If not set, stable subreleases are kept."
        ),
    )
    p.add_argument(
        "--delete-below-version",
        default=None,
        help=(
            "Delete any release with version strictly smaller than this threshold "
            "(PEP 440 comparison), e.g. 0.30.3"
        ),
    )
    p.add_argument(
        "--max-delete",
        type=int,
        default=None,
        help="Safety guard: fail if more than this many releases would be purged",
    )
    p.add_argument(
        "--execute",
        action="store_true",
        help="Actually delete releases using pypi-cleanup (default is report/query only)",
    )
    p.add_argument(
        "--run-pypi-cleanup",
        action="store_true",
        help="Run pypi-cleanup with the computed regex (default is print command only)",
    )
    p.add_argument(
        "--username",
        default=None,
        help=(
            "PyPI username for pypi-cleanup login. If omitted, pypi-cleanup's own "
            "defaults are used (e.g. ~/.pypirc)."
        ),
    )
    p.add_argument(
        "--pypi-host",
        default="https://pypi.org/",
        help="Host passed to pypi-cleanup (e.g. https://test.pypi.org/)",
    )
    p.add_argument(
        "--python-tag-prefix",
        default=None,
        help=(
            "Optional extra regex prefix to restrict versions before exact matching. "
            "Mostly useful for advanced workflows."
        ),
    )
    return p.parse_args()


def load_releases(project: str) -> Dict[str, List[dict]]:
    r = requests.get(PYPI_JSON.format(project=project), timeout=30)
    r.raise_for_status()
    return r.json().get("releases", {})


def newest_upload_time(files: List[dict]) -> dt.datetime:
    times = []
    for f in files:
        s = f.get("upload_time_iso_8601")
        if s:
            times.append(dt.datetime.fromisoformat(s.replace("Z", "+00:00")))
    return max(times) if times else dt.datetime.fromtimestamp(0, tz=dt.timezone.utc)


def version_obj(v: str):
    try:
        return Version(v)
    except InvalidVersion:
        return None


def build_release_infos(releases: Dict[str, List[dict]]) -> Tuple[List[ReleaseInfo], List[str]]:
    infos: List[ReleaseInfo] = []
    invalid_versions: List[str] = []
    for v, files in releases.items():
        if not files:
            continue
        vo = version_obj(v)
        if vo is None:
            invalid_versions.append(v)
            continue
        infos.append(
            ReleaseInfo(
                version_str=v,
                version_obj=vo,
                files=files,
                newest_upload=newest_upload_time(files),
            )
        )
    return infos, sorted(invalid_versions)


def keep_latest_stable_per_minor(infos: List[ReleaseInfo]) -> Set[str]:
    keep: Dict[Tuple[int, int], ReleaseInfo] = {}
    for info in infos:
        vo = info.version_obj
        if vo.is_prerelease:
            continue
        if len(vo.release) < 2:
            # Not a conventional major.minor.patch series. Keep by default.
            continue
        key = (vo.release[0], vo.release[1])
        current = keep.get(key)
        if current is None or vo > current.version_obj:
            keep[key] = info
    return {x.version_str for x in keep.values()}


def collect_candidates(
    infos: List[ReleaseInfo],
    stable_keep_set: Set[str],
    delete_prereleases: bool,
    delete_stable_subreleases: bool,
    delete_below_version: Optional[Version],
    older_than_days: Optional[int],
) -> List[Tuple[ReleaseInfo, str]]:
    now = dt.datetime.now(dt.timezone.utc)
    out: List[Tuple[ReleaseInfo, str]] = []

    for info in sorted(infos, key=lambda x: x.version_obj):
        is_prerelease = info.version_obj.is_prerelease
        age_days = (now - info.newest_upload).days
        reason: Optional[str] = None

        if delete_below_version is not None and info.version_obj < delete_below_version:
            reason = f"below_{delete_below_version}"
        elif info.version_str in stable_keep_set:
            continue
        elif is_prerelease and delete_prereleases:
            reason = "prerelease"
        elif not is_prerelease and delete_stable_subreleases:
            reason = "non_latest_patch_for_minor"

        if reason and older_than_days is not None and age_days <= older_than_days:
            reason = None
        elif reason and older_than_days is not None:
            reason = f"older_than_{older_than_days}_days"

        if reason:
            out.append((info, reason))

    return out


def build_exact_version_regex(versions: List[str], python_tag_prefix: Optional[str]) -> str:
    escaped = [re.escape(v) for v in sorted(versions)]
    body = "|".join(escaped)
    if python_tag_prefix:
        return rf"{python_tag_prefix}(?:{body})$"
    return rf"^(?:{body})$"


def build_cleanup_command(
    project: str,
    regex: str,
    execute: bool,
    username: Optional[str],
    host: str,
) -> List[str]:
    # pypi-cleanup uses interactive web login (password/TOTP), not upload API tokens.
    cmd = [
        "pypi-cleanup",
        "-p",
        project,
        "-r",
        regex,
        "-t",
        host,
    ]
    if username:
        cmd.extend(["-u", username])
    if execute:
        cmd.extend(["-y", "--do-it"])
    else:
        cmd.append("--query-only")
    return cmd


def maybe_run_cleanup(cmd: List[str], run_pypi_cleanup: bool):
    print(">", " ".join(cmd))
    if run_pypi_cleanup:
        try:
            subprocess.run(cmd, check=True)
        except subprocess.CalledProcessError as e:
            print(
                (
                    "pypi-cleanup failed. PyPI may be refusing deletion for one or more "
                    "matched releases (for example, if the delete form is unavailable)."
                ),
                file=sys.stderr,
            )
            if "No CSFR found" in str(e):
                print(
                    (
                        "Detected 'No CSFR found' from pypi-cleanup. This usually means "
                        "the release delete page did not expose a deletable form. "
                        "Try narrower filters (for example --delete-prereleases only) "
                        "or use yanking for non-deletable stable releases."
                    ),
                    file=sys.stderr,
                )
            raise


def main():
    args = parse_args()

    delete_below_version: Optional[Version] = None
    if args.delete_below_version:
        try:
            delete_below_version = Version(args.delete_below_version)
        except InvalidVersion:
            print(
                f"Invalid --delete-below-version: {args.delete_below_version}",
                file=sys.stderr,
            )
            sys.exit(2)

    releases = load_releases(args.project)
    infos, invalid_versions = build_release_infos(releases)
    stable_keep_set = keep_latest_stable_per_minor(infos)

    candidates = collect_candidates(
        infos=infos,
        stable_keep_set=stable_keep_set,
        delete_prereleases=args.delete_prereleases,
        delete_stable_subreleases=args.delete_stable_subreleases,
        delete_below_version=delete_below_version,
        older_than_days=args.older_than_days,
    )

    if args.max_delete is not None and len(candidates) > args.max_delete:
        print(
            (
                f"Refusing to continue: computed {len(candidates)} purge candidates, "
                f"which exceeds --max-delete={args.max_delete}."
            ),
            file=sys.stderr,
        )
        sys.exit(3)

    if not candidates:
        print("No matching releases to purge.")
        if invalid_versions:
            print(
                (
                    "Note: skipped unparseable versions: "
                    + ", ".join(invalid_versions)
                )
            )
        return

    print(f"Project: {args.project}")
    print(f"Parsed releases: {len(infos)}")
    print(f"Stable keep-set size (latest patch per major.minor): {len(stable_keep_set)}")
    print(f"Delete stable subreleases: {args.delete_stable_subreleases}")
    print(f"Delete prereleases: {args.delete_prereleases}")
    if delete_below_version is not None:
        print(f"Delete any version below: {delete_below_version}")
    if invalid_versions:
        print(f"Skipped unparseable versions: {', '.join(invalid_versions)}")

    print(f"Found {len(candidates)} versions to purge:")
    purge_versions: List[str] = []
    for info, reason in candidates:
        purge_versions.append(info.version_str)
        print(
            (
                f"  - {info.version_str:20} files={len(info.files):2d} "
                f"newest={info.newest_upload.isoformat()} reason={reason}"
            )
        )

    print("\nKeeping latest stable patch per minor:")
    for v in sorted(stable_keep_set, key=Version):
        print(f"  + {v}")

    regex = build_exact_version_regex(purge_versions, args.python_tag_prefix)
    cmd = build_cleanup_command(
        project=args.project,
        regex=regex,
        execute=args.execute,
        username=args.username,
        host=args.pypi_host,
    )

    print("\nCommand:")
    maybe_run_cleanup(cmd, args.run_pypi_cleanup)

    if args.execute and not args.run_pypi_cleanup:
        print(
            (
                "\nExecution requested but command was not run because "
                "--run-pypi-cleanup was not set."
            )
        )

if __name__ == "__main__":
    main()


