"""Small helper functions"""

from collections.abc import Sequence
from typing import Annotated, overload

import numpy
from numpy.typing import NDArray


def int_as_string_4b(value: int) -> str:
    """Interprete an integer to a 4 byte string"""

def int_as_string_8b(value: int) -> str:
    """Interprete an integer to a 8 byte string"""

def string_as_int_4b(value: str) -> int:
    """Interprete a 4 byte string to an integer"""

def string_as_int_8b(value: str) -> int:
    """Interprete a 8 byte string to an integer"""

def superscript(exponent: int) -> str:
    """convert integer number to superscript"""

def pytensor_load_ref(arg: Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')], /) -> None: ...

def pytensor_const_load_ref(arg: Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')], /) -> Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')]: ...

def pytensor_load_copy(arg: Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')], /) -> Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')]: ...

def pytensor_loop_ref(arg: Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')], /) -> None: ...

def pytensor_loop_ref2(arg: Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')], /) -> None: ...

def pytensor_sum_ref(arg: Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')], /) -> None: ...

def pytensor_sum_const_ref(arg: Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')], /) -> Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')]: ...

def pytensor_sum_const_ref2(arg: Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')], /) -> Annotated[NDArray[numpy.float64], dict(order='C')]: ...

def pytensor_sum_const_ref3(arg: Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')], /) -> Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')]: ...

def pytensor_view_ref(arg: Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')], /) -> None: ...

def pytensor_make(arg0: int, arg1: int, /) -> Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')]: ...

def pytensor_from(arg0: int, arg1: int, /) -> None: ...

def pytensor_make_xtensor(arg0: int, arg1: int, /) -> Annotated[NDArray[numpy.float64], dict(order='C')]: ...

class RangeDouble:
    """
    A continuous range with min and max values.

    Represents a range [min, max] that can be used to check containment
    and compute intersections with other ranges.

    Attributes
    ----------
    min : float
        Minimum value of the range (inclusive)
    max : float
        Maximum value of the range (inclusive)
    """

    def __init__(self, min_val: float, max_val: float) -> None:
        """Create a range with given min and max values"""

    @property
    def min(self) -> float:
        """Minimum value of the range"""

    @min.setter
    def min(self, arg: float, /) -> None: ...

    @property
    def max(self) -> float:
        """Maximum value of the range"""

    @max.setter
    def max(self, arg: float, /) -> None: ...

    def contains(self, value: float) -> bool:
        """Check if a value is within this range"""

    def overlaps(self, other: RangeDouble) -> bool:
        """Check if this range overlaps with another"""

    def intersection(self, other: RangeDouble) -> RangeDouble:
        """Get the intersection of this range with another"""

    def is_valid(self) -> bool:
        """Check if range is valid (min <= max)"""

    def __repr__(self) -> str: ...

class RangeFloat:
    """
    A continuous range with min and max values (float32).

    Represents a range [min, max] that can be used to check containment
    and compute intersections with other ranges.

    Attributes
    ----------
    min : float
        Minimum value of the range (inclusive)
    max : float
        Maximum value of the range (inclusive)
    """

    def __init__(self, min_val: float, max_val: float) -> None:
        """Create a range with given min and max values"""

    @property
    def min(self) -> float:
        """Minimum value of the range"""

    @min.setter
    def min(self, arg: float, /) -> None: ...

    @property
    def max(self) -> float:
        """Maximum value of the range"""

    @max.setter
    def max(self, arg: float, /) -> None: ...

    def contains(self, value: float) -> bool:
        """Check if a value is within this range"""

    def overlaps(self, other: RangeFloat) -> bool:
        """Check if this range overlaps with another"""

    def intersection(self, other: RangeFloat) -> RangeFloat:
        """Get the intersection of this range with another"""

    def is_valid(self) -> bool:
        """Check if range is valid (min <= max)"""

    def __repr__(self) -> str: ...

@overload
def get_sections(data: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], max_gap: float = float('nan')) -> list[RangeDouble]:
    """
    Extract continuous sections from a sorted container based on max_gap.

    A section is a range [min, max] where consecutive elements have gaps <= max_gap.

    Parameters
    ----------
    data : numpy.ndarray
        Sorted 1D array of values
    max_gap : float
        Maximum allowed gap between consecutive elements within a section.
        If <= 0 or non-finite, entire container is treated as one section.

    Returns
    -------
    list
        List of Range objects representing continuous sections
    """

@overload
def get_sections(data: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], max_gap: float = float('nan')) -> list[RangeFloat]:
    """
    Extract continuous sections from a sorted container based on max_gap.

    A section is a range [min, max] where consecutive elements have gaps <= max_gap.

    Parameters
    ----------
    data : numpy.ndarray
        Sorted 1D array of values (float32)
    max_gap : float
        Maximum allowed gap between consecutive elements within a section.

    Returns
    -------
    list
        List of Range objects representing continuous sections
    """

@overload
def get_shared_sections(containers: Sequence[Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')]], max_gap: float = float('nan')) -> list[RangeDouble]:
    """
    Find shared sections across multiple sorted containers.

    Each container is split into sections based on max_gap, then intersections
    across all containers are computed.

    Parameters
    ----------
    containers : list of numpy.ndarray
        List of sorted 1D arrays
    max_gap : float
        Maximum allowed gap between consecutive elements within a section.

    Returns
    -------
    list
        List of Range objects representing shared sections
    """

@overload
def get_shared_sections(containers: Sequence[Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]], max_gap: float = float('nan')) -> list[RangeFloat]:
    """
    Find shared sections across multiple sorted containers.

    Parameters
    ----------
    containers : list of numpy.ndarray
        List of sorted 1D arrays (float32)
    max_gap : float
        Maximum allowed gap between consecutive elements within a section.

    Returns
    -------
    list
        List of Range objects representing shared sections
    """

@overload
def cut_to_shared_sections(containers: Sequence[Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')]], max_gap: float = float('nan')) -> list[Annotated[NDArray[numpy.float64], dict(order='C')]]:
    """
    Cut multiple containers to only include values within shared sections.

    Each container is filtered to keep only values that fall within the
    intersection of all containers' sections.

    Parameters
    ----------
    containers : list of numpy.ndarray
        List of sorted 1D arrays
    max_gap : float
        Maximum allowed gap between consecutive elements within a section.

    Returns
    -------
    list of numpy.ndarray
        Filtered containers containing only values within shared sections
    """

@overload
def cut_to_shared_sections(containers: Sequence[Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]], max_gap: float = float('nan')) -> list[Annotated[NDArray[numpy.float32], dict(order='C')]]:
    """
    Cut multiple containers to only include values within shared sections.

    Parameters
    ----------
    containers : list of numpy.ndarray
        List of sorted 1D arrays (float32)
    max_gap : float
        Maximum allowed gap between consecutive elements within a section.

    Returns
    -------
    list of numpy.ndarray
        Filtered containers containing only values within shared sections
    """

@overload
def get_shared_section_indices(containers: Sequence[Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')]], max_gap: float = float('nan')) -> list[Annotated[NDArray[numpy.uint64], dict(order='C')]]:
    """
    Get indices of elements within shared sections for each container.

    Parameters
    ----------
    containers : list of numpy.ndarray
        List of sorted 1D arrays
    max_gap : float
        Maximum allowed gap between consecutive elements within a section.

    Returns
    -------
    list of numpy.ndarray
        For each container, indices of elements within shared sections
    """

@overload
def get_shared_section_indices(containers: Sequence[Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]], max_gap: float = float('nan')) -> list[Annotated[NDArray[numpy.uint64], dict(order='C')]]:
    """
    Get indices of elements within shared sections for each container.

    Parameters
    ----------
    containers : list of numpy.ndarray
        List of sorted 1D arrays (float32)
    max_gap : float
        Maximum allowed gap between consecutive elements within a section.

    Returns
    -------
    list of numpy.ndarray
        For each container, indices of elements within shared sections
    """

@overload
def get_shared_section_values(containers: Sequence[Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')]], max_gap: float = float('nan')) -> Annotated[NDArray[numpy.float64], dict(order='C')]:
    """
    Get unique values from all containers within shared sections.

    This function collects all unique values from all containers that fall
    within the shared sections, returning them as a sorted array.

    Parameters
    ----------
    containers : list of numpy.ndarray
        List of sorted 1D arrays
    max_gap : float
        Maximum allowed gap between consecutive elements within a section.

    Returns
    -------
    numpy.ndarray
        Sorted array of unique values within shared sections
    """

@overload
def get_shared_section_values(containers: Sequence[Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]], max_gap: float = float('nan')) -> Annotated[NDArray[numpy.float32], dict(order='C')]:
    """
    Get unique values from all containers within shared sections.

    Parameters
    ----------
    containers : list of numpy.ndarray
        List of sorted 1D arrays (float32)
    max_gap : float
        Maximum allowed gap between consecutive elements within a section.

    Returns
    -------
    numpy.ndarray
        Sorted array of unique values within shared sections
    """

@overload
def get_index_downsampling(data: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], downsample_interval: float, max_gap: float = float('nan')) -> Annotated[NDArray[numpy.uint64], dict(order='C')]:
    """
    Compute indices for downsampling a sorted data container

    This function takes a container of sorted values and returns indices
    of values that should be kept when downsampling at a specified
    interval. It also detects gaps in the data and does not bridge them
    (i.e., does not return indices that would require interpolating across
    a gap larger than max_gap).

    The function selects the first value, then selects subsequent values
    that are at least downsample_interval apart from the last selected
    value. When a gap larger than max_gap is encountered, the sampling
    restarts from the first value after the gap.

    Args:
        data: Container of values, must be sorted in ascending order
        downsample_interval: Interval between samples. Use 0, negative, or
                             NaN to disable downsampling (return all
                             indices)
        max_gap: Maximum allowed gap in the original data before
                 considering it a data gap. When a gap larger than this is
                 encountered, sampling restarts after the gap. If <= 0 or
                 NaN, defaults to 2x downsample_interval (or 10 if no
                 downsampling)

    Template Args:
        T: Container type (must support .size() and element access,
           contain floating point values)

    Returns:
        xt::xtensor_size_t_1 containing indices of values to keep

    @note The data must be sorted in ascending order. Behavior is
    undefined for unsorted input.
    """

@overload
def get_index_downsampling(data: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], downsample_interval: float, max_gap: float = float('nan')) -> Annotated[NDArray[numpy.uint64], dict(order='C')]: ...

@overload
def get_value_downsampling(data: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], downsample_interval: float, max_gap: float = float('nan')) -> Annotated[NDArray[numpy.float64], dict(order='C')]:
    """
    Downsample a sorted data container and return the downsampled values

    This function takes a container of sorted values and returns a new
    container with values at exact intervals starting from the first
    value. It also detects gaps in the data and restarts sampling after
    gaps.

    Unlike get_index_downsampling which returns indices into the original
    data, this function generates exact sample points at regular
    intervals.

    Args:
        data: Container of values, must be sorted in ascending order
        downsample_interval: Interval between samples. Use 0, negative, or
                             NaN to disable downsampling (return copy of
                             data)
        max_gap: Maximum allowed gap in the original data before
                 considering it a data gap. When a gap larger than this is
                 encountered, sampling restarts after the gap. If <= 0 or
                 NaN, defaults to 2x downsample_interval (or 10 if no
                 downsampling)

    Template Args:
        T: Container type (must support .size() and element access,
           contain floating point values)

    Returns:
        xt::xtensor_value_type_1 containing the downsampled values at
           exact intervals, where value_type is determined from the input
           container (e.g., float for vector_float)

    @note The data must be sorted in ascending order. Behavior is
    undefined for unsorted input.
    """

@overload
def get_value_downsampling(data: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], downsample_interval: float, max_gap: float = float('nan')) -> Annotated[NDArray[numpy.float32], dict(order='C')]: ...
