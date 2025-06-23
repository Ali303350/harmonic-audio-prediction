import matplotlib.pyplot as plt

def plot_harmonic_coefficients(amps, title):
    plt.figure()
    plt.bar(range(1, len(amps)+1), amps)
    plt.xlabel("Harmonic Number")
    plt.ylabel("Amplitude")
    plt.title(title)
    plt.grid(axis='y')
    plt.tight_layout()
    plt.show()

    """
    Plots the harmonic model coefficients.

    Parameters:
    - coeffs (list or array): Harmonic amplitudes or coefficients.
    """