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

def trace_beam(launch_depth_in_meters: float, launch_angle_in_degrees: float, sound_velocity_profile: SoundVelocityProfile, two_way_travel_time_in_seconds: float, surface_sound_speed_in_meters_per_second: float = -1.0) -> BeamTrace:
    """
    Trace a single beam through a layered sound velocity profile.

    Emits one point at launch, one at each layer crossing and turning
    point, and a final point at the requested travel time (or when the ray
    exits the profile).

    The Snell ray parameter (the invariant that governs refraction) is
    defined by the launch angle and the sound speed at which the beam was
    formed. For a multibeam that is the measured surface/transducer sound
    speed (SSV). Pass it as ``surface_sound_speed_in_meters_per_second``
    whenever it differs from the profile value at the launch depth (e.g.
    the real-time SSV differs from the archived cast); otherwise the
    profile value at the launch depth is used, and both agree exactly when
    the two speeds are equal. Using the wrong launch sound speed
    introduces an angle-dependent (outer-beam) depth bias.

    Args:
        launch_depth_in_meters: launch depth (m, positive down); must be
                                inside the profile range.
        launch_angle_in_degrees: angle from straight down (deg); 0 = down,
                                 positive = port.
        sound_velocity_profile: profile to trace through.
        two_way_travel_time_in_seconds: two-way travel time budget (s).
        surface_sound_speed_in_meters_per_second: sound speed (m/s) at
                                                  which the beam was
                                                  formed; the ray
                                                  parameter is
                                                  sin(angle)/this. <= 0
                                                  (default) falls back to
                                                  the profile value at the
                                                  launch depth.

    Returns:
        BeamTrace with the launch point, layer crossings, turning points
        and the final point.
    """

class RayToDepth:
    """
    Endpoint of one ray leg traced down to a target depth (fast, no
    polyline).

    Produced by trace_beam_to_depth. The horizontal offset and path length
    are magnitudes for the single leg between the launch depth and the
    target depth; the caller carries the horizontal azimuth of the leg
    separately.
    """

    def __init__(self) -> None: ...

    @property
    def horizontal_offset_in_meters(self) -> float:
        """
        Horizontal distance (m, >= 0) from the launch point to the target
        depth.
        """

    @property
    def one_way_travel_time_in_seconds(self) -> float:
        """One-way travel time (s) from the launch point to the target depth."""

    @property
    def path_length_in_meters(self) -> float:
        """Along-ray path length (m) from the launch point to the target depth."""

    @property
    def cos_angle_at_target(self) -> float:
        """
        Cosine of the ray angle from straight down at the target depth (after
        refraction).
        """

    @property
    def reached_target(self) -> bool:
        """
        True if the ray reached the target depth (false if it turned or left
        the profile first).
        """

def trace_beam_to_depth(sound_velocity_profile: SoundVelocityProfile, launch_depth_in_meters: float, launch_zenith_angle_in_radians: float, target_depth_in_meters: float, surface_sound_speed_in_meters_per_second: float = -1.0) -> RayToDepth:
    """
    Trace one ray leg from a launch depth/angle down to a target depth.

    Uses the identical layered-Snell principle as trace_beam (the same
    tracebeam_detail closed-form iso/gradient segment kernels), but
    integrates to a target depth instead of a travel-time budget and only
    accumulates the endpoint (no polyline). This is the fast inner step of
    the bistatic solver, which calls it many times per beam while
    searching for the seabed point; once converged, the full per-layer
    polyline of each leg is produced with trace_beam.

    The launch is downward (0 = nadir); if the ray turns (becomes
    horizontal) or leaves the profile before the target depth,
    reached_target is false.

    Args:
        sound_velocity_profile: layered profile to trace through.
        launch_depth_in_meters: depth (m, positive down) of the leg
                                origin; must be within the profile.
        launch_zenith_angle_in_radians: ray angle from straight down at
                                        the launch point (0 = nadir).
        target_depth_in_meters: depth (m, positive down) to trace to; must
                                be > launch depth and within the profile.
        surface_sound_speed_in_meters_per_second: sound speed (m/s) at
                                                  which the beam was
                                                  formed; the ray
                                                  parameter is
                                                  sin(zenith)/this. <= 0
                                                  (default) falls back to
                                                  the profile value at the
                                                  launch depth. Must match
                                                  trace_beam so
                                                  mono/bistatic agree.

    Returns:
        RayToDepth endpoint of the leg.
    """

