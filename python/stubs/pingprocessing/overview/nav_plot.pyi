import matplotlib.axes._axes
import matplotlib.figure

from themachinethatgoesping.pingprocessing.core.progress import (
    get_progress_iterator as get_progress_iterator
)


def reproject_raster(src, dst_crs): ...

def create_figure(name: str, aspect: str = 'equal', close_plots: bool = True, background_image_path: str = None, background_colorbar_label=None, colorbar_orientation='vertical', add_grid=True, dst_crs='EPSG:4326', return_crs=False, **kwargs) -> tuple[matplotlib.figure.Figure, matplotlib.axes._axes.Axes]:
    """
    Create a figure with a given name and aspect ratio.

    Parameters:
        name (str): The name of the figure.
        aspect (str, optional): The aspect ratio of the figure. Defaults to "equal".
        close_plots (bool, optional): Whether to close existing plots. Defaults to True.
        background_image_path (str, optional): Path to the background image that can be opened
                                               with rastio and contains navigation reference(e.g. geotif).
                                               Defaults to None.
        **kwargs: Additional keyword arguments for the background_image (e.g. cmap).

    Returns:
        Tuple[plt.Figure, plt.Axes]: The created figure and axes.
    """

def plot_latlon(lat, lon, ax, label='survey', annotate=True, max_points=100000, **kwargs):
    """
    Plot latitude and longitude coordinates on a given axis.

    Parameters:
        lat (list): List of latitude coordinates.
        lon (list): List of longitude coordinates.
        ax (matplotlib.axes.Axes): The axis on which to plot the coordinates.
        label (str, optional): Name of the survey. Defaults to 'survey'.
        annotate (bool, optional): Whether to annotate the plot with the survey name. Defaults to True.
        max_points (int, optional): Maximum number of points to plot. Defaults to 100000.
        **kwargs: Additional keyword arguments to be passed to the plot function.

    Returns:
        None
    """
