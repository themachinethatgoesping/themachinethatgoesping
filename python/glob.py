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
    "subprojects/gridding",
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

    if (not 'python' in r) and (not 'src' in r):
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
                    continue

    new_sources="sources = [\n"
    new_headers="headers = [\n"
    python_files = []
    header_files = []
    source_files = []

    for r_,d_,f_ in os.walk(r):
        for file in f_:
            if file.endswith('.py') or file.endswith('.cpp') or file.endswith('.hpp') or file.endswith('.h') :
                break
        else:
            continue

        for file in sorted(f_):
            file = os.path.join(r_,file)
            file = file.split(r)[1]
            if file.startswith('/'):
                file = file[1:]

            if file.endswith('.py'):
                if file.startswith('themachinethatgoesping/'):   
                    python_files.append(file)
            if file.endswith('.hpp') or file.endswith('.h'):
                header_files.append(file)
            if file.endswith('.cpp'):
                source_files.append(file)
                
    def append_sources(files, source_string):
        last_subfolder = ""
        for file in files:                
            source_string += f"  '{file}',\n"
        return source_string + ']\n'

    if 'python' in r:
        new_sources = append_sources(python_files, new_sources)
    if 'src' in r:
        new_sources = append_sources(source_files, new_sources)
        new_headers = append_sources(header_files, new_headers)
                

    if (old_sources and (new_sources != old_sources) or (old_headers and (new_headers != old_headers))):
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
                        
        # print("\n\NEW FILE\n\n")
        # print(out)
        if True:
            with open(meson_file_path, "w") as meson_file:
                meson_file.write(out)
        print(f"Updated {meson_file_path}")
        #break
        