class BeamDirections:
    """
    Per-beam pointing directions of a multibeam swath.

    Stores one ship-referenced unit pointing vector per beam (x = forward,
    y = starboard, z = down, reference heading removed). From each
    direction the class derives, on access:
      * the signed beam pointing angle (the athwartships launch angle
        handed to
        trace_beam: 0 deg = nadir/down, +90 deg = horizontal to port, -90
                    deg =
        horizontal to starboard),
      * the beam azimuth (the fore-aft rotation about the vertical/down
        axis that lifts a 2-D trace (horizontal_offset, depth) back into
        ship-frame xyz),
      * the unsigned beam take-off angle from nadir.

    A traced beam point is lifted back into the ship frame by rotating it
    about the vertical (down) axis by the beam azimuth:
      x_forward   = -horizontal_offset * sin(beam_azimuth) y_starboard =
      horizontal_offset * cos(beam_azimuth) z_down      =  depth
    i.e. xyz = R_down(beam_azimuth) * (0, horizontal_offset, depth).
    """

    @overload
    def __init__(self) -> None:
        """Construct an empty BeamDirections (no beams stored)."""

    @overload
    def __init__(self, directions: Annotated[NDArray[numpy.float32], dict(order='C')]) -> None:
        """
        Construct from per-beam unit pointing vectors.
        Args:
            directions: [n_beams, 3] tensor of (forward, starboard, down)
                        components.

        Raises:
            std::runtime_error: if the second dimension is not 3.
        """

    def __eq__(self, other: BeamDirections) -> bool:
        """Equality comparison."""

    def set(self, directions: Annotated[NDArray[numpy.float32], dict(order='C')]) -> None:
        """
        Set the per-beam unit pointing vectors.
        Args:
            directions: [n_beams, 3] tensor of (forward, starboard, down)
                        components.

        Raises:
            std::runtime_error: if the second dimension is not 3.
        """

    def get_number_of_beams(self) -> int:
        """Number of beams stored."""

    def get_directions(self) -> Annotated[NDArray[numpy.float32], dict(order='C')]:
        """
        Per-beam ship-referenced unit pointing vectors [n_beams, 3] =
        (forward, starboard, down).
        """

    def get_beam_direction(self, beam_index: int) -> list[float]:
        """
        Ship-referenced unit pointing vector (forward, starboard, down) of a
        single beam.

        Convenience accessor for feeding one beam's direction as the
        concentric initial guess into trace_bistatic_beam.
        Args:
            beam_index: index of the beam.
        """

    def get_beam_pointing_angles_in_degrees(self) -> Annotated[NDArray[numpy.float32], dict(order='C')]:
        """
        Signed beam pointing angle (deg): the athwartships launch angle for
        trace_beam.

        0 deg is nadir (straight down), +90 deg is horizontal to port, -90 deg
        is horizontal to starboard. Its magnitude equals the take-off angle
        from nadir; its sign follows the port (+) / starboard (-) side of the
        beam. Combined with get_beam_azimuth_angles_in_degrees() it
        reconstructs the full 3-D direction:
          d = R_down(beam_azimuth) * (0, -sin(beam_pointing),
          cos(beam_pointing)).
        """

    def get_beam_azimuth_angles_in_degrees(self) -> Annotated[NDArray[numpy.float32], dict(order='C')]:
        """
        Beam azimuth (deg): the fore-aft rotation about the vertical (down)
        axis.

        Principal value in (-90, 90]; 0 deg means the beam lies in the
        athwartships plane (no fore-aft component). Used to lift a 2-D trace
        back into 3-D:
          xyz = R_down(beam_azimuth) * (0, horizontal_offset, depth).
        """

    def get_beam_takeoff_angles_in_degrees(self) -> Annotated[NDArray[numpy.float32], dict(order='C')]:
        """
        Unsigned beam take-off angle (deg) from nadir (straight down), always
        >= 0.

        0 deg is nadir, 90 deg is horizontal. Equals |beam pointing angle|.
        """

    def copy(self) -> BeamDirections:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> BeamDirections: ...

    def __deepcopy__(self, arg: dict, /) -> BeamDirections: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> BeamDirections:
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

