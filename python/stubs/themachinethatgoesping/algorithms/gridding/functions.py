"""
Submodule for gridding functions
"""
from __future__ import annotations
import numpy
import pybind11_stubgen.typing_ext
import typing
__all__: list[str] = ['compute_resampled_coordinates', 'get_grd_value', 'get_index', 'get_index_fraction', 'get_index_weights', 'get_minmax', 'get_value', 'grd_block_mean', 'grd_weighted_mean', 'group_blocks']
@typing.overload
def compute_resampled_coordinates(values_min: numpy.ndarray[numpy.float32], values_max: numpy.ndarray[numpy.float32], values_res: numpy.ndarray[numpy.float32], grid_min: float = ..., grid_max: float = ..., max_steps: int = 1024) -> numpy.ndarray[numpy.float32]:
    """
    Compute resampled coordinates for gridding operations using
    statistical heuristics
    
    This function generates a uniform grid of coordinates based on input
    data ranges and resolutions. It uses statistical analysis (quantiles
    and IQR) to determine appropriate grid bounds and resolution when
    explicit limits are not provided or when heuristic bounds are more
    suitable.
    
    Parameter ``values_min``:
        Array of minimum values for each data point (e.g., depth ranges)
    
    Parameter ``values_max``:
        Array of maximum values for each data point
    
    Parameter ``values_res``:
        Array of resolution values for each data point
    
    Parameter ``grid_min``:
        Explicit minimum grid bound (optional)
    
    Parameter ``grid_max``:
        Explicit maximum grid bound (optional)
    
    Parameter ``max_steps``:
        Maximum number of grid points. If exceeded, switches to linear
        spacing
    
    Returns:
        coordinates: xtensor array of uniformly spaced grid coordinates
    """
@typing.overload
def compute_resampled_coordinates(values_min: numpy.ndarray[numpy.float64], values_max: numpy.ndarray[numpy.float64], values_res: numpy.ndarray[numpy.float64], grid_min: float = ..., grid_max: float = ..., max_steps: int = 1024) -> numpy.ndarray[numpy.float64]:
    """
    Compute resampled coordinates for gridding operations using
    statistical heuristics
    
    This function generates a uniform grid of coordinates based on input
    data ranges and resolutions. It uses statistical analysis (quantiles
    and IQR) to determine appropriate grid bounds and resolution when
    explicit limits are not provided or when heuristic bounds are more
    suitable.
    
    Parameter ``values_min``:
        Array of minimum values for each data point (e.g., depth ranges)
    
    Parameter ``values_max``:
        Array of maximum values for each data point
    
    Parameter ``values_res``:
        Array of resolution values for each data point
    
    Parameter ``grid_min``:
        Explicit minimum grid bound (optional)
    
    Parameter ``grid_max``:
        Explicit maximum grid bound (optional)
    
    Parameter ``max_steps``:
        Maximum number of grid points. If exceeded, switches to linear
        spacing
    
    Returns:
        coordinates: xtensor array of uniformly spaced grid coordinates
    """
@typing.overload
def get_grd_value(value: float, grd_val_min: float, grd_res: float) -> float:
    ...
@typing.overload
def get_grd_value(value: float, grd_val_min: float, grd_res: float) -> float:
    ...
@typing.overload
def get_index(val: float, grd_val_min: float, grd_res: float) -> int:
    ...
@typing.overload
def get_index(val: float, grd_val_min: float, grd_res: float) -> int:
    ...
@typing.overload
def get_index_fraction(val: float, grd_val_min: float, grd_res: float) -> float:
    ...
@typing.overload
def get_index_fraction(val: float, grd_val_min: float, grd_res: float) -> float:
    ...
@typing.overload
def get_index_weights(frac_x: float, frac_y: float, frac_z: float) -> tuple[typing.Annotated[list[int], pybind11_stubgen.typing_ext.FixedSize(8)], typing.Annotated[list[int], pybind11_stubgen.typing_ext.FixedSize(8)], typing.Annotated[list[int], pybind11_stubgen.typing_ext.FixedSize(8)], typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(8)]]:
    ...
@typing.overload
def get_index_weights(frac_x: float, frac_y: float) -> tuple[typing.Annotated[list[int], pybind11_stubgen.typing_ext.FixedSize(4)], typing.Annotated[list[int], pybind11_stubgen.typing_ext.FixedSize(4)], typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(4)]]:
    ...
@typing.overload
def get_index_weights(frac_x: float) -> tuple[typing.Annotated[list[int], pybind11_stubgen.typing_ext.FixedSize(2)], typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(2)]]:
    ...
