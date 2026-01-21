import themachinethatgoesping.echosounders_nanopy.filetemplates as filetemplates
import themachinethatgoesping.echosounders_nanopy.filetemplates
from themachinethatgoesping.echosounders_nanopy.filetemplates import (
    I_Ping as I_Ping
)
import themachinethatgoesping.navigation as nav
from themachinethatgoesping.pingprocessing.core.progress import (
    get_progress_iterator as get_progress_iterator
)


def by_file_nr(pings: list[themachinethatgoesping.echosounders_nanopy.filetemplates.I_Ping], progress: bool = True) -> dict[int, list[themachinethatgoesping.echosounders_nanopy.filetemplates.I_Ping]]:
    """
    Splits a list of pings by the associated file number.

    Args:
        pings (List[I_Ping]): A list of pings to be split.
        progress (bool, optional): Whether to show a progress bar. Defaults to False.

    Returns:
        Dict[int, List[I_Ping]]: A dictionary where the keys are channel ids and the values are lists of pings.
    """

def by_file_path(pings: list[themachinethatgoesping.echosounders_nanopy.filetemplates.I_Ping], progress: bool = True) -> dict[str, list[themachinethatgoesping.echosounders_nanopy.filetemplates.I_Ping]]:
    """
    Splits a list of pings by the associated file path.

    Args:
        pings (List[I_Ping]): A list of pings to be split.
        progress (bool, optional): Whether to show a progress bar. Defaults to False.

    Returns:
        Dict[str, List[I_Ping]]: A dictionary where the keys are channel ids and the values are lists of pings.
    """

def by_folder_path(pings: list[themachinethatgoesping.echosounders_nanopy.filetemplates.I_Ping], progress: bool = True) -> dict[str, list[themachinethatgoesping.echosounders_nanopy.filetemplates.I_Ping]]:
    """
    Splits a list of pings by the folder path where the primary file is located.

    Args:
        pings (List[I_Ping]): A list of pings to be split.
        progress (bool, optional): Whether to show a progress bar. Defaults to True.

    Returns:
        Dict[str, List[I_Ping]]: A dictionary where the keys are folder paths and the values are lists of pings.
    """
