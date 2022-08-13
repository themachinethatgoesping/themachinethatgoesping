"""Progress indicators that can be called directly or passed to specific themachinethatgoesping functions"""
from __future__ import annotations
import themachinethatgoesping.tools.progressbars
import typing

__all__ = [
    "ConsoleProgressBar",
    "I_ProgressBar",
    "NoIndicator",
    "ProgressIndicator",
    "ProgressTqdm",
    "test_loop"
]


class I_ProgressBar():
    def __init__(self) -> None: ...
    def close(self, msg: str = 'done') -> None: ...
    def current(self) -> float: ...
    def init(self, first: float, last: float, process_name: str = 'process') -> None: ...
    def set_postfix(self, postfix: str) -> None: ...
    def set_progress(self, progress: float) -> None: ...
    def tick(self, increment: float = 1) -> None: ...
    pass
class ConsoleProgressBar(I_ProgressBar):
    def __init__(self) -> None: ...
    pass
class NoIndicator(I_ProgressBar):
    def __init__(self) -> None: ...
    pass
class ProgressIndicator(I_ProgressBar):
    def __init__(self) -> None: ...
    pass
class ProgressTqdm(I_ProgressBar):
    def __init__(self, tqdm: object) -> None: ...
    pass
def test_loop(ProgressBar: I_ProgressBar, loops: int = 1000, sleep_us: int = 10, show_progress: bool = True) -> None:
    pass
