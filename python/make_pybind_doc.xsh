#!/bin/xonsh

import os

path_mkdoc = []
for r,d,f in os.walk('../'):
    for file in f:
        if file == "mkdoc.xsh":
            path_mkdoc.append((os.path.abspath(r),file))
path_mkdoc.sort()

pwd = os.path.abspath(os.curdir) + '/'
echo "" > @(pwd)/log.txt
for r,f in path_mkdoc:
    #this only works using the xonsh shell which can call bash commands from python
    echo executing @(r) @(f)
    cd @(r)
    ./@(f) 2>> @(pwd)/log.txt

