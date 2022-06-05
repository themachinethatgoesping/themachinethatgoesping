#!/bin/bash
# Clean the notebook cache to save memory online
# Tutorial notebooks are pushed to git lfs!

jupyter nbconvert --ClearOutputPreprocessor.enabled=True --inplace *.ipynb

