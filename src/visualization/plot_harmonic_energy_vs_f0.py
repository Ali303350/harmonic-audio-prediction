import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from src.visualization.harmonic_model import harmonic_model

def plot_harmonic_energy_vs_f0(signal, rate, f0_range=(400, 600), num_harmonics=5, title=""):
    t = np.arange(len(signal)) / rate
    amps_vs_f0 = []
    f0_values = np.linspace(f0_range[0], f0_range[1], 100)
    for f0 in f0_values:
        harmonic_model.f0 = f0
        try:
            popt, _ = curve_fit(harmonic_model, t, signal, p0=[1]*num_harmonics)
            amps_vs_f0.append(abs(popt[0]))
        except RuntimeError:
            amps_vs_f0.append(0)
    best_f0 = f0_values[np.argmax(amps_vs_f0)]
    plt.figure()
    plt.plot(f0_values, amps_vs_f0, label="1st Harmonic Amplitude")
    plt.axvline(best_f0, color='red', linestyle='--', label=f"Max at f₀={best_f0:.2f} Hz")
    plt.scatter([best_f0], [max(amps_vs_f0)], color='red')
    plt.xlabel("f₀ (Hz)")
    plt.ylabel("Amplitude")
    plt.title(title)
    plt.legend()
    plt.grid()
    plt.tight_layout()
    plt.show()

    """
    Plots harmonic energy as a function of the fundamental frequency (f0).

    Parameters:
    - f0_values (list or array): Estimated fundamental frequencies.
    - energies (list or array): Corresponding harmonic energies.
    """