from __future__ import annotations
from collections import defaultdict
import os as os
from pathlib._local import Path
import pickle as pickle
from themachinethatgoesping.echosounders_nanopy import filetemplates
from tqdm.asyncio import tqdm_asyncio as tqdm
__all__: list[str] = ['Path', 'defaultdict', 'filetemplates', 'os', 'pickle', 'print_index_file_statistics', 'remove_name_from_index', 'tqdm']
def print_index_file_statistics(index_paths: typing.List[str]):
    ...
def remove_name_from_index(index_paths: typing.List[str], name: str) -> None:
    ...
