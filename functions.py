import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
from fitter import Fitter
import numpy as np
from pprint import pprint


def trim_non_visible(s):
    """Strip if s is a string, otherwise return s."""
    if isinstance(s, str):
        return s.strip()
    return s


def read_data(file):
    """Reads the first 4 columns from the given file and drops empty rows."""
    data = pd.read_csv(
        file, delimiter=",", usecols=[0, 1, 2, 3], parse_dates=[[0, 1]]
    )
    data.columns = ["date", "m", "v"]
    data = data[data["date"] != "nan nan"]
    data = data.dropna(how="all")
    data["date"] = pd.to_datetime(data["date"])
    data = data.applymap(trim_non_visible)
    return data.sort_values(by=["date"])


def _get_time_differences(df):
    """Returns the time differences between rocks in hours."""
    return df["date"].diff().dt.total_seconds() / 3600


def add_time_differences(df):
    """Adds the time differences to the dataframe."""
    df["time_differences"] = _get_time_differences(df)
    return df


def add_energy(df):
    """Adds the energy to the dataframe."""
    df["e"] = 0.5 * df["m"] * df["v"] ** 2
    return df


def reorder_columns(df):
    """Reorders the columns of the dataframe."""
    cols = ["zone", "date", "time_differences", "m", "v", "e"]
    existing_columns = [col for col in cols if col in df.columns]
    return df[existing_columns]


def scatter_plot(
    df: pd.DataFrame,
    col: str,
    c="zone",
    colorbar=False,
    colormap="viridis",
    title=None,
):
    """Plots the given column of the given dataframe as a scatter plot."""
    if title is None:
        title = f"{col.upper()} vs. Date"
    title = title + f"\nnumber of records: {len(df)}"
    df["date"] = pd.to_datetime(df["date"])
    ax = df.plot.scatter(
        x="date", y=col, c=c, colorbar=colorbar, colormap=colormap
    )
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d"))
    ax.xaxis.set_major_locator(mdates.AutoDateLocator())
    plt.title(
        f"{col} vs. date\nnumber of records: {len(df)}"
        if title is None
        else title
    )
    plt.xticks(rotation=90)


def plot_histogram(df: pd.DataFrame, col: str, zone: int, title: str = None):
    """Plots the given column of the given dataframe as a histogram."""
    if title is None:
        title = f"{col.upper()} for Zone {zone}"
    title = title + f"\nnumber of records: {len(df)}"
    df[col].hist(bins=np.sqrt(len(df[col])).astype(int) * 6)
    plt.xlabel(col.upper())
    plt.ylabel("Frequency")
    plt.title(title)
    plt.show()


def _fit_distributions(data, distributions=None):
    """Fits the given data to the most common distributions and returns the fitted object."""
    if distributions is None:
        distributions = [
            "norm",
            "expon",
            "gamma",
            "lognorm",
            "poison",
            "beta",
            "standard_normal",
            "binomial",
            "chauchy",
            "pareto",
            "weibull_min",
            "weibull_max",
        ]

    f = Fitter(data, distributions=distributions)
    f.fit()  # Maximum Likelihood Estimation (MLE)

    return f


def best_distributions(df, zones=None, cols=None, distributions=None):
    """Fits the given data to the most common distributions, return the best distributions for each zone and column."""
    if zones is None:
        zones = df["zone"].unique()
    if cols is None:
        cols = df.select_dtypes(include=[np.number]).columns

    fit = {}
    for zone in zones:
        for col in cols:
            f = _fit_distributions(
                df[df["zone"] == zone][col].dropna().values,
                distributions=distributions,
            )
            fit[(zone, col)] = f.fitted_param, f.df_errors.sort_values(
                by="sumsquare_error"
            )

    return fit


def print_fit(fit, zone, col):
    f = fit[zone, col][1][:5]
    print("parameters for each of the 5 best distributions:\n\n")
    for dist in f.index:
        print(f"{dist}: {fit[zone, col][0][dist]}")
    print("\n\n", f)
