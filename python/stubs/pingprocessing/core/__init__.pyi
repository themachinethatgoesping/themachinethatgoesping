from . import (
    asserts as asserts,
    helper as helper,
    progress as progress
)
from .asserts import (
    assert_length as assert_length,
    assert_valid_argument as assert_valid_argument
)
from .helper import (
    clear_memory as clear_memory,
    create_figure as create_figure,
    set_ax_timeformat as set_ax_timeformat
)
from .progress import get_progress_iterator as get_progress_iterator


close_plots: bool = True
