#!/bin/env python3

import os
import sys
import subprocess

path_mkdoc = []
for r,d,f in os.walk('../'):
    for file in f:
        if file == "mkdoc.py":
            path_mkdoc.append((os.path.abspath(r),file))
path_mkdoc.sort()

pwd = os.path.abspath(os.curdir) + '/'

with open("log.txt", "w") as log_out:
    for r,f in path_mkdoc:
        print (f"executing {r} {f}")
        
        os.chdir(r)
        subprocess.call([sys.executable, f])


