from typing import Union

from . import index_file_functions as index_file_functions
from .find_files import (
    find_files as find_files,
    find_folders_with_files as find_folders_with_files,
    get_hash as get_hash,
    group_by_hash as group_by_hash,
    remove_duplicates as remove_duplicates
)
from .get_index_paths import (
    get_index_path as get_index_path,
    get_index_paths as get_index_paths
)
from .index_file_functions import (
    print_index_file_statistics as print_index_file_statistics,
    remove_name_from_index as remove_name_from_index
)
import themachinethatgoesping.echosounders_nanopy.filetemplates as filetemplates


def find_files_and_index(folders: Union[str, list[str]], endings: Union[str, list[str]], followlinks: bool = False, remove_duplicated_files: bool = True, verbose: bool = True, index_file_ending: str = '.tmtgp.index', index_root: str = 'index', create_dir: bool = True) -> tuple[list[str], dict[str, str]]:
    """
    Find files and get their corresponding index paths.

    This function combines find_files and get_index_paths for convenience.

    Parameters
    ----------
    folders : Union[str, List[str]]
        The folders to search for files.
    endings : Union[str, List[str]]
        The file endings to match.
    followlinks : bool, optional
        If True, follows symbolic links. Defaults to False.
    remove_duplicated_files : bool, optional
        If True, removes any duplicate files found. Defaults to True.
    verbose : bool, optional
        If True, prints progress messages. Defaults to True.
    index_file_ending : str, optional
        The ending for index files. Defaults to '.tmtgp.index'.
    index_root : str, optional
        The path to the root folder containing all index files. Defaults to 'index'.
    create_dir : bool, optional
        If True, creates the index directory if it doesn't exist. Defaults to True.

    Returns
    -------
    Tuple[List[str], Dict[str, str]]
        A tuple containing:
        - file_paths: List of found file paths
        - index_paths: Dictionary mapping file paths to their index file paths
    """
