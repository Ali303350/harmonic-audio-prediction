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