@typing.overload
def get_index_weights(frac_x: float, frac_y: float, frac_z: float) -> tuple[typing.Annotated[list[int], pybind11_stubgen.typing_ext.FixedSize(8)], typing.Annotated[list[int], pybind11_stubgen.typing_ext.FixedSize(8)], typing.Annotated[list[int], pybind11_stubgen.typing_ext.FixedSize(8)], typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(8)]]:
    ...
@typing.overload
def get_index_weights(frac_x: float, frac_y: float) -> tuple[typing.Annotated[list[int], pybind11_stubgen.typing_ext.FixedSize(4)], typing.Annotated[list[int], pybind11_stubgen.typing_ext.FixedSize(4)], typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(4)]]:
    ...
@typing.overload
def get_index_weights(frac_x: float) -> tuple[typing.Annotated[list[int], pybind11_stubgen.typing_ext.FixedSize(2)], typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(2)]]:
    ...
@typing.overload
def get_minmax(sb: numpy.ndarray[numpy.float32], mp_cores: int = 1) -> tuple[float, float]:
    ...
@typing.overload
def get_minmax(sx: numpy.ndarray[numpy.float32], sy: numpy.ndarray[numpy.float32], mp_cores: int = 1) -> tuple[float, float, float, float]:
    ...
@typing.overload
def get_minmax(sx: numpy.ndarray[numpy.float32], sy: numpy.ndarray[numpy.float32], sz: numpy.ndarray[numpy.float32], mp_cores: int = 1) -> tuple[float, float, float, float, float, float]:
    ...
@typing.overload
def get_minmax(sb: numpy.ndarray[numpy.float64], mp_cores: int = 1) -> tuple[float, float]:
    ...
@typing.overload
def get_minmax(sx: numpy.ndarray[numpy.float64], sy: numpy.ndarray[numpy.float64], mp_cores: int = 1) -> tuple[float, float, float, float]:
    ...
@typing.overload
def get_minmax(sx: numpy.ndarray[numpy.float64], sy: numpy.ndarray[numpy.float64], sz: numpy.ndarray[numpy.float64], mp_cores: int = 1) -> tuple[float, float, float, float, float, float]:
    ...
@typing.overload
def get_value(index: float, grd_val_min: float, grd_res: float) -> float:
    ...
@typing.overload
def get_value(index: float, grd_val_min: float, grd_res: float) -> float:
    ...
@typing.overload
def grd_block_mean(sx: numpy.ndarray[numpy.float32], sy: numpy.ndarray[numpy.float32], sz: numpy.ndarray[numpy.float32], sv: numpy.ndarray[numpy.float32], xmin: float, xres: float, nx: int, ymin: float, yres: float, ny: int, zmin: float, zres: float, nz: int, image_values: numpy.ndarray[numpy.float32], image_weights: numpy.ndarray[numpy.float32]) -> None:
    ...
@typing.overload
def grd_block_mean(sx: numpy.ndarray[numpy.float32], sy: numpy.ndarray[numpy.float32], sv: numpy.ndarray[numpy.float32], xmin: float, xres: float, nx: int, ymin: float, yres: float, ny: int, image_values: numpy.ndarray[numpy.float32], image_weights: numpy.ndarray[numpy.float32]) -> None:
    ...
@typing.overload
def grd_block_mean(sx: numpy.ndarray[numpy.float32], sv: numpy.ndarray[numpy.float32], xmin: float, xres: float, nx: int, image_values: numpy.ndarray[numpy.float32], image_weights: numpy.ndarray[numpy.float32]) -> None:
    ...
@typing.overload
def grd_block_mean(sx: numpy.ndarray[numpy.float64], sy: numpy.ndarray[numpy.float64], sz: numpy.ndarray[numpy.float64], sv: numpy.ndarray[numpy.float64], xmin: float, xres: float, nx: int, ymin: float, yres: float, ny: int, zmin: float, zres: float, nz: int, image_values: numpy.ndarray[numpy.float64], image_weights: numpy.ndarray[numpy.float64]) -> None:
    ...
@typing.overload
def grd_block_mean(sx: numpy.ndarray[numpy.float64], sy: numpy.ndarray[numpy.float64], sv: numpy.ndarray[numpy.float64], xmin: float, xres: float, nx: int, ymin: float, yres: float, ny: int, image_values: numpy.ndarray[numpy.float64], image_weights: numpy.ndarray[numpy.float64]) -> None:
    ...
