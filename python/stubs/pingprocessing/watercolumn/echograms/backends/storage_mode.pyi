"""
Storage axis mode definitions for echogram backends.

This module defines how echogram data is stored (what coordinate system),
which affects how backends transform data for display.
"""

import dataclasses
import enum
from typing import Any, Union


class XAxisType(enum.Enum):
    """X-axis storage types."""

    PING_INDEX = ping_index
    """X-axis storage types."""

    PING_TIME = ping_time
    """X-axis storage types."""

class YAxisType(enum.Enum):
    """Y-axis storage types."""

    SAMPLE_INDEX = sample_index
    """Y-axis storage types."""

    SAMPLE_NR = sample_nr
    """Y-axis storage types."""

    DEPTH = depth
    """Y-axis storage types."""

    RANGE = range
    """Y-axis storage types."""

class ResolutionStrategy(enum.Enum):
    """
    Strategy for resolving resolution mismatches when saving combined echograms.
    """

    FINEST = finest
    """
    Strategy for resolving resolution mismatches when saving combined echograms.
    """

    COARSEST = coarsest
    """
    Strategy for resolving resolution mismatches when saving combined echograms.
    """

    SPECIFIED = specified
    """
    Strategy for resolving resolution mismatches when saving combined echograms.
    """

    AUTO = auto
    """
    Strategy for resolving resolution mismatches when saving combined echograms.
    """

class StorageAxisMode:
    """
    Describes the coordinate system of stored echogram data.

    This metadata tells backends how to interpret stored array indices
    and how to transform data for display in different coordinate systems.

    X-axis (ping dimension):
    - Can be irregular (one value per ping, default) or regular (fixed resolution grid)
    - Irregular preserves original ping timing
    - Regular enables more efficient storage and combination

    Y-axis (sample dimension):
    - Always regular grid within each ping (current behavior)
    - Resolution and origin define the mapping: y_value = y_origin + y_index * y_resolution

    Attributes:
        x_axis: Type of x-axis coordinate ("ping_index" or "ping_time")
        y_axis: Type of y-axis coordinate ("sample_index", "sample_nr", "depth", "range")
        x_resolution: X resolution (None = irregular, one per ping; float = regular grid)
        x_origin: Origin for regular x grid (only used if x_resolution is set)
        y_resolution: Y resolution (always regular, default 1.0 for sample_index)
        y_origin: Y origin value (default 0.0)
    """

    x_axis: str = 'ping_index'

    y_axis: str = 'sample_index'

    x_resolution: None = None

    x_origin: None = None

    y_resolution: float = 1.0

    y_origin: float = 0.0

    def __post_init__(self):
        """Validate axis types."""

    @property
    def is_x_regular(self) -> bool:
        """Whether x-axis is stored on a regular grid."""

    @property
    def is_default(self) -> bool:
        """Whether this is the default storage mode (ping_index, sample_index)."""

    @classmethod
    def default(cls) -> StorageAxisMode:
        """
        Create default storage mode: (ping_index, sample_index).

        This matches current behavior where data is stored as raw ping/sample indices.
        """

    @classmethod
    def ping_time_depth(cls, y_resolution: float = 0.1, y_origin: float = 0.0, x_resolution: Union[float, None] = None, x_origin: Union[float, None] = None) -> StorageAxisMode:
        """
        Create storage mode for ping_time/depth coordinates.

        Args:
            y_resolution: Depth resolution in meters (default 0.1m = 10cm).
            y_origin: Starting depth in meters (default 0.0).
            x_resolution: Time resolution in seconds (None = irregular).
            x_origin: Start timestamp (required if x_resolution is set).
        """

    @classmethod
    def ping_time_range(cls, y_resolution: float = 0.1, y_origin: float = 0.0, x_resolution: Union[float, None] = None, x_origin: Union[float, None] = None) -> StorageAxisMode:
        """
        Create storage mode for ping_time/range coordinates.

        Args:
            y_resolution: Range resolution in meters (default 0.1m).
            y_origin: Starting range in meters (default 0.0).
            x_resolution: Time resolution in seconds (None = irregular).
            x_origin: Start timestamp (required if x_resolution is set).
        """

    def to_dict(self) -> dict[str, Any]:
        """Convert to dictionary for JSON serialization."""

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> StorageAxisMode:
        """Create from dictionary (JSON deserialization)."""

    def __repr__(self) -> str: ...

    __dataclass_params__: dataclasses._DataclassParams = ...

    __annotations_cache__: dict = ...

    __dataclass_fields__: dict = ...

    __hash__: None = None

    def __init__(self, x_axis: str = 'ping_index', y_axis: str = 'sample_index', x_resolution: Union[float, None] = None, x_origin: Union[float, None] = None, y_resolution: float = 1.0, y_origin: float = 0.0) -> None: ...

    def __eq__(self, other): ...

    __match_args__: tuple = ...

def compute_resolution_from_backends(backends: list, axis: str, strategy: ResolutionStrategy = ResolutionStrategy.AUTO, specified_resolution: Union[float, None] = None) -> Union[float, None]:
    """
    Compute resolution for combining multiple backends.

    Args:
        backends: List of EchogramDataBackend instances.
        axis: "x" or "y".
        strategy: Resolution strategy to use.
        specified_resolution: Resolution value for SPECIFIED strategy.

    Returns:
        Computed resolution, or None if cannot be determined.
    """
