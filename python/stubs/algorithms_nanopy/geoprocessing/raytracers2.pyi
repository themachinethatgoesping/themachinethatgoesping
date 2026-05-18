"""
Layer-based closed-form Snell raytracer (next-generation successor to raytracers/RTConstantSVP).
"""

from collections.abc import Sequence
from typing import Annotated, overload

import numpy
from numpy.typing import NDArray

import themachinethatgoesping.navigation_nanopy
import themachinethatgoesping.navigation_nanopy.datastructures


class SoundVelocityProfile:
    """
    1-D depth-dependent sound velocity profile with precomputed layer constants.
    """

    @overload
    def __init__(self) -> None:
        """Construct an empty SoundVelocityProfile"""

    @overload
    def __init__(self, depths_in_meters: Annotated[NDArray[numpy.float32], dict(order='C')], sound_speeds_in_meters_per_second: Annotated[NDArray[numpy.float32], dict(order='C')]) -> None:
        """Construct from depth (m) and sound speed (m/s) arrays."""

    def __eq__(self, other: SoundVelocityProfile) -> bool: ...

    @staticmethod
    def uniform(c: float, z_max: float = 12000.0) -> SoundVelocityProfile:
        """Convenience: constant SVP from surface to z_max."""

    def set(self, depths_in_meters: Annotated[NDArray[numpy.float32], dict(order='C')], sound_speeds_in_meters_per_second: Annotated[NDArray[numpy.float32], dict(order='C')]) -> None:
        """Set depth/sound-speed tables and recompute layer constants."""

    def get_depths_in_meters(self) -> Annotated[NDArray[numpy.float32], dict(order='C')]:
        """All depth knots (m), absolute coordinates."""

    def get_sound_speeds_in_meters_per_second(self) -> Annotated[NDArray[numpy.float32], dict(order='C')]:
        """All sound speeds (m/s), one per depth knot."""

    def get_sound_speed_gradients_in_per_second(self) -> Annotated[NDArray[numpy.float32], dict(order='C')]:
        """Sound-speed gradient dc/dz (s⁻¹) per layer (size = number_of_layers)."""

    def get_inverse_sound_speed_gradients_in_seconds(self) -> Annotated[NDArray[numpy.float32], dict(order='C')]:
        """1/gradient (s) per layer; 0 for iso-velocity layers."""

    def get_isovelocity_flags(self) -> Annotated[NDArray[numpy.bool_], dict(order='C')]:
        """Per-layer iso-velocity flag (true when |gradient| < ISO_EPS)."""

    def get_number_of_layers(self) -> int:
        """Number of layers (= number of knots - 1)."""

    def get_sound_speed(self, depth_in_meters: float) -> float:
        """Sound speed at depth z (linear interp; clamped at endpoints)."""

    def get_depth_in_meters(self, index: int) -> float:
        """Depth (m) at the given knot index."""

    def get_sound_speed_in_meters_per_second(self, index: int) -> float:
        """Sound speed (m/s) at the given knot index."""

    def get_number_of_entries(self) -> int:
        """Number of (depth, sound speed) entries (= number_of_layers + 1)."""

    def get_timestamp(self) -> float | None:
        """Unix timestamp (seconds since epoch, UTC), or None if not set."""

    def set_timestamp(self, timestamp: float | None) -> None:
        """Set the unix timestamp (or None to clear)."""

    def has_timestamp(self) -> bool: ...

    def get_latitude(self) -> float | None:
        """Latitude (decimal degrees, +N), or None if not set."""

    def set_latitude(self, latitude: float | None) -> None:
        """Set latitude (or None to clear)."""

    def get_longitude(self) -> float | None:
        """Longitude (decimal degrees, +E), or None if not set."""

    def set_longitude(self, longitude: float | None) -> None:
        """Set longitude (or None to clear)."""

    def set_location(self, latitude: float | None, longitude: float | None) -> None:
        """Set both latitude and longitude at once."""

    def has_location(self) -> bool: ...

    def get_date_string(self, fractionalSecondsDigits: int = 2, format: str = '%z__%d-%m-%Y__%H:%M:%S') -> str:
        """Format the timestamp as a date string."""

    def copy(self) -> SoundVelocityProfile:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> SoundVelocityProfile: ...

    def __deepcopy__(self, arg: dict, /) -> SoundVelocityProfile: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> SoundVelocityProfile:
        """create T_CLASS object from bytearray"""

    def __getstate__(self) -> bytes: ...

    def __setstate__(self, arg: bytes, /) -> None: ...

    def __hash__(self) -> int:
        """hash function implemented using binary_hash"""

    def hash(self) -> int:
        """hash function implemented using binary_hash"""

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""