def compute_beam_directions(transmit_installation_ypr_in_degrees: Sequence[float], receive_installation_ypr_in_degrees: Sequence[float], transmit_attitude_ypr_in_degrees: Annotated[NDArray[numpy.float32], dict(order='C')], receive_attitude_ypr_in_degrees: Annotated[NDArray[numpy.float32], dict(order='C')], transmit_steering_angles_in_degrees: Annotated[NDArray[numpy.float32], dict(order='C')], receive_steering_angles_in_degrees: Annotated[NDArray[numpy.float32], dict(order='C')], reference_heading_in_degrees: float, mp_cores: int = 1) -> BeamDirections:
    """
    Compute the ship-referenced pointing direction of every beam.

    Each beam is the downward intersection of the transmit and receive
    array "fans" (Mills cross). The transmit array long axis (forward) and
    the receive array long axis (starboard) are placed in the world frame
    from their installation orientation and the vessel attitude at
    transmit / receive; the transmit and receive steering angles then fix
    the beam's projection onto each axis. The intersection is solved
    directly (no orthogonality assumption), so array non-orthogonality is
    exact and reverse mounts are handled by the installation quaternion
    alone (no manual sign flips).

    Args:
        transmit_installation_ypr_in_degrees: (yaw, pitch, roll) mounting
                                              orientation of the transmit
                                              array.
        receive_installation_ypr_in_degrees: (yaw, pitch, roll) mounting
                                             orientation of the receive
                                             array.
        transmit_attitude_ypr_in_degrees: [n_beams, 3] vessel (yaw, pitch,
                                          roll) at transmit time.
        receive_attitude_ypr_in_degrees: [n_beams, 3] vessel (yaw, pitch,
                                         roll) at receive time.
        transmit_steering_angles_in_degrees: [n_beams] fore-aft transmit
                                             tilt (positive forward).
        receive_steering_angles_in_degrees: [n_beams] across-track receive
                                            angle (positive to PORT).
        reference_heading_in_degrees: heading the output is expressed
                                      relative to.
        mp_cores: number of OpenMP cores for the per-beam solve (default
                  1).

    Returns:
        BeamDirections with one ship-referenced unit pointing vector per
        beam.
    """

def beam_direction_to_pointing_and_azimuth_in_degrees(forward: float, starboard: float, down: float) -> list[float]:
    """
    Decompose a ship-frame beam direction into a signed pointing angle and
    azimuth.

    Scalar counterpart of
    BeamDirections::get_beam_pointing_angles_in_degrees /
    get_beam_azimuth_angles_in_degrees, using the identical convention:
    the pointing angle is 0 deg at nadir, +90 deg horizontal to port, -90
    deg to starboard; the azimuth is the fore-aft rotation about the
    vertical (down) axis, principal value in (-90, 90]. Together they
    reconstruct the direction:
      d = R_down(azimuth) * (0, -sin(pointing), cos(pointing)).

    Args:
        forward: forward (x) component of the unit direction.
        starboard: starboard (y) component.
        down: down (z) component.

    Returns:
        {pointing_angle_in_degrees, azimuth_in_degrees}.
    """

def correct_steering_angles_for_surface_sound_speed(steering_angles_in_degrees: Annotated[NDArray[numpy.float32], dict(order='C')], surface_sound_speed_used_in_meters_per_second: float, surface_sound_speed_corrected_in_meters_per_second: float) -> Annotated[NDArray[numpy.float32], dict(order='C')]:
    """
    Snell correction of a beam steering angle for a changed surface sound
    speed.

    Multibeam beamforming forms every steering angle in the near field
    using the surface sound speed measured at the transducer. If that
    surface sound speed is wrong, the true beam angle in the water
    refracts across the transducer face following Snell's law:
      sin(corrected) = (c_corrected / c_used) * sin(steering).
    The correction must be applied to the transmit and receive steering
    angles *before* compute_beam_directions, because the steering angles
    are defined at the array face, which is where the refraction happens.
    Angles that would exceed the horizon are clamped to +-90 deg.

    Args:
        steering_angles_in_degrees: nominal steering angles (deg).
        surface_sound_speed_used_in_meters_per_second: surface sound speed
                                                       used when the beams
                                                       were formed.
        surface_sound_speed_corrected_in_meters_per_second: true /
                                                            corrected
                                                            surface sound
                                                            speed.

    Returns:
        corrected steering angles (deg).
    """

