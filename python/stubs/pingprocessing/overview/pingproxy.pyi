"""
Lightweight ping proxy objects that expose the same duck-typed interface
used by :mod:`~themachinethatgoesping.pingprocessing.filter_pings` and
:mod:`~themachinethatgoesping.pingprocessing.split_pings`, but are
backed by data stored in a :class:`PingOverview`.

This lets you **reuse every existing filter/split function** on overview
data without touching those functions at all.

Round-trip workflow::

    from themachinethatgoesping.pingprocessing.overview.pingproxy import (
        proxies_from_overview, overview_from_proxies,
    )
    from themachinethatgoesping.pingprocessing import filter_pings, split_pings

    # PingOverview → lightweight proxy list
    proxies = proxies_from_overview(overview)

    # Use any existing function unchanged
    filtered = filter_pings.by_time(proxies, min_timestamp=t0, max_timestamp=t1)
    groups   = split_pings.by_region(proxies, coordinates=coords)

    # Convert results back to PingOverview(s)
    overview_filtered = overview_from_proxies(filtered)
    overview_groups   = {k: overview_from_proxies(v) for k, v in groups.items()}

Supported ping methods
----------------------
The proxy implements exactly the methods that the filter/split functions
call on a ping:

- ``get_timestamp()``
- ``get_datetime()``
- ``get_geolocation()``  → returns a real ``GeolocationLatLon``
- ``file_data.get_primary_file_path()``
- ``file_data.get_file_paths()``

Functions that need methods not listed above (e.g. ``has_feature``,
``get_channel_id``, ``watercolumn``, ``bottom``) will not work — but
those don't make sense for overview-only data anyway.
"""

import types

import themachinethatgoesping.navigation as nav
import themachinethatgoesping.pingprocessing.overview.pingoverview
from themachinethatgoesping.pingprocessing.overview.pingoverview import (
    PingOverview as PingOverview
)


class PingProxy:
    """
    Lightweight read-only proxy that quacks like ``I_Ping``.

    Constructed from a single row of :class:`PingOverview` data.  Holds
    only scalar/small values — no heavy sonar data.

    The *overview_index* attribute records which row in the source
    overview this proxy represents, so you can map results back.
    """

    __slots__: tuple = ...

    def __init__(self, timestamp, datetime_val, latitude: float, longitude: float, primary_file_path: str, all_file_paths: list, overview_index: int, yaw: float = 0.0, pitch: float = 0.0, roll: float = 0.0): ...

    def get_timestamp(self): ...

    def get_datetime(self): ...

    def get_geolocation(self): ...

    def __repr__(self): ...

    file_data: types.MemberDescriptorType = ...

    overview_index: types.MemberDescriptorType = ...

def proxies_from_overview(overview: themachinethatgoesping.pingprocessing.overview.pingoverview.PingOverview) -> list[PingProxy]:
    """
    Create a list of :class:`PingProxy` objects from a PingOverview.

    Convenience wrapper around :meth:`PingOverview.to_ping_proxies`.

    Parameters
    ----------
    overview : PingOverview
        Source overview.

    Returns
    -------
    list of PingProxy
        One proxy per ping in the overview, in order.
    """

def overview_from_proxies(proxies: list[PingProxy]) -> themachinethatgoesping.pingprocessing.overview.pingoverview.PingOverview:
    """
    Reconstruct a :class:`PingOverview` from a list of :class:`PingProxy`.

    This is the inverse of :func:`proxies_from_overview`.  The returned
    overview has an ``original_indices`` attribute (list of int) mapping
    each position back to the source overview row.

    Parameters
    ----------
    proxies : list of PingProxy
        Proxy objects (typically the output of a filter/split function).

    Returns
    -------
    PingOverview
        A new overview built from the proxy data.
    """
