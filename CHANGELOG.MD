# Changelog

Ping is still in the bootstrapping phase, thus changes will be frequent and not always documented. 
Once the project is more stable, this changelog will be updated more frequently.

Versioning scheme is currently based on my mood, but will be changed to [Semantic Versioning](https://semver.org/) once the project is more stable. I do not create tags for the versions as none of them are stable enough to be considered a release.


---


## [Unreleased]

### Modules

- tools -> 0.21.4

### Update subproject wraps

- tools:[magic_enum] -> 0.9.5

## [0.13.0] - 2023-11-15

### Modules

- echosounders -> 0.30.0

### Breaking

- echosounders: Namespace and file renaming
  - em3000 -> kongsbergall
  - simrad -> simradraw
  - InputFile -> InputFileHandler
  - FileEm3000 -> KongsbergAllFileHandler
  - FileSimradRaw -> SimradRawFileHandler
  - simradraw_datagrams.hpp -> datagrams.hpp
  - simradraw_types.hpp -> types.hpp
  - kongsbergall_datagrams.hpp -> datagrams.hpp
  - kongsbergall_types.hpp -> types.hpp


### Update subproject wraps

- tools:[fast_float] -> 0.5.3
- tools:[magic_enum] -> 0.9.4
- tools:[xsimd]      -> 0.11.2


## [0.12.4] - 2023-11-15

- started change log


---


# Notes

The datum format used is [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) (YYYY-MM-DD).

We use the following tags based on [keepachangelog.com](https://keepachangelog.com/en/1.1.0/):

### Breaking
- `Breaking` for changes that will break existing functionality.

### Added
- `Added` for new features.

### Changed
- `Changed` for changes in existing functionality.

### Deprecated
- `Deprecated` for soon-to-be removed features.

### Removed
- `Removed` for now removed features.

### Fixed
- `Fixed` for any bug fixes.

### Security
- `Security` in case of vulnerabilities.