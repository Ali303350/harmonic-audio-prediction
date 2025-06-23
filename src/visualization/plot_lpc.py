import numpy as np
import matplotlib.pyplot as plt

def plot_lpc(seg, pred, rate, title):
    t = np.arange(len(seg)) / rate
    plt.figure()
    plt.plot(t, seg, label="Original")
    plt.plot(t, pred, label="Predicted", alpha=0.7)
    plt.xlabel("Time (s)")
    plt.title(title)
    plt.legend()
    plt.tight_layout()
    plt.show()

    """
    Plots the original audio signal and the LPC reconstructed signal.

    Parameters:
    - signal (numpy.ndarray): The original audio signal.
    - lpc_signal (numpy.ndarray): The LPC-reconstructed signal.
    - rate (int): Sampling rate of the audio.
    """