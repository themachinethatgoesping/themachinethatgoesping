"""
Classes that help adding common functionality to themachinethatgoesping classes
"""

from collections.abc import Sequence
from typing import overload


class ObjectPrinter:
    """
    Class that allows for easy pretty printing of class members
    usage:
     1. Implement a __printer__ function as public class member this
        function should return a ObjectPrinter object. Register all,
        values, containers, objects that are to be printed.
     2. Add the __CLASSHELPER_DEFAULT_PRINTING_FUNCTIONS__ macro to the
        public functions. This macro implements std::string info_string()
        and print(std::ostream) functions using the
    object printer
     3. Add the __PYCLASS_DEFAULT_PRINTING__ to the python module
        defintion. This macro implements __str__(), __repr__(),
        info_string() and print() as python functions
    """

    def __init__(self, name: str, float_precission: int, superscript_exponents: bool) -> None:
        """
        Construct a new Object Printer object

        Args:
            float_precision: default 2, set number of digits for floating
                             point values
        """

    def class_name(self) -> str:
        """
        Get the registered name of the object

        Returns:
            std::string
        """

    def create_str(self) -> str:
        """
        Create an info_string from the registered values/sections

        Returns:
            std::string
        """

    @overload
    def register_value(self, name: str, value: float, value_info: str = '', pos: int = -1) -> None:
        """
        register a single integer of floating point value for printing

        Args:
            name: name of the variable
            value: value of the variable
            value_info: additional info (is printed in [] behind the variable)
            pos: position where the value is registers (if negative, the value
                 is appended)

        Template Args:
            t_value: double or floating point
        """

    @overload
    def register_value(self, name: str, value: int, value_info: str = '', pos: int = -1) -> None: ...

    @overload
    def register_value(self, name: str, value: str, value_info: str = '', pos: int = -1) -> None: ...

    @overload
    def register_optional_value(self, name: str, value: float, value_info: str | None = '', optional_value: str = 'Not set', pos: int = -1) -> None:
        """
        Registers an optional value with the given name and additional
        information.

        This function checks if the optional value has a value. If it does, it
        registers the value using the provided name, value information, and
        position. If the optional value does not have a value, it registers
        the string "Not set" instead.

        Args:
            name: The name to register the value under.
            value: The optional value to register.
            value_info: Additional information about the value (default is an
                        empty string).
            pos: The position to register the value at (default is -1).

        Template Args:
            t_value: The type of the optional value.
        """

    @overload
    def register_optional_value(self, name: str, value: int, value_info: str | None = '', optional_value: str = 'Not set', pos: int = -1) -> None: ...

    @overload
    def register_optional_value(self, name: str, value: str, value_info: str | None = '', optional_value: str = 'Not set', pos: int = -1) -> None: ...

    def register_value_bytes(self, name: str, value: int, pos: int = -1) -> None:
        """
        register a single integer of floating point value for printing The
        value is assumed to be in bytes. It will be converted to bytes, KB,
        MB, GB

        Args:
            name: name of the variable
            value: value of the variable in bytes
            pos: position where the value is registers (if negative, the value
                 is appended)
        """

    @overload
    def register_container(self, name: str, value: Sequence[float], value_info: str = '', pos: int = -1) -> None:
        """
        register a 1D container for printing

        Args:
            name: name of the container
            value: container values
            value_info: additional info (is printed in [] behind the variable)
            pos: position where the value is registers (if negative, the value
                 is appended)

        Template Args:
            t_value: integer or floating point
        """

    @overload
    def register_container(self, name: str, value: Sequence[int], value_info: str = '', pos: int = -1) -> None: ...

    @overload
    def register_container(self, name: str, value: Sequence[str], value_info: str = '', pos: int = -1) -> None: ...

    def register_string(self, name: str, value: str, value_info: str = '', pos: int = -1, max_visible_elements: int = 0) -> None:
        """
        register a formatted string field for printing

        Args:
            name: name of the variable
            value: value of the variable
            value_info: additional info (is printed in [] behind the variable)
            pos: position where the value is registers (if negative, the value
                 is appended)
            max_visible_elements: maximum of chars that are printed (if 0, all
                                  elements are printed)
        """

    def register_string_with_delimiters(self, name: str, value: str, value_info: str = '', delimiter_left: str = '"', delimiter_right: str = '"', pos: int = -1, max_visible_elements: int = 0) -> None:
        """
        register a formatted string field for printing, with delimiters

        Args:
            name: name of the variable
            value: value of the variable
            delimiter_left: left delimiter
            delimiter_right: right delimiter
            value_info: additional info (is printed in [] behind the variable)
            pos: position where the value is registers (if negative, the value
                 is appended)
            max_visible_elements: maximum of chars that are printed (if 0, all
                                  elements are printed)
        """

    def register_section(self, name: str, underliner: str = '-', pos: int = -1) -> None:
        """
        register a section break for printing

        Args:
            name: name of the following section
            underliner: character used to underline the section name
            pos: position where the value is registers (if negative, the value
                 is appended)
        """

    def copy(self) -> ObjectPrinter:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> ObjectPrinter: ...

    def __deepcopy__(self, arg: dict, /) -> ObjectPrinter: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> ObjectPrinter:
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
