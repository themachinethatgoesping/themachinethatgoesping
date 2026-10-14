"""Trampoline classes for abstract file template classes"""
import typing

from collections.abc import Sequence
from typing import overload

import themachinethatgoesping.echosounders_nanopy.filetemplates


class FilePackageCache_XML_Parameter_Channel:
    def __init__(self) -> None: ...

    def __eq__(self, other: themachinethatgoesping.echosounders_nanopy.filetemplates.FilePackageCache_XML_Parameter_Channel) -> bool: ...

    def get_package(self, file_pos: int, timestamp: float, sub_package_nr: int = 0) -> typing.Any: ...

    def get_packages(self, file_pos: int, timestamp: float) -> list[typing.Any]: ...

    def get_subpackage_count(self, file_pos: int) -> int: ...

    def has_package(self, file_pos: int) -> bool: ...

    def get_hash_cache(self) -> dict[int, str]: ...

    def get_package_buffer(self) -> dict[int, list[str]]: ...

    def copy(self) -> themachinethatgoesping.echosounders_nanopy.filetemplates.FilePackageCache_XML_Parameter_Channel:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> themachinethatgoesping.echosounders_nanopy.filetemplates.FilePackageCache_XML_Parameter_Channel: ...

    def __deepcopy__(self, arg: dict, /) -> themachinethatgoesping.echosounders_nanopy.filetemplates.FilePackageCache_XML_Parameter_Channel: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> themachinethatgoesping.echosounders_nanopy.filetemplates.FilePackageCache_XML_Parameter_Channel:
        """create T_CLASS object from bytearray"""

    def __getstate__(self) -> bytes: ...

    def __setstate__(self, arg: bytes, /) -> None: ...

    def __hash__(self) -> int:
        """hash function implemented using binary_hash"""

    def hash(self) -> int:
        """hash function implemented using binary_hash"""

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

class FileCache:
    @overload
    def __init__(self, file_name: str, file_size: int) -> None: ...

    @overload
    def __init__(self, index_path: str, file_name: str, file_size: int, cache_keys: Sequence[str] = []) -> None: ...

    def __eq__(self, other: FileCache) -> bool: ...

    def update_file(self, index_path: str, emulate_only: bool = False) -> None:
        """
        Update or create the cache file at the specified path

        Args:
            index_path: Path where to write the cache file
            emulate_only: If true, only simulate the update without actually
                          writing
        """

    @staticmethod
    def from_file(index_path: str) -> FileCache:
        """
        Create a FileCache from a file

        Args:
            index_path: Path to the cache file to read

        Returns:
            FileCache object created from the file
        """

    def remove_from_cache(self, name: str) -> None:
        """
        Remove a cache entry and all entries added after it

        Args:
            name: Name of the cache entry to remove
        """

    def get_cache_names(self) -> list[str]: ...

    def get_loaded_cache_names(self) -> list[str]: ...

    def get_not_loaded_cache_names(self) -> list[str]: ...

    def has_cache(self, cache_name: str) -> bool:
        """
        Check if a cache entry with the given name exists

        Args:
            name: Name of the cache entry to check

        Returns:
            true if the cache entry exists
        """

    def get_file_name(self) -> str: ...

    def get_file_size(self) -> int: ...

    def get_cache_buffer(self) -> dict[str, str]: ...

    def get_cache_buffer_header(self) -> list[typing.Any]: ...

    def copy(self) -> FileCache:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> FileCache: ...

    def __deepcopy__(self, arg: dict, /) -> FileCache: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> FileCache:
        """create T_CLASS object from bytearray"""

    def __getstate__(self) -> bytes: ...

    def __setstate__(self, arg: bytes, /) -> None: ...

    def __hash__(self) -> int:
        """hash function implemented using binary_hash"""

    def hash(self) -> int:
        """hash function implemented using binary_hash"""

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""
