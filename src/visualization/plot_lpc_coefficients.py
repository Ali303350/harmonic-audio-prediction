import matplotlib.pyplot as plt

def plot_lpc_coefficients(coeffs, title):
    plt.figure()
    plt.bar(range(len(coeffs)), coeffs)
    plt.xlabel("Coefficient Index")
    plt.ylabel("Value")
    plt.title(title)
    plt.grid(axis='y')
    plt.tight_layout()
    plt.show()

    """
    Plots the LPC coefficients.

    Parameters:
    - coeffs (list or numpy.ndarray): List of LPC coefficients.
    
    """