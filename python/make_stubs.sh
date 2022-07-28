#!/usr/bin/bash

rm -vr stubs
#pybind11-stubgen themachinethatgoesping --ignore-invalid=all --skip-signature-downgrade
pybind11-stubgen themachinethatgoesping --ignore-invalid=all

