"""
Submodule for gridding (raytracers and georefencing) echosounder samples
"""

from typing import Annotated, overload

import numpy
from numpy.typing import NDArray

from . import functions as functions


class ForwardGridder1D:
    """
    Simple class to generate 1D grids and interpolate x data onto a grid
    using simple forward mapping algorithms (e.g. block mean, weighted
    mean interpolation)
    """

    def __init__(self, xres: float, min_x: float, max_x: float, xbase: float = 0.0) -> None:
        """
        Initialize forward gridder class using grid parameters.

        Args:
            xres: x resolution of the grid
            min_x: smallest x value that must be contained within the grid
            max_x: largest x value that must be contained within the grid
            xbase: x base position of the grid, by default 0.0
        """

    @staticmethod
    def from_res(res: float, min_x: float, max_x: float) -> ForwardGridder1D:
        """
        Create gridder setting xres to "res"

        Args:
            res: x resolution of the grid
            min_x: smallest x value that must be contained within the grid
            max_x: largest x value that must be contained within the grid

        Returns:
            ForwardGridder1D object
        """

    @staticmethod
    def from_data(res: float, sx: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')]) -> ForwardGridder1D:
        """
        Create gridder with resolution "res" xmin,xmax are determined to
        exactly contain the given data vector (sx)

        Args:
            res: x resolution of the grid
            sx: array with x data

        Returns:
            ForwardGridder1D object
        """

    def get_empty_grd_images(self) -> tuple[Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')]]:
        """
        Create empty grid images

        Returns:
            std::tuple<xt::xtensor<t_float, 1>, xt::xtensor_t_float_1>
                image_values, image_weights
        """

    def group_blocks(self, sx: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], sv: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')]) -> dict[int, list[float]]: ...

    def interpolate_block_mean(self, sx: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], s_val: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')]) -> tuple[Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')]]:
        """
        Interpolate 1D points onto 1d images using block mean interpolation

        Args:
            sx: x values
            s_val: amplitudes / volume backscattering coefficients
            image_values: Image with values. If empty a new image will be
                          created.
            image_weights: Image with weights. If empty a new image will be
                           created.

        Template Args:
            T_vector: 

        Returns:
            std::tuple<xt::xtensor<t_float, 1>, xt::xtensor_t_float_1>
                image_values, image_weights
        """

    def interpolate_block_mean_inplace(self, sx: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], s_val: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], image_values: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], image_weights: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')]) -> None:
        """
        Interpolate 1D points onto 1d images using block mean interpolation
        (inplace version)

        Args:
            sx: x values
            s_val: amplitudes / volume backscattering coefficients
            image_values: Image with values will be edited inplace
            image_weights: Image with weights will be edited inplace

        Template Args:
            T_vector: 

        Returns:
            std::tuple<xt::xtensor<t_float, 1>, xt::xtensor_t_float_1>
                image_values, image_weights
        """

    def interpolate_weighted_mean(self, sx: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], s_val: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')]) -> tuple[Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')]]:
        """
        Interpolate 1D points onto 1d images using weighted mean interpolation

        Args:
            sx: x values
            s_val: amplitudes / volume backscattering coefficients

        Template Args:
            T_vector: 

        Returns:
            std::tuple<xt::xtensor<t_float, 1>, xt::xtensor_t_float_1>
                image_values, image_weights
        """

    def interpolate_weighted_mean_inplace(self, sx: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], s_val: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], image_values: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], image_weights: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')]) -> None:
        """
        Interpolate 1D points onto 1d images using weighted mean interpolation

        Args:
            sx: x values
            s_val: amplitudes / volume backscattering coefficients
            image_values: Image with values. If empty a new image will be
                          created.
            image_weights: Image with weights. If empty a new image will be
                           created.

        Template Args:
            T_vector: 

        Returns:
            std::tuple<xt::xtensor<t_float, 1>, xt::xtensor_t_float_1>
                image_values, image_weights
        """

    def get_xres(self) -> float: ...

    def get_xmin(self) -> float: ...

    def get_xmax(self) -> float: ...

    def get_xbase(self) -> float: ...

    def get_nx(self) -> int: ...

    def get_border_xmin(self) -> float: ...

    def get_border_xmax(self) -> float: ...

    @overload
    def get_x_index(self, x: float) -> int: ...

    @overload
    def get_x_index(self, x: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')]) -> Annotated[NDArray[numpy.int32], dict(shape=(None,), order='C')]: ...

    @overload
    def get_x_index_fraction(self, x: float) -> float: ...

    @overload
    def get_x_index_fraction(self, x: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')]) -> Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')]: ...

    @overload
    def get_x_value(self, x_index: int) -> float: ...

    @overload
    def get_x_value(self, x_index: Annotated[NDArray[numpy.int32], dict(shape=(None,), order='C')]) -> Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')]: ...

    @overload
    def get_x_grd_value(self, x: float) -> float: ...

    @overload
    def get_x_grd_value(self, x: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')]) -> Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')]: ...

    def get_extent_x(self) -> list[float]: ...

    def get_extent(self, axis: str = 'x') -> list[float]: ...

    def get_x_coordinates(self) -> list[float]: ...

    @staticmethod
    def get_minmax(sx: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')]) -> tuple[float, float]:
        """
        Returns the min/max value of a list.

        Args:
            sx: 1D array with x positions

        Template Args:
            T_vector: 

        Returns:
            std::tuple<t_float, t_float> (xmin,xmax)
        """

    @overload
    def __repr__(self) -> str: ...

    @overload
    def __repr__(self) -> str:
        """Return object information as string"""

    def __eq__(self, other: ForwardGridder1D) -> bool: ...

    def copy(self) -> ForwardGridder1D:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> ForwardGridder1D: ...

    def __deepcopy__(self, arg: dict, /) -> ForwardGridder1D: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> ForwardGridder1D:
        """create T_CLASS object from bytearray"""

    def __getstate__(self) -> bytes: ...

    def __setstate__(self, arg: bytes, /) -> None: ...

    def __hash__(self) -> int:
        """hash function implemented using binary_hash"""

    def hash(self) -> int:
        """hash function implemented using binary_hash"""

    def __str__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

class ForwardGridder1DF:
    """
    Simple class to generate 1D grids and interpolate x data onto a grid
    using simple forward mapping algorithms (e.g. block mean, weighted
    mean interpolation)
    """

    def __init__(self, xres: float, min_x: float, max_x: float, xbase: float = 0.0) -> None:
        """
        Initialize forward gridder class using grid parameters.

        Args:
            xres: x resolution of the grid
            min_x: smallest x value that must be contained within the grid
            max_x: largest x value that must be contained within the grid
            xbase: x base position of the grid, by default 0.0
        """

    @staticmethod
    def from_res(res: float, min_x: float, max_x: float) -> ForwardGridder1DF:
        """
        Create gridder setting xres to "res"

        Args:
            res: x resolution of the grid
            min_x: smallest x value that must be contained within the grid
            max_x: largest x value that must be contained within the grid

        Returns:
            ForwardGridder1D object
        """

    @staticmethod
    def from_data(res: float, sx: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]) -> ForwardGridder1DF:
        """
        Create gridder with resolution "res" xmin,xmax are determined to
        exactly contain the given data vector (sx)

        Args:
            res: x resolution of the grid
            sx: array with x data

        Returns:
            ForwardGridder1D object
        """

    def get_empty_grd_images(self) -> tuple[Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]]:
        """
        Create empty grid images

        Returns:
            std::tuple<xt::xtensor<t_float, 1>, xt::xtensor_t_float_1>
                image_values, image_weights
        """

    def group_blocks(self, sx: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], sv: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]) -> dict[int, list[float]]: ...

    def interpolate_block_mean(self, sx: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], s_val: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]) -> tuple[Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]]:
        """
        Interpolate 1D points onto 1d images using block mean interpolation

        Args:
            sx: x values
            s_val: amplitudes / volume backscattering coefficients
            image_values: Image with values. If empty a new image will be
                          created.
            image_weights: Image with weights. If empty a new image will be
                           created.

        Template Args:
            T_vector: 

        Returns:
            std::tuple<xt::xtensor<t_float, 1>, xt::xtensor_t_float_1>
                image_values, image_weights
        """

    def interpolate_block_mean_inplace(self, sx: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], s_val: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], image_values: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], image_weights: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]) -> None:
        """
        Interpolate 1D points onto 1d images using block mean interpolation
        (inplace version)

        Args:
            sx: x values
            s_val: amplitudes / volume backscattering coefficients
            image_values: Image with values will be edited inplace
            image_weights: Image with weights will be edited inplace

        Template Args:
            T_vector: 

        Returns:
            std::tuple<xt::xtensor<t_float, 1>, xt::xtensor_t_float_1>
                image_values, image_weights
        """

    def interpolate_weighted_mean(self, sx: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], s_val: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]) -> tuple[Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]]:
        """
        Interpolate 1D points onto 1d images using weighted mean interpolation

        Args:
            sx: x values
            s_val: amplitudes / volume backscattering coefficients

        Template Args:
            T_vector: 

        Returns:
            std::tuple<xt::xtensor<t_float, 1>, xt::xtensor_t_float_1>
                image_values, image_weights
        """

    def interpolate_weighted_mean_inplace(self, sx: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], s_val: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], image_values: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], image_weights: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]) -> None:
        """
        Interpolate 1D points onto 1d images using weighted mean interpolation

        Args:
            sx: x values
            s_val: amplitudes / volume backscattering coefficients
            image_values: Image with values. If empty a new image will be
                          created.
            image_weights: Image with weights. If empty a new image will be
                           created.

        Template Args:
            T_vector: 

        Returns:
            std::tuple<xt::xtensor<t_float, 1>, xt::xtensor_t_float_1>
                image_values, image_weights
        """

    def get_xres(self) -> float: ...

    def get_xmin(self) -> float: ...

    def get_xmax(self) -> float: ...

    def get_xbase(self) -> float: ...

    def get_nx(self) -> int: ...

    def get_border_xmin(self) -> float: ...

    def get_border_xmax(self) -> float: ...

    @overload
    def get_x_index(self, x: float) -> int: ...

    @overload
    def get_x_index(self, x: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]) -> Annotated[NDArray[numpy.int32], dict(shape=(None,), order='C')]: ...

    @overload
    def get_x_index_fraction(self, x: float) -> float: ...

    @overload
    def get_x_index_fraction(self, x: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]) -> Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]: ...

    @overload
    def get_x_value(self, x_index: int) -> float: ...

    @overload
    def get_x_value(self, x_index: Annotated[NDArray[numpy.int32], dict(shape=(None,), order='C')]) -> Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]: ...

    @overload
    def get_x_grd_value(self, x: float) -> float: ...

    @overload
    def get_x_grd_value(self, x: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]) -> Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]: ...

    def get_extent_x(self) -> list[float]: ...

    def get_extent(self, axis: str = 'x') -> list[float]: ...

    def get_x_coordinates(self) -> list[float]: ...

    @staticmethod
    def get_minmax(sx: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]) -> tuple[float, float]:
        """
        Returns the min/max value of a list.

        Args:
            sx: 1D array with x positions

        Template Args:
            T_vector: 

        Returns:
            std::tuple<t_float, t_float> (xmin,xmax)
        """

    @overload
    def __repr__(self) -> str: ...

    @overload
    def __repr__(self) -> str:
        """Return object information as string"""

    def __eq__(self, other: ForwardGridder1DF) -> bool: ...

    def copy(self) -> ForwardGridder1DF:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> ForwardGridder1DF: ...

    def __deepcopy__(self, arg: dict, /) -> ForwardGridder1DF: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> ForwardGridder1DF:
        """create T_CLASS object from bytearray"""

    def __getstate__(self) -> bytes: ...

    def __setstate__(self, arg: bytes, /) -> None: ...

    def __hash__(self) -> int:
        """hash function implemented using binary_hash"""

    def hash(self) -> int:
        """hash function implemented using binary_hash"""

    def __str__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

