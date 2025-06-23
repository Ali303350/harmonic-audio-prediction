import numpy as np
from scipy.optimize import curve_fit
from src.visualization.harmonic_model import harmonic_model

def fit_harmonics(seg, rate, f0, n_harm=5):
    t = np.arange(len(seg)) / rate
    harmonic_model.f0 = f0
    p0 = [np.std(seg)] * n_harm
    popt, _ = curve_fit(harmonic_model, t, seg, p0=p0)
    return popt

    """
    Fit a sum of sinusoids to the signal segment using harmonic frequencies.

    Parameters:
    segment (numpy.ndarray): Audio segment to analyze.
    rate (int): Sampling rate in Hz.
    f0 (float): Fundamental frequency.
    num_harmonics (int): Number of harmonic components to include.

    Returns:
    coefficients (numpy.ndarray): Amplitude coefficients of the harmonics.
    """