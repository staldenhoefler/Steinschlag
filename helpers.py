import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import scipy.stats as ss
from scipy.stats import  expon, norm, gamma, beta, lognorm
from scipy.stats._continuous_distns import beta_gen, gamma_gen
from scipy import stats
from datetime import datetime, timedelta


def plot_fit(data):
    distributions = [ss.norm, ss.lognorm, ss.expon, ss.gamma]


    # Plot the CDF of the data and the fitted distribution
    plt.hist(data, bins=len(data), density=True, cumulative=True, alpha=0.5, label='Data')
    x = np.linspace(data.min(), data.max()*2, 1000)
    
    for dist in distributions:
        params = dist.fit(data)
        plt.plot(x, dist(*params).cdf(x), label=dist.name)
        plt.xlabel(data.name)
        plt.ylabel('Cumulative probability')
        plt.legend()
    
    plt.show()
    

def fit_best_distribution(data):
    # Define candidate distributions
    dist_names = [norm, lognorm, expon, gamma]

    # Set up initial best parameters and likelihoods
    best_dist = None
    best_params = {}
    best_ll = 1_000_000

    # Set up a dictionary to store the log-likelihoods of each distribution
    ll_dict = {}

    # Iterate through candidate distributions and find the best fit
    for dist_name in dist_names:
        # Fit the distribution to the data using MLE
        params = dist_name.fit(data)

        # Get the negative log-likelihood of the data under the distribution
        ll = -dist_name.logpdf(data, *params).sum()

        # If the fit is better than the current best, update the best fit
        if ll < best_ll:
            best_dist = dist_name
            best_params = params
            best_ll = ll

        # Store the log-likelihood of the fit for this distribution
        ll_dict[dist_name] = ll

    # Sort the distributions by the log-likelihood of their fit
    sorted_dists = sorted(ll_dict, key=ll_dict.get)

    # Generate a list of strings describing the fit of each distribution
    dist_strings = []
    for dist_name in sorted_dists:
        dist_strings.append(f'distribution: {dist_name.name}  score: {ll_dict[dist_name]}')

    # Return the best distribution, its parameters, and the list of distribution fit strings
    return dist_strings
    
    
def compare_simulated_to_original(column):
    plt.hist(zone1[column], bins=num_bins, color='red', alpha=0.5, label='Zone 1', density=True, cumulative=cumulative)
    plt.hist(simulated1[column], bins=num_bins, color='orange', alpha=0.5, label='Simulated 1', density=True, cumulative=cumulative)

    ax1.set_xlabel(column.name)
    ax1.set_ylabel('Frequency Density')
    ax1.legend()