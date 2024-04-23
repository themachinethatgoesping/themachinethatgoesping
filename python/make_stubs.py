#!/bin/env python3

import os
import shutil as sh
import subprocess

if os.path.exists('stubs'):
  sh.rmtree('stubs')

#pybind11-stubgen themachinethatgoesping --ignore-invalid=all --skip-signature-downgrade
#pybind11-stubgen themachinethatgoesping --ignore-invalid-expressions=all --ignore-invalid-identifiers=all
subprocess.call(['pybind11-stubgen', 'themachinethatgoesping', '--ignore-invalid-expressions=all', '--ignore-invalid-identifiers=all'])

#sh.copytree('themachinethatgoesping-stubs', 'stubs/themachinethatgoesping')

#os.remove('stubs/themachinethatgoesping/setup.py')

#rename all .pyi files in stubs/themachinethatgoesping to .py
for r,d,f in os.walk('stubs/themachinethatgoesping'):
  for file in f:
    if file.endswith('.pyi'):
      fin = r + '/' + file
      fout = fin.replace('.pyi','.py')
      os.rename(fin,fout)