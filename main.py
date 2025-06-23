from src.analysis.compare_recordings import compare_recordings




if __name__ == "__main__":
    path1 = "data/rec1.wav"
    path2 = "data/rec2.wav"

    print("### Comparing recordings ###")
    compare_recordings(path1, path2)