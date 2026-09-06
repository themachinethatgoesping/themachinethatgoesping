"""Teledyne RESON .s7k (7k) file data types"""
import typing

from typing import overload

import themachinethatgoesping.echosounders_nanopy.filetemplates
import themachinethatgoesping.echosounders_nanopy.s7k
import themachinethatgoesping.echosounders_nanopy.s7k.filedatainterfaces


class S7KPingFileData_stream(themachinethatgoesping.echosounders_nanopy.filetemplates.I_PingFileData):
    """
    Raw file data of a single s7k ping. Holds the datagram index of the
    ping (via the S7KDatagramInterface base) and provides raw access to
    the ping's datagrams.



    $.. note::

    The datagram-processing functions are not implemented yet. This class
    currently only provides the structure so it can be filled in in a
    later step.

    Template Args:
        t_ifstream:
    """

    def copy(self) -> S7KPingFileData_stream:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> S7KPingFileData_stream: ...

    def __deepcopy__(self, arg: dict, /) -> S7KPingFileData_stream: ...

    @overload
    def __str__(self) -> str: ...

    @overload
    def __str__(self) -> str:
        """Return object information as string"""

    @overload
    def __repr__(self) -> str: ...

    @overload
    def __repr__(self) -> str:
        """Return object information as string"""

    @overload
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str: ...

    @overload
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    @overload
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None: ...

    @overload
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def get_timestamp_first(self) -> float: ...

    def get_timestamp_last(self) -> float: ...

    def get_timestamp_range(self) -> typing.Any: ...

    def keys(self) -> list[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier]: ...

    @overload
    def datagrams(self, skip_data: bool = False) -> object: ...

    @overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders_nanopy.s7k.o_S7KDatagramIdentifier, skip_data: bool = False) -> object: ...

    @overload
    def datagram_headers(self) -> object: ...

    @overload
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_nanopy.s7k.o_S7KDatagramIdentifier) -> object: ...

    @overload
    def datagrams_raw(self) -> object: ...

    @overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_nanopy.s7k.o_S7KDatagramIdentifier) -> object: ...

    def per_file(self) -> list[themachinethatgoesping.echosounders_nanopy.s7k.filedatainterfaces.S7KDatagramInterface_stream]: ...

class S7KPingFileData(themachinethatgoesping.echosounders_nanopy.filetemplates.I_PingFileData):
    """
    Raw file data of a single s7k ping. Holds the datagram index of the
    ping (via the S7KDatagramInterface base) and provides raw access to
    the ping's datagrams.



    $.. note::

    The datagram-processing functions are not implemented yet. This class
    currently only provides the structure so it can be filled in in a
    later step.

    Template Args:
        t_ifstream:
    """

    def copy(self) -> S7KPingFileData:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> S7KPingFileData: ...

    def __deepcopy__(self, arg: dict, /) -> S7KPingFileData: ...

    @overload
    def __str__(self) -> str: ...

    @overload
    def __str__(self) -> str:
        """Return object information as string"""

    @overload
    def __repr__(self) -> str: ...

    @overload
    def __repr__(self) -> str:
        """Return object information as string"""

    @overload
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str: ...

    @overload
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    @overload
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None: ...

    @overload
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

    def get_timestamp_first(self) -> float: ...

    def get_timestamp_last(self) -> float: ...

    def get_timestamp_range(self) -> typing.Any: ...

    def keys(self) -> list[themachinethatgoesping.echosounders_nanopy.s7k.t_S7KDatagramIdentifier]: ...

    @overload
    def datagrams(self, skip_data: bool = False) -> object: ...

    @overload
    def datagrams(self, datagram_type: themachinethatgoesping.echosounders_nanopy.s7k.o_S7KDatagramIdentifier, skip_data: bool = False) -> object: ...

    @overload
    def datagram_headers(self) -> object: ...

    @overload
    def datagram_headers(self, datagram_type: themachinethatgoesping.echosounders_nanopy.s7k.o_S7KDatagramIdentifier) -> object: ...

    @overload
    def datagrams_raw(self) -> object: ...

    @overload
    def datagrams_raw(self, datagram_type: themachinethatgoesping.echosounders_nanopy.s7k.o_S7KDatagramIdentifier) -> object: ...

    def per_file(self) -> list[themachinethatgoesping.echosounders_nanopy.s7k.filedatainterfaces.S7KDatagramInterface]: ...

