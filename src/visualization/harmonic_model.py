import numpy as np

def harmonic_model(t, *amps):
    f0 = harmonic_model.f0
    return sum(amps[i] * np.sin(2 * np.pi * f0 * (i+1) * t) for i in range(len(amps)))

    """
    Generates a harmonic model signal based on time samples and harmonic parameters.

    Parameters:
    - t (numpy.ndarray): Time array.
    - *params (float): Harmonic parameters in the form [a0, a1, f1, a2, f2, ..., an, fn],
      where:
        - a0 is the DC component (offset)
        - ai and fi are amplitude and frequency of the i-th harmonic

    Returns:
    - numpy.ndarray: The signal modeled as a sum of sinusoids (harmonics).
    """