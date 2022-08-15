#!/usr/bin/xonsh

import os

rm -vr stubs
#pybind11-stubgen themachinethatgoesping --ignore-invalid=all --skip-signature-downgrade
pybind11-stubgen themachinethatgoesping --ignore-invalid=all

cp stubs/themachinethatgoesping-stubs/ stubs/themachinethatgoesping -r

rm stubs/themachinethatgoesping/setup.py
#rename all .pyi files in stubs/themachinethatgoesping to .py
for r,d,f in os.walk('stubs/themachinethatgoesping'):
  for file in f:
    if file.endswith('.pyi'):
      fin = r + '/' + file
      fout = fin.replace('.pyi','.py')
      mv @(fin) @(fout) -v