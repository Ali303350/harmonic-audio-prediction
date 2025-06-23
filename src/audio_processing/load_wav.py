from scipy.io import wavfile

def load_wav(path):
    rate, data = wavfile.read(path)
    if data.ndim > 1:
        data = data[:, 0]
    return rate, data.astype(float)

    """
    Loads a WAV audio file from the specified path.

    Parameters:
        path (str): Path to the WAV file.

    Returns:
        rate (int): Sampling rate of the audio file.
        data (numpy.ndarray): Audio samples as a NumPy array.
    """