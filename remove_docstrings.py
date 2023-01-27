#!/bin/env python3

import os
import shutil as sh

#search for .docstrings folders
del_dirs=[]
for r,d,f in os.walk('.'):
  for directory in d:
    if directory == ".docstrings":
      del_dirs.append(r+"/"+directory)

del_dirs.sort()

for d in del_dirs:
  print("To be removed:",d)

answer = input('Please indicate approval: [y/n]')
if not answer or answer[0].lower() != 'y':
    print('You did approve')
    exit(1)

print("deleting ..." )
for d in del_dirs:
  print("removing:",d)
  sh.rmtree(d)
print("done")

