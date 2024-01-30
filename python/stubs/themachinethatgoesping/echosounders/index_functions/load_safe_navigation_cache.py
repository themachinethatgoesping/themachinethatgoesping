from __future__ import annotations
from collections import defaultdict
import os as os
from pathlib import Path
import pickle as pickle
from themachinethatgoesping.echosounders.index_functions.load_safe_index_cache import load_index_cache_files
from themachinethatgoesping.echosounders.index_functions.load_safe_index_cache import update_index_cache_files
__all__ = ['Path', 'defaultdict', 'load_index_cache_files', 'load_navigation_cache_files', 'os', 'pickle', 'update_index_cache_files', 'update_navigation_cache_files']
def load_navigation_cache_files(file_paths: typing.List[str], force_new: bool = False, cache_name: str = 'tmtgp.navcache', cache_root: str = 'cache', update_cache: typing.Dict[str, str] = None, verbose: bool = False, create_dir: bool = True) -> typing.Dict[str, str]:
    """
    Load navigation cache files for a given list of file paths
    
        Parameters
        ----------
        file_paths : list of str
            The list of file paths to load navigation cache files for
        force_new : bool, optional
            If true: force the creation of new cache files, by default False
        cache_name : str, optional
            The name of the cache file, by default 'tmtgp.navcache'
        cache_root : str, optional
            The path to the root folder containing all cache files, by default 'cache'
        update_cache : dict, optional
            A dictionary to update with the loaded cache data, by default None
        verbose : bool, optional
            If true: print verbose output, by default False
        create_dir : bool, optional
            If true: create a subdirectory, by default True
    
        Returns
        -------
        dict
            A dictionary containing the loaded navigation cache data
        
    """
def update_navigation_cache_files(cached_navigation_dict: typing.Dict[str, str], force_new: bool = False, cache_name: str = 'tmtgp.navcache', cache_root: str = 'cache', verbose: bool = False, create_dir: bool = True) -> None:
    """
    Update navigation cache files with a given dictionary of navigation data
    
        Parameters
        ----------
        cached_navigation_dict : dict
            A dictionary containing the navigation data to update the navigation files with
        force_new : bool, optional
            If true: force the creation of new navigation files, by default False
        cache_name : str, optional
            The name of the navigation file, by default 'tmtgp.navcache'
        cache_root : str, optional
            The path to the root folder containing all cache files, by default 'cache'
        verbose : bool, optional
            If true: print verbose output, by default False
        create_dir : bool, optional
            If true: create a subdirectory, by default True
        
    """
