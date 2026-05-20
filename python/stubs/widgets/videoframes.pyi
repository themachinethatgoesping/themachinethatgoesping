"""
VideoFrames – container for captured viewer frames with export helpers.
"""

import np


class VideoFrames:
    """
    Container for captured video frames with per-frame metadata.

    Stores RGB numpy arrays together with timestamps so that export
    can use either a fixed frame rate or timing derived from the
    actual ping timestamps.

    Examples
    --------
    >>> viewer.frames.export_avif("out.avif", fps=10)
    >>> viewer.frames.export_mp4("out.mp4", fps=25)
    >>> viewer.frames.export_avif("out.avif", ping_time_speed=3.0)
    """

    def __init__(self) -> None: ...

    def clear(self) -> None:
        """Remove all stored frames."""

    def append(self, frame: np.ndarray, timestamp: Optional[float] = None) -> None:
        """Append a single RGB frame with optional ping timestamp."""

    def __len__(self) -> int: ...

    def __getitem__(self, idx: int) -> np.ndarray: ...

    @property
    def frames(self) -> List[np.ndarray]:
        """All stored RGB frames."""

    @property
    def timestamps(self) -> List[Optional[float]]:
        """Per-frame timestamps (may contain None)."""

    def export_avif(self, filename: str = 'video.avif', fps: Optional[float] = None, ping_time_speed: Optional[float] = None, quality: int = 75, loop: int = 0) -> str:
        """
        Export frames as animated AVIF.

        Parameters
        ----------
        filename : str
            Output path.
        fps : float, optional
            Fixed frame rate.  Ignored when *ping_time_speed* is set.
        ping_time_speed : float, optional
            Use real ping timestamps scaled by this speed factor
            (e.g. 3.0 = 3× real-time).
        quality : int
            AVIF quality 1–100.
        loop : int
            Number of loops (0 = infinite).

        Returns
        -------
        str
            The filename that was written.
        """

    def export_mp4(self, filename: str = 'video.mp4', fps: Optional[float] = None, ping_time_speed: Optional[float] = None, codec: str = 'libx264', quality: int = 8) -> str:
        """
        Export frames as MP4 video.

        Parameters
        ----------
        filename : str
            Output path.
        fps : float, optional
            Fixed frame rate.  Ignored when *ping_time_speed* is set.
        ping_time_speed : float, optional
            Use real ping timestamps; the *average* resulting fps is
            passed to ffmpeg (per-frame variable rate is not supported
            by most containers).
        codec : str
            FFmpeg video codec.
        quality : int
            FFmpeg quality parameter.

        Returns
        -------
        str
            The filename that was written.
        """

    def __repr__(self) -> str: ...
