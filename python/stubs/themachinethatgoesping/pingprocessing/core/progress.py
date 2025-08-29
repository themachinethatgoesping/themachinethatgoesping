from __future__ import annotations
from tqdm.asyncio import tqdm_asyncio as tqdm
import typing
from typing import Any
__all__: list[str] = ['Any', 'get_progress_iterator', 'tqdm']
def get_progress_iterator(iteratable: typing.Iterable[typing.Any], progress: typing.Union[bool, typing.Type[typing.Callable[..., typing.Any]], NoneType] = False, **kwargs: typing.Any) -> typing.Iterable[typing.Any]:
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
