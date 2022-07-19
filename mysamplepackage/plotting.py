"""This is a basic plotting submodule."""
import matplotlib.pyplot as plt


def plot_line(x, y):
    """
    Plot a line from two arrays.

    Parameters
    ----------
    x : array
        array with x data values.
    y : array
        array with y data values.

    Returns
    -------
    None.

    """
    plt.plot(x, y)
    plt.show()