class S7KPingCommon_stream:
    """
    Common base for the s7k ping (and its bottom / watercolumn sub-
    objects). Holds the shared S7KPingFileData (the raw file data /
    datagram index of the ping).

    Template Args:
        t_ifstream:
    """

    @property
    def file_data(self) -> S7KPingFileData_stream: ...

    def copy(self) -> S7KPingCommon_stream:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> S7KPingCommon_stream: ...

    def __deepcopy__(self, arg: dict, /) -> S7KPingCommon_stream: ...

class S7KPingCommon:
    """
    Common base for the s7k ping (and its bottom / watercolumn sub-
    objects). Holds the shared S7KPingFileData (the raw file data /
    datagram index of the ping).

    Template Args:
        t_ifstream:
    """

    @property
    def file_data(self) -> S7KPingFileData: ...

    def copy(self) -> S7KPingCommon:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> S7KPingCommon: ...

    def __deepcopy__(self, arg: dict, /) -> S7KPingCommon: ...

class S7KPingBottom_stream(themachinethatgoesping.echosounders_nanopy.filetemplates.I_PingBottom):
    """
    Bottom detection (bathymetry) accessor of an s7k ping.



    $.. note::

    The bottom-detection processing functions are not implemented yet;
    they inherit the base I_PingBottom "not implemented" behavior. This
    class currently only provides the structure so it can be filled in in
    a later step.

    Template Args:
        t_ifstream:
    """

    def copy(self) -> S7KPingBottom_stream:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> S7KPingBottom_stream: ...

    def __deepcopy__(self, arg: dict, /) -> S7KPingBottom_stream: ...

class S7KPingBottom(themachinethatgoesping.echosounders_nanopy.filetemplates.I_PingBottom):
    """
    Bottom detection (bathymetry) accessor of an s7k ping.



    $.. note::

    The bottom-detection processing functions are not implemented yet;
    they inherit the base I_PingBottom "not implemented" behavior. This
    class currently only provides the structure so it can be filled in in
    a later step.

    Template Args:
        t_ifstream:
    """

    def copy(self) -> S7KPingBottom:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> S7KPingBottom: ...

    def __deepcopy__(self, arg: dict, /) -> S7KPingBottom: ...

class S7KPingWatercolumn_stream(themachinethatgoesping.echosounders_nanopy.filetemplates.I_PingWatercolumn):
    """
    Water column accessor of an s7k ping.



    $.. note::

    The water-column processing functions are not implemented yet; they
    inherit the base I_PingWatercolumn "not implemented" behavior. This
    class currently only provides the structure so it can be filled in in
    a later step.

    Template Args:
        t_ifstream:
    """

    def copy(self) -> S7KPingWatercolumn_stream:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> S7KPingWatercolumn_stream: ...

    def __deepcopy__(self, arg: dict, /) -> S7KPingWatercolumn_stream: ...

class S7KPingWatercolumn(themachinethatgoesping.echosounders_nanopy.filetemplates.I_PingWatercolumn):
    """
    Water column accessor of an s7k ping.



    $.. note::

    The water-column processing functions are not implemented yet; they
    inherit the base I_PingWatercolumn "not implemented" behavior. This
    class currently only provides the structure so it can be filled in in
    a later step.

    Template Args:
        t_ifstream:
    """

    def copy(self) -> S7KPingWatercolumn:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> S7KPingWatercolumn: ...

    def __deepcopy__(self, arg: dict, /) -> S7KPingWatercolumn: ...

class S7KPing_stream(themachinethatgoesping.echosounders_nanopy.filetemplates.I_Ping):
    """
    A single ping of an s7k file. Groups all datagrams (sonar settings,
    bathymetry, water column) that belong to the same ping and exposes
    them via the bottom() and watercolumn() sub-objects.



    $.. note::

    The datagram-processing functions are not implemented yet. This class
    currently only provides the structure so the ping can be filled in in
    a later step.

    Template Args:
        t_ifstream:
    """

    @property
    def file_data(self) -> S7KPingFileData_stream: ...

    def copy(self) -> S7KPing_stream:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> S7KPing_stream: ...

    def __deepcopy__(self, arg: dict, /) -> S7KPing_stream: ...

class S7KPing(themachinethatgoesping.echosounders_nanopy.filetemplates.I_Ping):
    """
    A single ping of an s7k file. Groups all datagrams (sonar settings,
    bathymetry, water column) that belong to the same ping and exposes
    them via the bottom() and watercolumn() sub-objects.



    $.. note::

    The datagram-processing functions are not implemented yet. This class
    currently only provides the structure so the ping can be filled in in
    a later step.

    Template Args:
        t_ifstream:
    """

    @property
    def file_data(self) -> S7KPingFileData: ...

    def copy(self) -> S7KPing:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> S7KPing: ...

    def __deepcopy__(self, arg: dict, /) -> S7KPing: ...
