"""A submodule to do some math."""
import numpy as np


def sum1(x):
    """
    Sum 1 to the argument.

    Parameters
    ----------
    x : float or array

    Returns
    -------
    float or array

    """
    return x + 1


def compute_mean(x):
    """
    Compute the mean of an array.

    Parameters
    ----------
    x : array

    Returns
    -------
    float

    """
    return np.mean(x)
