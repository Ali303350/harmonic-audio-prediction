import scipy.signal as sig

def compute_periodogram(seg, rate):
    freqs, Pxx = sig.periodogram(seg, fs=rate, window='hann', scaling='density')
    return freqs, Pxx


    """
    Compute the power spectral density (PSD) of a signal using a periodogram.

    Parameters:
    data (numpy.ndarray): The input signal data.
    rate (int): The sampling rate of the signal in Hz.

    Returns:
    freqs (numpy.ndarray): Array of frequency bins.
    power (numpy.ndarray): Power spectral density values for each frequency.
    """