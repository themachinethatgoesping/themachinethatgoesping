from typing import Annotated, overload

import numpy
from numpy.typing import NDArray


@overload
def compute_resampled_coordinates(values_min: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], values_max: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], values_res: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], grid_min: float = float('nan'), grid_max: float = float('nan'), max_steps: int = 1024) -> Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]:
    """
    Compute resampled coordinates for gridding operations using
    statistical heuristics

    This function generates a uniform grid of coordinates based on input
    data ranges and resolutions. It uses statistical analysis (quantiles
    and IQR) to determine appropriate grid bounds and resolution when
    explicit limits are not provided or when heuristic bounds are more
    suitable.

    Args:
        values_min: Array of minimum values for each data point (e.g.,
                    depth ranges)
        values_max: Array of maximum values for each data point
        values_res: Array of resolution values for each data point
        grid_min: Explicit minimum grid bound (optional)
        grid_max: Explicit maximum grid bound (optional)
        max_steps: Maximum number of grid points. If exceeded, switches to
                   linear spacing

    Returns:
        coordinates: xtensor array of uniformly spaced grid coordinates
    """

@overload
def compute_resampled_coordinates(values_min: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], values_max: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], values_res: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], grid_min: float = float('nan'), grid_max: float = float('nan'), max_steps: int = 1024) -> Annotated[NDArray[numpy.float64], dict(shape=(None,), order='C')]: ...

@overload
def get_minmax(sb: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], mp_cores: int = 1) -> tuple[float, float]: ...

@overload
def get_minmax(sx: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], sy: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], mp_cores: int = 1) -> tuple[float, float, float, float]: ...

@overload
def get_minmax(sx: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], sy: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], sz: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], mp_cores: int = 1) -> tuple[float, float, float, float, float, float]: ...

@overload
def get_minmax(sb: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], mp_cores: int = 1) -> tuple[float, float]: ...

@overload
def get_minmax(sx: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], sy: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], mp_cores: int = 1) -> tuple[float, float, float, float]: ...

@overload
def get_minmax(sx: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], sy: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], sz: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], mp_cores: int = 1) -> tuple[float, float, float, float, float, float]: ...

@overload
def get_index(val: float, grd_val_min: float, grd_res: float) -> int: ...

@overload
def get_index(val: float, grd_val_min: float, grd_res: float) -> int: ...

@overload
def group_blocks(sx: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], sy: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], sz: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], sv: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], xmin: float, xres: float, nx: int, ymin: float, yres: float, ny: int, zmin: float, zres: float, nz: int) -> dict[int, list[float]]: ...

@overload
def group_blocks(sx: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], sy: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], sv: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], xmin: float, xres: float, nx: int, ymin: float, yres: float, ny: int) -> dict[int, list[float]]: ...

@overload
def group_blocks(sx: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], sv: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], xmin: float, xres: float, nx: int) -> dict[int, list[float]]: ...

@overload
def group_blocks(sx: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], sy: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], sz: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], sv: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], xmin: float, xres: float, nx: int, ymin: float, yres: float, ny: int, zmin: float, zres: float, nz: int) -> dict[int, list[float]]: ...

@overload
def group_blocks(sx: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], sy: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], sv: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], xmin: float, xres: float, nx: int, ymin: float, yres: float, ny: int) -> dict[int, list[float]]: ...

@overload
def group_blocks(sx: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], sv: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], xmin: float, xres: float, nx: int) -> dict[int, list[float]]: ...

@overload
def get_index_fraction(val: float, grd_val_min: float, grd_res: float) -> float: ...

@overload
def get_index_fraction(val: float, grd_val_min: float, grd_res: float) -> float: ...

@overload
def get_value(index: float, grd_val_min: float, grd_res: float) -> float: ...

@overload
def get_value(index: float, grd_val_min: float, grd_res: float) -> float: ...

@overload
def get_grd_value(value: float, grd_val_min: float, grd_res: float) -> float: ...

@overload
def get_grd_value(value: float, grd_val_min: float, grd_res: float) -> float: ...