def correct_steering_angle_for_surface_sound_speed(steering_angle_in_degrees: float, surface_sound_speed_used_in_meters_per_second: float, surface_sound_speed_corrected_in_meters_per_second: float) -> float:
    """
    Scalar overload of correct_steering_angles_for_surface_sound_speed.


    $See also:

    correct_steering_angles_for_surface_sound_speed
    """

class BistaticBeamTrace:
    """
    True-bistatic trace of a single multibeam beam: two refracted legs
    meeting at the seabed.

    Stores the transmit leg and the receive leg each as a BeamTrace (the
    per-layer polyline in that leg's own vertical plane, exactly as
    trace_beam produces them), together with the horizontal azimuth of
    each leg (used to lift its 2-D polyline into the common ship frame),
    the solved seabed point (forward, starboard, down) and the final
    solver residual. Launch angles, the seabed incidence and the modelled
    two-way travel time are derived from the two legs on access rather
    than stored.

    The per-layer TRANSMIT ray direction used for backscatter is the
    transmit leg's incident-angle series
    (BeamTrace::get_incident_angles_in_degrees / get_cos_incident_angles);
    its value at the last point is the seabed incidence.

    A 2-D leg point (horizontal_offset, depth) is lifted into the ship
    frame by the leg azimuth psi and that leg's array position P:
      x_forward   = P_forward   - horizontal_offset * sin(psi) y_starboard
      = P_starboard + horizontal_offset * cos(psi) z_down      = depth
    """

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, transmit_leg: BeamTrace, receive_leg: BeamTrace, transmit_azimuth_in_degrees: float, receive_azimuth_in_degrees: float, bottom_position: Sequence[float], solver_residual_in_meters: float) -> None:
        """
        Construct from the two converged legs and the solved seabed point.

        Args:
            transmit_leg: per-layer transmit polyline (from trace_beam).
            receive_leg: per-layer receive polyline (from trace_beam).
            transmit_azimuth_in_degrees: azimuth (deg, forward->starboard) of
                                         the transmit plane.
            receive_azimuth_in_degrees: azimuth (deg, forward->starboard) of
                                        the receive plane.
            bottom_position: solved seabed point (forward, starboard, down) in
                             m.
            solver_residual_in_meters: final solver residual in m.
        """

    def __eq__(self, other: BistaticBeamTrace) -> bool: ...

    def get_transmit_leg(self) -> BeamTrace:
        """
        Transmit leg polyline (per-layer points in the transmit vertical
        plane).
        """

    def get_receive_leg(self) -> BeamTrace:
        """Receive leg polyline (per-layer points in the receive vertical plane)."""

    def get_transmit_azimuth_in_degrees(self) -> float:
        """
        Transmit leg azimuth (deg): rotation about the down axis,
        BeamDirections convention.
        """

    def get_receive_azimuth_in_degrees(self) -> float:
        """
        Receive leg azimuth (deg): rotation about the down axis,
        BeamDirections convention.
        """

    def get_bottom_position(self) -> list[float]:
        """
        Solved seabed point (forward, starboard, down) in the common input
        frame [m].
        """

    def get_solver_residual_in_meters(self) -> float:
        """
        Final solver residual [m]; small values indicate a converged bistatic
        solve.
        """

    def get_transmit_launch_angle_in_degrees(self) -> float:
        """
        Transmit-leg launch angle (deg from nadir, port +) at the transmit
        array.
        """

    def get_receive_launch_angle_in_degrees(self) -> float:
        """
        Receive-leg launch angle (deg from nadir, port +) at the receive
        array.
        """

    def get_bottom_incidence_angle_in_degrees(self) -> float:
        """
        Seabed incidence angle (deg from nadir, signed) of the TRANSMIT ray,
        for backscatter.
        """

    def get_two_way_travel_time_in_seconds(self) -> float:
        """Modelled two-way travel time [s] = transmit one-way + receive one-way."""

    def copy(self) -> BistaticBeamTrace:
        """return a copy using the c++ default copy constructor"""

    def __copy__(self) -> BistaticBeamTrace: ...

    def __deepcopy__(self, arg: dict, /) -> BistaticBeamTrace: ...

    def to_binary(self, resize_buffer: bool = True) -> bytes:
        """convert object to bytearray"""

    @staticmethod
    def from_binary(buffer: bytes, check_buffer_is_read_completely: bool = True) -> BistaticBeamTrace:
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

