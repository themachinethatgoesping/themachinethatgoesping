#!/usr/bin/env python3

import os
from collections import defaultdict

dirs = [
    "subprojects/tools/python/",
    "subprojects/tools/src/",
    "subprojects/echosounders/python/",
    "subprojects/echosounders/src/",
    "subprojects/navigation/python/",
    "subprojects/navigation/src/",
    "subprojects/meta/python/",
    "subprojects/meta/src/",
    "subprojects/gridding/python/",
    "subprojects/gridding/src/",
    ]

ignore_dirs = [
    ".mypy_cache",
    "__pycache__",
    "nogit"
    ]

lines = 0
files = 0
text_ext="txt cpp h hpp build py"
extensions = defaultdict(int)
lines_ext  = defaultdict(int)
for src_dir in dirs:
    for r,d,f in os.walk(src_dir):
        cont = False
        for idir in ignore_dirs:
            if idir in r:
                cont = True
        if cont:
            continue

        print(r)
        for file in f:
            ext = file.split(".")[-1]
            file = r + "/" + file
            files += 1

            extensions[ext] +=1

            if ext in text_ext:
                with open(file,"r") as infile:
                    for line in infile:
                        if line.strip():
                            lines +=1
                            lines_ext[ext] += 1

print("--- files ---")
for k,v in extensions.items():
    print(".{}:\t{}".format(k,v))
print("---")
print("files:",files)
print()
print("--- lines ---")
for k,v in lines_ext.items():
    print(".{}:\t{}".format(k,v))
print("---")
print("lines:",lines)

input('Press enter to continue: ')
        
