import numpy as np

def estimate_f0_autocorr(seg, rate, fmin=50, fmax=1000):
    corr = np.correlate(seg, seg, mode='full')
    corr = corr[len(corr)//2:]
    i_min = int(rate/fmax)
    i_max = int(rate/fmin)
    peak = np.argmax(corr[i_min:i_max]) + i_min
    f0 = rate / peak
    return f0


    """
    Estimate the fundamental frequency (f0) of a signal segment using autocorrelation.

    Parameters:
    segment (numpy.ndarray): The segment of the audio signal.
    rate (int): Sampling rate of the signal in Hz.

    Returns:
    f0 (float): Estimated fundamental frequency in Hz.
    """