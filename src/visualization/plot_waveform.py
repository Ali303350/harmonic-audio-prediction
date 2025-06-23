import numpy as np
import matplotlib.pyplot as plt

def plot_waveform(seg, rate, title="Waveform"):
    t = np.arange(len(seg)) / rate
    plt.figure()
    plt.plot(t, seg)
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.title(title)
    plt.tight_layout()
    plt.show()

    """
    Plots the waveform of an audio signal.

    Parameters:
    - signal (numpy.ndarray): The audio data array.
    - rate (int): The sample rate of the audio.
    - title (str): Title of the plot.
    
    """