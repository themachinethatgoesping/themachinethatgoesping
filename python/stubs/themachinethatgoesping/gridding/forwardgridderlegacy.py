"""

Simple gridder class that can create quantitative 3D images from x,z,y,val from some custom data.
"""
from __future__ import annotations
import numpy
import numpy as np
from themachinethatgoesping.gridding.functions import gridfunctions as grdf
import typing
__all__: list[str] = ['ArrayLike', 'ForwardGridderLegacy', 'grdf', 'np']
class ForwardGridderLegacy:
    """
    Simple class to generate 3D grids (images) and interpolate xyz data onto a grid using simple forward mapping algorithms.
    (e.g. block mean, weighted mean interpolation)
    """
    @staticmethod
    def get_minmax(sx: typing.Union[collections.abc.Buffer, numpy._typing._array_like._SupportsArray[numpy.dtype[typing.Any]], numpy._typing._nested_sequence._NestedSequence[numpy._typing._array_like._SupportsArray[numpy.dtype[typing.Any]]], bool, int, float, complex, str, bytes, numpy._typing._nested_sequence._NestedSequence[bool | int | float | complex | str | bytes]], sy: typing.Union[collections.abc.Buffer, numpy._typing._array_like._SupportsArray[numpy.dtype[typing.Any]], numpy._typing._nested_sequence._NestedSequence[numpy._typing._array_like._SupportsArray[numpy.dtype[typing.Any]]], bool, int, float, complex, str, bytes, numpy._typing._nested_sequence._NestedSequence[bool | int | float | complex | str | bytes]], sz: typing.Union[collections.abc.Buffer, numpy._typing._array_like._SupportsArray[numpy.dtype[typing.Any]], numpy._typing._nested_sequence._NestedSequence[numpy._typing._array_like._SupportsArray[numpy.dtype[typing.Any]]], bool, int, float, complex, str, bytes, numpy._typing._nested_sequence._NestedSequence[bool | int | float | complex | str | bytes]]) -> tuple:
        """
        returns the min/max value of three lists (same size).
        Sometimes faster than separate numpy functions because it only loops once.
        
        Parameters
        ----------
        sx : ArrayLike
            1D array with x positions (same size)
        sy : ArrayLike
            1D array with x positions (same size)
        sz : ArrayLike
            1D array with x positions (same size)
        
        Returns
        -------
        tuple
            with (xmin,xmax,ymin,ymax,zmin,zmax)
        """
    @classmethod
    def from_data(cls, res: float, sx: typing.Union[collections.abc.Buffer, numpy._typing._array_like._SupportsArray[numpy.dtype[typing.Any]], numpy._typing._nested_sequence._NestedSequence[numpy._typing._array_like._SupportsArray[numpy.dtype[typing.Any]]], bool, int, float, complex, str, bytes, numpy._typing._nested_sequence._NestedSequence[bool | int | float | complex | str | bytes]], sy: typing.Union[collections.abc.Buffer, numpy._typing._array_like._SupportsArray[numpy.dtype[typing.Any]], numpy._typing._nested_sequence._NestedSequence[numpy._typing._array_like._SupportsArray[numpy.dtype[typing.Any]]], bool, int, float, complex, str, bytes, numpy._typing._nested_sequence._NestedSequence[bool | int | float | complex | str | bytes]], sz: typing.Union[collections.abc.Buffer, numpy._typing._array_like._SupportsArray[numpy.dtype[typing.Any]], numpy._typing._nested_sequence._NestedSequence[numpy._typing._array_like._SupportsArray[numpy.dtype[typing.Any]]], bool, int, float, complex, str, bytes, numpy._typing._nested_sequence._NestedSequence[bool | int | float | complex | str | bytes]]):
        """
        Create gridder with resolution "res"
        xmin,xmax,ymin,ymax,zmin,zmax are determined to exactly contain the given data vectors (sx,sy,sz)
        
        Parameters
        ----------
        res : float
            x,y and z resolution of the grid
        sx : ArrayLike
            array with x data
        sy : ArrayLike
            array with y data
        sz : ArrayLike
            array with z data
        
        Returns
        -------
        ForwardGridder
            ForwardGridder object
        """
    @classmethod
    def from_res(cls, res: float, min_x: float, max_x: float, min_y: float, max_y: float, min_z: float, max_z: float):
        """
        Create gridder setting xres,yres and zres to "res"
        
        Parameters
        ----------
        res : float
            x,y and z resolution of the grid
        min_x : float
            smallest x value that must be contained within the grid
        max_x : float
            largest x value that must be contained within the grid
        min_y : float
            smallest y value that must be contained within the grid
        max_y : float
            smallest y value that must be contained within the grid
        min_z : float
            smallest z value that must be contained within the grid
        max_z : float
            smallest z value that must be contained within the grid
        
        Returns
        -------
        ForwardGridder
            ForwardGridder object
        """
    def __init__(self, xres: float, yres: float, zres: float, min_x: float, max_x: float, min_y: float, max_y: float, min_z: float, max_z: float, xbase: float = 0.0, ybase: float = 0.0, zbase: float = 0.0):
        """
        Initialize forward gridder class using grid parameters.
        
        Parameters
        ----------
        xres : float
            x resolution of the grid
        yres : float
            y resolution of the grid
        zres : float
            z resolution of the grid
        min_x : float
            smallest x value that must be contained within the grid
        max_x : float
            largest x value that must be contained within the grid
        min_y : float
            smallest y value that must be contained within the grid
        max_y : float
            largest y value that must be contained within the grid
        min_z : float
            smallest z value that must be contained within the grid
        max_z : float
            largest z value that must be contained within the grid
        xbase : float, optional
            x base position of the grid, by default 0.0
        ybase : float, optional
            y base position of the grid, by default 0.0
        zbase : float, optional
            z base position of the grid, by default 0.0
        """
    def _get_min_and_offset(self):
        ...
    def get_empty_grd_images(self) -> tuple:
        """
        create empty num and sum grid images
        
        Returns
        -------
        (image_values, image_weights):
            image_values: summed value for each grid position
            image_weights: weights for each grid position
        """
    def get_extent(self, axis: str = 'xyz') -> list:
        """
        return x,y,z extend (useful for plotting)
        """
    def get_extent_x(self) -> list:
        """
        return x extend (useful for plotting)
        """
    def get_extent_y(self) -> list:
        """
        return y extend (useful for plotting)
        """
    def get_extent_z(self) -> list:
        """
        return z extend (useful for plotting)
        """
    def get_x_coordinates(self) -> list:
        """
        return valid x grid coordinates as list
        """
    def get_x_grd_value(self, x: float) -> float:
        """
        return the x value of the grid cell that contains x
        
        Parameters
        ----------
        x : float
        
        Returns
        -------
        x_value of grid cell : float
        """
    def get_x_index(self, x: float) -> int:
        """
        get the x index of the grid cell that physically contains "x"
        
        Parameters
        ----------
        x : float
        
        Returns
        -------
        x_index : int
        """
    def get_x_index_fraction(self, x: float) -> float:
        """
        get the fractional x index of "x" within the 3D grid image
        
        Parameters
        ----------
        x : float
        
        Returns
        -------
        x_index : float
        """
    def get_x_value(self, x_index: float) -> float:
        """
        return the x value of the grid cell of index x_index
        
        Parameters
        ----------
        x_index : int
        
        Returns
        -------
        x : float
        """
    def get_y_coordinates(self) -> list:
        """
        return valid y grid coordinates as list
        """
    def get_y_grd_value(self, y: float) -> float:
        """
        return the y value of the grid cell that contains y
        
        Parameters
        ----------
        y : float
        
        Returns
        -------
        y_value of grid cell : float
        """
    def get_y_index(self, y: float) -> int:
        """
        get the y index of the grid cell that physically contains "x"
        
        Parameters
        ----------
        y : float
        
        Returns
        -------
        y_index : int
        """
    def get_y_index_fraction(self, y: float) -> float:
        """
        get the fractional y index of "y" within the 3D grid image
        
        Parameters
        ----------
        y : float
        
        Returns
        -------
        y_index : float
        """
    def get_y_value(self, y_index: int) -> float:
        """
        return the y value of the grid cell of index y_index
        
        Parameters
        ----------
        y_index : int
        
        Returns
        -------
        y : float
        """
    def get_z_coordinates(self) -> list:
        """
        return valid z grid coordinates as list
        """
    def get_z_grd_value(self, z: float) -> float:
        """
        return the z value of the grid cell that contains z
        
        Parameters
        ----------
        z : float
        
        Returns
        -------
        z_value of grid cell : float
        """
    def get_z_index(self, z: float) -> int:
        """
        get the y index of the grid cell that physically contains "z"
        
        Parameters
        ----------
        z : float
        
        Returns
        -------
        z_index : int
        """
    def get_z_index_fraction(self, z: float) -> float:
        """
        get the fractional z index of "z" within the 3D grid image
        
        Parameters
        ----------
        z : float
        
        Returns
        -------
        z_index : float
        """
    def get_z_value(self, z_index: int) -> float:
        """
        return the z value of the grid cell of index z_index
        
        Parameters
        ----------
        z_index : int
        
        Returns
        -------
        z : float
        """
    def interpolate_block_mean(self, sx: typing.Union[collections.abc.Buffer, numpy._typing._array_like._SupportsArray[numpy.dtype[typing.Any]], numpy._typing._nested_sequence._NestedSequence[numpy._typing._array_like._SupportsArray[numpy.dtype[typing.Any]]], bool, int, float, complex, str, bytes, numpy._typing._nested_sequence._NestedSequence[bool | int | float | complex | str | bytes]], sy: typing.Union[collections.abc.Buffer, numpy._typing._array_like._SupportsArray[numpy.dtype[typing.Any]], numpy._typing._nested_sequence._NestedSequence[numpy._typing._array_like._SupportsArray[numpy.dtype[typing.Any]]], bool, int, float, complex, str, bytes, numpy._typing._nested_sequence._NestedSequence[bool | int | float | complex | str | bytes]], sz: typing.Union[collections.abc.Buffer, numpy._typing._array_like._SupportsArray[numpy.dtype[typing.Any]], numpy._typing._nested_sequence._NestedSequence[numpy._typing._array_like._SupportsArray[numpy.dtype[typing.Any]]], bool, int, float, complex, str, bytes, numpy._typing._nested_sequence._NestedSequence[bool | int | float | complex | str | bytes]], s_val: typing.Union[collections.abc.Buffer, numpy._typing._array_like._SupportsArray[numpy.dtype[typing.Any]], numpy._typing._nested_sequence._NestedSequence[numpy._typing._array_like._SupportsArray[numpy.dtype[typing.Any]]], bool, int, float, complex, str, bytes, numpy._typing._nested_sequence._NestedSequence[bool | int | float | complex | str | bytes]], image_values: numpy.ndarray = None, image_weights: numpy.ndarray = None, skip_invalid: bool = True) -> tuple:
        """
        interpolate 3D points onto 3d images using block mean interpolation
        
        Parameters
        ----------
        sx : ArrayLike
            x values
        sy : ArrayLike
            y values
        sz : ArrayLike
            z values
        s_val : ArrayLike
            amplitudes / volume backscattering coefficients
        image_values : np.ndarray, optional
            Image with values. If None a new image will be created. Dimensions must fit the internal nx,ny,nz
        image_weights : np.ndarray, optional
            Image with weights. If None a new image will be created. Dimensions must fit the internal nx,ny,nz
        skip_invalid : bool, optional
            skip values that exceed border_xmin, _xmax, _ymin, _ymax, _zmin, _zmax. Otherwise throw exception by default True
        
        Returns
        -------
        tuple
            image_values, image_weights
        """
    def interpolate_weighted_mean(self, sx: typing.Union[collections.abc.Buffer, numpy._typing._array_like._SupportsArray[numpy.dtype[typing.Any]], numpy._typing._nested_sequence._NestedSequence[numpy._typing._array_like._SupportsArray[numpy.dtype[typing.Any]]], bool, int, float, complex, str, bytes, numpy._typing._nested_sequence._NestedSequence[bool | int | float | complex | str | bytes]], sy: typing.Union[collections.abc.Buffer, numpy._typing._array_like._SupportsArray[numpy.dtype[typing.Any]], numpy._typing._nested_sequence._NestedSequence[numpy._typing._array_like._SupportsArray[numpy.dtype[typing.Any]]], bool, int, float, complex, str, bytes, numpy._typing._nested_sequence._NestedSequence[bool | int | float | complex | str | bytes]], sz: typing.Union[collections.abc.Buffer, numpy._typing._array_like._SupportsArray[numpy.dtype[typing.Any]], numpy._typing._nested_sequence._NestedSequence[numpy._typing._array_like._SupportsArray[numpy.dtype[typing.Any]]], bool, int, float, complex, str, bytes, numpy._typing._nested_sequence._NestedSequence[bool | int | float | complex | str | bytes]], s_val: typing.Union[collections.abc.Buffer, numpy._typing._array_like._SupportsArray[numpy.dtype[typing.Any]], numpy._typing._nested_sequence._NestedSequence[numpy._typing._array_like._SupportsArray[numpy.dtype[typing.Any]]], bool, int, float, complex, str, bytes, numpy._typing._nested_sequence._NestedSequence[bool | int | float | complex | str | bytes]], image_values: numpy.ndarray = None, image_weights: numpy.ndarray = None, skip_invalid: bool = True):
        """
        interpolate 3D points onto 3d images using weighted mean interpolation
        
        Parameters
        ----------
        sx : ArrayLike
            x values
        sy : ArrayLike
            y values
        sz : ArrayLike
            z values
        s_val : ArrayLike
            amplitudes / volume backscattering coefficients
        image_values : np.ndarray, optional
            Image with values. If None a new image will be created. Dimensions must fit the internal nx,ny,nz
        image_weights : np.ndarray, optional
            Image with weights. If None a new image will be created. Dimensions must fit the internal nx,ny,nz
        skip_invalid : bool, optional
            skip values that exceed border_xmin, _xmax, _ymin, _ymax, _zmin, _zmax. Otherwise throw exception by default True
        
        Returns
        -------
        tuple
            image_values, image_weights
        """
ArrayLike: typing._UnionGenericAlias  # value = typing.Union[collections.abc.Buffer, numpy._typing._array_like._SupportsArray[numpy.dtype[typing.Any]], numpy._typing._nested_sequence._NestedSequence[numpy._typing._array_like._SupportsArray[numpy.dtype[typing.Any]]], bool, int, float, complex, str, bytes, numpy._typing._nested_sequence._NestedSequence[bool | int | float | complex | str | bytes]]