class LayerRaytracer:
    """
    Closed-form Snell raytracer through a 1-D layered SVP. Returns world-frame [K+1, n_beams, 3] xyz at user-supplied one-way travel-time knots, anchored exactly to each knot.
    """

    @overload
    def __init__(self) -> None:
        """Construct an empty LayerRaytracer (SVP must be set before tracing)"""

    @overload
    def __init__(self, svp: SoundVelocityProfile) -> None:
        """Construct a LayerRaytracer with the given SoundVelocityProfile."""

    def __eq__(self, other: LayerRaytracer) -> bool: ...

    def get_svp(self) -> SoundVelocityProfile: ...

    def set_svp(self, svp: SoundVelocityProfile) -> None: ...

    @overload
    def trace_at_times(self, launch_dirs: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')], knot_times: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], tx_poses: Sequence[themachinethatgoesping.navigation_nanopy.datastructures.Geolocation], rx_poses: Sequence[themachinethatgoesping.navigation_nanopy.datastructures.Geolocation], mp_cores: int = 1) -> Annotated[NDArray[numpy.float32], dict(order='C')]:
        """
        Trace beams to one-way travel-time knots using separate TX/RX poses.
        launch_dirs: [n_beams, 3] vehicle-frame unit vectors (forward, starboard, down).
        knot_times:  [K+1] one-way travel times (s), monotone, [0] >= 0.
        tx_poses, rx_poses: length K+1 lists of Geolocation (one pose per knot).
        Returns [K+1, n_beams, 3] world-frame xyz (NaN where ray turned/exited).
        """

    @overload
    def trace_at_times(self, launch_dirs: Annotated[NDArray[numpy.float32], dict(shape=(None, None), order='C')], knot_times: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], poses: Sequence[themachinethatgoesping.navigation_nanopy.datastructures.Geolocation], mp_cores: int = 1) -> Annotated[NDArray[numpy.float32], dict(order='C')]:
        """
        Trace beams to one-way travel-time knots using a single per-knot pose (equivalent to passing tx_poses == rx_poses).
        """

    @staticmethod
    def launch_dirs_from_angles(tilt_deg: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], crosstrack_deg: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')]) -> Annotated[NDArray[numpy.float32], dict(order='C')]:
        """
        Convert per-beam (tilt_deg, crosstrack_deg) into [n_beams, 3] vehicle-frame unit launch directions (forward, starboard, down). tilt: positive forward; crosstrack: positive starboard.
        """

    @overload
    def trace_at_angles(self, tilt_deg: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], crosstrack_deg: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], knot_times: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], tx_poses: Sequence[themachinethatgoesping.navigation_nanopy.datastructures.Geolocation], rx_poses: Sequence[themachinethatgoesping.navigation_nanopy.datastructures.Geolocation], mp_cores: int = 1) -> Annotated[NDArray[numpy.float32], dict(order='C')]:
        """
        Trace beams given per-beam (tilt_deg, crosstrack_deg) and TX/RX poses.
        tilt_deg, crosstrack_deg: [n_beams] floats. tilt positive forward, crosstrack positive starboard.
        """

    @overload
    def trace_at_angles(self, tilt_deg: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], crosstrack_deg: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], knot_times: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], poses: Sequence[themachinethatgoesping.navigation_nanopy.datastructures.Geolocation], mp_cores: int = 1) -> Annotated[NDArray[numpy.float32], dict(order='C')]:
        """
        Same as trace_at_angles(tx_poses, rx_poses) but with a single per-knot pose.
        """

    def trace_to_xyz(self, tilt_deg: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], crosstrack_deg: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], two_way_travel_times: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], tx_delays: Annotated[NDArray[numpy.float32], dict(shape=(None,), order='C')], tx_mount: themachinethatgoesping.navigation_nanopy.datastructures.PositionalOffsets, rx_mount: themachinethatgoesping.navigation_nanopy.datastructures.PositionalOffsets, tx_face_depth_m: float, n_knots: int = 2, nav: themachinethatgoesping.navigation_nanopy.NavigationInterpolatorLatLon | None = None, t_tx_ping: float = 0.0, mp_cores: int = 1) -> Annotated[NDArray[numpy.float32], dict(order='C')]:
        """
        Trace beams using Kongsberg-native dual-array inputs.
        Output frame: TX-body axes (forward, starboard, down) at
        t_tx_ping, origin = TX transducer face at t_tx_ping. Apply
        BeamSampleGeometry::with_rigid_transform with the world TX-face
        pose at t_tx_ping to obtain world coordinates.

        tilt_deg:        [N] tilt re TX array, +forward (deg)
        crosstrack_deg:  [N] beam pointing re RX array, +starboard (deg)
        two_way_travel_times: [N] (s)
        tx_delays:       [N] per-beam sector TX delay re t_tx_ping (s)
        tx_mount, rx_mount: PositionalOffsets of the TX and RX arrays
        tx_face_depth_m: absolute world depth of TX face at t_tx_ping (m)
        n_knots:         number of trace knots (>=2). Knot k is at
                         one-way time twtt[i]*k/(2*(n_knots-1));
                         k = n_knots-1 is the bottom return.
        nav:             optional NavigationInterpolatorLatLon for
                         motion compensation (sampled at t_tx_eff,
                         t_rx_eff and t_tx_ping). Pass None to skip.
        t_tx_ping:       wall-clock time of the ping (s).
        Returns [n_knots, N, 3] xyz in TX-body-at-t_tx_ping; NaN where
        the ray turned or input was non-finite.
        """

    def copy(self) -> LayerRaytracer:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> LayerRaytracer: ...

    def __deepcopy__(self, arg: dict, /) -> LayerRaytracer: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> LayerRaytracer:
        """create T_CLASS object from bytearray"""

    def __getstate__(self) -> bytes: ...

    def __setstate__(self, arg: bytes, /) -> None: ...

    def __hash__(self) -> int:
        """hash function implemented using binary_hash"""

    def hash(self) -> int:
        """hash function implemented using binary_hash"""

    def __str__(self) -> str:
        """Return object information as string"""

    def __repr__(self) -> str:
        """Return object information as string"""

    def info_string(self, float_precision: int = 3, superscript_exponents: bool = True) -> str:
        """Return object information as string"""

    def print(self, float_precision: int = 3, superscript_exponents: bool = True) -> None:
        """Print object information"""
