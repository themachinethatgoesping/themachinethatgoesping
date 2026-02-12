"""
Functions for filtering and matching pings across multiple PingOverview objects
based on spatial or temporal proximity.

Uses a sparse-grid approach: pings are hashed into grid cells, a bitmask
tracks which overviews occupy each cell, and a 3×3 dilation finds cells
where *all* overviews are present in the local neighbourhood.

Complexity: O(N) time and memory (N = total pings across all overviews).

Typical usage::

    from themachinethatgoesping.pingprocessing.overview import overlap_filter

    filtered = overlap_filter.filter_by_spatial_overlap(
        [overview_a, overview_b, overview_c],
        max_distance_m=100.0,
    )
    # filtered[i].original_indices  → indices into the original overview
"""

import themachinethatgoesping.pingprocessing.overview.pingoverview
from themachinethatgoesping.pingprocessing.overview.pingoverview import (
    PingOverview as PingOverview
)


def subset_overview(overview: themachinethatgoesping.pingprocessing.overview.pingoverview.PingOverview, indices) -> themachinethatgoesping.pingprocessing.overview.pingoverview.PingOverview:
    """
    Create a new PingOverview containing only the specified ping indices.

    Parameters
    ----------
    overview : PingOverview
        Source overview.
    indices : array-like of int
        Ping indices to keep (0-based, must be sorted and unique).

    Returns
    -------
    PingOverview
        New overview with ``original_indices`` attribute mapping each
        new ping position back to its index in the source overview.
    """

def filter_by_spatial_overlap(overviews: list[themachinethatgoesping.pingprocessing.overview.pingoverview.PingOverview], max_distance_m: float = 100.0, progress: bool = True) -> list[themachinethatgoesping.pingprocessing.overview.pingoverview.PingOverview]:
    """
    Keep only pings in areas where **all** overviews have coverage.

    Algorithm
    ---------
    1. Project lat/lon to a common UTM coordinate system (metres).
    2. Hash every ping into a square grid cell of size *max_distance_m*.
    3. For each cell, record which overviews are present (bitmask).
    4. A cell is an **overlap cell** if, considering itself and its 8
       immediate neighbours (3 × 3 block), every overview is represented.
    5. Retain only pings whose cell is an overlap cell.

    This is an *area-based* filter: it guarantees that for every kept
    ping there are pings from all other overviews within roughly
    *max_distance_m* (up to ~1.5 × due to cell-boundary effects).
    Use a smaller *max_distance_m* if tighter control is needed.

    Parameters
    ----------
    overviews : list of PingOverview
        Two or more overviews to compare.
    max_distance_m : float
        Grid cell size in metres (default 100).
    progress : bool
        Show tqdm progress bars (default True).

    Returns
    -------
    list of PingOverview
        One filtered overview per input.  Each has an attribute
        ``original_indices`` (np.ndarray of int) mapping new-ping-index
        → source-ping-index::

            matched_pings = [pings_a[i] for i in filtered[0].original_indices]
    """

def filter_by_temporal_overlap(overviews: list[themachinethatgoesping.pingprocessing.overview.pingoverview.PingOverview], max_time_s: float = 1.0, progress: bool = True) -> list[themachinethatgoesping.pingprocessing.overview.pingoverview.PingOverview]:
    """
    Keep only pings in time windows where **all** overviews have coverage.

    Same grid approach as :func:`filter_by_spatial_overlap` but in 1-D
    (timestamps in seconds).

    Parameters
    ----------
    overviews : list of PingOverview
    max_time_s : float
        Grid cell size in seconds (default 1).
    progress : bool
        Show tqdm progress bars (default True).

    Returns
    -------
    list of PingOverview
        Filtered overviews with ``original_indices`` attribute.
    """

def filter_by_speed(overview: themachinethatgoesping.pingprocessing.overview.pingoverview.PingOverview, min_knots: float = None, max_knots: float = None) -> themachinethatgoesping.pingprocessing.overview.pingoverview.PingOverview:
    """
    Filter a PingOverview by inter-ping speed.

    Computes the speed between consecutive pings and keeps only pings
    where the speed is within [*min_knots*, *max_knots*].

    Parameters
    ----------
    overview : PingOverview
        The overview to filter.
    min_knots : float, optional
        Minimum speed in knots (inclusive). Pings below this are removed.
    max_knots : float, optional
        Maximum speed in knots (inclusive). Pings above this are removed.

    Returns
    -------
    PingOverview
        Filtered overview with ``original_indices`` attribute.
    """
