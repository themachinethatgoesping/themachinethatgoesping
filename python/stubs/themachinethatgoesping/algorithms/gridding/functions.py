"""
Submodule for gridding functions
"""
from __future__ import annotations
import numpy
import pybind11_stubgen.typing_ext
import typing
__all__ = ['get_grd_value', 'get_index', 'get_index_fraction', 'get_index_weights', 'get_minmax', 'get_value', 'grd_block_mean', 'grd_weighted_mean', 'group_blocks']
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
