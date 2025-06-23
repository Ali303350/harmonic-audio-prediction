import matplotlib.pyplot as plt

def plot_periodogram(freqs, Pxx, title="Periodogram"):
    plt.figure()
    plt.semilogy(freqs, Pxx)
    plt.xlim(0, freqs.max())
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Power Density")
    plt.title(title)
    plt.tight_layout()
    plt.show()

    """
    Plots the periodogram (power spectrum) of a signal.

    Parameters:
    - freqs (numpy.ndarray): Array of frequency bins.
    - spectrum (numpy.ndarray): Power spectrum values.
    - title (str): Title of the plot.
    """