from themachinethatgoesping.scripts.oceanographic import (
    knots_to_ms as knots_to_ms
)
from themachinethatgoesping.scripts.plot_tools import (
    prepare_plt as prepare_plt
)


class SBES:
    def __init__(self, beamopening_angle, x=0, z=0): ...

    def calc_footprint(self, depth: float, beamopening_angle: float = None) -> float:
        """:rtype: float"""

    def calc_overlap_pingrate(self, speed: float, depth: float, beamopening_angle: float = None) -> float: ...

    @staticmethod
    def calc_pingdistance(speed, pingrate): ...

    def calc_overlap_depth(self, delta_x): ...

    def calc_overlap_depth_for_pingrate(self, speed, pingrate): ...

    def get_beam_xmin(self, depth: float) -> float: ...

    def get_beam_xmax(self, depth: float) -> float: ...

    def get_beam_limits(self, depth: float) -> tuple: ...

    def get_horizontal_line(self, depth: float) -> tuple: ...

    def plot(self, depth, color, aspect=True, add_bottom=True, axes=None): ...

    def plot_pingoverlap_at_pingrate(self, depth, speed, pingrate, color1='r', color2='b', print_vars=True, add_bottom=True, axes=None, make_figure=True): ...

    def plot_pingoverlap_at_overlapdepth(self, depth, speed, overlapdepth, color1='r', color2='b', print_vars=True, add_bottom=True, axes=None, make_figure=True): ...

    plt_title: str = 'SBES overlap'

    plt_xlabel: str = 'Alongtrack (m)'

    plt_ylabel: str = 'Depth (m)'

    plt_aspect: bool = False

    plt_grid: bool = True

    def make_figure(self, title=None, xlabel=None, ylabel=None, aspect=None, grid=None): ...

    @staticmethod
    def show(): ...
