"""
Most of this code is from 
https://github.com/merely-useful/py-rse/blob/book/zipf/bin/plotcounts.py originally 
released under a CC-BY license by the Research Software Engineering for Python
authors.
"""

import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy.optimize import minimize_scalar


def compute_summary(word_counts):
    """
    Compute summary stats for the word count distribution.
    """
    wc = np.array(list(word_counts.values()))
    alpha, C = estimate_zipf(wc)

    return {"total_words": wc.sum(), "distinct_words": len(wc), "alpha": alpha, "C": C}


def estimate_zipf(word_counts):
    """
    Fit Zipf distribution to a a set of word counts.

    Arguments:
        word_counts: distribution of word counts, as a numpy array

    Returns:
        The alpha parameter of the word count distribution.

    References:

        Moreno-Sanchez et al (2016) define alpha (Eq. 1),
        beta (Eq. 2) and the maximum likelihood estimation (mle)
        of beta (Eq. 6).
        Moreno-Sanchez I, Font-Clos F, Corral A (2016)
        Large-Scale Analysis of Zipf's Law in English Texts.
        PLoS ONE 11(1): e0147073.
        https://doi.org/10.1371/journal.pone.0147073
    """
    assert (
        type(word_counts) == np.ndarray
    ), "Input must be a numerical (numpy) array of word counts"
    mle = minimize_scalar(
        _nlog_likelihood, bracket=(1 + 1e-10, 4), args=word_counts, method="brent"
    )
    beta = mle.x
    alpha = 1 / (beta - 1)

    # Estimate the constant C so that this distribution integrates to 1.
    # https://en.wikipedia.org/wiki/Zipf%27s_law
    C = ((np.arange(len(word_counts)) + 1) ** (-alpha)).sum()

    return alpha, C


def _nlog_likelihood(beta, counts):
    """Log-likelihood function."""
    likelihood = -np.sum(
        np.log((1 / counts) ** (beta - 1) - (1 / (counts + 1)) ** (beta - 1))
    )
    return likelihood
