"""
Progress indicators that can be called directly or passed to specific themachinethatgoesping functions
"""
from __future__ import annotations
import typing
__all__ = ['ConsoleProgressBar', 'I_ProgressBar', 'I_ProgressBarTimed', 'NoIndicator', 'ProgressIndicator', 'ProgressTqdm', 'test_loop']
class ConsoleProgressBar(I_ProgressBar):
    """
    Old-school progress bar that prints to terminal. For reference only,
    might be removed in the future.
    
    This class is based in I_ProgressBarTimed such that the callbacks are
    guarded by a timer.
    """
    def __init__(self) -> None:
        ...
class I_ProgressBar:
    """
    This is a generic (abstract) class for progress bars. Usage: call
    init() and close() to initialize and finalize the progress bar. Then
    call set_progress() or tick() to update the progress bar.
    set_postfix() can be used to set a postfix message.
    
    Note: Functions the set_progress and tick functions can significantly
    slow down processes that use the progressbar. Consider using the
    ProgressBarTimed interface instead.
    """
    def __init__(self) -> None:
        """
        Construct a new i progressbar object
        """
    def close(self, msg: str = ...) -> None:
        """
        Finalize the progressbar
        
        Parameter ``msg``:
            A message that can be appended as postfix
        """
    def current(self) -> float:
        """
        Get the current progress state
        
        Returns:
            progress state
        """
    def init(self, first: float, last: float, process_name: str = ...) -> None:
        """
        Initialize a new progressbar within the given range
        
        Parameter ``first``:
            lowest number in the range (typically 0.0)
        
        Parameter ``last``:
            highest number in the range (typically 100.0)
        
        Parameter ``process_name``:
            Name of the progress
        """
    def set_postfix(self, postfix: str) -> None:
        """
        Append a postfix message to the progressbar
        
        Parameter ``postfix``:
            postfix message
        """
    def set_prefix(self, prefix: str) -> None:
        """
        Append a prefix message to the progressbar
        
        Parameter ``prefix``:
            prefix message
        """
    def set_progress(self, progress: float) -> None:
        """
        Set the progress state to the given value. Note some implementations
        may require the new_progress to be higher than the current progress!
        
        Parameter ``new_progress``:
            New progress state (within the given first/last range)
        """
    def tick(self, increment: float = ...) -> None:
        """
        Increment the progress state by the given amount
        
        Parameter ``increment``:
            Number of steps to increment the progress by
        """
class I_ProgressBarTimed(I_ProgressBar):
    """
    This is a generic (abstract) class for progress bars. Usage: call
    init() and close() to initialize and finalize the progress bar. Then
    call set_progress() or tick() to update the progress bar.
    set_postfix() can be used to set a postfix message. *
    
    The above name functions are guarded by a timer (100ms). The timer is
    started when calling set_progress() or tick(). Repetitively calling of
    these functions (in a loop) will update the internal state but not
    update the progress bar until the timer (100ms) expires.
    
    This ensures a low overhead even for slow progressbar implementations.
    
    All functions are thread-safe.
    
    To implement this interface the abstract callback_ functions must be
    implemented.
    """
    def __init__(self) -> None:
        ...
    def callback_close(self, msg: str = ...) -> None:
        """
        Finalize the progressbar
        
        Parameter ``msg``:
            A message that can be appended as postfix
        """
    def callback_current(self) -> float:
        """
        Get the current progress state
        
        Returns:
            progress state
        """
    def callback_init(self, first: float, last: float, process_name: str = ...) -> None:
        """
        Initialize a new progressbar within the given range
        
        Parameter ``first``:
            lowest number in the range (typically 0.0)
        
        Parameter ``last``:
            highest number in the range (typically 100.0)
        
        Parameter ``process_name``:
            Name of the progress
        """
    def callback_set_postfix(self, postfix: str) -> None:
        """
        Append a postfix message to the progressbar
        
        This callback is guarded by a timer (100ms). If skipped, the postfix
        is stored to the internal state and will be applied with the next
        successful call to set_progress(), tick() or set_postfix().
        
        Parameter ``postfix``:
            postfix message
        """
    def callback_set_prefix(self, prefix: str) -> None:
        """
        Set the prefix message to the progressbar
        
        This callback is guarded by a timer (100ms). If skipped, the prefix is
        stored to the internal state and will be applied with the next
        successful call to set_progress(), tick() or set_prefix().
        
        Parameter ``prefix``:
            prefix message
        """
    def callback_set_progress(self, progress: float) -> None:
        """
        Set the progress state to the given value. Note some implementations
        may require the new_progress to be higher than the current progress!
        
        This callback is guarded by a timer (100ms). If skipped, the progress
        is stored to the internal state and will be applied with the next
        successful call to set_progress(), tick() or set_postfix().
        
        Parameter ``new_progress``:
            New progress state (within the given first/last range)
        """
    def callback_tick(self, increment: float = ...) -> None:
        """
        Increment the progress state by the given amount This callback is
        guarded a timer (100ms).
        
        If skipped, the increment is added to the internal counter and will be
        applied with the next unskipped call to tick().
        
        Parameter ``increment``:
            Number of steps to increment the progress by
        """
class NoIndicator(I_ProgressBar):
    """
    A progress bar that does not show any progress and has nearly no
    overhead.
    """
    def __init__(self) -> None:
        ...
class ProgressIndicator(I_ProgressBar):
    """
    Text based ProgressBar that uses the indicators library.
    (https://github.com/p-ranav/indicators)
    
    This class is based in I_ProgressBarTimed such that the callbacks are
    guarded by a timer.
    """
    def __init__(self) -> None:
        ...
class ProgressTqdm(I_ProgressBar):
    """
    Python ProgressBar that uses the tqdm. This is a test implementation
    for reference only. Do not use in production! Including this header
    will result in a compilation error if the project is not linked
    against pybind11 (not default for themachinethatgoesping_tools).
    
    This class is based in I_ProgressBarTimed such that the callbacks are
    guarded by a timer.
    """
    def __init__(self, tqdm: typing.Any) -> None:
        """
        Construct a new Progress Tqdm object To initialize a tqdm object call:
        from tqdm import tqdm, and use tqdm()
        
        Parameter ``tqdm``:
            A python tqdm class object
        """
def test_loop(ProgressBar: I_ProgressBar, loops: int = ..., sleep_us: int = ..., show_progress: bool = ...) -> float:
    ...
