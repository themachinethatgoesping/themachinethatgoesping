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
    1-D depth-dependent sound velocity profile with layered analytic
           precomputations for use by the LayerRaytracer.

    Depths are absolute (e.g. metres below the sea surface). Optional
    metadata (timestamp, latitude, longitude) is stored as
    ``std::optional_double``.
    """

    @overload
    def __init__(self) -> None:
        """Construct an empty SoundVelocityProfile."""

    @overload
    def __init__(self, depths_in_meters: Annotated[NDArray[numpy.float32], dict(order='C')], sound_speeds_in_meters_per_second: Annotated[NDArray[numpy.float32], dict(order='C')]) -> None:
        """
        Construct from depth/sound-speed tables.
        Args:
            z: monotonically increasing depth knots (m, positive down).
            c: corresponding sound speeds (m/s, must be positive).
        """

    def __eq__(self, other: SoundVelocityProfile) -> bool:
        """Equality comparison (metadata is ignored)."""

    @staticmethod
    def uniform(c: float, z_max: float = 12000.0) -> SoundVelocityProfile:
        """
        Constant-velocity profile from the surface to z_max.
        Args:
            c: sound speed (m/s).
            z_max: maximum depth (m); default 12 000 m.

        Returns:
            SoundVelocityProfile with uniform sound speed.
        """

    def set(self, depths_in_meters: Annotated[NDArray[numpy.float32], dict(order='C')], sound_speeds_in_meters_per_second: Annotated[NDArray[numpy.float32], dict(order='C')]) -> None:
        """
        Set depth/sound-speed tables and recompute layer constants.
        Args:
            z: monotonically increasing depth knots (m, positive down).
            c: corresponding sound speeds (m/s, must be positive).

        Raises:
            std::runtime_error: if sizes differ, fewer than 2 entries, or non-
                monotone depths.
        """

    def get_depths_in_meters(self) -> Annotated[NDArray[numpy.float32], dict(order='C')]:
        """All depth knots (m), absolute coordinates."""

    def get_sound_speeds_in_meters_per_second(self) -> Annotated[NDArray[numpy.float32], dict(order='C')]:
        """All sound speeds (m/s), one per depth knot."""

    def get_sound_speed_gradients_in_per_second(self) -> Annotated[NDArray[numpy.float32], dict(order='C')]:
        """Sound-speed gradient dc/dz (s⁻¹) per layer (size = number_of_layers)."""

    def get_inverse_sound_speed_gradients_in_seconds(self) -> Annotated[NDArray[numpy.float32], dict(order='C')]:
        """
        1 / gradient (s) per layer; 0 for iso-velocity layers (size =
        number_of_layers).
        """

    def get_isovelocity_flags(self) -> Annotated[NDArray[numpy.bool_], dict(order='C')]:
        """
        Per-layer iso-velocity flag: true when |gradient| < ISO_EPS (size =
        number_of_layers).
        """

    def get_number_of_layers(self) -> int:
        """Number of layers (= number of knots − 1)."""

    def get_sound_speed(self, depth_in_meters: float) -> float:
        """Sound speed at depth z (linear interp inside layers, clamped at ends)."""

    def get_depth_in_meters(self, index: int) -> float:
        """Depth (m) at the given knot index."""

    def get_sound_speed_in_meters_per_second(self, index: int) -> float:
        """Sound speed (m/s) at the given knot index."""

    def get_number_of_entries(self) -> int:
        """Number of (depth, sound speed) entries (= number of layers + 1)."""

    def get_timestamp(self) -> float | None:
        """
        Unix timestamp (s, UTC) when the profile was measured, or std::nullopt
        if unset.
        """

    def set_timestamp(self, timestamp: float | None) -> None:
        """Set the unix timestamp (s, UTC); pass std::nullopt to clear."""

    def has_timestamp(self) -> bool:
        """True iff a timestamp is set."""

    def get_latitude(self) -> float | None:
        """
        Latitude (decimal degrees, +N) where the profile was measured, or
        std::nullopt if unset.
        """

    def set_latitude(self, latitude: float | None) -> None:
        """Set latitude (decimal degrees, +N); pass std::nullopt to clear."""

    def get_longitude(self) -> float | None:
        """
        Longitude (decimal degrees, +E) where the profile was measured, or
        std::nullopt if unset.
        """

    def set_longitude(self, longitude: float | None) -> None:
        """Set longitude (decimal degrees, +E); pass std::nullopt to clear."""

    def set_location(self, latitude: float | None, longitude: float | None) -> None:
        """
        Set both latitude (decimal degrees, +N) and longitude (decimal
        degrees, +E) at once.
        """

    def has_location(self) -> bool:
        """True iff both latitude and longitude are set."""

    def get_date_string(self, fractionalSecondsDigits: int = 2, format: str = '%z__%d-%m-%Y__%H:%M:%S') -> str:
        """
        Format ``_timestamp`` as a date string.

        Returns ``"no timestamp"`` if no timestamp is set.

        Args:
            fractionalSecondsDigits: passed to
                                     ``timeconv::unixtime_to_datestring``
            format: passed to ``timeconv::unixtime_to_datestring``
        """

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

class BeamTrace:
    """
    Path of a single traced beam through a layered sound velocity profile.

    The stored points describe the ray polyline in the athwartships y-z
    plane (forward coordinate x is zero). Point 0 is the launch point.
    Depth, horizontal offset, two-way travel time and the cosine of the
    ray angle are stored; incident angle (deg) and cumulative range (m)
    are derived on access.
    """

    @overload
    def __init__(self) -> None:
        """Construct an empty BeamTrace (no points stored)."""

    @overload
    def __init__(self, depths_in_meters: Annotated[NDArray[numpy.float32], dict(order='C')], horizontal_offsets_in_meters: Annotated[NDArray[numpy.float32], dict(order='C')], two_way_travel_times_in_seconds: Annotated[NDArray[numpy.float32], dict(order='C')], cos_incident_angles: Annotated[NDArray[numpy.float32], dict(order='C')]) -> None:
        """
        Construct from the four stored per-point tables (all must have the
        same length).
        Args:
            depths: depth z (m, positive down); point 0 is the launch point.
            horizontal_offsets: signed athwartships offset y (m, positive
                                starboard).
            two_way_travel_times: two-way travel time (s).
            cos_incident_angles: cosine of the ray angle from +z (1=down,
                                 0=turning, −1=up).
        """

    def __eq__(self, other: BeamTrace) -> bool:
        """Equality comparison."""

    def set(self, depths_in_meters: Annotated[NDArray[numpy.float32], dict(order='C')], horizontal_offsets_in_meters: Annotated[NDArray[numpy.float32], dict(order='C')], two_way_travel_times_in_seconds: Annotated[NDArray[numpy.float32], dict(order='C')], cos_incident_angles: Annotated[NDArray[numpy.float32], dict(order='C')]) -> None:
        """
        Set all stored tables at once (all must have the same length).
        Raises:
            std::runtime_error: if table sizes differ.
        """

    def get_number_of_points(self) -> int:
        """
        Number of stored points (>= 1 for a valid trace; point 0 is the launch
        point).
        """

    def get_depths_in_meters(self) -> Annotated[NDArray[numpy.float32], dict(order='C')]:
        """Depth z (m, positive down) at each point."""

    def get_horizontal_offsets_in_meters(self) -> Annotated[NDArray[numpy.float32], dict(order='C')]:
        """Signed athwartships offset y (m, positive starboard) at each point."""

    def get_two_way_travel_times_in_seconds(self) -> Annotated[NDArray[numpy.float32], dict(order='C')]:
        """Two-way travel time (s) at each point."""

    def get_cos_incident_angles(self) -> Annotated[NDArray[numpy.float32], dict(order='C')]:
        """
        Cosine of the ray angle from +z (1 down, 0 turning, -1 up) at each
        point.
        """

    def get_incident_angles_in_degrees(self) -> Annotated[NDArray[numpy.float32], dict(order='C')]:
        """
        Incident angle (deg) from straight down at each point.

        0 deg points down, +-90 deg is horizontal, +-180 deg points up.
        Positive angles correspond to the port side (negative y), consistent
        with a right-handed rotation about +x.
        """

    def get_ranges_in_meters(self) -> Annotated[NDArray[numpy.float32], dict(order='C')]:
        """
        Cumulative along-ray range (m) from the launch point.
        Returns:
            Range array; element 0 is always 0 (launch point).
        """

    def copy(self) -> BeamTrace:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> BeamTrace: ...

    def __deepcopy__(self, arg: dict, /) -> BeamTrace: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> BeamTrace:
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

def trace_beam(launch_depth_in_meters: float, launch_angle_in_degrees: float, sound_velocity_profile: SoundVelocityProfile, two_way_travel_time_in_seconds: float) -> BeamTrace:
    """
    Trace a single beam through a layered sound velocity profile.

    Emits one point at launch, one at each layer crossing and turning
    point, and a final point at the requested travel time (or when the ray
    exits the profile).

    Args:
        launch_depth_in_meters: launch depth (m, positive down); must be
                                inside the profile range.
        launch_angle_in_degrees: angle from straight down (deg); 0 = down,
                                 positive = port.
        sound_velocity_profile: profile to trace through.
        two_way_travel_time_in_seconds: two-way travel time budget (s).

    Returns:
        BeamTrace with the launch point, layer crossings, turning points
        and the final point.
    """
