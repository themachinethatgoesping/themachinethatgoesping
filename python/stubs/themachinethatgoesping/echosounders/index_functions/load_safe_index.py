from __future__ import annotations
from collections import defaultdict
import os as os
import pathlib
from pathlib import Path
import pickle as pickle
from themachinethatgoesping.echosounders_cppy import em3000
from themachinethatgoesping.echosounders_cppy import simrad
__all__ = ['Path', 'defaultdict', 'em3000', 'get_index_file_name', 'load_index_files', 'os', 'pickle', 'simrad', 'update_index_files']
def get_index_file_name(folder_path, index_root, index_name, create_dir = True) -> pathlib.Path:
    ...
def load_index_files(file_paths, force_new = False, index_name = 'tmtgp.index', index_root = 'index', update_index = None, verbose = False, create_dir = True):
    ...
def update_index_files(cached_index_dict, force_new = False, index_name = 'tmtgp.index', index_root = 'index', verbose = False, create_dir = True):
    ...
