"""EM3000 (kongsberg .all/.wcd) file data interface classes"""
from __future__ import annotations
import themachinethatgoesping.echosounders.em3000.filedataInterfaces
import typing

__all__ = [
    "EM3000DatagramInterface",
    "EM3000DatagramInterface_mapped"
]


class EM3000DatagramInterface():
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    @staticmethod
    @typing.overload
    def datagram_headers(*args, **kwargs) -> typing.Any: ...
    @typing.overload
    def datagram_headers(self) -> object: ...
    @staticmethod
    @typing.overload
    def datagrams(*args, **kwargs) -> typing.Any: ...
    @typing.overload
    def datagrams(self) -> object: ...
    @staticmethod
    @typing.overload
    def datagrams_raw(*args, **kwargs) -> typing.Any: ...
    @typing.overload
    def datagrams_raw(self) -> object: ...
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    pass
class EM3000DatagramInterface_mapped():
    def __repr__(self) -> str: 
        """
        Return object information as string
        """
    def __str__(self) -> str: 
        """
        Return object information as string
        """
    @staticmethod
    @typing.overload
    def datagram_headers(*args, **kwargs) -> typing.Any: ...
    @typing.overload
    def datagram_headers(self) -> object: ...
    @staticmethod
    @typing.overload
    def datagrams(*args, **kwargs) -> typing.Any: ...
    @typing.overload
    def datagrams(self) -> object: ...
    @staticmethod
    @typing.overload
    def datagrams_raw(*args, **kwargs) -> typing.Any: ...
    @typing.overload
    def datagrams_raw(self) -> object: ...
    def info_string(self, float_precision: int = 2) -> str: 
        """
        Return object information as string
        """
    def print(self, float_precision: int = 2) -> None: 
        """
        Print object information
        """
    pass
