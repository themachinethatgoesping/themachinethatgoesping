#!/bin/env python3

import os
import sys
import subprocess

# import argparse
# parser = argparse.ArgumentParser()
# parser.add_argument("--meson_file_path", help="meson.build file path to modify and glob", action="store_true")
# parser.add_argument("--sources_endings", help="List of endings for the sources variable", action="store_true")
# parser.add_argument("--headers_endings", help="List of endings for the headers variable", action="store_true")
# args = parser.parse_args()

# MESON_FILE_PATH = args.meson_file_path
# BASE_PATH = os.path.split(MESON_FILE_PATH)[0]
# src_endings = args.sources_endings
# header_endings = args.headers_endings

subproject_list = [
    "subprojects/meta",
    "subprojects/tools",
    "subprojects/navigation",
    "subprojects/algorithms",
    "subprojects/echosounders",
    "subprojects/pingprocessing",
    #"subprojects/gridding",
]

path_mkdoc = []
for r,d,f in os.walk('../'):

    for sp in subproject_list:
        if sp in r:
            break
    else:
        continue

    # skip subprojects of subprojects
    if r.count('subprojects') == 2:
        continue

    if 'stubs' in r:
        continue

    if not 'meson.build' in f:
        continue

    if not 'python' in r:
        continue

    meson_file_path = os.path.join(r,"meson.build")
    base_path = r

    #extract the sources and headers variables
    old_sources = ""
    old_headers = ""
    with open(meson_file_path, "r") as meson_file:
        src_string = ""
        append_src = ""
        for line in meson_file:
            if "sources = [" in line:
                append_src = "src"
            if "headers = [" in line:
                append_src = "headers"
                
            if append_src:
                src_string += line
                if "]" in line:

                    if append_src == "src":
                        old_sources = src_string
                    else:
                        old_headers = src_string

                    append_src = ""
                    break

    new_sources=""
    new_headers=""
    last_subfolder = ""
    if 'python' in r:
        new_sources = "sources = ["
        prnt=True

        for r_,d_,f_ in os.walk(r):
            for file in f_:
                if file.endswith('.py'):
                    break
            else:
                continue

            for file in sorted(f_):
                if file.endswith('.py'):
                    p = os.path.join(r_,file)
                    p = p.split(r)[1]
                    if p.startswith('/'):
                        p = p[1:]

                    if p.startswith('themachinethatgoesping/'):   
                        file_path = f"  '{p}',\n"
                        
                        folder_path = file_path.split('/')
                        if len(folder_path) > 4:
                            folder_path = folder_path[:4]
                        folder_path = folder_path[:-1]
                        folder_path = "/".join(folder_path)

                        if last_subfolder != folder_path:
                            last_subfolder = folder_path
                            new_sources += "\n"
                            
                        new_sources += file_path
        new_sources += "]\n"
                

    if new_sources != old_sources:
        old_out = ""
        out = ""
        with open(meson_file_path, "r") as meson_file:
            append_src = ""
            for line in meson_file:
                if "sources = [" in line:
                    append_src = "src"
                if "headers = [" in line:
                    append_src = "headers"
                        
                if append_src:
                    if "]" in line:
                        if append_src == "src":
                            out += new_sources
                        if append_src == "headers":
                            out += new_headers
                        append_src = ""
                else:
                    out += line
                old_out += line
                        
        # print(old_out)
        # print("\n\NEW FILE\n\n")
        # print(out)
        with open(meson_file_path, "w") as meson_file:
            meson_file.write(out)
        print(f"Updated {meson_file_path}")
        