@typing.overload
def grd_block_mean(sx: numpy.ndarray[numpy.float64], sv: numpy.ndarray[numpy.float64], xmin: float, xres: float, nx: int, image_values: numpy.ndarray[numpy.float64], image_weights: numpy.ndarray[numpy.float64]) -> None:
    ...
@typing.overload
def grd_weighted_mean(sx: numpy.ndarray[numpy.float32], sy: numpy.ndarray[numpy.float32], sz: numpy.ndarray[numpy.float32], sv: numpy.ndarray[numpy.float32], xmin: float, xres: float, nx: int, ymin: float, yres: float, ny: int, zmin: float, zres: float, nz: int, image_values: numpy.ndarray[numpy.float32], image_weights: numpy.ndarray[numpy.float32]) -> None:
    ...
@typing.overload
def grd_weighted_mean(sx: numpy.ndarray[numpy.float32], sy: numpy.ndarray[numpy.float32], sv: numpy.ndarray[numpy.float32], xmin: float, xres: float, nx: int, ymin: float, yres: float, ny: int, image_values: numpy.ndarray[numpy.float32], image_weights: numpy.ndarray[numpy.float32]) -> None:
    ...
@typing.overload
def grd_weighted_mean(sx: numpy.ndarray[numpy.float32], sv: numpy.ndarray[numpy.float32], xmin: float, xres: float, nx: int, image_values: numpy.ndarray[numpy.float32], image_weights: numpy.ndarray[numpy.float32]) -> None:
    ...
@typing.overload
def grd_weighted_mean(sx: numpy.ndarray[numpy.float64], sy: numpy.ndarray[numpy.float64], sz: numpy.ndarray[numpy.float64], sv: numpy.ndarray[numpy.float64], xmin: float, xres: float, nx: int, ymin: float, yres: float, ny: int, zmin: float, zres: float, nz: int, image_values: numpy.ndarray[numpy.float64], image_weights: numpy.ndarray[numpy.float64]) -> None:
    ...
@typing.overload
def grd_weighted_mean(sx: numpy.ndarray[numpy.float64], sy: numpy.ndarray[numpy.float64], sv: numpy.ndarray[numpy.float64], xmin: float, xres: float, nx: int, ymin: float, yres: float, ny: int, image_values: numpy.ndarray[numpy.float64], image_weights: numpy.ndarray[numpy.float64]) -> None:
    ...
@typing.overload
def grd_weighted_mean(sx: numpy.ndarray[numpy.float64], sv: numpy.ndarray[numpy.float64], xmin: float, xres: float, nx: int, image_values: numpy.ndarray[numpy.float64], image_weights: numpy.ndarray[numpy.float64]) -> None:
    ...
@typing.overload
def group_blocks(sx: numpy.ndarray[numpy.float32], sy: numpy.ndarray[numpy.float32], sz: numpy.ndarray[numpy.float32], sv: numpy.ndarray[numpy.float32], xmin: float, xres: float, nx: int, ymin: float, yres: float, ny: int, zmin: float, zres: float, nz: int) -> dict[int, list[float]]:
    ...
@typing.overload
def group_blocks(sx: numpy.ndarray[numpy.float32], sy: numpy.ndarray[numpy.float32], sv: numpy.ndarray[numpy.float32], xmin: float, xres: float, nx: int, ymin: float, yres: float, ny: int) -> dict[int, list[float]]:
    ...
@typing.overload
def group_blocks(sx: numpy.ndarray[numpy.float32], sv: numpy.ndarray[numpy.float32], xmin: float, xres: float, nx: int) -> dict[int, list[float]]:
    ...
@typing.overload
def group_blocks(sx: numpy.ndarray[numpy.float64], sy: numpy.ndarray[numpy.float64], sz: numpy.ndarray[numpy.float64], sv: numpy.ndarray[numpy.float64], xmin: float, xres: float, nx: int, ymin: float, yres: float, ny: int, zmin: float, zres: float, nz: int) -> dict[int, list[float]]:
    ...
@typing.overload
def group_blocks(sx: numpy.ndarray[numpy.float64], sy: numpy.ndarray[numpy.float64], sv: numpy.ndarray[numpy.float64], xmin: float, xres: float, nx: int, ymin: float, yres: float, ny: int) -> dict[int, list[float]]:
    ...
@typing.overload
def group_blocks(sx: numpy.ndarray[numpy.float64], sv: numpy.ndarray[numpy.float64], xmin: float, xres: float, nx: int) -> dict[int, list[float]]:
    ...
