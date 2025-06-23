def select_segment(data, rate, start_ms=100, duration_ms=100):
    start = int(start_ms / 1000 * rate)
    end = start + int(duration_ms / 1000 * rate)
    return data[start:end]

    """
    Selects a segment from the audio data based on start time and duration.

    Parameters:
        data (numpy.ndarray): Full audio data array.
        rate (int): Sampling rate of the audio.
        start_sec (float): Start time in seconds.
        duration_sec (float): Duration of the segment in seconds.

    Returns:
        numpy.ndarray: The selected audio segment.
    """