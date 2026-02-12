"""
Spatial clustering of PingOverview objects.

Provides two clustering approaches:

- :func:`cluster_by_region` — Grid-based connected components.
  **O(n)** time and memory, fastest option.  Best for splitting survey
  data into separate geographic areas or lines.

- :func:`cluster_by_kmeans` — Mini-Batch K-Means on downsampled UTM
  coordinates.  Supports automatic *k* selection via a maximum cluster
  radius.  Requires ``scikit-learn``.

Both return a :class:`ClusterResult` containing the sub-overviews,
cluster-center coordinates, and per-ping labels.

Typical usage::

    from themachinethatgoesping.pingprocessing.overview import cluster

    # Split survey into contiguous geographic regions (O(n), no extra deps)
    result = cluster.cluster_by_region(overview, max_distance_m=500)

    # Or use K-Means with automatic cluster count
    result = cluster.cluster_by_kmeans(
        overview, max_cluster_radius_m=2000, downsample_factor=10,
    )

    for i, ov in enumerate(result):
        lat, lon = result.centers_latlon[i]
        print(f"Cluster {i}: {len(ov.variables['latitude'])} pings "
              f"at ({lat:.4f}, {lon:.4f})")
"""

import dataclasses

import numpy

from themachinethatgoesping.pingprocessing.overview.overlap_filter import (
    subset_overview as subset_overview
)
import themachinethatgoesping.pingprocessing.overview.pingoverview
from themachinethatgoesping.pingprocessing.overview.pingoverview import (
    PingOverview as PingOverview
)


class ClusterResult:
    """
    Result of spatial clustering.

    Attributes
    ----------
    overviews : list of PingOverview
        One PingOverview per cluster, sorted largest-first.
        Each has an ``original_indices`` attribute mapping back to
        the source overview.
    centers_latlon : list of (float, float)
        (latitude, longitude) of each cluster centroid.
    labels : np.ndarray
        Cluster label (0 .. k−1) for every ping in the original overview.
        Labels are ordered so 0 = largest cluster.
        Pings dropped by *min_cluster_size* have label −1.
    """

    def __len__(self): ...

    def __getitem__(self, idx): ...

    def __iter__(self): ...

    def __repr__(self): ...

    __dataclass_params__: dataclasses._DataclassParams = ...

    __annotations_cache__: dict = ...

    __dataclass_fields__: dict = ...

    __hash__: None = None

    def __init__(self, overviews: list[themachinethatgoesping.pingprocessing.overview.pingoverview.PingOverview], centers_latlon: list[tuple[float, float]], labels: numpy.ndarray) -> None: ...

    def __eq__(self, other): ...

    __match_args__: tuple = ('overviews', 'centers_latlon', 'labels')

def cluster_by_region(overview: themachinethatgoesping.pingprocessing.overview.pingoverview.PingOverview, max_distance_m: float = 1000.0, min_cluster_size: int = 10, progress: bool = True) -> ClusterResult:
    """
    Cluster pings into contiguous geographic regions.

    Pings are hashed into square grid cells and adjacent occupied cells
    (8-connected) are merged via union-find.  Each connected component
    becomes one cluster.

    **Complexity**: O(n) time and memory — typically < 1 s for 1 M pings.

    Parameters
    ----------
    overview : PingOverview
        The overview to cluster.
    max_distance_m : float
        Grid cell size in metres (default 1 000).  Pings up to ~1.4×
        this distance apart (cell diagonal) can end up in the same cluster.
    min_cluster_size : int
        Drop clusters with fewer pings (default 10).
    progress : bool
        Show tqdm progress bars (default True).

    Returns
    -------
    ClusterResult
        Clusters sorted largest-first.  Each sub-overview has an
        ``original_indices`` attribute.

    Examples
    --------
    >>> result = cluster_by_region(overview, max_distance_m=500)
    >>> for i, ov in enumerate(result):
    ...     lat, lon = result.centers_latlon[i]
    ...     print(f"Cluster {i}: {len(ov.variables['latitude'])} pings")
    """

def cluster_by_kmeans(overview: themachinethatgoesping.pingprocessing.overview.pingoverview.PingOverview, n_clusters: int = None, max_cluster_radius_m: float = None, downsample_factor: int = 10, min_cluster_size: int = 10, batch_size: int = 1024, max_k: int = 50, progress: bool = True) -> ClusterResult:
    """
    Cluster pings using Mini-Batch K-Means on UTM coordinates.

    Specify **either** *n_clusters* (fixed) **or** *max_cluster_radius_m*
    (automatic: *k* is increased from 2 until every cluster fits within
    the radius, up to *max_k*).

    Fitting is done on downsampled coordinates (every
    *downsample_factor*-th ping); **all** pings are then assigned to the
    nearest center in a batched, memory-efficient pass.

    **Complexity**: O(n) assignment + O(n/ds × k × iters) fitting.
    For 2 M pings with downsample=10 and k≈10, runs in ~1–2 s.

    Requires ``scikit-learn`` (``pip install scikit-learn``).

    Parameters
    ----------
    overview : PingOverview
        The overview to cluster.
    n_clusters : int, optional
        Fixed number of clusters.
    max_cluster_radius_m : float, optional
        Maximum allowed cluster radius in metres.  *k* is increased
        from 2 until satisfied (up to *max_k*).
    downsample_factor : int
        Subsample every n-th ping for fitting (default 10).
    min_cluster_size : int
        Drop clusters with fewer pings (default 10).
    batch_size : int
        Mini-batch size for K-Means (default 1 024).
    max_k : int
        Upper bound on *k* for auto-selection (default 50).
    progress : bool
        Show tqdm progress bars (default True).

    Returns
    -------
    ClusterResult
        Clusters sorted largest-first.

    Raises
    ------
    ImportError
        If scikit-learn is not installed.
    ValueError
        If neither *n_clusters* nor *max_cluster_radius_m* is given.
    """
