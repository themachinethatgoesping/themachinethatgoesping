from __future__ import annotations
from matplotlib import pyplot as plt
import numpy as np
__all__: list[str] = ['minimum_recommended_calibration_range', 'nearfield_range_sbes', 'np', 'plot_nearfield_range', 'plot_recommended_sphere_range', 'plt']
def _compute_kappa(wavelength):
    ...
def _compute_wavelength(frequency, sound_speed):
    ...
def _estimate_diameter(kappa, beam_width_degrees):
    ...
def _nearfield_range_sbes_1(transducer_diameter, wavelength):
    ...
def _nearfield_range_sbes_2(transducer_diameter, wavelength):
    ...
def _nearfield_range_sbes_3(beam_width_degrees, frequency, sound_speed):
    ...
def minimum_recommended_calibration_range(beam_width_degrees, frequency_khz, sound_speed_ms = 1470, model = 2):
    """
    
    Calculate the minimum recommended calibration range for a single beam echo sounder.
    
    Parameters
    ----------
    beam_width_degrees : float
        Beam width in degrees.
    frequency_khz : float
        Frequency of the sound wave in kHz.
    sound_speed_ms : float, optional
        Speed of sound in water in m/s, by default 1470.
    model : int, optional
        Model to use for calculation (1 or 2), by default 2.
    
    Model 1: Simmonds and MacLennan (2005) in Demer et al. (2015)
    Model 2: Medwin and Clay (1998) in Demer et al. (2015)
    
    Returns
    -------
    float
        Minimum recommended calibration range in meters.
    
    Raises
    ------
    ValueError
        If the model is not 1 or 2.
    """
def nearfield_range_sbes(beam_width_degrees, frequency_khz, sound_speed_ms = 1470, model = 2):
    """
    
    Calculate the nearfield range for a single beam echo sounder. (Circular piston transducer)
    
    Parameters
    ----------
    beam_width_degrees : float
        Beam width in degrees.
    frequency_khz : float
        Frequency of the sound wave in kHz.
    sound_speed_ms : float, optional
        Speed of sound in water in m/s, by default 1470.
    model : int, optional
        Model to use for calculation (1 or 2), by default 2.
        
    Model 1: Simmonds and MacLennan (2005) in Demer et al. (2015)
    Model 2: Medwin and Clay (1998) in Demer et al. (2015)
    
    Returns
    -------
    float
        Nearfield range in meters.
    
    Raises
    ------
    ValueError
        If the model is not 1 or 2.
    """
def plot_nearfield_range(frequencies_kHz = [333, 200, 120, 70, 38, 18, 12], beamwidth_range = (2, 12), yticks = [1, 1.5, 2, 3, 4, 6, 8, 10, 15, 20], sound_speed_ms = 1470, model = 2, ax = None, name = ''):
    """
    
    Plot the estimated nearfield range for different frequencies and beam widths.
    """
def plot_recommended_sphere_range(frequencies_kHz = [333, 200, 120, 70, 38, 18, 12], beamwidth_range = (2, 12), yticks = [1, 1.5, 2, 3, 4, 6, 8, 10, 15, 20], sound_speed_ms = 1470, model = 2, ax = None, name = ''):
    """
    
    Plot the recommended sphere range for different frequencies and beam widths.
    """
