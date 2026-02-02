"""
Request objects for echogram image building.

This module defines the data structures used to communicate between
the coordinate system and backends for efficient image generation.
"""

import dataclasses

import np


class EchogramImageRequest:
    """
    Everything a backend needs to produce a downsampled echogram image.

    The coordinate system generates this request containing:
    - Output image dimensions (nx, ny)
    - Which ping maps to each output x column
    - Affine parameters for y→sample index conversion per ping

    The affine mapping is: sample_idx = round(a[p] + b[p] * y)
    where p is the ping index and y is the y-coordinate.

    Attributes:
        nx: Number of output x columns (image width).
        ny: Number of output y rows (image height).
        y_coordinates: The y-axis grid values, shape (ny,).
        ping_indexer: For each x column, which ping to use. Shape (nx,).
            Values are ping indices into backend data, or -1 for invalid.
        affine_a: Affine intercept per ping for y→sample mapping.
            Shape (n_pings,), NaN where undefined.
        affine_b: Affine slope per ping for y→sample mapping.
            Shape (n_pings,), NaN where undefined.
        max_sample_indices: Maximum valid sample index per ping.
            Shape (n_pings,). Used for bounds checking.
        fill_value: Value to use for invalid/missing data.
    """

    fill_value: float = float('nan')

    def compute_sample_indices(self, ping_idx: int) -> np.ndarray:
        """
        Compute sample indices for a single ping.

        Args:
            ping_idx: The ping index (into affine arrays).

        Returns:
            Array of sample indices, shape (ny,). Invalid values are -1.
        """

    def compute_all_sample_indices(self) -> np.ndarray:
        """
        Compute sample indices for all pings at once (vectorized).

        Returns:
            Array of sample indices, shape (n_pings, ny). Invalid values are -1.
        """

    __dataclass_params__: dataclasses._DataclassParams = ...

    __dataclass_fields__: dict = ...

    def __hash__(self): ...

    def __init__(self, nx: int, ny: int, y_coordinates: np.ndarray, ping_indexer: np.ndarray, affine_a: np.ndarray, affine_b: np.ndarray, max_sample_indices: np.ndarray, fill_value: float = float('nan')) -> None: ...

    def __repr__(self): ...

    def __eq__(self, other): ...

    def __setattr__(self, name, value): ...

    def __delattr__(self, name): ...

    __match_args__: tuple = ...
