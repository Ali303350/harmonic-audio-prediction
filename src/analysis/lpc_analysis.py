import librosa
import scipy.signal as sig

def lpc_analysis(seg, order=12):
    a = librosa.lpc(seg, order=order)
    pred = sig.lfilter([-1]+list(a[1:]), 1, seg)
    err = seg - pred
    return a, pred, err


    """
    Perform Linear Predictive Coding (LPC) analysis on a signal segment.

    Parameters:
    segment (numpy.ndarray): Audio signal segment.
    order (int): LPC order (number of coefficients).

    Returns:
    lpc_coeffs (numpy.ndarray): LPC coefficients.
    error (float): Prediction error (residual energy).
    """