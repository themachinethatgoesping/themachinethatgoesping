"""Classes related to Kongsberg EM3000 data files (old Kongsberg .all / .wcd format, used until SIS 4.0)"""
from __future__ import annotations
import themachinethatgoesping.echosounders.em3000
import typing
import themachinethatgoesping.tools.progressbars

__all__ = [
    "FileEM3000",
    "FileEM3000_mapped",
    "datagrams",
    "filedataInterfaces"
]


class FileEM3000():
    @typing.overload
    def __init__(self, file_path: str, init: bool = True, show_progress: bool = True) -> None: ...
    @typing.overload
    def __init__(self, file_path: str, init: bool, progress_bar: themachinethatgoesping.tools.progressbars.I_ProgressBar) -> None: ...
    @typing.overload
    def __init__(self, file_path: typing.List[str], init: bool = True, show_progress: bool = True) -> None: ...
    @typing.overload
    def __init__(self, file_paths: typing.List[str], init: bool, progress_bar: themachinethatgoesping.tools.progressbars.I_ProgressBar) -> None: ...
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    @typing.overload
    def init_interfaces(self, force: bool = False, show_progress: bool = True) -> None: ...
    @typing.overload
    def init_interfaces(self, force: bool, progress_bar: themachinethatgoesping.tools.progressbars.I_ProgressBar) -> None: ...
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    @property
    def datagram_interface(self) -> filedataInterfaces.EM3000DatagramInterface:
        """
        :type: filedataInterfaces.EM3000DatagramInterface
        """
    pass
class FileEM3000_mapped():
    @typing.overload
    def __init__(self, file_path: str, init: bool = True, show_progress: bool = True) -> None: ...
    @typing.overload
    def __init__(self, file_path: str, init: bool, progress_bar: themachinethatgoesping.tools.progressbars.I_ProgressBar) -> None: ...
    @typing.overload
    def __init__(self, file_path: typing.List[str], init: bool = True, show_progress: bool = True) -> None: ...
    @typing.overload
    def __init__(self, file_paths: typing.List[str], init: bool, progress_bar: themachinethatgoesping.tools.progressbars.I_ProgressBar) -> None: ...
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    @typing.overload
    def init_interfaces(self, force: bool = False, show_progress: bool = True) -> None: ...
    @typing.overload
    def init_interfaces(self, force: bool, progress_bar: themachinethatgoesping.tools.progressbars.I_ProgressBar) -> None: ...
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    @property
    def datagram_interface(self) -> filedataInterfaces.EM3000DatagramInterface_mapped:
        """
        :type: filedataInterfaces.EM3000DatagramInterface_mapped
        """
    pass