class ForwardGridder2D:
    """
    Simple class to generate 2D grids (images) and interpolate xy data
    onto a grid using simple forward mapping algorithms (e.g. block mean,
    weighted mean interpolation)
    """

    def __init__(self, xres: float, yres: float, min_x: float, max_x: float, min_y: float, max_y: float, xbase: float = 0.0, ybase: float = 0.0) -> None:
        """
        Initialize forward gridder class using grid parameters.

        Args:
            xres: x resolution of the grid
            yres: y resolution of the grid
            min_x: smallest x value that must be contained within the grid
            max_x: largest x value that must be contained within the grid
            min_y: smallest y value that must be contained within the grid
            max_y: largest y value that must be contained within the grid
            xbase: x base position of the grid, by default 0.0
            ybase: y base position of the grid, by default 0.0
        """

    @staticmethod
    def from_res(res: float, min_x: float, max_x: float, min_y: float, max_y: float) -> ForwardGridder2D:
        """
        Create gridder setting xres and yres to "res"

        Args:
            res: x and y resolution of the grid
            min_x: smallest x value that must be contained within the grid
            max_x: largest x value that must be contained within the grid
            min_y: smallest y value that must be contained within the grid
            max_y: largest y value that must be contained within the grid

        Returns:
            ForwardGridder2D object
        """

    @staticmethod
    def from_data(res: float, sx: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], sy: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')]) -> ForwardGridder2D:
        """
        Create gridder with resolution "res" xmin,xmax,ymin,ymax are
        determined to exactly contain the given data vectors (sx,sy)

        Args:
            res: x and y resolution of the grid
            sx: array with x data
            sy: array with y data

        Returns:
            ForwardGridder2D object
        """

    def get_empty_grd_images(self) -> tuple[Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')], Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')]]:
        """
        Create empty grid images

        Returns:
            std::tuple<xt::xtensor<t_float, 2>, xt::xtensor_t_float_2>
                image_values, image_weights
        """

    def group_blocks(self, sx: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], sy: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], sv: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')]) -> dict[int, list[float]]: ...

    def interpolate_block_mean(self, sx: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], sy: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], s_val: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')]) -> tuple[Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')], Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')]]:
        """
        Interpolate 2D points onto 2d images using block mean interpolation

        Args:
            sx: x values
            sy: y values
            s_val: amplitudes / volume backscattering coefficients

        Template Args:
            T_vector: 

        Returns:
            std::tuple<xt::xtensor<t_float, 2>, xt::xtensor_t_float_2>
                image_values, image_weights
        """

    def interpolate_block_mean_inplace(self, sx: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], sy: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], s_val: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], image_values: Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')], image_weights: Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')]) -> None:
        """
        Interpolate 2D points onto 2d images using block mean interpolation
        (inplace version)

        Args:
            sx: x values
            sy: y values
            s_val: amplitudes / volume backscattering coefficients
            image_values: Image with values will be edited inplace
            image_weights: Image with weights will be edited inplace

        Template Args:
            T_vector:
        """

    def interpolate_weighted_mean(self, sx: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], sy: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], s_val: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')]) -> tuple[Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')], Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')]]:
        """
        Interpolate 2D points onto 2d images using weighted mean interpolation

        Args:
            sx: x values
            sy: y values
            s_val: amplitudes / volume backscattering coefficients

        Template Args:
            T_vector: 

        Returns:
            std::tuple<xt::xtensor<t_float, 2>, xt::xtensor_t_float_2>
                image_values, image_weights
        """

    def interpolate_weighted_mean_inplace(self, sx: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], sy: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], s_val: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], image_values: Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')], image_weights: Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='C')]) -> None:
        """
        Interpolate 2D points onto 2d images using weighted mean interpolation
        (inplace version)

        Args:
            sx: x values
            sy: y values
            s_val: amplitudes / volume backscattering coefficients
            image_values: Image with values will be edited inplace
            image_weights: Image with weights will be edited inplace

        Template Args:
            T_vector:
        """

    def get_xres(self) -> float: ...

    def get_yres(self) -> float: ...

    def get_xmin(self) -> float: ...

    def get_xmax(self) -> float: ...

    def get_ymin(self) -> float: ...

    def get_ymax(self) -> float: ...

    def get_xbase(self) -> float: ...

    def get_ybase(self) -> float: ...

    def get_nx(self) -> int: ...

    def get_ny(self) -> int: ...

    def get_border_xmin(self) -> float: ...

    def get_border_xmax(self) -> float: ...

    def get_border_ymin(self) -> float: ...

    def get_border_ymax(self) -> float: ...

    @overload
    def get_x_index(self, x: float) -> int: ...

    @overload
    def get_x_index(self, x: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')]) -> Annotated[NDArray[numpy.int32], dict(shape=(None,), order='C')]: ...

    @overload
    def get_y_index(self, y: float) -> int: ...

    @overload
    def get_y_index(self, y: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')]) -> Annotated[NDArray[numpy.int32], dict(shape=(None,), order='C')]: ...

    @overload
    def get_x_index_fraction(self, x: float) -> float: ...

    @overload
    def get_x_index_fraction(self, x: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')]) -> Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')]: ...

    @overload
    def get_y_index_fraction(self, y: float) -> float: ...

    @overload
    def get_y_index_fraction(self, y: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')]) -> Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')]: ...

    @overload
    def get_x_value(self, x_index: int) -> float: ...

    @overload
    def get_x_value(self, x_index: Annotated[NDArray[numpy.int32], dict(shape=(None,), order='C')]) -> Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')]: ...

    @overload
    def get_y_value(self, y_index: int) -> float: ...

    @overload
    def get_y_value(self, y_index: Annotated[NDArray[numpy.int32], dict(shape=(None,), order='C')]) -> Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')]: ...

    @overload
    def get_x_grd_value(self, x: float) -> float: ...

    @overload
    def get_x_grd_value(self, x: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')]) -> Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')]: ...

    @overload
    def get_y_grd_value(self, y: float) -> float: ...

    @overload
    def get_y_grd_value(self, y: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')]) -> Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')]: ...

    def get_extent_x(self) -> list[float]: ...

    def get_extent_y(self) -> list[float]: ...

    def get_extent(self, axis: str = 'xy') -> list[float]: ...

    def get_x_coordinates(self) -> list[float]: ...

    def get_y_coordinates(self) -> list[float]: ...

    @staticmethod
    def get_minmax(sx: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], sy: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')]) -> tuple[float, float, float, float]:
        """
        Returns the min/max value of two lists (same size).

        Args:
            sx: 1D array with x positions
            sy: 1D array with y positions

        Template Args:
            T_vector: 

        Returns:
            std::tuple<t_float, t_float, t_float, t_float>
                (xmin,xmax,ymin,ymax)
        """

    @overload
    def __repr__(self) -> str: ...

    @overload
    def __repr__(self) -> str:
        """Return object information as string"""

    def __eq__(self, other: ForwardGridder2D) -> bool: ...

    def copy(self) -> ForwardGridder2D:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> ForwardGridder2D: ...

    def __deepcopy__(self, arg: dict, /) -> ForwardGridder2D: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> ForwardGridder2D:
        """create T_CLASS object from bytearray"""

    def __getstate__(self) -> bytes: ...

    def __setstate__(self, arg: bytes, /) -> None: ...

    def __hash__(self) -> int:
        """hash function implemented using binary_hash"""

    def hash(self) -> int:
        """hash function implemented using binary_hash"""

    def __str__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

