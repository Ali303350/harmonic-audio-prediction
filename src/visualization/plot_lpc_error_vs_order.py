import matplotlib.pyplot as plt
import numpy as np
import librosa
import scipy.signal as sig

def plot_lpc_error_vs_order(signal, rate, max_order=30, title=""):
    errors = []
    orders = list(range(2, max_order+1))
    for order in orders:
        a = librosa.lpc(signal, order=order)
        pred = sig.lfilter([-1]+list(a[1:]), 1, signal)
        err = signal - pred
        mse = np.mean(err**2)
        errors.append(mse)
    plt.figure()
    plt.plot(orders, errors, marker='o')
    plt.xlabel("Prediction Order (p)")
    plt.ylabel("Mean Squared Error (MSE)")
    plt.title(title)
    plt.grid()
    plt.tight_layout()
    plt.show()

    """
    Plots LPC prediction error as a function of model order.

    Parameters:
    - orders (list): LPC model orders.
    - errors (list): Corresponding prediction errors.
    """