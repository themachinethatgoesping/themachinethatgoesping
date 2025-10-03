"""
Submodule for gridding (raytracers and georefencing) echosounder samples
"""
from __future__ import annotations
import numpy
import typing
from . import functions
__all__: list[str] = ['ForwardGridder1D', 'ForwardGridder1DF', 'ForwardGridder2D', 'ForwardGridder2DF', 'ForwardGridder3D', 'ForwardGridder3DF', 'functions']
class ForwardGridder1D:
    """
    Simple class to generate 1D grids and interpolate x data onto a grid
    using simple forward mapping algorithms (e.g. block mean, weighted
    mean interpolation)
    """
    from_binary: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    from_data: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    from_res: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    get_minmax: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __copy__(self) -> ForwardGridder1D:
        ...
    def __deepcopy__(self, arg: dict) -> ForwardGridder1D:
        ...
    def __eq__(self, other: ForwardGridder1D) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def __init__(self, xres: float, min_x: float, max_x: float, xbase: float = 0.0) -> None:
        """
        Initialize forward gridder class using grid parameters.
        
        Parameter ``xres``:
            x resolution of the grid
        
        Parameter ``min_x``:
            smallest x value that must be contained within the grid
        
        Parameter ``max_x``:
            largest x value that must be contained within the grid
        
        Parameter ``xbase``:
            x base position of the grid, by default 0.0
        """
    def __repr__(self) -> str:
        """
        __repr__(self) -> str
        
        Overloaded function.
        
        1. ``__repr__(self) -> str``
        
        
        2. ``__repr__(self) -> str``
        
        Return object information as string
        """
    def __setstate__(self, arg: bytes) -> None:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def copy(self) -> ForwardGridder1D:
        """
        return a copy using the c++ default copy constructor
        """
    def get_border_xmax(self) -> float:
        ...
    def get_border_xmin(self) -> float:
        ...
    def get_empty_grd_images(self) -> tuple[numpy.ndarray[dtype=float64, ..., order='A'], numpy.ndarray[dtype=float64, ..., order='A']]:
        """
        Create empty grid images
        
        Returns:
            std::tuple<xt::xtensor<t_float, 1>, xt::xtensor<t_float, 1>>
            image_values, image_weights
        """
    def get_extent(self, axis: str = 'x') -> list[float]:
        ...
    def get_extent_x(self) -> list[float]:
        ...
    def get_nx(self) -> int:
        ...
    def get_x_coordinates(self) -> list[float]:
        ...
    def get_x_grd_value(self, x: float) -> float:
        """
        get_x_grd_value(self, x: numpy.ndarray[dtype=float64, shape=(*), order='A']) -> numpy.ndarray[dtype=float64, shape=(*), order='A']
        """
    def get_x_index(self, x: float) -> int:
        """
        get_x_index(self, x: numpy.ndarray[dtype=float64, shape=(*), order='A']) -> numpy.ndarray[dtype=int32, shape=(*), order='A']
        """
    def get_x_index_fraction(self, x: float) -> float:
        """
        get_x_index_fraction(self, x: numpy.ndarray[dtype=float64, shape=(*), order='A']) -> numpy.ndarray[dtype=float64, shape=(*), order='A']
        """
    def get_x_value(self, x_index: int) -> float:
        """
        get_x_value(self, x_index: numpy.ndarray[dtype=int32, shape=(*), order='A']) -> numpy.ndarray[dtype=float64, shape=(*), order='A']
        """
    def get_xbase(self) -> float:
        ...
    def get_xmax(self) -> float:
        ...
    def get_xmin(self) -> float:
        ...
    def get_xres(self) -> float:
        ...
    def group_blocks(self, sx: numpy.ndarray[dtype=float64, ..., order='A'], sv: numpy.ndarray[dtype=float64, ..., order='A']) -> ...:
        ...
    def hash(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def interpolate_block_mean(self, sx: numpy.ndarray[dtype=float64, ..., order='A'], s_val: numpy.ndarray[dtype=float64, ..., order='A']) -> tuple[numpy.ndarray[dtype=float64, ..., order='A'], numpy.ndarray[dtype=float64, ..., order='A']]:
        """
        Interpolate 1D points onto 1d images using block mean interpolation
        
        Template parameter ``T_vector``:
            $Parameter ``sx``:
        
        x values
        
        Parameter ``s_val``:
            amplitudes / volume backscattering coefficients
        
        Parameter ``image_values``:
            Image with values. If empty a new image will be created.
        
        Parameter ``image_weights``:
            Image with weights. If empty a new image will be created.
        
        Returns:
            std::tuple<xt::xtensor<t_float, 1>, xt::xtensor<t_float, 1>>
            image_values, image_weights
        """
    def interpolate_block_mean_inplace(self, sx: numpy.ndarray[dtype=float64, ..., order='A'], s_val: numpy.ndarray[dtype=float64, ..., order='A'], image_values: numpy.ndarray[dtype=float64, ..., order='A'], image_weights: numpy.ndarray[dtype=float64, ..., order='A']) -> None:
        """
        Interpolate 1D points onto 1d images using block mean interpolation
        (inplace version)
        
        Template parameter ``T_vector``:
            $Parameter ``sx``:
        
        x values
        
        Parameter ``s_val``:
            amplitudes / volume backscattering coefficients
        
        Parameter ``image_values``:
            Image with values will be edited inplace
        
        Parameter ``image_weights``:
            Image with weights will be edited inplace
        
        Returns:
            std::tuple<xt::xtensor<t_float, 1>, xt::xtensor<t_float, 1>>
            image_values, image_weights
        """
    def interpolate_weighted_mean(self, sx: numpy.ndarray[dtype=float64, ..., order='A'], s_val: numpy.ndarray[dtype=float64, ..., order='A']) -> tuple[numpy.ndarray[dtype=float64, ..., order='A'], numpy.ndarray[dtype=float64, ..., order='A']]:
        """
        Interpolate 1D points onto 1d images using weighted mean interpolation
        
        Template parameter ``T_vector``:
            $Parameter ``sx``:
        
        x values
        
        Parameter ``s_val``:
            amplitudes / volume backscattering coefficients
        
        Returns:
            std::tuple<xt::xtensor<t_float, 1>, xt::xtensor<t_float, 1>>
            image_values, image_weights
        """
    def interpolate_weighted_mean_inplace(self, sx: numpy.ndarray[dtype=float64, ..., order='A'], s_val: numpy.ndarray[dtype=float64, ..., order='A'], image_values: numpy.ndarray[dtype=float64, ..., order='A'], image_weights: numpy.ndarray[dtype=float64, ..., order='A']) -> None:
        """
        Interpolate 1D points onto 1d images using weighted mean interpolation
        
        Template parameter ``T_vector``:
            $Parameter ``sx``:
        
        x values
        
        Parameter ``s_val``:
            amplitudes / volume backscattering coefficients
        
        Parameter ``image_values``:
            Image with values. If empty a new image will be created.
        
        Parameter ``image_weights``:
            Image with weights. If empty a new image will be created.
        
        Returns:
            std::tuple<xt::xtensor<t_float, 1>, xt::xtensor<t_float, 1>>
            image_values, image_weights
        """
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
class ForwardGridder1DF:
    """
    Simple class to generate 1D grids and interpolate x data onto a grid
    using simple forward mapping algorithms (e.g. block mean, weighted
    mean interpolation)
    """
    from_binary: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    from_data: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    from_res: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    get_minmax: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __copy__(self) -> ForwardGridder1DF:
        ...
    def __deepcopy__(self, arg: dict) -> ForwardGridder1DF:
        ...
    def __eq__(self, other: ForwardGridder1DF) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def __init__(self, xres: float, min_x: float, max_x: float, xbase: float = 0.0) -> None:
        """
        Initialize forward gridder class using grid parameters.
        
        Parameter ``xres``:
            x resolution of the grid
        
        Parameter ``min_x``:
            smallest x value that must be contained within the grid
        
        Parameter ``max_x``:
            largest x value that must be contained within the grid
        
        Parameter ``xbase``:
            x base position of the grid, by default 0.0
        """
    def __repr__(self) -> str:
        """
        __repr__(self) -> str
        
        Overloaded function.
        
        1. ``__repr__(self) -> str``
        
        
        2. ``__repr__(self) -> str``
        
        Return object information as string
        """
    def __setstate__(self, arg: bytes) -> None:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def copy(self) -> ForwardGridder1DF:
        """
        return a copy using the c++ default copy constructor
        """
    def get_border_xmax(self) -> float:
        ...
    def get_border_xmin(self) -> float:
        ...
    def get_empty_grd_images(self) -> tuple[numpy.ndarray[dtype=float32, ..., order='A'], numpy.ndarray[dtype=float32, ..., order='A']]:
        """
        Create empty grid images
        
        Returns:
            std::tuple<xt::xtensor<t_float, 1>, xt::xtensor<t_float, 1>>
            image_values, image_weights
        """
    def get_extent(self, axis: str = 'x') -> list[float]:
        ...
    def get_extent_x(self) -> list[float]:
        ...
    def get_nx(self) -> int:
        ...
    def get_x_coordinates(self) -> list[float]:
        ...
    def get_x_grd_value(self, x: float) -> float:
        """
        get_x_grd_value(self, x: numpy.ndarray[dtype=float32, shape=(*), order='A']) -> numpy.ndarray[dtype=float32, shape=(*), order='A']
        """
    def get_x_index(self, x: float) -> int:
        """
        get_x_index(self, x: numpy.ndarray[dtype=float32, shape=(*), order='A']) -> numpy.ndarray[dtype=int32, shape=(*), order='A']
        """
    def get_x_index_fraction(self, x: float) -> float:
        """
        get_x_index_fraction(self, x: numpy.ndarray[dtype=float32, shape=(*), order='A']) -> numpy.ndarray[dtype=float32, shape=(*), order='A']
        """
    def get_x_value(self, x_index: int) -> float:
        """
        get_x_value(self, x_index: numpy.ndarray[dtype=int32, shape=(*), order='A']) -> numpy.ndarray[dtype=float32, shape=(*), order='A']
        """
    def get_xbase(self) -> float:
        ...
    def get_xmax(self) -> float:
        ...
    def get_xmin(self) -> float:
        ...
    def get_xres(self) -> float:
        ...
    def group_blocks(self, sx: numpy.ndarray[dtype=float32, ..., order='A'], sv: numpy.ndarray[dtype=float32, ..., order='A']) -> ...:
        ...
    def hash(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def interpolate_block_mean(self, sx: numpy.ndarray[dtype=float32, ..., order='A'], s_val: numpy.ndarray[dtype=float32, ..., order='A']) -> tuple[numpy.ndarray[dtype=float32, ..., order='A'], numpy.ndarray[dtype=float32, ..., order='A']]:
        """
        Interpolate 1D points onto 1d images using block mean interpolation
        
        Template parameter ``T_vector``:
            $Parameter ``sx``:
        
        x values
        
        Parameter ``s_val``:
            amplitudes / volume backscattering coefficients
        
        Parameter ``image_values``:
            Image with values. If empty a new image will be created.
        
        Parameter ``image_weights``:
            Image with weights. If empty a new image will be created.
        
        Returns:
            std::tuple<xt::xtensor<t_float, 1>, xt::xtensor<t_float, 1>>
            image_values, image_weights
        """
    def interpolate_block_mean_inplace(self, sx: numpy.ndarray[dtype=float32, ..., order='A'], s_val: numpy.ndarray[dtype=float32, ..., order='A'], image_values: numpy.ndarray[dtype=float32, ..., order='A'], image_weights: numpy.ndarray[dtype=float32, ..., order='A']) -> None:
        """
        Interpolate 1D points onto 1d images using block mean interpolation
        (inplace version)
        
        Template parameter ``T_vector``:
            $Parameter ``sx``:
        
        x values
        
        Parameter ``s_val``:
            amplitudes / volume backscattering coefficients
        
        Parameter ``image_values``:
            Image with values will be edited inplace
        
        Parameter ``image_weights``:
            Image with weights will be edited inplace
        
        Returns:
            std::tuple<xt::xtensor<t_float, 1>, xt::xtensor<t_float, 1>>
            image_values, image_weights
        """
    def interpolate_weighted_mean(self, sx: numpy.ndarray[dtype=float32, ..., order='A'], s_val: numpy.ndarray[dtype=float32, ..., order='A']) -> tuple[numpy.ndarray[dtype=float32, ..., order='A'], numpy.ndarray[dtype=float32, ..., order='A']]:
        """
        Interpolate 1D points onto 1d images using weighted mean interpolation
        
        Template parameter ``T_vector``:
            $Parameter ``sx``:
        
        x values
        
        Parameter ``s_val``:
            amplitudes / volume backscattering coefficients
        
        Returns:
            std::tuple<xt::xtensor<t_float, 1>, xt::xtensor<t_float, 1>>
            image_values, image_weights
        """
    def interpolate_weighted_mean_inplace(self, sx: numpy.ndarray[dtype=float32, ..., order='A'], s_val: numpy.ndarray[dtype=float32, ..., order='A'], image_values: numpy.ndarray[dtype=float32, ..., order='A'], image_weights: numpy.ndarray[dtype=float32, ..., order='A']) -> None:
        """
        Interpolate 1D points onto 1d images using weighted mean interpolation
        
        Template parameter ``T_vector``:
            $Parameter ``sx``:
        
        x values
        
        Parameter ``s_val``:
            amplitudes / volume backscattering coefficients
        
        Parameter ``image_values``:
            Image with values. If empty a new image will be created.
        
        Parameter ``image_weights``:
            Image with weights. If empty a new image will be created.
        
        Returns:
            std::tuple<xt::xtensor<t_float, 1>, xt::xtensor<t_float, 1>>
            image_values, image_weights
        """
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
class ForwardGridder2D:
    """
    Simple class to generate 2D grids (images) and interpolate xy data
    onto a grid using simple forward mapping algorithms (e.g. block mean,
    weighted mean interpolation)
    """
    from_binary: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    from_data: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    from_res: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    get_minmax: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __copy__(self) -> ForwardGridder2D:
        ...
    def __deepcopy__(self, arg: dict) -> ForwardGridder2D:
        ...
    def __eq__(self, other: ForwardGridder2D) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def __init__(self, xres: float, yres: float, min_x: float, max_x: float, min_y: float, max_y: float, xbase: float = 0.0, ybase: float = 0.0) -> None:
        """
        Initialize forward gridder class using grid parameters.
        
        Parameter ``xres``:
            x resolution of the grid
        
        Parameter ``yres``:
            y resolution of the grid
        
        Parameter ``min_x``:
            smallest x value that must be contained within the grid
        
        Parameter ``max_x``:
            largest x value that must be contained within the grid
        
        Parameter ``min_y``:
            smallest y value that must be contained within the grid
        
        Parameter ``max_y``:
            largest y value that must be contained within the grid
        
        Parameter ``xbase``:
            x base position of the grid, by default 0.0
        
        Parameter ``ybase``:
            y base position of the grid, by default 0.0
        """
    def __repr__(self) -> str:
        """
        __repr__(self) -> str
        
        Overloaded function.
        
        1. ``__repr__(self) -> str``
        
        
        2. ``__repr__(self) -> str``
        
        Return object information as string
        """
    def __setstate__(self, arg: bytes) -> None:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def copy(self) -> ForwardGridder2D:
        """
        return a copy using the c++ default copy constructor
        """
    def get_border_xmax(self) -> float:
        ...
    def get_border_xmin(self) -> float:
        ...
    def get_border_ymax(self) -> float:
        ...
    def get_border_ymin(self) -> float:
        ...
    def get_empty_grd_images(self) -> tuple[numpy.ndarray[dtype=float64, ..., order='A'], numpy.ndarray[dtype=float64, ..., order='A']]:
        """
        Create empty grid images
        
        Returns:
            std::tuple<xt::xtensor<t_float, 2>, xt::xtensor<t_float, 2>>
            image_values, image_weights
        """
    def get_extent(self, axis: str = 'xy') -> list[float]:
        ...
    def get_extent_x(self) -> list[float]:
        ...
    def get_extent_y(self) -> list[float]:
        ...
    def get_nx(self) -> int:
        ...
    def get_ny(self) -> int:
        ...
    def get_x_coordinates(self) -> list[float]:
        ...
    def get_x_grd_value(self, x: float) -> float:
        """
        get_x_grd_value(self, x: numpy.ndarray[dtype=float64, shape=(*), order='A']) -> numpy.ndarray[dtype=float64, shape=(*), order='A']
        """
    def get_x_index(self, x: float) -> int:
        """
        get_x_index(self, x: numpy.ndarray[dtype=float64, shape=(*), order='A']) -> numpy.ndarray[dtype=int32, shape=(*), order='A']
        """
    def get_x_index_fraction(self, x: float) -> float:
        """
        get_x_index_fraction(self, x: numpy.ndarray[dtype=float64, shape=(*), order='A']) -> numpy.ndarray[dtype=float64, shape=(*), order='A']
        """
    def get_x_value(self, x_index: int) -> float:
        """
        get_x_value(self, x_index: numpy.ndarray[dtype=int32, shape=(*), order='A']) -> numpy.ndarray[dtype=float64, shape=(*), order='A']
        """
    def get_xbase(self) -> float:
        ...
    def get_xmax(self) -> float:
        ...
    def get_xmin(self) -> float:
        ...
    def get_xres(self) -> float:
        ...
    def get_y_coordinates(self) -> list[float]:
        ...
    def get_y_grd_value(self, y: float) -> float:
        """
        get_y_grd_value(self, y: numpy.ndarray[dtype=float64, shape=(*), order='A']) -> numpy.ndarray[dtype=float64, shape=(*), order='A']
        """
    def get_y_index(self, y: float) -> int:
        """
        get_y_index(self, y: numpy.ndarray[dtype=float64, shape=(*), order='A']) -> numpy.ndarray[dtype=int32, shape=(*), order='A']
        """
    def get_y_index_fraction(self, y: float) -> float:
        """
        get_y_index_fraction(self, y: numpy.ndarray[dtype=float64, shape=(*), order='A']) -> numpy.ndarray[dtype=float64, shape=(*), order='A']
        """
    def get_y_value(self, y_index: int) -> float:
        """
        get_y_value(self, y_index: numpy.ndarray[dtype=int32, shape=(*), order='A']) -> numpy.ndarray[dtype=float64, shape=(*), order='A']
        """
    def get_ybase(self) -> float:
        ...
    def get_ymax(self) -> float:
        ...
    def get_ymin(self) -> float:
        ...
    def get_yres(self) -> float:
        ...
    def group_blocks(self, sx: numpy.ndarray[dtype=float64, ..., order='A'], sy: numpy.ndarray[dtype=float64, ..., order='A'], sv: numpy.ndarray[dtype=float64, ..., order='A']) -> ...:
        ...
    def hash(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def interpolate_block_mean(self, sx: numpy.ndarray[dtype=float64, ..., order='A'], sy: numpy.ndarray[dtype=float64, ..., order='A'], s_val: numpy.ndarray[dtype=float64, ..., order='A']) -> tuple[numpy.ndarray[dtype=float64, ..., order='A'], numpy.ndarray[dtype=float64, ..., order='A']]:
        """
        Interpolate 2D points onto 2d images using block mean interpolation
        
        Template parameter ``T_vector``:
            $Parameter ``sx``:
        
        x values
        
        Parameter ``sy``:
            y values
        
        Parameter ``s_val``:
            amplitudes / volume backscattering coefficients
        
        Returns:
            std::tuple<xt::xtensor<t_float, 2>, xt::xtensor<t_float, 2>>
            image_values, image_weights
        """
    def interpolate_block_mean_inplace(self, sx: numpy.ndarray[dtype=float64, ..., order='A'], sy: numpy.ndarray[dtype=float64, ..., order='A'], s_val: numpy.ndarray[dtype=float64, ..., order='A'], image_values: numpy.ndarray[dtype=float64, ..., order='A'], image_weights: numpy.ndarray[dtype=float64, ..., order='A']) -> None:
        """
        Interpolate 2D points onto 2d images using block mean interpolation
        (inplace version)
        
        Template parameter ``T_vector``:
            $Parameter ``sx``:
        
        x values
        
        Parameter ``sy``:
            y values
        
        Parameter ``s_val``:
            amplitudes / volume backscattering coefficients
        
        Parameter ``image_values``:
            Image with values will be edited inplace
        
        Parameter ``image_weights``:
            Image with weights will be edited inplace
        """
    def interpolate_weighted_mean(self, sx: numpy.ndarray[dtype=float64, ..., order='A'], sy: numpy.ndarray[dtype=float64, ..., order='A'], s_val: numpy.ndarray[dtype=float64, ..., order='A']) -> tuple[numpy.ndarray[dtype=float64, ..., order='A'], numpy.ndarray[dtype=float64, ..., order='A']]:
        """
        Interpolate 2D points onto 2d images using weighted mean interpolation
        
        Template parameter ``T_vector``:
            $Parameter ``sx``:
        
        x values
        
        Parameter ``sy``:
            y values
        
        Parameter ``s_val``:
            amplitudes / volume backscattering coefficients
        
        Returns:
            std::tuple<xt::xtensor<t_float, 2>, xt::xtensor<t_float, 2>>
            image_values, image_weights
        """
    def interpolate_weighted_mean_inplace(self, sx: numpy.ndarray[dtype=float64, ..., order='A'], sy: numpy.ndarray[dtype=float64, ..., order='A'], s_val: numpy.ndarray[dtype=float64, ..., order='A'], image_values: numpy.ndarray[dtype=float64, ..., order='A'], image_weights: numpy.ndarray[dtype=float64, ..., order='A']) -> None:
        """
        Interpolate 2D points onto 2d images using weighted mean interpolation
        (inplace version)
        
        Template parameter ``T_vector``:
            $Parameter ``sx``:
        
        x values
        
        Parameter ``sy``:
            y values
        
        Parameter ``s_val``:
            amplitudes / volume backscattering coefficients
        
        Parameter ``image_values``:
            Image with values will be edited inplace
        
        Parameter ``image_weights``:
            Image with weights will be edited inplace
        """
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
class ForwardGridder2DF:
    """
    Simple class to generate 2D grids (images) and interpolate xy data
    onto a grid using simple forward mapping algorithms (e.g. block mean,
    weighted mean interpolation)
    """
    from_binary: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    from_data: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    from_res: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    get_minmax: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __copy__(self) -> ForwardGridder2DF:
        ...
    def __deepcopy__(self, arg: dict) -> ForwardGridder2DF:
        ...
    def __eq__(self, other: ForwardGridder2DF) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def __init__(self, xres: float, yres: float, min_x: float, max_x: float, min_y: float, max_y: float, xbase: float = 0.0, ybase: float = 0.0) -> None:
        """
        Initialize forward gridder class using grid parameters.
        
        Parameter ``xres``:
            x resolution of the grid
        
        Parameter ``yres``:
            y resolution of the grid
        
        Parameter ``min_x``:
            smallest x value that must be contained within the grid
        
        Parameter ``max_x``:
            largest x value that must be contained within the grid
        
        Parameter ``min_y``:
            smallest y value that must be contained within the grid
        
        Parameter ``max_y``:
            largest y value that must be contained within the grid
        
        Parameter ``xbase``:
            x base position of the grid, by default 0.0
        
        Parameter ``ybase``:
            y base position of the grid, by default 0.0
        """
    def __repr__(self) -> str:
        """
        __repr__(self) -> str
        
        Overloaded function.
        
        1. ``__repr__(self) -> str``
        
        
        2. ``__repr__(self) -> str``
        
        Return object information as string
        """
    def __setstate__(self, arg: bytes) -> None:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def copy(self) -> ForwardGridder2DF:
        """
        return a copy using the c++ default copy constructor
        """
    def get_border_xmax(self) -> float:
        ...
    def get_border_xmin(self) -> float:
        ...
    def get_border_ymax(self) -> float:
        ...
    def get_border_ymin(self) -> float:
        ...
    def get_empty_grd_images(self) -> tuple[numpy.ndarray[dtype=float32, ..., order='A'], numpy.ndarray[dtype=float32, ..., order='A']]:
        """
        Create empty grid images
        
        Returns:
            std::tuple<xt::xtensor<t_float, 2>, xt::xtensor<t_float, 2>>
            image_values, image_weights
        """
    def get_extent(self, axis: str = 'xy') -> list[float]:
        ...
    def get_extent_x(self) -> list[float]:
        ...
    def get_extent_y(self) -> list[float]:
        ...
    def get_nx(self) -> int:
        ...
    def get_ny(self) -> int:
        ...
    def get_x_coordinates(self) -> list[float]:
        ...
    def get_x_grd_value(self, x: float) -> float:
        """
        get_x_grd_value(self, x: numpy.ndarray[dtype=float32, shape=(*), order='A']) -> numpy.ndarray[dtype=float32, shape=(*), order='A']
        """
    def get_x_index(self, x: float) -> int:
        """
        get_x_index(self, x: numpy.ndarray[dtype=float32, shape=(*), order='A']) -> numpy.ndarray[dtype=int32, shape=(*), order='A']
        """
    def get_x_index_fraction(self, x: float) -> float:
        """
        get_x_index_fraction(self, x: numpy.ndarray[dtype=float32, shape=(*), order='A']) -> numpy.ndarray[dtype=float32, shape=(*), order='A']
        """
    def get_x_value(self, x_index: int) -> float:
        """
        get_x_value(self, x_index: numpy.ndarray[dtype=int32, shape=(*), order='A']) -> numpy.ndarray[dtype=float32, shape=(*), order='A']
        """
    def get_xbase(self) -> float:
        ...
    def get_xmax(self) -> float:
        ...
    def get_xmin(self) -> float:
        ...
    def get_xres(self) -> float:
        ...
    def get_y_coordinates(self) -> list[float]:
        ...
    def get_y_grd_value(self, y: float) -> float:
        """
        get_y_grd_value(self, y: numpy.ndarray[dtype=float32, shape=(*), order='A']) -> numpy.ndarray[dtype=float32, shape=(*), order='A']
        """
    def get_y_index(self, y: float) -> int:
        """
        get_y_index(self, y: numpy.ndarray[dtype=float32, shape=(*), order='A']) -> numpy.ndarray[dtype=int32, shape=(*), order='A']
        """
    def get_y_index_fraction(self, y: float) -> float:
        """
        get_y_index_fraction(self, y: numpy.ndarray[dtype=float32, shape=(*), order='A']) -> numpy.ndarray[dtype=float32, shape=(*), order='A']
        """
    def get_y_value(self, y_index: int) -> float:
        """
        get_y_value(self, y_index: numpy.ndarray[dtype=int32, shape=(*), order='A']) -> numpy.ndarray[dtype=float32, shape=(*), order='A']
        """
    def get_ybase(self) -> float:
        ...
    def get_ymax(self) -> float:
        ...
    def get_ymin(self) -> float:
        ...
    def get_yres(self) -> float:
        ...
    def group_blocks(self, sx: numpy.ndarray[dtype=float32, ..., order='A'], sy: numpy.ndarray[dtype=float32, ..., order='A'], sv: numpy.ndarray[dtype=float32, ..., order='A']) -> ...:
        ...
    def hash(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def interpolate_block_mean(self, sx: numpy.ndarray[dtype=float32, ..., order='A'], sy: numpy.ndarray[dtype=float32, ..., order='A'], s_val: numpy.ndarray[dtype=float32, ..., order='A']) -> tuple[numpy.ndarray[dtype=float32, ..., order='A'], numpy.ndarray[dtype=float32, ..., order='A']]:
        """
        Interpolate 2D points onto 2d images using block mean interpolation
        
        Template parameter ``T_vector``:
            $Parameter ``sx``:
        
        x values
        
        Parameter ``sy``:
            y values
        
        Parameter ``s_val``:
            amplitudes / volume backscattering coefficients
        
        Returns:
            std::tuple<xt::xtensor<t_float, 2>, xt::xtensor<t_float, 2>>
            image_values, image_weights
        """
    def interpolate_block_mean_inplace(self, sx: numpy.ndarray[dtype=float32, ..., order='A'], sy: numpy.ndarray[dtype=float32, ..., order='A'], s_val: numpy.ndarray[dtype=float32, ..., order='A'], image_values: numpy.ndarray[dtype=float32, ..., order='A'], image_weights: numpy.ndarray[dtype=float32, ..., order='A']) -> None:
        """
        Interpolate 2D points onto 2d images using block mean interpolation
        (inplace version)
        
        Template parameter ``T_vector``:
            $Parameter ``sx``:
        
        x values
        
        Parameter ``sy``:
            y values
        
        Parameter ``s_val``:
            amplitudes / volume backscattering coefficients
        
        Parameter ``image_values``:
            Image with values will be edited inplace
        
        Parameter ``image_weights``:
            Image with weights will be edited inplace
        """
    def interpolate_weighted_mean(self, sx: numpy.ndarray[dtype=float32, ..., order='A'], sy: numpy.ndarray[dtype=float32, ..., order='A'], s_val: numpy.ndarray[dtype=float32, ..., order='A']) -> tuple[numpy.ndarray[dtype=float32, ..., order='A'], numpy.ndarray[dtype=float32, ..., order='A']]:
        """
        Interpolate 2D points onto 2d images using weighted mean interpolation
        
        Template parameter ``T_vector``:
            $Parameter ``sx``:
        
        x values
        
        Parameter ``sy``:
            y values
        
        Parameter ``s_val``:
            amplitudes / volume backscattering coefficients
        
        Returns:
            std::tuple<xt::xtensor<t_float, 2>, xt::xtensor<t_float, 2>>
            image_values, image_weights
        """
    def interpolate_weighted_mean_inplace(self, sx: numpy.ndarray[dtype=float32, ..., order='A'], sy: numpy.ndarray[dtype=float32, ..., order='A'], s_val: numpy.ndarray[dtype=float32, ..., order='A'], image_values: numpy.ndarray[dtype=float32, ..., order='A'], image_weights: numpy.ndarray[dtype=float32, ..., order='A']) -> None:
        """
        Interpolate 2D points onto 2d images using weighted mean interpolation
        (inplace version)
        
        Template parameter ``T_vector``:
            $Parameter ``sx``:
        
        x values
        
        Parameter ``sy``:
            y values
        
        Parameter ``s_val``:
            amplitudes / volume backscattering coefficients
        
        Parameter ``image_values``:
            Image with values will be edited inplace
        
        Parameter ``image_weights``:
            Image with weights will be edited inplace
        """
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
class ForwardGridder3D:
    """
    Simple class to generate 3D grids (images) and interpolate xyz data
    onto a grid using simple forward mapping algorithms (e.g. block mean,
    weighted mean interpolation)
    """
    from_binary: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    from_data: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    from_res: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    get_minmax: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __copy__(self) -> ForwardGridder3D:
        ...
    def __deepcopy__(self, arg: dict) -> ForwardGridder3D:
        ...
    def __eq__(self, other: ForwardGridder3D) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def __init__(self, xres: float, yres: float, zres: float, min_x: float, max_x: float, min_y: float, max_y: float, min_z: float, max_z: float, xbase: float = 0.0, ybase: float = 0.0, zbase: float = 0.0) -> None:
        """
        Initialize forward gridder class using grid parameters.
        
        Parameter ``xres``:
            x resolution of the grid
        
        Parameter ``yres``:
            y resolution of the grid
        
        Parameter ``zres``:
            z resolution of the grid
        
        Parameter ``min_x``:
            smallest x value that must be contained within the grid
        
        Parameter ``max_x``:
            largest x value that must be contained within the grid
        
        Parameter ``min_y``:
            smallest y value that must be contained within the grid
        
        Parameter ``max_y``:
            largest y value that must be contained within the grid
        
        Parameter ``min_z``:
            smallest z value that must be contained within the grid
        
        Parameter ``max_z``:
            largest z value that must be contained within the grid
        
        Parameter ``xbase``:
            x base position of the grid, by default 0.0
        
        Parameter ``ybase``:
            y base position of the grid, by default 0.0
        
        Parameter ``zbase``:
            z base position of the grid, by default 0.0
        """
    def __repr__(self) -> str:
        """
        __repr__(self) -> str
        
        Overloaded function.
        
        1. ``__repr__(self) -> str``
        
        
        2. ``__repr__(self) -> str``
        
        Return object information as string
        """
    def __setstate__(self, arg: bytes) -> None:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def copy(self) -> ForwardGridder3D:
        """
        return a copy using the c++ default copy constructor
        """
    def get_border_xmax(self) -> float:
        ...
    def get_border_xmin(self) -> float:
        ...
    def get_border_ymax(self) -> float:
        ...
    def get_border_ymin(self) -> float:
        ...
    def get_border_zmax(self) -> float:
        ...
    def get_border_zmin(self) -> float:
        ...
    def get_empty_grd_images(self) -> tuple[numpy.ndarray[dtype=float64, ..., order='A'], numpy.ndarray[dtype=float64, ..., order='A']]:
        """
        Create empty grid images
        
        Returns:
            std::tuple<xt::xtensor<t_float, 3>, xt::xtensor<t_float, 3>>
            image_values, image_weights
        """
    def get_extent(self, axis: str = 'xyz') -> list[float]:
        ...
    def get_extent_x(self) -> list[float]:
        ...
    def get_extent_y(self) -> list[float]:
        ...
    def get_extent_z(self) -> list[float]:
        ...
    def get_nx(self) -> int:
        ...
    def get_ny(self) -> int:
        ...
    def get_nz(self) -> int:
        ...
    def get_x_coordinates(self) -> list[float]:
        ...
    def get_x_grd_value(self, x: float) -> float:
        """
        get_x_grd_value(self, x: numpy.ndarray[dtype=float64, shape=(*), order='A']) -> numpy.ndarray[dtype=float64, shape=(*), order='A']
        """
    def get_x_index(self, x: float) -> int:
        """
        get_x_index(self, x: numpy.ndarray[dtype=float64, shape=(*), order='A']) -> numpy.ndarray[dtype=int32, shape=(*), order='A']
        """
    def get_x_index_fraction(self, x: float) -> float:
        """
        get_x_index_fraction(self, x: numpy.ndarray[dtype=float64, shape=(*), order='A']) -> numpy.ndarray[dtype=float64, shape=(*), order='A']
        """
    def get_x_value(self, x_index: int) -> float:
        """
        get_x_value(self, x_index: numpy.ndarray[dtype=int32, shape=(*), order='A']) -> numpy.ndarray[dtype=float64, shape=(*), order='A']
        """
    def get_xbase(self) -> float:
        ...
    def get_xmax(self) -> float:
        ...
    def get_xmin(self) -> float:
        ...
    def get_xres(self) -> float:
        ...
    def get_y_coordinates(self) -> list[float]:
        ...
    def get_y_grd_value(self, y: float) -> float:
        """
        get_y_grd_value(self, y: numpy.ndarray[dtype=float64, shape=(*), order='A']) -> numpy.ndarray[dtype=float64, shape=(*), order='A']
        """
    def get_y_index(self, y: float) -> int:
        """
        get_y_index(self, y: numpy.ndarray[dtype=float64, shape=(*), order='A']) -> numpy.ndarray[dtype=int32, shape=(*), order='A']
        """
    def get_y_index_fraction(self, y: float) -> float:
        """
        get_y_index_fraction(self, y: numpy.ndarray[dtype=float64, shape=(*), order='A']) -> numpy.ndarray[dtype=float64, shape=(*), order='A']
        """
    def get_y_value(self, y_index: int) -> float:
        """
        get_y_value(self, y_index: numpy.ndarray[dtype=int32, shape=(*), order='A']) -> numpy.ndarray[dtype=float64, shape=(*), order='A']
        """
    def get_ybase(self) -> float:
        ...
    def get_ymax(self) -> float:
        ...
    def get_ymin(self) -> float:
        ...
    def get_yres(self) -> float:
        ...
    def get_z_coordinates(self) -> list[float]:
        ...
    def get_z_grd_value(self, z: float) -> float:
        """
        get_z_grd_value(self, z: numpy.ndarray[dtype=float64, shape=(*), order='A']) -> numpy.ndarray[dtype=float64, shape=(*), order='A']
        """
    def get_z_index(self, z: float) -> int:
        """
        get_z_index(self, z: numpy.ndarray[dtype=float64, shape=(*), order='A']) -> numpy.ndarray[dtype=int32, shape=(*), order='A']
        """
    def get_z_index_fraction(self, z: float) -> float:
        """
        get_z_index_fraction(self, z: numpy.ndarray[dtype=float64, shape=(*), order='A']) -> numpy.ndarray[dtype=float64, shape=(*), order='A']
        """
    def get_z_value(self, z_index: int) -> float:
        """
        get_z_value(self, z_index: numpy.ndarray[dtype=int32, shape=(*), order='A']) -> numpy.ndarray[dtype=float64, shape=(*), order='A']
        """
    def get_zbase(self) -> float:
        ...
    def get_zmax(self) -> float:
        ...
    def get_zmin(self) -> float:
        ...
    def get_zres(self) -> float:
        ...
    def group_blocks(self, sx: numpy.ndarray[dtype=float64, ..., order='A'], sy: numpy.ndarray[dtype=float64, ..., order='A'], sz: numpy.ndarray[dtype=float64, ..., order='A'], sv: numpy.ndarray[dtype=float64, ..., order='A']) -> ...:
        ...
    def hash(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def interpolate_block_mean(self, sx: numpy.ndarray[dtype=float64, ..., order='A'], sy: numpy.ndarray[dtype=float64, ..., order='A'], sz: numpy.ndarray[dtype=float64, ..., order='A'], s_val: numpy.ndarray[dtype=float64, ..., order='A']) -> tuple[numpy.ndarray[dtype=float64, ..., order='A'], numpy.ndarray[dtype=float64, ..., order='A']]:
        """
        Interpolate 3D points onto 3d images using block mean interpolation
        
        Template parameter ``T_vector``:
            $Parameter ``sx``:
        
        x values
        
        Parameter ``sy``:
            y values
        
        Parameter ``sz``:
            z values
        
        Parameter ``s_val``:
            amplitudes / volume backscattering coefficients
        
        Returns:
            std::tuple<xt::xtensor<t_float, 3>, xt::xtensor<t_float, 3>>
            image_values, image_weights
        """
    def interpolate_block_mean_inplace(self, sx: numpy.ndarray[dtype=float64, ..., order='A'], sy: numpy.ndarray[dtype=float64, ..., order='A'], sz: numpy.ndarray[dtype=float64, ..., order='A'], s_val: numpy.ndarray[dtype=float64, ..., order='A'], image_values: numpy.ndarray[dtype=float64, ..., order='A'], image_weights: numpy.ndarray[dtype=float64, ..., order='A']) -> None:
        """
        Interpolate 3D points onto 3d images using block mean interpolation
        (inplace version)
        
        Template parameter ``T_vector``:
            $Parameter ``sx``:
        
        x values
        
        Parameter ``sy``:
            y values
        
        Parameter ``sz``:
            z values
        
        Parameter ``s_val``:
            amplitudes / volume backscattering coefficients
        
        Parameter ``image_values``:
            Image with values will be edited inplace
        
        Parameter ``image_weights``:
            Image with weights will be edited inplace
        """
    def interpolate_weighted_mean(self, sx: numpy.ndarray[dtype=float64, ..., order='A'], sy: numpy.ndarray[dtype=float64, ..., order='A'], sz: numpy.ndarray[dtype=float64, ..., order='A'], s_val: numpy.ndarray[dtype=float64, ..., order='A']) -> tuple[numpy.ndarray[dtype=float64, ..., order='A'], numpy.ndarray[dtype=float64, ..., order='A']]:
        """
        Interpolate 3D points onto 3d images using weighted mean interpolation
        
        Template parameter ``T_vector``:
            $Parameter ``sx``:
        
        x values
        
        Parameter ``sy``:
            y values
        
        Parameter ``sz``:
            z values
        
        Parameter ``s_val``:
            amplitudes / volume backscattering coefficients
        
        Returns:
            std::tuple<xt::xtensor<t_float, 3>, xt::xtensor<t_float, 3>>
            image_values, image_weights
        """
    def interpolate_weighted_mean_inplace(self, sx: numpy.ndarray[dtype=float64, ..., order='A'], sy: numpy.ndarray[dtype=float64, ..., order='A'], sz: numpy.ndarray[dtype=float64, ..., order='A'], s_val: numpy.ndarray[dtype=float64, ..., order='A'], image_values: numpy.ndarray[dtype=float64, ..., order='A'], image_weights: numpy.ndarray[dtype=float64, ..., order='A']) -> None:
        """
        Interpolate 3D points onto 3d images using weighted mean interpolation
        (inplace version)
        
        Template parameter ``T_vector``:
            $Parameter ``sx``:
        
        x values
        
        Parameter ``sy``:
            y values
        
        Parameter ``sz``:
            z values
        
        Parameter ``s_val``:
            amplitudes / volume backscattering coefficients
        
        Parameter ``image_values``:
            Image with values will be edited inplace
        
        Parameter ``image_weights``:
            Image with weights will be edited inplace
        """
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
class ForwardGridder3DF:
    """
    Simple class to generate 3D grids (images) and interpolate xyz data
    onto a grid using simple forward mapping algorithms (e.g. block mean,
    weighted mean interpolation)
    """
    from_binary: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    from_data: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    from_res: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    get_minmax: typing.ClassVar[nanobind.nb_func]  # value = <nanobind.nb_func object>
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __copy__(self) -> ForwardGridder3DF:
        ...
    def __deepcopy__(self, arg: dict) -> ForwardGridder3DF:
        ...
    def __eq__(self, other: ForwardGridder3DF) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def __init__(self, xres: float, yres: float, zres: float, min_x: float, max_x: float, min_y: float, max_y: float, min_z: float, max_z: float, xbase: float = 0.0, ybase: float = 0.0, zbase: float = 0.0) -> None:
        """
        Initialize forward gridder class using grid parameters.
        
        Parameter ``xres``:
            x resolution of the grid
        
        Parameter ``yres``:
            y resolution of the grid
        
        Parameter ``zres``:
            z resolution of the grid
        
        Parameter ``min_x``:
            smallest x value that must be contained within the grid
        
        Parameter ``max_x``:
            largest x value that must be contained within the grid
        
        Parameter ``min_y``:
            smallest y value that must be contained within the grid
        
        Parameter ``max_y``:
            largest y value that must be contained within the grid
        
        Parameter ``min_z``:
            smallest z value that must be contained within the grid
        
        Parameter ``max_z``:
            largest z value that must be contained within the grid
        
        Parameter ``xbase``:
            x base position of the grid, by default 0.0
        
        Parameter ``ybase``:
            y base position of the grid, by default 0.0
        
        Parameter ``zbase``:
            z base position of the grid, by default 0.0
        """
    def __repr__(self) -> str:
        """
        __repr__(self) -> str
        
        Overloaded function.
        
        1. ``__repr__(self) -> str``
        
        
        2. ``__repr__(self) -> str``
        
        Return object information as string
        """
    def __setstate__(self, arg: bytes) -> None:
        ...
    def __str__(self) -> str:
        """
        Return object information as string
        """
    def copy(self) -> ForwardGridder3DF:
        """
        return a copy using the c++ default copy constructor
        """
    def get_border_xmax(self) -> float:
        ...
    def get_border_xmin(self) -> float:
        ...
    def get_border_ymax(self) -> float:
        ...
    def get_border_ymin(self) -> float:
        ...
    def get_border_zmax(self) -> float:
        ...
    def get_border_zmin(self) -> float:
        ...
    def get_empty_grd_images(self) -> tuple[numpy.ndarray[dtype=float32, ..., order='A'], numpy.ndarray[dtype=float32, ..., order='A']]:
        """
        Create empty grid images
        
        Returns:
            std::tuple<xt::xtensor<t_float, 3>, xt::xtensor<t_float, 3>>
            image_values, image_weights
        """
    def get_extent(self, axis: str = 'xyz') -> list[float]:
        ...
    def get_extent_x(self) -> list[float]:
        ...
    def get_extent_y(self) -> list[float]:
        ...
    def get_extent_z(self) -> list[float]:
        ...
    def get_nx(self) -> int:
        ...
    def get_ny(self) -> int:
        ...
    def get_nz(self) -> int:
        ...
    def get_x_coordinates(self) -> list[float]:
        ...
    def get_x_grd_value(self, x: float) -> float:
        """
        get_x_grd_value(self, x: numpy.ndarray[dtype=float32, shape=(*), order='A']) -> numpy.ndarray[dtype=float32, shape=(*), order='A']
        """
    def get_x_index(self, x: float) -> int:
        """
        get_x_index(self, x: numpy.ndarray[dtype=float32, shape=(*), order='A']) -> numpy.ndarray[dtype=int32, shape=(*), order='A']
        """
    def get_x_index_fraction(self, x: float) -> float:
        """
        get_x_index_fraction(self, x: numpy.ndarray[dtype=float32, shape=(*), order='A']) -> numpy.ndarray[dtype=float32, shape=(*), order='A']
        """
    def get_x_value(self, x_index: int) -> float:
        """
        get_x_value(self, x_index: numpy.ndarray[dtype=int32, shape=(*), order='A']) -> numpy.ndarray[dtype=float32, shape=(*), order='A']
        """
    def get_xbase(self) -> float:
        ...
    def get_xmax(self) -> float:
        ...
    def get_xmin(self) -> float:
        ...
    def get_xres(self) -> float:
        ...
    def get_y_coordinates(self) -> list[float]:
        ...
    def get_y_grd_value(self, y: float) -> float:
        """
        get_y_grd_value(self, y: numpy.ndarray[dtype=float32, shape=(*), order='A']) -> numpy.ndarray[dtype=float32, shape=(*), order='A']
        """
    def get_y_index(self, y: float) -> int:
        """
        get_y_index(self, y: numpy.ndarray[dtype=float32, shape=(*), order='A']) -> numpy.ndarray[dtype=int32, shape=(*), order='A']
        """
    def get_y_index_fraction(self, y: float) -> float:
        """
        get_y_index_fraction(self, y: numpy.ndarray[dtype=float32, shape=(*), order='A']) -> numpy.ndarray[dtype=float32, shape=(*), order='A']
        """
    def get_y_value(self, y_index: int) -> float:
        """
        get_y_value(self, y_index: numpy.ndarray[dtype=int32, shape=(*), order='A']) -> numpy.ndarray[dtype=float32, shape=(*), order='A']
        """
    def get_ybase(self) -> float:
        ...
    def get_ymax(self) -> float:
        ...
    def get_ymin(self) -> float:
        ...
    def get_yres(self) -> float:
        ...
    def get_z_coordinates(self) -> list[float]:
        ...
    def get_z_grd_value(self, z: float) -> float:
        """
        get_z_grd_value(self, z: numpy.ndarray[dtype=float32, shape=(*), order='A']) -> numpy.ndarray[dtype=float32, shape=(*), order='A']
        """
    def get_z_index(self, z: float) -> int:
        """
        get_z_index(self, z: numpy.ndarray[dtype=float32, shape=(*), order='A']) -> numpy.ndarray[dtype=int32, shape=(*), order='A']
        """
    def get_z_index_fraction(self, z: float) -> float:
        """
        get_z_index_fraction(self, z: numpy.ndarray[dtype=float32, shape=(*), order='A']) -> numpy.ndarray[dtype=float32, shape=(*), order='A']
        """
    def get_z_value(self, z_index: int) -> float:
        """
        get_z_value(self, z_index: numpy.ndarray[dtype=int32, shape=(*), order='A']) -> numpy.ndarray[dtype=float32, shape=(*), order='A']
        """
    def get_zbase(self) -> float:
        ...
    def get_zmax(self) -> float:
        ...
    def get_zmin(self) -> float:
        ...
    def get_zres(self) -> float:
        ...
    def group_blocks(self, sx: numpy.ndarray[dtype=float32, ..., order='A'], sy: numpy.ndarray[dtype=float32, ..., order='A'], sz: numpy.ndarray[dtype=float32, ..., order='A'], sv: numpy.ndarray[dtype=float32, ..., order='A']) -> ...:
        ...
    def hash(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def interpolate_block_mean(self, sx: numpy.ndarray[dtype=float32, ..., order='A'], sy: numpy.ndarray[dtype=float32, ..., order='A'], sz: numpy.ndarray[dtype=float32, ..., order='A'], s_val: numpy.ndarray[dtype=float32, ..., order='A']) -> tuple[numpy.ndarray[dtype=float32, ..., order='A'], numpy.ndarray[dtype=float32, ..., order='A']]:
        """
        Interpolate 3D points onto 3d images using block mean interpolation
        
        Template parameter ``T_vector``:
            $Parameter ``sx``:
        
        x values
        
        Parameter ``sy``:
            y values
        
        Parameter ``sz``:
            z values
        
        Parameter ``s_val``:
            amplitudes / volume backscattering coefficients
        
        Returns:
            std::tuple<xt::xtensor<t_float, 3>, xt::xtensor<t_float, 3>>
            image_values, image_weights
        """
    def interpolate_block_mean_inplace(self, sx: numpy.ndarray[dtype=float32, ..., order='A'], sy: numpy.ndarray[dtype=float32, ..., order='A'], sz: numpy.ndarray[dtype=float32, ..., order='A'], s_val: numpy.ndarray[dtype=float32, ..., order='A'], image_values: numpy.ndarray[dtype=float32, ..., order='A'], image_weights: numpy.ndarray[dtype=float32, ..., order='A']) -> None:
        """
        Interpolate 3D points onto 3d images using block mean interpolation
        (inplace version)
        
        Template parameter ``T_vector``:
            $Parameter ``sx``:
        
        x values
        
        Parameter ``sy``:
            y values
        
        Parameter ``sz``:
            z values
        
        Parameter ``s_val``:
            amplitudes / volume backscattering coefficients
        
        Parameter ``image_values``:
            Image with values will be edited inplace
        
        Parameter ``image_weights``:
            Image with weights will be edited inplace
        """
    def interpolate_weighted_mean(self, sx: numpy.ndarray[dtype=float32, ..., order='A'], sy: numpy.ndarray[dtype=float32, ..., order='A'], sz: numpy.ndarray[dtype=float32, ..., order='A'], s_val: numpy.ndarray[dtype=float32, ..., order='A']) -> tuple[numpy.ndarray[dtype=float32, ..., order='A'], numpy.ndarray[dtype=float32, ..., order='A']]:
        """
        Interpolate 3D points onto 3d images using weighted mean interpolation
        
        Template parameter ``T_vector``:
            $Parameter ``sx``:
        
        x values
        
        Parameter ``sy``:
            y values
        
        Parameter ``sz``:
            z values
        
        Parameter ``s_val``:
            amplitudes / volume backscattering coefficients
        
        Returns:
            std::tuple<xt::xtensor<t_float, 3>, xt::xtensor<t_float, 3>>
            image_values, image_weights
        """
    def interpolate_weighted_mean_inplace(self, sx: numpy.ndarray[dtype=float32, ..., order='A'], sy: numpy.ndarray[dtype=float32, ..., order='A'], sz: numpy.ndarray[dtype=float32, ..., order='A'], s_val: numpy.ndarray[dtype=float32, ..., order='A'], image_values: numpy.ndarray[dtype=float32, ..., order='A'], image_weights: numpy.ndarray[dtype=float32, ..., order='A']) -> None:
        """
        Interpolate 3D points onto 3d images using weighted mean interpolation
        (inplace version)
        
        Template parameter ``T_vector``:
            $Parameter ``sx``:
        
        x values
        
        Parameter ``sy``:
            y values
        
        Parameter ``sz``:
            z values
        
        Parameter ``s_val``:
            amplitudes / volume backscattering coefficients
        
        Parameter ``image_values``:
            Image with values will be edited inplace
        
        Parameter ``image_weights``:
            Image with weights will be edited inplace
        """
    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
