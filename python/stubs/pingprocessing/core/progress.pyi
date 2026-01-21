from collections.abc import (
    Callable as _Callable,
    Iterable as _Iterable
)
from typing import Any, Union


def get_progress_iterator(iteratable: _Iterable[Any], progress: Union[bool, type[_Callable[..., Any]], None] = False, **kwargs: Any) -> _Iterable[Any]:
    """
    Returns an iterator that optionally displays a progress bar.

    Args:
        iteratable: The iterable to iterate over.
        progress: If True, displays a progress bar using the default tqdm implementation.
                  If a callable is provided, it should be a progress bar implementation that takes an iterable as its first argument.
                  If False, returns the original iterable without any progress bar.

    Returns:
        An iterator that optionally displays a progress bar.
    """
