import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import pandas as pd
from fitter import Fitter
import numpy as np


def read_data(file):
    """Reads the first 4 columns from the given file and drops empty rows."""
    data = pd.read_csv(file, delimiter=',', usecols=[0, 1, 2, 3],
                       parse_dates=[[0, 1]])
    data.columns = ['date', 'm', 'v']
    data = data[data['date'] != 'nan nan']
    data = data.dropna(how='all')
    data['date'] = pd.to_datetime(data['date'])
    return data.sort_values(by=['date'])


def _get_time_differences(df):
    """Returns the time differences between rocks in hours."""
    return df['date'].diff().dt.total_seconds() / 3600


def add_time_differences(df):
    """Adds the time differences to the dataframe."""
    df['time_differences'] = _get_time_differences(df)
    return df


def add_energy(df):
    """Adds the energy to the dataframe."""
    df['e'] = 0.5 * df['m'] * df['v'] ** 2
    return df


def reorder_columns(df):
    """Reorders the columns of the dataframe."""
    cols = ['zone', 'date', 'time_differences', 'm', 'v', 'e']
    existing_columns = [col for col in cols if col in df.columns]
    return df[existing_columns]


def scatter_plot(df: pd.DataFrame, col: str, c='zone', colorbar=False,
                 colormap='viridis', title=None):
    """Plots the given column of the given dataframe as a scatter plot."""
    df['date'] = pd.to_datetime(df['date'])
    ax = df.plot.scatter(x='date', y=col, c=c, colorbar=colorbar,
                         colormap=colormap, title=f'{col} vs. date' if title is None else title)
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    ax.xaxis.set_major_locator(mdates.AutoDateLocator())
    plt.xticks(rotation=90)


def plot_histogram(df: pd.DataFrame, col: str, zone: int):
    """Plots the given column of the given dataframe as a histogram."""
    df[col].hist(bins=np.sqrt(len(df[col])).astype(int) * 6)
    plt.title(f'{col.upper()} for Zone {zone}')
    plt.xlabel(col.upper())
    plt.ylabel('Frequency')
    plt.show()


def _fit_common_distributions(data):
    """Fits the given data to the most common distributions and returns the fitted object."""
    f = Fitter(data,
               distributions=['norm', 'expon', 'gamma', 'lognorm', 'poison', 'beta', 'standard_normal', 'binomial', 'chauchy', 'pareto', 'weibull_min', 'weibull_max'])
    f.fit()
    return f


def show_best_distribution(data):
    """Fits the given data to the most common distributions, prints the best distribution and shows a plot of the best distributions."""
    f = _fit_common_distributions(data)
    print(f.get_best())
    print(f.summary())
