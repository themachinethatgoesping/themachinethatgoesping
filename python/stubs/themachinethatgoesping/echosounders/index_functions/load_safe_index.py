from __future__ import annotations
from collections import defaultdict
import os as os
import pathlib
from pathlib import Path
import pickle as pickle
__all__ = ['Path', 'defaultdict', 'get_index_file_name', 'load_index_files', 'os', 'pickle', 'update_index_files']
def get_index_file_name(folder_path: typing.Union[str, pathlib.Path], index_root: typing.Union[str, pathlib.Path, NoneType] = None, index_name: str = 'tmtgp.index', create_dir: bool = True) -> pathlib.Path:
    """
    Return the path to the index file for a given folder path
    
        Parameters
        ----------
        folder_path : str or Path
            The path to the folder containing files that are indexed
        index_root : str or Path, optional
            The path to the root folder containing all index files. If None, the index file will be in the same folder as the data files
        index_name : str, optional
            The name of the index file
        create_dir : bool, optional
            If true: create a subdirectory, by default True
    
        Returns
        -------
        Path
            The path to the index file
        
    """
def load_index_files(file_paths: typing.List[str], force_new: bool = False, index_name: str = 'tmtgp.index', index_root: str = 'index', update_index: typing.Dict[str, str] = None, verbose: bool = False, create_dir: bool = True) -> typing.Dict[str, str]:
    """
    Load index files for a given list of file paths
    
        Parameters
        ----------
        file_paths : list of str
            The list of file paths to load index files for
        force_new : bool, optional
            If true: force the creation of new index files, by default False
        index_name : str, optional
            The name of the index file, by default 'tmtgp.index'
        index_root : str, optional
            The path to the root folder containing all index files, by default 'index'
        update_index : dict, optional
            A dictionary to update with the loaded index data, by default None
        verbose : bool, optional
            If true: print verbose output, by default False
        create_dir : bool, optional
            If true: create a subdirectory, by default True
    
        Returns
        -------
        dict
            A dictionary containing the loaded index data
        
    """
def update_index_files(cached_index_dict: typing.Dict[str, str], force_new: bool = False, index_name: str = 'tmtgp.index', index_root: str = 'index', verbose: bool = False, create_dir: bool = True) -> None:
    """
    Update index files with a given dictionary of index data
    
        Parameters
        ----------
        cached_index_dict : dict
            A dictionary containing the index data to update the index files withu
        force_new : bool, optional
            If true: force the creation of new index files, by default False
        index_name : str, optional
            The name of the index file, by default 'tmtgp.index'
        index_root : str, optional
            The path to the root folder containing all index files, by default 'index'
        verbose : bool, optional
            If true: print verbose output, by default False
        create_dir : bool, optional
            If true: create a subdirectory, by default True
        
    """
