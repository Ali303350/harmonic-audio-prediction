from src.audio_processing.load_wav import load_wav
from src.audio_processing.select_segment import select_segment
from src.visualization.plot_waveform import plot_waveform
from src.analysis.compute_periodogram import compute_periodogram
from src.visualization.plot_periodogram import plot_periodogram
from src.analysis.estimate_f0_autocorr import estimate_f0_autocorr
from src.analysis.fit_harmonics import fit_harmonics
from src.visualization.plot_original_vs_harmonic_fit import plot_original_vs_harmonic_fit
from src.visualization.plot_harmonic_energy_vs_f0 import plot_harmonic_energy_vs_f0
from src.visualization.plot_harmonic_coefficients import plot_harmonic_coefficients

def compare_recordings(path1, path2):
    r1, d1 = load_wav(path1)
    r2, d2 = load_wav(path2)
    seg1 = select_segment(d1, r1)
    seg2 = select_segment(d2, r2)
    plot_waveform(seg1, r1, "Rec1 Waveform")
    plot_waveform(seg2, r2, "Rec2 Waveform")
    f1, P1 = compute_periodogram(seg1, r1)
    f2, P2 = compute_periodogram(seg2, r2)
    plot_periodogram(f1, P1, "Rec1 Spectrum")
    plot_periodogram(f2, P2, "Rec2 Spectrum")
    f0_1 = estimate_f0_autocorr(seg1, r1)
    f0_2 = estimate_f0_autocorr(seg2, r2)
    print(f"Fundamental Rec1: {f0_1:.1f} Hz")
    print(f"Fundamental Rec2: {f0_2:.1f} Hz")
    amps1 = fit_harmonics(seg1, r1, f0_1)
    amps2 = fit_harmonics(seg2, r2, f0_2)
    print("Harmonic Amplitudes Rec1:", amps1)
    print("Harmonic Amplitudes Rec2:", amps2)
    plot_original_vs_harmonic_fit(seg1, r1, f0_1, amps1, "Rec1: Original vs Harmonic Fit")
    plot_original_vs_harmonic_fit(seg2, r2, f0_2, amps2, "Rec2: Original vs Harmonic Fit")
    plot_harmonic_energy_vs_f0(seg1, r1, title="Rec1: 1st Harmonic Energy vs f₀")
    plot_harmonic_energy_vs_f0(seg2, r2, title="Rec2: 1st Harmonic Energy vs f₀")
    plot_harmonic_coefficients(amps1, title="Rec1: Harmonic Coefficients")
    plot_harmonic_coefficients(amps2, title="Rec2: Harmonic Coefficients")

    """
    Perform Linear Predictive Coding (LPC) analysis on a signal segment.

    Parameters:
    segment (numpy.ndarray): Audio signal segment.
    order (int): LPC order (number of coefficients).

    Returns:
    lpc_coeffs (numpy.ndarray): LPC coefficients.
    error (float): Prediction error (residual energy).
    """