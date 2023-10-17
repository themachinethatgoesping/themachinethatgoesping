from __future__ import annotations
import os as os
import pathlib
from pathlib import Path
__all__ = ['Path', 'get_index_file_name', 'load_index_files', 'os', 'update_index_files']
def get_index_file_name(folder_path, index_root, index_name) -> pathlib.Path:
    ...
def load_index_files(file_paths, force_new = False, index_name = 'tmtgp.index', index_root = 'index', update_index = None, verbose = False):
    ...
def update_index_files(cached_index_dict, force_new = False, index_name = 'tmtgp.index', index_root = 'index', verbose = False):
    ...
