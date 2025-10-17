#!/usr/bin/bash

python3 scripts/header_analysis/include_collector.py --subprojects tools,algorithms,navigation,echosounders,pingprocessing --internal-prefix themachinethatgoesping --pch-output pch_headers
