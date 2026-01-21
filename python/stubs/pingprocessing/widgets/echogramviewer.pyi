import themachinethatgoesping as theping
import themachinethatgoesping.pingprocessing.watercolumn.echograms as echograms


class EchogramViewer:
    def __init__(self, echogramdata, name='Echogram', names=None, figure=None, progress=None, show=True, voffsets=None, cmap='YlGnBu_r', cmap_layer='jet', auto_update: bool = True, auto_update_delay_ms: int = 300, **kwargs): ...

    def show(self): ...

    def init_ax(self, adapt_axis_names=True): ...

    def show_background_echogram(self): ...

    def clear_output(self, event=0): ...

    def show_background_zoom(self, event=0) -> None:
        """
        Trigger a background load for the current zoom level.

        This method is non-blocking: it starts loading in a background thread
        and updates the view when complete.
        """

    def pan_view(self, direction: str, fraction: float = 0.25) -> None:
        """
        Pan the view in the specified direction.

        Args:
            direction: One of 'left', 'right', 'up', 'down'
            fraction: Fraction of the current view width/height to pan (default 25%)
        """

    def set_nav_fraction(self, fraction: float = 0.25) -> None:
        """
        Set the fraction of view to pan per button click.

        Args:
            fraction: Fraction of view to pan (default 25%)
        """

    def cleanup(self) -> None:
        """Clean up resources (call when done with the viewer)."""

    def __del__(self) -> None:
        """Destructor to ensure cleanup when viewer is garbage collected."""

    def invert_y_axis(self): ...

    def get_args_plot(self, axis_nr, layer=False): ...

    def update_view(self, w=None, reset=False): ...

    def callback_view(self): ...

    def on_key_press(self, event): ...

    def update_ping_line(self, event=0): ...

    def disconnect_pingviewer(self): ...

    def connect_pingviewer(self, pingviewer): ...