@overload
def get_index_weights(frac_x: float, frac_y: float, frac_z: float) -> tuple[list[int], list[int], list[int], list[float]]: ...

@overload
def get_index_weights(frac_x: float, frac_y: float) -> tuple[list[int], list[int], list[float]]: ...

@overload
def get_index_weights(frac_x: float) -> tuple[list[int], list[float]]: ...

@overload
def get_index_weights(frac_x: float, frac_y: float, frac_z: float) -> tuple[list[int], list[int], list[int], list[float]]: ...

@overload
def get_index_weights(frac_x: float, frac_y: float) -> tuple[list[int], list[int], list[float]]: ...

@overload
def get_index_weights(frac_x: float) -> tuple[list[int], list[float]]: ...

@overload
def grd_weighted_mean(sx: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], sy: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], sz: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], sv: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], xmin: float, xres: float, nx: int, ymin: float, yres: float, ny: int, zmin: float, zres: float, nz: int, image_values: Annotated[NDArray[numpy.float32], dict(shape=(None, None, None), order='A')], image_weights: Annotated[NDArray[numpy.float32], dict(shape=(None, None, None), order='A')]) -> None: ...

@overload
def grd_weighted_mean(sx: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], sy: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], sv: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], xmin: float, xres: float, nx: int, ymin: float, yres: float, ny: int, image_values: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='A')], image_weights: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='A')]) -> None: ...

@overload
def grd_weighted_mean(sx: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], sv: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], xmin: float, xres: float, nx: int, image_values: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], image_weights: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')]) -> None: ...

@overload
def grd_weighted_mean(sx: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], sy: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], sz: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], sv: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], xmin: float, xres: float, nx: int, ymin: float, yres: float, ny: int, zmin: float, zres: float, nz: int, image_values: Annotated[NDArray[numpy.float64], dict(shape=(None, None, None), order='A')], image_weights: Annotated[NDArray[numpy.float64], dict(shape=(None, None, None), order='A')]) -> None: ...

@overload
def grd_weighted_mean(sx: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], sy: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], sv: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], xmin: float, xres: float, nx: int, ymin: float, yres: float, ny: int, image_values: Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='A')], image_weights: Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='A')]) -> None: ...

@overload
def grd_weighted_mean(sx: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], sv: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], xmin: float, xres: float, nx: int, image_values: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], image_weights: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')]) -> None: ...

@overload
def grd_block_mean(sx: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], sy: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], sz: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], sv: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], xmin: float, xres: float, nx: int, ymin: float, yres: float, ny: int, zmin: float, zres: float, nz: int, image_values: Annotated[NDArray[numpy.float32], dict(shape=(None, None, None), order='A')], image_weights: Annotated[NDArray[numpy.float32], dict(shape=(None, None, None), order='A')]) -> None: ...

@overload
def grd_block_mean(sx: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], sy: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], sv: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], xmin: float, xres: float, nx: int, ymin: float, yres: float, ny: int, image_values: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='A')], image_weights: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='A')]) -> None: ...

@overload
def grd_block_mean(sx: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], sv: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], xmin: float, xres: float, nx: int, image_values: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')], image_weights: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='A')]) -> None: ...

@overload
def grd_block_mean(sx: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], sy: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], sz: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], sv: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], xmin: float, xres: float, nx: int, ymin: float, yres: float, ny: int, zmin: float, zres: float, nz: int, image_values: Annotated[NDArray[numpy.float64], dict(shape=(None, None, None), order='A')], image_weights: Annotated[NDArray[numpy.float64], dict(shape=(None, None, None), order='A')]) -> None: ...

@overload
def grd_block_mean(sx: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], sy: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], sv: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], xmin: float, xres: float, nx: int, ymin: float, yres: float, ny: int, image_values: Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='A')], image_weights: Annotated[NDArray[numpy.float64], dict(shape=(None, None), order='A')]) -> None: ...

@overload
def grd_block_mean(sx: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], sv: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], xmin: float, xres: float, nx: int, image_values: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')], image_weights: Annotated[NDArray[numpy.float64], dict(shape=(None,), order='A')]) -> None: ...
