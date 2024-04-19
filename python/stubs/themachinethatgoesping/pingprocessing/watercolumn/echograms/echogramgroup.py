from __future__ import annotations
from collections import defaultdict
import datetime as dt
import matplotlib as mpl
from matplotlib import dates as mdates
import numpy as np
from themachinethatgoesping import tools as ptools
from tqdm.asyncio import tqdm_asyncio as tqdm
__all__ = ['EchogramGroup', 'create_echogram_groups', 'defaultdict', 'dt', 'get_time_error', 'mdates', 'mpl', 'np', 'ptools', 'tqdm']
class EchogramGroup:
    def __init__(self):
        ...
    def __len__(self):
        ...
    def add(self, ping, pnr):
        ...
    def to_tuple(self):
        ...
def create_echogram_groups(pings: typing.List, min_num_pings_per_group: int = 2, max_section_size: int = 10000, max_time_diff_error = 0.499, show_progress = True, pbar = None) -> typing.List[typing.Tuple]:
    ...
def get_time_error(echogram_times, ping_time):
    ...
