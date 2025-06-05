#!/bin/env python3

import os
import sys
import subprocess

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--regenerate", help="Regenerate all docstrings", action="store_true")
parser.add_argument("--renew", help="Delete all docstring folders first", action="store_true")
args = parser.parse_args()

FORCE_REGENERATE = args.regenerate
FORCE_RENEW = args.renew

# FORCE_RENEW = False
# FORCE_REGENERATE = False

more_args = []
if FORCE_REGENERATE: more_args.append("--regenerate")
if FORCE_RENEW: more_args.append("--renew")

path_mkdoc = []
for r,d,f in os.walk('../'):

    # skip subprojects of subprojects
    if r.count('subprojects') == 2:
        continue
    
    if 'output' in r:
        continue
    if 'build' in r:
        continue
    
    for file in f:
        if file == "mkdoc.py":
            path_mkdoc.append((os.path.abspath(r),file))
path_mkdoc.sort()

pwd = os.path.abspath(os.curdir) + '/'

with open("log.txt", "w") as log_out:
    for r,f in path_mkdoc:
        print (f"executing {r} {f} {[arg for arg in more_args]}")

        command = [sys.executable, f]
        if more_args:
            command.extend(more_args)
        print(command)
        
        os.chdir(r)
        subprocess.call(command)