def trace_bistatic_beam(transmit_installation_ypr_in_degrees: Sequence[float], transmit_attitude_ypr_in_degrees: Sequence[float], transmit_steering_angle_in_degrees: float, transmit_position_xyz: Sequence[float], receive_installation_ypr_in_degrees: Sequence[float], receive_attitude_ypr_in_degrees: Sequence[float], receive_steering_angle_in_degrees: float, receive_position_xyz: Sequence[float], two_way_travel_time_in_seconds: float, sound_velocity_profile: SoundVelocityProfile, concentric_beam_direction: Sequence[float], max_iterations: int = 30, tolerance_in_percent: float = 0.0010000000474974513, surface_sound_speed_in_meters_per_second: float = -1.0, reference_heading_in_degrees: float = 0.0) -> BistaticBeamTrace:
    """
    Solve the true-bistatic seabed trace of a single multibeam beam.

    Traces the transmit ray from the transmit array and the receive ray
    from the receive array through the layered sound-velocity profile and
    finds the seabed point where the two legs meet with a combined one-way
    travel time equal to the measured two-way travel time. The seabed
    depth and each leg's cone rotation angle (see bistatic_detail::
    SteeringCone) are found with a damped Newton iteration seeded by the
    concentric beam direction. Each converged leg is then re-traced with
    trace_beam so the returned legs are identical to the monostatic model
    when the transmit and receive poses coincide.

    All poses are in the common x=forward, y=starboard, z=down frame. The
    vessel attitudes may carry the full heading in their yaw component;
    pass that same heading as ``reference_heading_in_degrees`` so it is
    removed from both arrays (exactly like compute_beam_directions), which
    puts the solved seabed point in the ship frame. The concentric guess
    must be in that same (heading-removed) frame.

    Args:
        transmit_installation_ypr_in_degrees: (yaw, pitch, roll) mounting
                                              of the transmit array.
        transmit_attitude_ypr_in_degrees: (yaw, pitch, roll) vessel
                                          attitude at transmit time.
        transmit_steering_angle_in_degrees: electronic transmit steering
                                            (positive forward).
        transmit_position_xyz: transmit array position (forward,
                               starboard, down) [m].
        receive_installation_ypr_in_degrees: (yaw, pitch, roll) mounting
                                             of the receive array.
        receive_attitude_ypr_in_degrees: (yaw, pitch, roll) vessel
                                         attitude at receive time.
        receive_steering_angle_in_degrees: electronic receive steering
                                           (positive to port).
        receive_position_xyz: receive array position (forward, starboard,
                              down) [m].
        two_way_travel_time_in_seconds: measured two-way travel time [s].
        sound_velocity_profile: layered profile to trace through.
        concentric_beam_direction: ship-frame unit guess (fwd, stbd,
                                   down), e.g. BeamDirections::get_beam_di
                                   rection(beam).
        max_iterations: maximum Newton iterations (default 30).
        tolerance_in_percent: convergence tolerance as a percentage of the
                              nominal slant range (default 0.001).
        surface_sound_speed_in_meters_per_second: sound speed (m/s) at
                                                  which the beams were
                                                  formed (the measured
                                                  surface/transducer SSV);
                                                  applied to both legs'
                                                  ray parameters. <= 0
                                                  (default) uses the
                                                  profile value at each
                                                  array depth.
        reference_heading_in_degrees: heading (deg) removed from both
                                      vessel attitudes so the result is in
                                      the ship frame; use the same value
                                      passed to compute_beam_directions. 0
                                      (default) keeps the attitudes as
                                      given.

    Returns:
        BistaticBeamTrace with both legs, azimuths, seabed point and
        residual.
    """
