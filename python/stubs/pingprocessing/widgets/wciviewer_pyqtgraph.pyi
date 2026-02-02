"""PyQtGraph-based Water Column Image (WCI) viewer."""

import matplotlib.axes
import matplotlib.figure

import themachinethatgoesping.echosounders as echosounders
import themachinethatgoesping.pingprocessing.watercolumn.image as mi
import themachinethatgoesping.pingprocessing.widgets.pyqtgraph_helpers as pgh
from themachinethatgoesping.pingprocessing.widgets.tqdmwidget import (
    TqdmWidget as TqdmWidget
)


WCI_VALUE_CHOICES: list = ...

class WCIViewerPyQtGraph:
    """Replacement for the Matplotlib-based WCI viewer using PyQtGraph."""

    def __init__(self, pings: Sequence[Any], horizontal_pixels: int = 1024, name: str = 'WCI', figure: Optional[Any] = None, progress: Optional[Any] = None, show: bool = True, cmap: str = 'YlGnBu_r', widget_height_px: Optional[int] = None, widget_width_px: int = 900, **kwargs: Any) -> None: ...

    def fix_xy(self, _event: Any = None) -> None: ...

    def unfix_xy(self, _event: Any = None) -> None: ...

    def update_data(self, _change: Any = None) -> None: ...

    def update_view(self, _change: Any = None) -> None: ...

    def process_events(self) -> None:
        """
        Process pending Qt events.

        Call this method when updating the viewer from a loop to ensure
        the UI remains responsive and updates are displayed.

        Example:
            for i in range(len(viewer.pings)):
                viewer.w_index.value = i
                viewer.process_events()
        """

    def redraw(self, force: bool = True) -> None:
        """
        Force an immediate redraw of the widget.

        Processes pending Qt events and sends frame to browser.
        Use this when updating the viewer from a loop to ensure changes
        are immediately visible.

        Parameters
        ----------
        force : bool, default True
            If True, bypasses the normal frame scheduling and sends the
            frame directly (required for updates in tight loops).
            If False, uses the standard request_draw mechanism.

        Example:
            for i in range(len(viewer.pings)):
                viewer.w_index.value = i
                viewer.redraw()
        """

    def set_widget_height(self, height_px: int) -> None: ...

    def export_image(self, filename: str, width: Optional[int] = None, height: Optional[int] = None) -> None:
        """
        Export the current view as an image file (PNG, JPG, TIFF, etc.).

        Parameters
        ----------
        filename : str
            Output filename. Format is determined by extension.
        width : int, optional
            Image width in pixels. If None, uses current widget size.
        height : int, optional  
            Image height in pixels. If None, uses current widget size.

        Example:
            viewer.export_image('watercolumn.png')
            viewer.export_image('watercolumn.png', width=1920, height=1080)
        """

    def export_svg(self, filename: str) -> None:
        """
        Export the current view as an SVG file.

        Parameters
        ----------
        filename : str
            Output filename (should end with .svg).

        Example:
            viewer.export_svg('watercolumn.svg')
        """

    def export_matplotlib(self) -> 'matplotlib.figure.Figure':
        """
        Export the current view to a matplotlib figure.

        Note: MatplotlibExporter works best with line plots. For image data
        like water column images, consider using `get_figure_data()` instead
        to recreate the plot in matplotlib directly.

        Returns
        -------
        matplotlib.figure.Figure
            The matplotlib figure containing the exported plot.

        Example:
            fig = viewer.export_matplotlib()
            fig.savefig('watercolumn_mpl.png', dpi=300)
        """

    def get_figure_data(self) -> Dict[str, Any]:
        """
        Get the current image data and metadata for external plotting.

        This is useful for recreating the plot in matplotlib or other
        plotting libraries with full control over the output.

        Returns
        -------
        dict
            Dictionary containing:
            - 'image': The 2D numpy array of the water column image
            - 'extent': Tuple (x0, x1, y0, y1) for image positioning
            - 'vmin': Colorbar minimum value
            - 'vmax': Colorbar maximum value
            - 'cmap': Colormap name (if available)
            - 'xlabel': X-axis label
            - 'ylabel': Y-axis label
            - 'title': Plot title (ping info)

        Example:
            import matplotlib.pyplot as plt
            data = viewer.get_figure_data()
            fig, ax = plt.subplots()
            im = ax.imshow(data['image'].T, extent=data['extent'],
                          aspect='auto', origin='upper',
                          vmin=data['vmin'], vmax=data['vmax'],
                          cmap='YlGnBu_r')
            ax.set_xlabel(data['xlabel'])
            ax.set_ylabel(data['ylabel'])
            plt.colorbar(im, label='dB')
            plt.savefig('watercolumn.png', dpi=300)
        """

    def to_matplotlib(self, ax: Optional['matplotlib.axes.Axes'] = None, cmap: str = 'YlGnBu_r', colorbar: bool = True, **kwargs: Any) -> 'matplotlib.axes.Axes':
        """
        Render the current water column image using matplotlib.

        Parameters
        ----------
        ax : matplotlib.axes.Axes, optional
            Axes to plot on. If None, creates a new figure.
        cmap : str, default 'YlGnBu_r'
            Matplotlib colormap name.
        colorbar : bool, default True
            Whether to add a colorbar.
        **kwargs
            Additional arguments passed to ax.imshow().

        Returns
        -------
        matplotlib.axes.Axes
            The axes containing the plot.

        Example:
            import matplotlib.pyplot as plt
            fig, ax = plt.subplots(figsize=(10, 6))
            viewer.to_matplotlib(ax=ax)
            plt.savefig('watercolumn.png', dpi=300)
        """

    def copy_to_clipboard(self) -> None:
        """
        Copy the current view as an image to the clipboard.

        Example:
            viewer.copy_to_clipboard()
            # Now paste into any application
        """

    def get_image_bytes(self, format: str = 'png') -> bytes:
        """
        Get the current view as image bytes.

        Parameters
        ----------
        format : str, default 'png'
            Image format ('png', 'jpg', etc.)

        Returns
        -------
        bytes
            The image data as bytes.

        Example:
            img_bytes = viewer.get_image_bytes()
            with open('watercolumn.png', 'wb') as f:
                f.write(img_bytes)
        """
