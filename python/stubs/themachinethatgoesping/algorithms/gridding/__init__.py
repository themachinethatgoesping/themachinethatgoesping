"""
Submodule for gridding (raytracers and georefencing) echosounder samples
"""
from __future__ import annotations
import numpy
import numpy.typing
import typing
from . import functions
__all__: list[str] = ['ForwardGridder1D', 'ForwardGridder1DF', 'ForwardGridder2D', 'ForwardGridder2DF', 'ForwardGridder3D', 'ForwardGridder3DF', 'functions']
class ForwardGridder1D:
    """
    Simple class to generate 1D grids and interpolate x data onto a grid
    using simple forward mapping algorithms (e.g. block mean, weighted
    mean interpolation)
    """
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> ForwardGridder1D:
        """
        create T_CLASS object from bytearray
        """
    @staticmethod
    def from_data(res: typing.SupportsFloat, sx: numpy.ndarray[numpy.float64]) -> ForwardGridder1D:
        """
        Create gridder with resolution "res" xmin,xmax are determined to
        exactly contain the given data vector (sx)
        
        Parameter ``res``:
            x resolution of the grid
        
        Parameter ``sx``:
            array with x data
        
        Returns:
            ForwardGridder1D object
        """
    @staticmethod
    def from_res(res: typing.SupportsFloat, min_x: typing.SupportsFloat, max_x: typing.SupportsFloat) -> ForwardGridder1D:
        """
        Create gridder setting xres to "res"
        
        Parameter ``res``:
            x resolution of the grid
        
        Parameter ``min_x``:
            smallest x value that must be contained within the grid
        
        Parameter ``max_x``:
            largest x value that must be contained within the grid
        
        Returns:
            ForwardGridder1D object
        """
    @staticmethod
    def get_minmax(sx: numpy.ndarray[numpy.float64]) -> tuple[float, float]:
        """
        Returns the min/max value of a list.
        
        Template parameter ``T_vector``:
            $Parameter ``sx``:
        
        1D array with x positions
        
        Returns:
            std::tuple<t_float, t_float> (xmin,xmax)
        """
    def __copy__(self) -> ForwardGridder1D:
        ...
    def __deepcopy__(self, arg0: dict) -> ForwardGridder1D:
        ...
    def __eq__(self, other: ForwardGridder1D) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def __init__(self, xres: typing.SupportsFloat, min_x: typing.SupportsFloat, max_x: typing.SupportsFloat, xbase: typing.SupportsFloat = 0.0) -> None:
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
    @typing.overload
    def __repr__(self) -> str:
        ...
    @typing.overload
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __setstate__(self, arg0: bytes) -> None:
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
    def get_empty_grd_images(self) -> tuple[numpy.ndarray[numpy.float64], numpy.ndarray[numpy.float64]]:
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
    @typing.overload
    def get_x_grd_value(self, x: typing.Annotated[numpy.typing.ArrayLike, numpy.float64]) -> typing.Any:
        ...
    @typing.overload
    def get_x_grd_value(self, x: numpy.ndarray[numpy.float64]) -> numpy.ndarray[numpy.float64]:
        ...
    @typing.overload
    def get_x_index(self, x: typing.Annotated[numpy.typing.ArrayLike, numpy.float64]) -> typing.Any:
        ...
    @typing.overload
    def get_x_index(self, x: numpy.ndarray[numpy.float64]) -> numpy.ndarray[numpy.int32]:
        ...
    @typing.overload
    def get_x_index_fraction(self, x: typing.Annotated[numpy.typing.ArrayLike, numpy.float64]) -> typing.Any:
        ...
    @typing.overload
    def get_x_index_fraction(self, x: numpy.ndarray[numpy.float64]) -> numpy.ndarray[numpy.float64]:
        ...
    @typing.overload
    def get_x_value(self, x_index: typing.Annotated[numpy.typing.ArrayLike, numpy.int32]) -> typing.Any:
        ...
    @typing.overload
    def get_x_value(self, x_index: numpy.ndarray[numpy.int32]) -> numpy.ndarray[numpy.float64]:
        ...
    def get_xbase(self) -> float:
        ...
    def get_xmax(self) -> float:
        ...
    def get_xmin(self) -> float:
        ...
    def get_xres(self) -> float:
        ...
    def group_blocks(self, sx: numpy.ndarray[numpy.float64], sv: numpy.ndarray[numpy.float64]) -> dict[int, list[float]]:
        ...
    def hash(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def info_string(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def interpolate_block_mean(self, sx: numpy.ndarray[numpy.float64], s_val: numpy.ndarray[numpy.float64]) -> tuple[numpy.ndarray[numpy.float64], numpy.ndarray[numpy.float64]]:
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
    def interpolate_block_mean_inplace(self, sx: numpy.ndarray[numpy.float64], s_val: numpy.ndarray[numpy.float64], image_values: numpy.ndarray[numpy.float64], image_weights: numpy.ndarray[numpy.float64]) -> None:
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
    def interpolate_weighted_mean(self, sx: numpy.ndarray[numpy.float64], s_val: numpy.ndarray[numpy.float64]) -> tuple[numpy.ndarray[numpy.float64], numpy.ndarray[numpy.float64]]:
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
    def interpolate_weighted_mean_inplace(self, sx: numpy.ndarray[numpy.float64], s_val: numpy.ndarray[numpy.float64], image_values: numpy.ndarray[numpy.float64], image_weights: numpy.ndarray[numpy.float64]) -> None:
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
    def print(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> None:
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
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> ForwardGridder1DF:
        """
        create T_CLASS object from bytearray
        """
    @staticmethod
    def from_data(res: typing.SupportsFloat, sx: numpy.ndarray[numpy.float32]) -> ForwardGridder1DF:
        """
        Create gridder with resolution "res" xmin,xmax are determined to
        exactly contain the given data vector (sx)
        
        Parameter ``res``:
            x resolution of the grid
        
        Parameter ``sx``:
            array with x data
        
        Returns:
            ForwardGridder1D object
        """
    @staticmethod
    def from_res(res: typing.SupportsFloat, min_x: typing.SupportsFloat, max_x: typing.SupportsFloat) -> ForwardGridder1DF:
        """
        Create gridder setting xres to "res"
        
        Parameter ``res``:
            x resolution of the grid
        
        Parameter ``min_x``:
            smallest x value that must be contained within the grid
        
        Parameter ``max_x``:
            largest x value that must be contained within the grid
        
        Returns:
            ForwardGridder1D object
        """
    @staticmethod
    def get_minmax(sx: numpy.ndarray[numpy.float32]) -> tuple[float, float]:
        """
        Returns the min/max value of a list.
        
        Template parameter ``T_vector``:
            $Parameter ``sx``:
        
        1D array with x positions
        
        Returns:
            std::tuple<t_float, t_float> (xmin,xmax)
        """
    def __copy__(self) -> ForwardGridder1DF:
        ...
    def __deepcopy__(self, arg0: dict) -> ForwardGridder1DF:
        ...
    def __eq__(self, other: ForwardGridder1DF) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def __init__(self, xres: typing.SupportsFloat, min_x: typing.SupportsFloat, max_x: typing.SupportsFloat, xbase: typing.SupportsFloat = 0.0) -> None:
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
    @typing.overload
    def __repr__(self) -> str:
        ...
    @typing.overload
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __setstate__(self, arg0: bytes) -> None:
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
    def get_empty_grd_images(self) -> tuple[numpy.ndarray[numpy.float32], numpy.ndarray[numpy.float32]]:
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
    @typing.overload
    def get_x_grd_value(self, x: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> typing.Any:
        ...
    @typing.overload
    def get_x_grd_value(self, x: numpy.ndarray[numpy.float32]) -> numpy.ndarray[numpy.float32]:
        ...
    @typing.overload
    def get_x_index(self, x: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> typing.Any:
        ...
    @typing.overload
    def get_x_index(self, x: numpy.ndarray[numpy.float32]) -> numpy.ndarray[numpy.int32]:
        ...
    @typing.overload
    def get_x_index_fraction(self, x: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> typing.Any:
        ...
    @typing.overload
    def get_x_index_fraction(self, x: numpy.ndarray[numpy.float32]) -> numpy.ndarray[numpy.float32]:
        ...
    @typing.overload
    def get_x_value(self, x_index: typing.Annotated[numpy.typing.ArrayLike, numpy.int32]) -> typing.Any:
        ...
    @typing.overload
    def get_x_value(self, x_index: numpy.ndarray[numpy.int32]) -> numpy.ndarray[numpy.float32]:
        ...
    def get_xbase(self) -> float:
        ...
    def get_xmax(self) -> float:
        ...
    def get_xmin(self) -> float:
        ...
    def get_xres(self) -> float:
        ...
    def group_blocks(self, sx: numpy.ndarray[numpy.float32], sv: numpy.ndarray[numpy.float32]) -> dict[int, list[float]]:
        ...
    def hash(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def info_string(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def interpolate_block_mean(self, sx: numpy.ndarray[numpy.float32], s_val: numpy.ndarray[numpy.float32]) -> tuple[numpy.ndarray[numpy.float32], numpy.ndarray[numpy.float32]]:
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
    def interpolate_block_mean_inplace(self, sx: numpy.ndarray[numpy.float32], s_val: numpy.ndarray[numpy.float32], image_values: numpy.ndarray[numpy.float32], image_weights: numpy.ndarray[numpy.float32]) -> None:
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
    def interpolate_weighted_mean(self, sx: numpy.ndarray[numpy.float32], s_val: numpy.ndarray[numpy.float32]) -> tuple[numpy.ndarray[numpy.float32], numpy.ndarray[numpy.float32]]:
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
    def interpolate_weighted_mean_inplace(self, sx: numpy.ndarray[numpy.float32], s_val: numpy.ndarray[numpy.float32], image_values: numpy.ndarray[numpy.float32], image_weights: numpy.ndarray[numpy.float32]) -> None:
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
    def print(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> None:
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
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> ForwardGridder2D:
        """
        create T_CLASS object from bytearray
        """
    @staticmethod
    def from_data(res: typing.SupportsFloat, sx: numpy.ndarray[numpy.float64], sy: numpy.ndarray[numpy.float64]) -> ForwardGridder2D:
        """
        Create gridder with resolution "res" xmin,xmax,ymin,ymax are
        determined to exactly contain the given data vectors (sx,sy)
        
        Parameter ``res``:
            x and y resolution of the grid
        
        Parameter ``sx``:
            array with x data
        
        Parameter ``sy``:
            array with y data
        
        Returns:
            ForwardGridder2D object
        """
    @staticmethod
    def from_res(res: typing.SupportsFloat, min_x: typing.SupportsFloat, max_x: typing.SupportsFloat, min_y: typing.SupportsFloat, max_y: typing.SupportsFloat) -> ForwardGridder2D:
        """
        Create gridder setting xres and yres to "res"
        
        Parameter ``res``:
            x and y resolution of the grid
        
        Parameter ``min_x``:
            smallest x value that must be contained within the grid
        
        Parameter ``max_x``:
            largest x value that must be contained within the grid
        
        Parameter ``min_y``:
            smallest y value that must be contained within the grid
        
        Parameter ``max_y``:
            largest y value that must be contained within the grid
        
        Returns:
            ForwardGridder2D object
        """
    @staticmethod
    def get_minmax(sx: numpy.ndarray[numpy.float64], sy: numpy.ndarray[numpy.float64]) -> tuple[float, float, float, float]:
        """
        Returns the min/max value of two lists (same size).
        
        Template parameter ``T_vector``:
            $Parameter ``sx``:
        
        1D array with x positions
        
        Parameter ``sy``:
            1D array with y positions
        
        Returns:
            std::tuple<t_float, t_float, t_float, t_float>
            (xmin,xmax,ymin,ymax)
        """
    def __copy__(self) -> ForwardGridder2D:
        ...
    def __deepcopy__(self, arg0: dict) -> ForwardGridder2D:
        ...
    def __eq__(self, other: ForwardGridder2D) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def __init__(self, xres: typing.SupportsFloat, yres: typing.SupportsFloat, min_x: typing.SupportsFloat, max_x: typing.SupportsFloat, min_y: typing.SupportsFloat, max_y: typing.SupportsFloat, xbase: typing.SupportsFloat = 0.0, ybase: typing.SupportsFloat = 0.0) -> None:
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
    @typing.overload
    def __repr__(self) -> str:
        ...
    @typing.overload
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __setstate__(self, arg0: bytes) -> None:
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
    def get_empty_grd_images(self) -> tuple[numpy.ndarray[numpy.float64], numpy.ndarray[numpy.float64]]:
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
    def get_x_grd_value(self, x: typing.Annotated[numpy.typing.ArrayLike, numpy.float64]) -> typing.Any:
        ...
    def get_x_index(self, x: typing.Annotated[numpy.typing.ArrayLike, numpy.float64]) -> typing.Any:
        ...
    def get_x_index_fraction(self, x: typing.Annotated[numpy.typing.ArrayLike, numpy.float64]) -> typing.Any:
        ...
    def get_x_value(self, x_index: typing.Annotated[numpy.typing.ArrayLike, numpy.int32]) -> typing.Any:
        ...
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
    def get_y_grd_value(self, y: typing.Annotated[numpy.typing.ArrayLike, numpy.float64]) -> typing.Any:
        ...
    def get_y_index(self, y: typing.Annotated[numpy.typing.ArrayLike, numpy.float64]) -> typing.Any:
        ...
    def get_y_index_fraction(self, y: typing.Annotated[numpy.typing.ArrayLike, numpy.float64]) -> typing.Any:
        ...
    def get_y_value(self, y_index: typing.Annotated[numpy.typing.ArrayLike, numpy.int32]) -> typing.Any:
        ...
    def get_ybase(self) -> float:
        ...
    def get_ymax(self) -> float:
        ...
    def get_ymin(self) -> float:
        ...
    def get_yres(self) -> float:
        ...
    def group_blocks(self, sx: numpy.ndarray[numpy.float64], sy: numpy.ndarray[numpy.float64], sv: numpy.ndarray[numpy.float64]) -> dict[int, list[float]]:
        ...
    def hash(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def info_string(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def interpolate_block_mean(self, sx: numpy.ndarray[numpy.float64], sy: numpy.ndarray[numpy.float64], s_val: numpy.ndarray[numpy.float64]) -> tuple[numpy.ndarray[numpy.float64], numpy.ndarray[numpy.float64]]:
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
    def interpolate_block_mean_inplace(self, sx: numpy.ndarray[numpy.float64], sy: numpy.ndarray[numpy.float64], s_val: numpy.ndarray[numpy.float64], image_values: numpy.ndarray[numpy.float64], image_weights: numpy.ndarray[numpy.float64]) -> None:
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
    def interpolate_weighted_mean(self, sx: numpy.ndarray[numpy.float64], sy: numpy.ndarray[numpy.float64], s_val: numpy.ndarray[numpy.float64]) -> tuple[numpy.ndarray[numpy.float64], numpy.ndarray[numpy.float64]]:
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
    def interpolate_weighted_mean_inplace(self, sx: numpy.ndarray[numpy.float64], sy: numpy.ndarray[numpy.float64], s_val: numpy.ndarray[numpy.float64], image_values: numpy.ndarray[numpy.float64], image_weights: numpy.ndarray[numpy.float64]) -> None:
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
    def print(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> None:
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
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> ForwardGridder2DF:
        """
        create T_CLASS object from bytearray
        """
    @staticmethod
    def from_data(res: typing.SupportsFloat, sx: numpy.ndarray[numpy.float32], sy: numpy.ndarray[numpy.float32]) -> ForwardGridder2DF:
        """
        Create gridder with resolution "res" xmin,xmax,ymin,ymax are
        determined to exactly contain the given data vectors (sx,sy)
        
        Parameter ``res``:
            x and y resolution of the grid
        
        Parameter ``sx``:
            array with x data
        
        Parameter ``sy``:
            array with y data
        
        Returns:
            ForwardGridder2D object
        """
    @staticmethod
    def from_res(res: typing.SupportsFloat, min_x: typing.SupportsFloat, max_x: typing.SupportsFloat, min_y: typing.SupportsFloat, max_y: typing.SupportsFloat) -> ForwardGridder2DF:
        """
        Create gridder setting xres and yres to "res"
        
        Parameter ``res``:
            x and y resolution of the grid
        
        Parameter ``min_x``:
            smallest x value that must be contained within the grid
        
        Parameter ``max_x``:
            largest x value that must be contained within the grid
        
        Parameter ``min_y``:
            smallest y value that must be contained within the grid
        
        Parameter ``max_y``:
            largest y value that must be contained within the grid
        
        Returns:
            ForwardGridder2D object
        """
    @staticmethod
    def get_minmax(sx: numpy.ndarray[numpy.float32], sy: numpy.ndarray[numpy.float32]) -> tuple[float, float, float, float]:
        """
        Returns the min/max value of two lists (same size).
        
        Template parameter ``T_vector``:
            $Parameter ``sx``:
        
        1D array with x positions
        
        Parameter ``sy``:
            1D array with y positions
        
        Returns:
            std::tuple<t_float, t_float, t_float, t_float>
            (xmin,xmax,ymin,ymax)
        """
    def __copy__(self) -> ForwardGridder2DF:
        ...
    def __deepcopy__(self, arg0: dict) -> ForwardGridder2DF:
        ...
    def __eq__(self, other: ForwardGridder2DF) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def __init__(self, xres: typing.SupportsFloat, yres: typing.SupportsFloat, min_x: typing.SupportsFloat, max_x: typing.SupportsFloat, min_y: typing.SupportsFloat, max_y: typing.SupportsFloat, xbase: typing.SupportsFloat = 0.0, ybase: typing.SupportsFloat = 0.0) -> None:
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
    @typing.overload
    def __repr__(self) -> str:
        ...
    @typing.overload
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __setstate__(self, arg0: bytes) -> None:
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
    def get_empty_grd_images(self) -> tuple[numpy.ndarray[numpy.float32], numpy.ndarray[numpy.float32]]:
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
    def get_x_grd_value(self, x: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> typing.Any:
        ...
    def get_x_index(self, x: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> typing.Any:
        ...
    def get_x_index_fraction(self, x: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> typing.Any:
        ...
    def get_x_value(self, x_index: typing.Annotated[numpy.typing.ArrayLike, numpy.int32]) -> typing.Any:
        ...
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
    def get_y_grd_value(self, y: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> typing.Any:
        ...
    def get_y_index(self, y: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> typing.Any:
        ...
    def get_y_index_fraction(self, y: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> typing.Any:
        ...
    def get_y_value(self, y_index: typing.Annotated[numpy.typing.ArrayLike, numpy.int32]) -> typing.Any:
        ...
    def get_ybase(self) -> float:
        ...
    def get_ymax(self) -> float:
        ...
    def get_ymin(self) -> float:
        ...
    def get_yres(self) -> float:
        ...
    def group_blocks(self, sx: numpy.ndarray[numpy.float32], sy: numpy.ndarray[numpy.float32], sv: numpy.ndarray[numpy.float32]) -> dict[int, list[float]]:
        ...
    def hash(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def info_string(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def interpolate_block_mean(self, sx: numpy.ndarray[numpy.float32], sy: numpy.ndarray[numpy.float32], s_val: numpy.ndarray[numpy.float32]) -> tuple[numpy.ndarray[numpy.float32], numpy.ndarray[numpy.float32]]:
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
    def interpolate_block_mean_inplace(self, sx: numpy.ndarray[numpy.float32], sy: numpy.ndarray[numpy.float32], s_val: numpy.ndarray[numpy.float32], image_values: numpy.ndarray[numpy.float32], image_weights: numpy.ndarray[numpy.float32]) -> None:
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
    def interpolate_weighted_mean(self, sx: numpy.ndarray[numpy.float32], sy: numpy.ndarray[numpy.float32], s_val: numpy.ndarray[numpy.float32]) -> tuple[numpy.ndarray[numpy.float32], numpy.ndarray[numpy.float32]]:
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
    def interpolate_weighted_mean_inplace(self, sx: numpy.ndarray[numpy.float32], sy: numpy.ndarray[numpy.float32], s_val: numpy.ndarray[numpy.float32], image_values: numpy.ndarray[numpy.float32], image_weights: numpy.ndarray[numpy.float32]) -> None:
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
    def print(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> None:
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
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> ForwardGridder3D:
        """
        create T_CLASS object from bytearray
        """
    @staticmethod
    def from_data(res: typing.SupportsFloat, sx: numpy.ndarray[numpy.float64], sy: numpy.ndarray[numpy.float64], sz: numpy.ndarray[numpy.float64]) -> ForwardGridder3D:
        """
        Create gridder with resolution "res" xmin,xmax,ymin,ymax,zmin,zmax are
        determined to exactly contain the given data vectors (sx,sy,sz)
        
        Parameter ``res``:
            x,y and z resolution of the grid
        
        Parameter ``sx``:
            array with x data
        
        Parameter ``sy``:
            array with y data
        
        Parameter ``sz``:
            array with z data
        
        Returns:
            ForwardGridder3D object
        """
    @staticmethod
    def from_res(res: typing.SupportsFloat, min_x: typing.SupportsFloat, max_x: typing.SupportsFloat, min_y: typing.SupportsFloat, max_y: typing.SupportsFloat, min_z: typing.SupportsFloat, max_z: typing.SupportsFloat) -> ForwardGridder3D:
        """
        Create gridder setting xres,yres and zres to "res"
        
        Parameter ``res``:
            x,y and z resolution of the grid
        
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
        
        Returns:
            ForwardGridder3D object
        """
    @staticmethod
    def get_minmax(sx: numpy.ndarray[numpy.float64], sy: numpy.ndarray[numpy.float64], sz: numpy.ndarray[numpy.float64]) -> tuple[float, float, float, float, float, float]:
        """
        Returns the min/max value of three lists (same size).
        
        Template parameter ``T_vector``:
            $Parameter ``sx``:
        
        1D array with x positions
        
        Parameter ``sy``:
            1D array with y positions
        
        Parameter ``sz``:
            1D array with z positions
        
        Returns:
            std::tuple<t_float, t_float, t_float, t_float, t_float, t_float>
            (xmin,xmax,ymin,ymax,zmin,zmax)
        """
    def __copy__(self) -> ForwardGridder3D:
        ...
    def __deepcopy__(self, arg0: dict) -> ForwardGridder3D:
        ...
    def __eq__(self, other: ForwardGridder3D) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def __init__(self, xres: typing.SupportsFloat, yres: typing.SupportsFloat, zres: typing.SupportsFloat, min_x: typing.SupportsFloat, max_x: typing.SupportsFloat, min_y: typing.SupportsFloat, max_y: typing.SupportsFloat, min_z: typing.SupportsFloat, max_z: typing.SupportsFloat, xbase: typing.SupportsFloat = 0.0, ybase: typing.SupportsFloat = 0.0, zbase: typing.SupportsFloat = 0.0) -> None:
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
    @typing.overload
    def __repr__(self) -> str:
        ...
    @typing.overload
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __setstate__(self, arg0: bytes) -> None:
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
    def get_empty_grd_images(self) -> tuple[numpy.ndarray[numpy.float64], numpy.ndarray[numpy.float64]]:
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
    def get_x_grd_value(self, x: typing.Annotated[numpy.typing.ArrayLike, numpy.float64]) -> typing.Any:
        ...
    def get_x_index(self, x: typing.Annotated[numpy.typing.ArrayLike, numpy.float64]) -> typing.Any:
        ...
    def get_x_index_fraction(self, x: typing.Annotated[numpy.typing.ArrayLike, numpy.float64]) -> typing.Any:
        ...
    def get_x_value(self, x_index: typing.Annotated[numpy.typing.ArrayLike, numpy.int32]) -> typing.Any:
        ...
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
    def get_y_grd_value(self, y: typing.Annotated[numpy.typing.ArrayLike, numpy.float64]) -> typing.Any:
        ...
    def get_y_index(self, y: typing.Annotated[numpy.typing.ArrayLike, numpy.float64]) -> typing.Any:
        ...
    def get_y_index_fraction(self, y: typing.Annotated[numpy.typing.ArrayLike, numpy.float64]) -> typing.Any:
        ...
    def get_y_value(self, y_index: typing.Annotated[numpy.typing.ArrayLike, numpy.int32]) -> typing.Any:
        ...
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
    def get_z_grd_value(self, z: typing.Annotated[numpy.typing.ArrayLike, numpy.float64]) -> typing.Any:
        ...
    def get_z_index(self, z: typing.Annotated[numpy.typing.ArrayLike, numpy.float64]) -> typing.Any:
        ...
    def get_z_index_fraction(self, z: typing.Annotated[numpy.typing.ArrayLike, numpy.float64]) -> typing.Any:
        ...
    def get_z_value(self, z_index: typing.Annotated[numpy.typing.ArrayLike, numpy.int32]) -> typing.Any:
        ...
    def get_zbase(self) -> float:
        ...
    def get_zmax(self) -> float:
        ...
    def get_zmin(self) -> float:
        ...
    def get_zres(self) -> float:
        ...
    def group_blocks(self, sx: numpy.ndarray[numpy.float64], sy: numpy.ndarray[numpy.float64], sz: numpy.ndarray[numpy.float64], sv: numpy.ndarray[numpy.float64]) -> dict[int, list[float]]:
        ...
    def hash(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def info_string(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def interpolate_block_mean(self, sx: numpy.ndarray[numpy.float64], sy: numpy.ndarray[numpy.float64], sz: numpy.ndarray[numpy.float64], s_val: numpy.ndarray[numpy.float64]) -> tuple[numpy.ndarray[numpy.float64], numpy.ndarray[numpy.float64]]:
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
    def interpolate_block_mean_inplace(self, sx: numpy.ndarray[numpy.float64], sy: numpy.ndarray[numpy.float64], sz: numpy.ndarray[numpy.float64], s_val: numpy.ndarray[numpy.float64], image_values: numpy.ndarray[numpy.float64], image_weights: numpy.ndarray[numpy.float64]) -> None:
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
    def interpolate_weighted_mean(self, sx: numpy.ndarray[numpy.float64], sy: numpy.ndarray[numpy.float64], sz: numpy.ndarray[numpy.float64], s_val: numpy.ndarray[numpy.float64]) -> tuple[numpy.ndarray[numpy.float64], numpy.ndarray[numpy.float64]]:
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
    def interpolate_weighted_mean_inplace(self, sx: numpy.ndarray[numpy.float64], sy: numpy.ndarray[numpy.float64], sz: numpy.ndarray[numpy.float64], s_val: numpy.ndarray[numpy.float64], image_values: numpy.ndarray[numpy.float64], image_weights: numpy.ndarray[numpy.float64]) -> None:
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
    def print(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> None:
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
    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> ForwardGridder3DF:
        """
        create T_CLASS object from bytearray
        """
    @staticmethod
    def from_data(res: typing.SupportsFloat, sx: numpy.ndarray[numpy.float32], sy: numpy.ndarray[numpy.float32], sz: numpy.ndarray[numpy.float32]) -> ForwardGridder3DF:
        """
        Create gridder with resolution "res" xmin,xmax,ymin,ymax,zmin,zmax are
        determined to exactly contain the given data vectors (sx,sy,sz)
        
        Parameter ``res``:
            x,y and z resolution of the grid
        
        Parameter ``sx``:
            array with x data
        
        Parameter ``sy``:
            array with y data
        
        Parameter ``sz``:
            array with z data
        
        Returns:
            ForwardGridder3D object
        """
    @staticmethod
    def from_res(res: typing.SupportsFloat, min_x: typing.SupportsFloat, max_x: typing.SupportsFloat, min_y: typing.SupportsFloat, max_y: typing.SupportsFloat, min_z: typing.SupportsFloat, max_z: typing.SupportsFloat) -> ForwardGridder3DF:
        """
        Create gridder setting xres,yres and zres to "res"
        
        Parameter ``res``:
            x,y and z resolution of the grid
        
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
        
        Returns:
            ForwardGridder3D object
        """
    @staticmethod
    def get_minmax(sx: numpy.ndarray[numpy.float32], sy: numpy.ndarray[numpy.float32], sz: numpy.ndarray[numpy.float32]) -> tuple[float, float, float, float, float, float]:
        """
        Returns the min/max value of three lists (same size).
        
        Template parameter ``T_vector``:
            $Parameter ``sx``:
        
        1D array with x positions
        
        Parameter ``sy``:
            1D array with y positions
        
        Parameter ``sz``:
            1D array with z positions
        
        Returns:
            std::tuple<t_float, t_float, t_float, t_float, t_float, t_float>
            (xmin,xmax,ymin,ymax,zmin,zmax)
        """
    def __copy__(self) -> ForwardGridder3DF:
        ...
    def __deepcopy__(self, arg0: dict) -> ForwardGridder3DF:
        ...
    def __eq__(self, other: ForwardGridder3DF) -> bool:
        ...
    def __getstate__(self) -> bytes:
        ...
    def __hash__(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def __init__(self, xres: typing.SupportsFloat, yres: typing.SupportsFloat, zres: typing.SupportsFloat, min_x: typing.SupportsFloat, max_x: typing.SupportsFloat, min_y: typing.SupportsFloat, max_y: typing.SupportsFloat, min_z: typing.SupportsFloat, max_z: typing.SupportsFloat, xbase: typing.SupportsFloat = 0.0, ybase: typing.SupportsFloat = 0.0, zbase: typing.SupportsFloat = 0.0) -> None:
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
    @typing.overload
    def __repr__(self) -> str:
        ...
    @typing.overload
    def __repr__(self) -> str:
        """
        Return object information as string
        """
    def __setstate__(self, arg0: bytes) -> None:
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
    def get_empty_grd_images(self) -> tuple[numpy.ndarray[numpy.float32], numpy.ndarray[numpy.float32]]:
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
    def get_x_grd_value(self, x: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> typing.Any:
        ...
    def get_x_index(self, x: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> typing.Any:
        ...
    def get_x_index_fraction(self, x: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> typing.Any:
        ...
    def get_x_value(self, x_index: typing.Annotated[numpy.typing.ArrayLike, numpy.int32]) -> typing.Any:
        ...
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
    def get_y_grd_value(self, y: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> typing.Any:
        ...
    def get_y_index(self, y: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> typing.Any:
        ...
    def get_y_index_fraction(self, y: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> typing.Any:
        ...
    def get_y_value(self, y_index: typing.Annotated[numpy.typing.ArrayLike, numpy.int32]) -> typing.Any:
        ...
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
    def get_z_grd_value(self, z: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> typing.Any:
        ...
    def get_z_index(self, z: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> typing.Any:
        ...
    def get_z_index_fraction(self, z: typing.Annotated[numpy.typing.ArrayLike, numpy.float32]) -> typing.Any:
        ...
    def get_z_value(self, z_index: typing.Annotated[numpy.typing.ArrayLike, numpy.int32]) -> typing.Any:
        ...
    def get_zbase(self) -> float:
        ...
    def get_zmax(self) -> float:
        ...
    def get_zmin(self) -> float:
        ...
    def get_zres(self) -> float:
        ...
    def group_blocks(self, sx: numpy.ndarray[numpy.float32], sy: numpy.ndarray[numpy.float32], sz: numpy.ndarray[numpy.float32], sv: numpy.ndarray[numpy.float32]) -> dict[int, list[float]]:
        ...
    def hash(self) -> int:
        """
        hash function implemented using binary_hash
        """
    def info_string(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> str:
        """
        Return object information as string
        """
    def interpolate_block_mean(self, sx: numpy.ndarray[numpy.float32], sy: numpy.ndarray[numpy.float32], sz: numpy.ndarray[numpy.float32], s_val: numpy.ndarray[numpy.float32]) -> tuple[numpy.ndarray[numpy.float32], numpy.ndarray[numpy.float32]]:
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
    def interpolate_block_mean_inplace(self, sx: numpy.ndarray[numpy.float32], sy: numpy.ndarray[numpy.float32], sz: numpy.ndarray[numpy.float32], s_val: numpy.ndarray[numpy.float32], image_values: numpy.ndarray[numpy.float32], image_weights: numpy.ndarray[numpy.float32]) -> None:
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
    def interpolate_weighted_mean(self, sx: numpy.ndarray[numpy.float32], sy: numpy.ndarray[numpy.float32], sz: numpy.ndarray[numpy.float32], s_val: numpy.ndarray[numpy.float32]) -> tuple[numpy.ndarray[numpy.float32], numpy.ndarray[numpy.float32]]:
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
    def interpolate_weighted_mean_inplace(self, sx: numpy.ndarray[numpy.float32], sy: numpy.ndarray[numpy.float32], sz: numpy.ndarray[numpy.float32], s_val: numpy.ndarray[numpy.float32], image_values: numpy.ndarray[numpy.float32], image_weights: numpy.ndarray[numpy.float32]) -> None:
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
    def print(self, float_precision: typing.SupportsInt = 3, superscript_exponents: bool = True) -> None:
        """
        Print object information
        """
    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """
        convert object to bytearray
        """