class ForwardGridder2DF:
    """
    Simple class to generate 2D grids (images) and interpolate xy data
    onto a grid using simple forward mapping algorithms (e.g. block mean,
    weighted mean interpolation)
    """

    def __init__(self, xres: float, yres: float, min_x: float, max_x: float, min_y: float, max_y: float, xbase: float = 0.0, ybase: float = 0.0) -> None:
        """
        Initialize forward gridder class using grid parameters.

        Args:
            xres: x resolution of the grid
            yres: y resolution of the grid
            min_x: smallest x value that must be contained within the grid
            max_x: largest x value that must be contained within the grid
            min_y: smallest y value that must be contained within the grid
            max_y: largest y value that must be contained within the grid
            xbase: x base position of the grid, by default 0.0
            ybase: y base position of the grid, by default 0.0
        """

    @staticmethod
    def from_res(res: float, min_x: float, max_x: float, min_y: float, max_y: float) -> ForwardGridder2DF:
        """
        Create gridder setting xres and yres to "res"

        Args:
            res: x and y resolution of the grid
            min_x: smallest x value that must be contained within the grid
            max_x: largest x value that must be contained within the grid
            min_y: smallest y value that must be contained within the grid
            max_y: largest y value that must be contained within the grid

        Returns:
            ForwardGridder2D object
        """

    @staticmethod
    def from_data(res: float, sx: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], sy: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]) -> ForwardGridder2DF:
        """
        Create gridder with resolution "res" xmin,xmax,ymin,ymax are
        determined to exactly contain the given data vectors (sx,sy)

        Args:
            res: x and y resolution of the grid
            sx: array with x data
            sy: array with y data

        Returns:
            ForwardGridder2D object
        """

    def get_empty_grd_images(self) -> tuple[Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')], Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')]]:
        """
        Create empty grid images

        Returns:
            std::tuple<xt::xtensor<t_float, 2>, xt::xtensor_t_float_2>
                image_values, image_weights
        """

    def group_blocks(self, sx: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], sy: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], sv: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]) -> dict[int, list[float]]: ...

    def interpolate_block_mean(self, sx: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], sy: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], s_val: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]) -> tuple[Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')], Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')]]:
        """
        Interpolate 2D points onto 2d images using block mean interpolation

        Args:
            sx: x values
            sy: y values
            s_val: amplitudes / volume backscattering coefficients

        Template Args:
            T_vector: 

        Returns:
            std::tuple<xt::xtensor<t_float, 2>, xt::xtensor_t_float_2>
                image_values, image_weights
        """

    def interpolate_block_mean_inplace(self, sx: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], sy: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], s_val: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], image_values: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')], image_weights: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')]) -> None:
        """
        Interpolate 2D points onto 2d images using block mean interpolation
        (inplace version)

        Args:
            sx: x values
            sy: y values
            s_val: amplitudes / volume backscattering coefficients
            image_values: Image with values will be edited inplace
            image_weights: Image with weights will be edited inplace

        Template Args:
            T_vector:
        """

    def interpolate_weighted_mean(self, sx: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], sy: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], s_val: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]) -> tuple[Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')], Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')]]:
        """
        Interpolate 2D points onto 2d images using weighted mean interpolation

        Args:
            sx: x values
            sy: y values
            s_val: amplitudes / volume backscattering coefficients

        Template Args:
            T_vector: 

        Returns:
            std::tuple<xt::xtensor<t_float, 2>, xt::xtensor_t_float_2>
                image_values, image_weights
        """

    def interpolate_weighted_mean_inplace(self, sx: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], sy: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], s_val: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], image_values: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')], image_weights: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')]) -> None:
        """
        Interpolate 2D points onto 2d images using weighted mean interpolation
        (inplace version)

        Args:
            sx: x values
            sy: y values
            s_val: amplitudes / volume backscattering coefficients
            image_values: Image with values will be edited inplace
            image_weights: Image with weights will be edited inplace

        Template Args:
            T_vector:
        """

    def get_xres(self) -> float: ...

    def get_yres(self) -> float: ...

    def get_xmin(self) -> float: ...

    def get_xmax(self) -> float: ...

    def get_ymin(self) -> float: ...

    def get_ymax(self) -> float: ...

    def get_xbase(self) -> float: ...

    def get_ybase(self) -> float: ...

    def get_nx(self) -> int: ...

    def get_ny(self) -> int: ...

    def get_border_xmin(self) -> float: ...

    def get_border_xmax(self) -> float: ...

    def get_border_ymin(self) -> float: ...

    def get_border_ymax(self) -> float: ...

    @overload
    def get_x_index(self, x: float) -> int: ...

    @overload
    def get_x_index(self, x: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]) -> Annotated[NDArray[numpy.int32], dict(shape=(None,), order='C')]: ...

    @overload
    def get_y_index(self, y: float) -> int: ...

    @overload
    def get_y_index(self, y: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]) -> Annotated[NDArray[numpy.int32], dict(shape=(None,), order='C')]: ...

    @overload
    def get_x_index_fraction(self, x: float) -> float: ...

    @overload
    def get_x_index_fraction(self, x: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]) -> Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]: ...

    @overload
    def get_y_index_fraction(self, y: float) -> float: ...

    @overload
    def get_y_index_fraction(self, y: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]) -> Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]: ...

    @overload
    def get_x_value(self, x_index: int) -> float: ...

    @overload
    def get_x_value(self, x_index: Annotated[NDArray[numpy.int32], dict(shape=(None,), order='C')]) -> Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]: ...

    @overload
    def get_y_value(self, y_index: int) -> float: ...

    @overload
    def get_y_value(self, y_index: Annotated[NDArray[numpy.int32], dict(shape=(None,), order='C')]) -> Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]: ...

    @overload
    def get_x_grd_value(self, x: float) -> float: ...

    @overload
    def get_x_grd_value(self, x: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]) -> Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]: ...

    @overload
    def get_y_grd_value(self, y: float) -> float: ...

    @overload
    def get_y_grd_value(self, y: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]) -> Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]: ...

    def get_extent_x(self) -> list[float]: ...

    def get_extent_y(self) -> list[float]: ...

    def get_extent(self, axis: str = 'xy') -> list[float]: ...

    def get_x_coordinates(self) -> list[float]: ...

    def get_y_coordinates(self) -> list[float]: ...

    @staticmethod
    def get_minmax(sx: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], sy: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]) -> tuple[float, float, float, float]:
        """
        Returns the min/max value of two lists (same size).

        Args:
            sx: 1D array with x positions
            sy: 1D array with y positions

        Template Args:
            T_vector: 

        Returns:
            std::tuple<t_float, t_float, t_float, t_float>
                (xmin,xmax,ymin,ymax)
        """

    @overload
    def __repr__(self) -> str: ...

    @overload
    def __repr__(self) -> str:
        """Return object information as string"""

    def __eq__(self, other: ForwardGridder2DF) -> bool: ...

    def copy(self) -> ForwardGridder2DF:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> ForwardGridder2DF: ...

    def __deepcopy__(self, arg: dict, /) -> ForwardGridder2DF: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> ForwardGridder2DF:
        """create T_CLASS object from bytearray"""

    def __getstate__(self) -> bytes: ...

    def __setstate__(self, arg: bytes, /) -> None: ...

    def __hash__(self) -> int:
        """hash function implemented using binary_hash"""

    def hash(self) -> int:
        """hash function implemented using binary_hash"""

    def __str__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

