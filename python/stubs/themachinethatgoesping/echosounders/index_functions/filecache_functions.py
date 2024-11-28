from __future__ import annotations
from collections import defaultdict
import os as os
from pathlib._local import Path
import pickle as pickle
from themachinethatgoesping.echosounders_cppy import filetemplates
from tqdm.asyncio import tqdm_asyncio as tqdm
__all__ = ['Path', 'defaultdict', 'filetemplates', 'os', 'pickle', 'print_cache_file_statistics', 'remove_name_from_cache', 'tqdm']
def print_cache_file_statistics(file_cache_paths: typing.List[str]):
    ...
def remove_name_from_cache(file_cache_paths: typing.List[str], name: str) -> None:
    ...
