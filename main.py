from src.audio_processing.load_wav import load_wav
from src.audio_processing.select_segment import select_segment
from src.analysis.compare_recordings import compare_recordings
from src.visualization.plot_waveform import plot_waveform
from src.analysis.compute_periodogram import compute_periodogram
from src.visualization.plot_periodogram import plot_periodogram
from src.analysis.estimate_f0_autocorr import estimate_f0_autocorr
from src.analysis.fit_harmonics import fit_harmonics
from src.visualization.plot_original_vs_harmonic_fit import plot_original_vs_harmonic_fit
from src.visualization.plot_harmonic_energy_vs_f0 import plot_harmonic_energy_vs_f0
from src.visualization.plot_harmonic_coefficients import plot_harmonic_coefficients
from src.analysis.lpc_analysis import lpc_analysis
from src.visualization.plot_lpc import plot_lpc
from src.visualization.plot_lpc_coefficients import plot_lpc_coefficients
from src.visualization.plot_lpc_error_vs_order import plot_lpc_error_vs_order
from src.analysis.compare_recordings import compare_recordings


if __name__ == "__main__":
    path1 = "data/rec1.wav"
    path2 = "data/rec2.wav"

    print("### Comparing recordings ###")
    compare_recordings(path1, path2)

    print("\n### LPC on Rec1 ###")
    rate1, data1 = load_wav(path1)
    seg1 = select_segment(data1, rate1)
    a1, pred1, err1 = lpc_analysis(seg1, order=16)
    print("LPC Coefficients Rec1:", a1)
    plot_lpc(seg1, pred1, rate1, "Rec1: LPC Prediction")
    plot_lpc_coefficients(a1, "Rec1: LPC Coefficients")
    plot_lpc_error_vs_order(seg1, rate1, title="Rec1: LPC Prediction Error vs Order")


    print("\n### LPC on Rec2 ###")
    rate2, data2 = load_wav(path2)
    seg2 = select_segment(data2, rate2)
    a2, pred2, err2 = lpc_analysis(seg2, order=16)
    print("LPC Coefficients Rec2:", a2)
    plot_lpc(seg2, pred2, rate2, "Rec2: LPC Prediction")
    plot_lpc_coefficients(a2, "Rec2: LPC Coefficients")
    plot_lpc_error_vs_order(seg2, rate2, title="Rec2: LPC Prediction Error vs Order")