class ForwardGridder3D:
    """
    Simple class to generate 3D grids (images) and interpolate xyz data
    onto a grid using simple forward mapping algorithms (e.g. block mean,
    weighted mean interpolation)
    """

    def __init__(self, xres: float, yres: float, zres: float, min_x: float, max_x: float, min_y: float, max_y: float, min_z: float, max_z: float, xbase: float = 0.0, ybase: float = 0.0, zbase: float = 0.0) -> None:
        """
        Initialize forward gridder class using grid parameters.

        Args:
            xres: x resolution of the grid
            yres: y resolution of the grid
            zres: z resolution of the grid
            min_x: smallest x value that must be contained within the grid
            max_x: largest x value that must be contained within the grid
            min_y: smallest y value that must be contained within the grid
            max_y: largest y value that must be contained within the grid
            min_z: smallest z value that must be contained within the grid
            max_z: largest z value that must be contained within the grid
            xbase: x base position of the grid, by default 0.0
            ybase: y base position of the grid, by default 0.0
            zbase: z base position of the grid, by default 0.0
        """

    @staticmethod
    def from_res(res: float, min_x: float, max_x: float, min_y: float, max_y: float, min_z: float, max_z: float) -> ForwardGridder3D:
        """
        Create gridder setting xres,yres and zres to "res"

        Args:
            res: x,y and z resolution of the grid
            min_x: smallest x value that must be contained within the grid
            max_x: largest x value that must be contained within the grid
            min_y: smallest y value that must be contained within the grid
            max_y: largest y value that must be contained within the grid
            min_z: smallest z value that must be contained within the grid
            max_z: largest z value that must be contained within the grid

        Returns:
            ForwardGridder3D object
        """

    @staticmethod
    def from_data(res: float, sx: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], sy: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], sz: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')]) -> ForwardGridder3D:
        """
        Create gridder with resolution "res" xmin,xmax,ymin,ymax,zmin,zmax are
        determined to exactly contain the given data vectors (sx,sy,sz)

        Args:
            res: x,y and z resolution of the grid
            sx: array with x data
            sy: array with y data
            sz: array with z data

        Returns:
            ForwardGridder3D object
        """

    def get_empty_grd_images(self) -> tuple[Annotated[NDArray[numpy.float64], dict(shape=(None, None, None), order='C')], Annotated[NDArray[numpy.float64], dict(shape=(None, None, None), order='C')]]:
        """
        Create empty grid images

        Returns:
            std::tuple<xt::xtensor<t_float, 3>, xt::xtensor_t_float_3>
                image_values, image_weights
        """

    def group_blocks(self, sx: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], sy: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], sz: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], sv: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')]) -> dict[int, list[float]]: ...

    def interpolate_block_mean(self, sx: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], sy: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], sz: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], s_val: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')]) -> tuple[Annotated[NDArray[numpy.float64], dict(shape=(None, None, None), order='C')], Annotated[NDArray[numpy.float64], dict(shape=(None, None, None), order='C')]]:
        """
        Interpolate 3D points onto 3d images using block mean interpolation

        Args:
            sx: x values
            sy: y values
            sz: z values
            s_val: amplitudes / volume backscattering coefficients

        Template Args:
            T_vector: 

        Returns:
            std::tuple<xt::xtensor<t_float, 3>, xt::xtensor_t_float_3>
                image_values, image_weights
        """

    def interpolate_block_mean_inplace(self, sx: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], sy: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], sz: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], s_val: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], image_values: Annotated[NDArray[numpy.float64], dict(shape=(None, None, None), order='C')], image_weights: Annotated[NDArray[numpy.float64], dict(shape=(None, None, None), order='C')]) -> None:
        """
        Interpolate 3D points onto 3d images using block mean interpolation
        (inplace version)

        Args:
            sx: x values
            sy: y values
            sz: z values
            s_val: amplitudes / volume backscattering coefficients
            image_values: Image with values will be edited inplace
            image_weights: Image with weights will be edited inplace

        Template Args:
            T_vector:
        """

    def interpolate_weighted_mean(self, sx: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], sy: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], sz: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], s_val: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')]) -> tuple[Annotated[NDArray[numpy.float64], dict(shape=(None, None, None), order='C')], Annotated[NDArray[numpy.float64], dict(shape=(None, None, None), order='C')]]:
        """
        Interpolate 3D points onto 3d images using weighted mean interpolation

        Args:
            sx: x values
            sy: y values
            sz: z values
            s_val: amplitudes / volume backscattering coefficients

        Template Args:
            T_vector: 

        Returns:
            std::tuple<xt::xtensor<t_float, 3>, xt::xtensor_t_float_3>
                image_values, image_weights
        """

    def interpolate_weighted_mean_inplace(self, sx: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], sy: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], sz: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], s_val: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], image_values: Annotated[NDArray[numpy.float64], dict(shape=(None, None, None), order='C')], image_weights: Annotated[NDArray[numpy.float64], dict(shape=(None, None, None), order='C')]) -> None:
        """
        Interpolate 3D points onto 3d images using weighted mean interpolation
        (inplace version)

        Args:
            sx: x values
            sy: y values
            sz: z values
            s_val: amplitudes / volume backscattering coefficients
            image_values: Image with values will be edited inplace
            image_weights: Image with weights will be edited inplace

        Template Args:
            T_vector:
        """

    def get_xres(self) -> float: ...

    def get_yres(self) -> float: ...

    def get_zres(self) -> float: ...

    def get_xmin(self) -> float: ...

    def get_xmax(self) -> float: ...

    def get_ymin(self) -> float: ...

    def get_ymax(self) -> float: ...

    def get_zmin(self) -> float: ...

    def get_zmax(self) -> float: ...

    def get_xbase(self) -> float: ...

    def get_ybase(self) -> float: ...

    def get_zbase(self) -> float: ...

    def get_nx(self) -> int: ...

    def get_ny(self) -> int: ...

    def get_nz(self) -> int: ...

    def get_border_xmin(self) -> float: ...

    def get_border_xmax(self) -> float: ...

    def get_border_ymin(self) -> float: ...

    def get_border_ymax(self) -> float: ...

    def get_border_zmin(self) -> float: ...

    def get_border_zmax(self) -> float: ...

    @overload
    def get_x_index(self, x: float) -> int: ...

    @overload
    def get_x_index(self, x: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')]) -> Annotated[NDArray[numpy.int32], dict(shape=(None,), order='C')]: ...

    @overload
    def get_y_index(self, y: float) -> int: ...

    @overload
    def get_y_index(self, y: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')]) -> Annotated[NDArray[numpy.int32], dict(shape=(None,), order='C')]: ...

    @overload
    def get_z_index(self, z: float) -> int: ...

    @overload
    def get_z_index(self, z: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')]) -> Annotated[NDArray[numpy.int32], dict(shape=(None,), order='C')]: ...

    @overload
    def get_x_index_fraction(self, x: float) -> float: ...

    @overload
    def get_x_index_fraction(self, x: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')]) -> Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')]: ...

    @overload
    def get_y_index_fraction(self, y: float) -> float: ...

    @overload
    def get_y_index_fraction(self, y: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')]) -> Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')]: ...

    @overload
    def get_z_index_fraction(self, z: float) -> float: ...

    @overload
    def get_z_index_fraction(self, z: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')]) -> Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')]: ...

    @overload
    def get_x_value(self, x_index: int) -> float: ...

    @overload
    def get_x_value(self, x_index: Annotated[NDArray[numpy.int32], dict(shape=(None,), order='C')]) -> Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')]: ...

    @overload
    def get_y_value(self, y_index: int) -> float: ...

    @overload
    def get_y_value(self, y_index: Annotated[NDArray[numpy.int32], dict(shape=(None,), order='C')]) -> Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')]: ...

    @overload
    def get_z_value(self, z_index: int) -> float: ...

    @overload
    def get_z_value(self, z_index: Annotated[NDArray[numpy.int32], dict(shape=(None,), order='C')]) -> Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')]: ...

    @overload
    def get_x_grd_value(self, x: float) -> float: ...

    @overload
    def get_x_grd_value(self, x: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')]) -> Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')]: ...

    @overload
    def get_y_grd_value(self, y: float) -> float: ...

    @overload
    def get_y_grd_value(self, y: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')]) -> Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')]: ...

    @overload
    def get_z_grd_value(self, z: float) -> float: ...

    @overload
    def get_z_grd_value(self, z: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')]) -> Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')]: ...

    def get_extent_x(self) -> list[float]: ...

    def get_extent_y(self) -> list[float]: ...

    def get_extent_z(self) -> list[float]: ...

    def get_extent(self, axis: str = 'xyz') -> list[float]: ...

    def get_x_coordinates(self) -> list[float]: ...

    def get_y_coordinates(self) -> list[float]: ...

    def get_z_coordinates(self) -> list[float]: ...

    @staticmethod
    def get_minmax(sx: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], sy: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')], sz: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')]) -> tuple[float, float, float, float, float, float]:
        """
        Returns the min/max value of three lists (same size).

        Args:
            sx: 1D array with x positions
            sy: 1D array with y positions
            sz: 1D array with z positions

        Template Args:
            T_vector: 

        Returns:
            std::tuple<t_float, t_float, t_float, t_float, t_float, t_float>
                (xmin,xmax,ymin,ymax,zmin,zmax)
        """

    @overload
    def __repr__(self) -> str: ...

    @overload
    def __repr__(self) -> str:
        """Return object information as string"""

    def __eq__(self, other: ForwardGridder3D) -> bool: ...

    def copy(self) -> ForwardGridder3D:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> ForwardGridder3D: ...

    def __deepcopy__(self, arg: dict, /) -> ForwardGridder3D: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> ForwardGridder3D:
        """create T_CLASS object from bytearray"""

    def __getstate__(self) -> bytes: ...

    def __setstate__(self, arg: bytes, /) -> None: ...

    def __hash__(self) -> int:
        """hash function implemented using binary_hash"""

    def hash(self) -> int:
        """hash function implemented using binary_hash"""

    def __str__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

