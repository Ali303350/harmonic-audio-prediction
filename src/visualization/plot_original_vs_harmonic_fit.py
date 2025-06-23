import numpy as np
import matplotlib.pyplot as plt
from src.visualization.harmonic_model import harmonic_model

def plot_original_vs_harmonic_fit(signal, rate, f0, amps, title):
    t = np.arange(len(signal)) / rate
    harmonic_model.f0 = f0
    reconstructed = harmonic_model(t, *amps)
    plt.figure()
    plt.plot(signal, label="Original")
    plt.plot(reconstructed, label="Reconstructed", alpha=0.7)
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.title(title)
    plt.legend()
    plt.tight_layout()
    plt.show()

    """
    Plots the original signal against its harmonic model approximation.

    Parameters:
    - original_signal (numpy.ndarray): The original audio signal.
    - harmonic_fit (numpy.ndarray): The estimated harmonic fit.
    - rate (int): Sample rate of the signal.
    """