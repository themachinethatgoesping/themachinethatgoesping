"""
Classes that help adding common functionality to themachinethatgoesping classes
"""
from __future__ import annotations
import collections.abc
import typing
__all__: list[str] = ['ObjectPrinter']
class ObjectPrinter:
    """
    Class that allows for easy pretty printing of class members usage: 1.
    Implement a __printer__ function as public class member this function
    should return a ObjectPrinter object. Register all, values,
    containers, objects that are to be printed. 2. Add the
    __CLASSHELPER_DEFAULT_PRINTING_FUNCTIONS__ macro to the public
    functions. This macro implements std::string info_string() and
    print(std::ostream) functions using the object printer 3. Add the
    __PYCLASS_DEFAULT_PRINTING__ to the python module defintion. This
    macro implements __str__(), __repr__(), info_string() and print() as
    python functions
    """
    from_binary: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __copy__(self) -> ObjectPrinter:
        ...
    def __deepcopy__(self, arg: dict) -> ObjectPrinter:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def __init__(self, name: str, float_precission: int, superscript_exponents: bool) -> None:
        """
        Construct a new Object Printer object
        
        Parameter ``float_precision``:
            default 2, set number of digits for floating point values
        """
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __setstate__(self, arg: bytes) -> None:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def class_name(self) -> str:
        """
        Get the registered name of the object
        
        Returns:
            std::string
        """
    def copy(self) -> ObjectPrinter:
        """
        return a copy using the c++ default copy constructor
        """
    def create_str(self) -> str:
        """
        Create an info_string from the registered values/sections
        
        Returns:
            std::string
        """
    def hash(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def register_container(self, name: str, value: collections.abc.Sequence[float], value_info: str = '', pos: int = -1) -> None:
        """
        register_container(self, name: str, value: collections.abc.Sequence[int], value_info: str = '', pos: int = -1) -> None
        register_container(self, name: str, value: collections.abc.Sequence[str], value_info: str = '', pos: int = -1) -> None
        
        register a 1D container for printing
        
        Template parameter ``t_value``:
            integer or floating point
        
        Parameter ``name``:
            name of the container
        
        Parameter ``value``:
            container values
        
        Parameter ``value_info``:
            additional info (is printed in [] behind the variable)
        
        Parameter ``pos``:
            position where the value is registers (if negative, the value is
            appended)
        """
    def register_optional_value(self, name: str, value: float, value_info: str = '', optional_value: str = 'Not set', pos: int = -1) -> None:
        """
        register_optional_value(self, name: str, value: int, value_info: str = '', optional_value: str = 'Not set', pos: int = -1) -> None
        register_optional_value(self, name: str, value: str, value_info: str = '', optional_value: str = 'Not set', pos: int = -1) -> None
        
        Registers an optional value with the given name and additional
        information.
        
        This function checks if the optional value has a value. If it does, it
        registers the value using the provided name, value information, and
        position. If the optional value does not have a value, it registers
        the string "Not set" instead.
        
        Template parameter ``t_value``:
            The type of the optional value.
        
        Parameter ``name``:
            The name to register the value under.
        
        Parameter ``value``:
            The optional value to register.
        
        Parameter ``value_info``:
            Additional information about the value (default is an empty
            string).
        
        Parameter ``pos``:
            The position to register the value at (default is -1).
        """
    def register_section(self, name: str, underliner: str = '-', pos: int = -1) -> None:
        """
        register a section break for printing
        
        Parameter ``name``:
            name of the following section
        
        Parameter ``underliner``:
            character used to underline the section name
        
        Parameter ``pos``:
            position where the value is registers (if negative, the value is
            appended)
        """
    def register_string(self, name: str, value: str, value_info: str = '', pos: int = -1, max_visible_elements: int = 0) -> None:
        """
        register a formatted string field for printing
        
        Parameter ``name``:
            name of the variable
        
        Parameter ``value``:
            value of the variable
        
        Parameter ``value_info``:
            additional info (is printed in [] behind the variable)
        
        Parameter ``pos``:
            position where the value is registers (if negative, the value is
            appended)
        
        Parameter ``max_visible_elements``:
            maximum of chars that are printed (if 0, all elements are printed)
        """
    def register_string_with_delimiters(self, name: str, value: str, value_info: str = '', delimiter_left: str = '"', delimiter_right: str = '"', pos: int = -1, max_visible_elements: int = 0) -> None:
        """
        register a formatted string field for printing, with delimiters
        
        Parameter ``name``:
            name of the variable
        
        Parameter ``value``:
            value of the variable
        
        Parameter ``delimiter_left``:
            left delimiter
        
        Parameter ``delimiter_right``:
            right delimiter
        
        Parameter ``value_info``:
            additional info (is printed in [] behind the variable)
        
        Parameter ``pos``:
            position where the value is registers (if negative, the value is
            appended)
        
        Parameter ``max_visible_elements``:
            maximum of chars that are printed (if 0, all elements are printed)
        """
    def register_value(self, name: str, value: float, value_info: str = '', pos: int = -1) -> None:
        """
        register_value(self, name: str, value: int, value_info: str = '', pos: int = -1) -> None
        register_value(self, name: str, value: str, value_info: str = '', pos: int = -1) -> None
        
        register a single integer of floating point value for printing
        
        Template parameter ``t_value``:
            double or floating point
        
        Parameter ``name``:
            name of the variable
        
        Parameter ``value``:
            value of the variable
        
        Parameter ``value_info``:
            additional info (is printed in [] behind the variable)
        
        Parameter ``pos``:
            position where the value is registers (if negative, the value is
            appended)
        """
    def register_value_bytes(self, name: str, value: int, pos: int = -1) -> None:
        """
        register a single integer of floating point value for printing The
        value is assumed to be in bytes. It will be converted to bytes, KB,
        MB, GB
        
        Parameter ``name``:
            name of the variable
        
        Parameter ``value``:
            value of the variable in bytes
        
        Parameter ``pos``:
            position where the value is registers (if negative, the value is
            appended)
        """
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