class ForwardGridder3DF:
    """
    Simple class to generate 3D grids (images) and interpolate xyz data
    onto a grid using simple forward mapping algorithms (e.g. block mean,
    weighted mean interpolation)
    """

    def __init__(self, xres: float, yres: float, zres: float, min_x: float, max_x: float, min_y: float, max_y: float, min_z: float, max_z: float, xbase: float = 0.0, ybase: float = 0.0, zbase: float = 0.0) -> None:
        """
        Initialize forward gridder class using grid parameters.

        Args:
            xres: x resolution of the grid
            yres: y resolution of the grid
            zres: z resolution of the grid
            min_x: smallest x value that must be contained within the grid
            max_x: largest x value that must be contained within the grid
            min_y: smallest y value that must be contained within the grid
            max_y: largest y value that must be contained within the grid
            min_z: smallest z value that must be contained within the grid
            max_z: largest z value that must be contained within the grid
            xbase: x base position of the grid, by default 0.0
            ybase: y base position of the grid, by default 0.0
            zbase: z base position of the grid, by default 0.0
        """

    @staticmethod
    def from_res(res: float, min_x: float, max_x: float, min_y: float, max_y: float, min_z: float, max_z: float) -> ForwardGridder3DF:
        """
        Create gridder setting xres,yres and zres to "res"

        Args:
            res: x,y and z resolution of the grid
            min_x: smallest x value that must be contained within the grid
            max_x: largest x value that must be contained within the grid
            min_y: smallest y value that must be contained within the grid
            max_y: largest y value that must be contained within the grid
            min_z: smallest z value that must be contained within the grid
            max_z: largest z value that must be contained within the grid

        Returns:
            ForwardGridder3D object
        """

    @staticmethod
    def from_data(res: float, sx: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], sy: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], sz: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]) -> ForwardGridder3DF:
        """
        Create gridder with resolution "res" xmin,xmax,ymin,ymax,zmin,zmax are
        determined to exactly contain the given data vectors (sx,sy,sz)

        Args:
            res: x,y and z resolution of the grid
            sx: array with x data
            sy: array with y data
            sz: array with z data

        Returns:
            ForwardGridder3D object
        """

    def get_empty_grd_images(self) -> tuple[Annotated[NDArray[numpy.float32], dict(shape=(None, None, None), order='C')], Annotated[NDArray[numpy.float32], dict(shape=(None, None, None), order='C')]]:
        """
        Create empty grid images

        Returns:
            std::tuple<xt::xtensor<t_float, 3>, xt::xtensor_t_float_3>
                image_values, image_weights
        """

    def group_blocks(self, sx: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], sy: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], sz: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], sv: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]) -> dict[int, list[float]]: ...

    def interpolate_block_mean(self, sx: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], sy: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], sz: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], s_val: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]) -> tuple[Annotated[NDArray[numpy.float32], dict(shape=(None, None, None), order='C')], Annotated[NDArray[numpy.float32], dict(shape=(None, None, None), order='C')]]:
        """
        Interpolate 3D points onto 3d images using block mean interpolation

        Args:
            sx: x values
            sy: y values
            sz: z values
            s_val: amplitudes / volume backscattering coefficients

        Template Args:
            T_vector: 

        Returns:
            std::tuple<xt::xtensor<t_float, 3>, xt::xtensor_t_float_3>
                image_values, image_weights
        """

    def interpolate_block_mean_inplace(self, sx: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], sy: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], sz: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], s_val: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], image_values: Annotated[NDArray[numpy.float32], dict(shape=(None, None, None), order='C')], image_weights: Annotated[NDArray[numpy.float32], dict(shape=(None, None, None), order='C')]) -> None:
        """
        Interpolate 3D points onto 3d images using block mean interpolation
        (inplace version)

        Args:
            sx: x values
            sy: y values
            sz: z values
            s_val: amplitudes / volume backscattering coefficients
            image_values: Image with values will be edited inplace
            image_weights: Image with weights will be edited inplace

        Template Args:
            T_vector:
        """

    def interpolate_weighted_mean(self, sx: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], sy: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], sz: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], s_val: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]) -> tuple[Annotated[NDArray[numpy.float32], dict(shape=(None, None, None), order='C')], Annotated[NDArray[numpy.float32], dict(shape=(None, None, None), order='C')]]:
        """
        Interpolate 3D points onto 3d images using weighted mean interpolation

        Args:
            sx: x values
            sy: y values
            sz: z values
            s_val: amplitudes / volume backscattering coefficients

        Template Args:
            T_vector: 

        Returns:
            std::tuple<xt::xtensor<t_float, 3>, xt::xtensor_t_float_3>
                image_values, image_weights
        """

    def interpolate_weighted_mean_inplace(self, sx: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], sy: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], sz: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], s_val: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], image_values: Annotated[NDArray[numpy.float32], dict(shape=(None, None, None), order='C')], image_weights: Annotated[NDArray[numpy.float32], dict(shape=(None, None, None), order='C')]) -> None:
        """
        Interpolate 3D points onto 3d images using weighted mean interpolation
        (inplace version)

        Args:
            sx: x values
            sy: y values
            sz: z values
            s_val: amplitudes / volume backscattering coefficients
            image_values: Image with values will be edited inplace
            image_weights: Image with weights will be edited inplace

        Template Args:
            T_vector:
        """

    def get_xres(self) -> float: ...

    def get_yres(self) -> float: ...

    def get_zres(self) -> float: ...

    def get_xmin(self) -> float: ...

    def get_xmax(self) -> float: ...

    def get_ymin(self) -> float: ...

    def get_ymax(self) -> float: ...

    def get_zmin(self) -> float: ...

    def get_zmax(self) -> float: ...

    def get_xbase(self) -> float: ...

    def get_ybase(self) -> float: ...

    def get_zbase(self) -> float: ...

    def get_nx(self) -> int: ...

    def get_ny(self) -> int: ...

    def get_nz(self) -> int: ...

    def get_border_xmin(self) -> float: ...

    def get_border_xmax(self) -> float: ...

    def get_border_ymin(self) -> float: ...

    def get_border_ymax(self) -> float: ...

    def get_border_zmin(self) -> float: ...

    def get_border_zmax(self) -> float: ...

    @overload
    def get_x_index(self, x: float) -> int: ...

    @overload
    def get_x_index(self, x: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]) -> Annotated[NDArray[numpy.int32], dict(shape=(None,), order='C')]: ...

    @overload
    def get_y_index(self, y: float) -> int: ...

    @overload
    def get_y_index(self, y: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]) -> Annotated[NDArray[numpy.int32], dict(shape=(None,), order='C')]: ...

    @overload
    def get_z_index(self, z: float) -> int: ...

    @overload
    def get_z_index(self, z: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]) -> Annotated[NDArray[numpy.int32], dict(shape=(None,), order='C')]: ...

    @overload
    def get_x_index_fraction(self, x: float) -> float: ...

    @overload
    def get_x_index_fraction(self, x: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]) -> Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]: ...

    @overload
    def get_y_index_fraction(self, y: float) -> float: ...

    @overload
    def get_y_index_fraction(self, y: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]) -> Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]: ...

    @overload
    def get_z_index_fraction(self, z: float) -> float: ...

    @overload
    def get_z_index_fraction(self, z: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]) -> Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]: ...

    @overload
    def get_x_value(self, x_index: int) -> float: ...

    @overload
    def get_x_value(self, x_index: Annotated[NDArray[numpy.int32], dict(shape=(None,), order='C')]) -> Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]: ...

    @overload
    def get_y_value(self, y_index: int) -> float: ...

    @overload
    def get_y_value(self, y_index: Annotated[NDArray[numpy.int32], dict(shape=(None,), order='C')]) -> Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]: ...

    @overload
    def get_z_value(self, z_index: int) -> float: ...

    @overload
    def get_z_value(self, z_index: Annotated[NDArray[numpy.int32], dict(shape=(None,), order='C')]) -> Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]: ...

    @overload
    def get_x_grd_value(self, x: float) -> float: ...

    @overload
    def get_x_grd_value(self, x: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]) -> Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]: ...

    @overload
    def get_y_grd_value(self, y: float) -> float: ...

    @overload
    def get_y_grd_value(self, y: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]) -> Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]: ...

    @overload
    def get_z_grd_value(self, z: float) -> float: ...

    @overload
    def get_z_grd_value(self, z: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]) -> Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]: ...

    def get_extent_x(self) -> list[float]: ...

    def get_extent_y(self) -> list[float]: ...

    def get_extent_z(self) -> list[float]: ...

    def get_extent(self, axis: str = 'xyz') -> list[float]: ...

    def get_x_coordinates(self) -> list[float]: ...

    def get_y_coordinates(self) -> list[float]: ...

    def get_z_coordinates(self) -> list[float]: ...

    @staticmethod
    def get_minmax(sx: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], sy: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], sz: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]) -> tuple[float, float, float, float, float, float]:
        """
        Returns the min/max value of three lists (same size).

        Args:
            sx: 1D array with x positions
            sy: 1D array with y positions
            sz: 1D array with z positions

        Template Args:
            T_vector: 

        Returns:
            std::tuple<t_float, t_float, t_float, t_float, t_float, t_float>
                (xmin,xmax,ymin,ymax,zmin,zmax)
        """

    @overload
    def __repr__(self) -> str: ...

    @overload
    def __repr__(self) -> str:
        """Return object information as string"""

    def __eq__(self, other: ForwardGridder3DF) -> bool: ...

    def copy(self) -> ForwardGridder3DF:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> ForwardGridder3DF: ...

    def __deepcopy__(self, arg: dict, /) -> ForwardGridder3DF: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> ForwardGridder3DF:
        """create T_CLASS object from bytearray"""

    def __getstate__(self) -> bytes: ...

    def __setstate__(self, arg: bytes, /) -> None: ...

    def __hash__(self) -> int:
        """hash function implemented using binary_hash"""

    def hash(self) -> int:
        """hash function implemented using binary_hash"""

    def __str__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""
