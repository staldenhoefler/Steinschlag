import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def load_data(file_name):
    return pd.read_csv(file_name, parse_dates=[0])


def add_time_differences(df):
    df['time_difference'] = df['date'].diff().dt.total_seconds()
    return df


def main():
    data = load_data("data/data.csv")
    data = add_time_differences(data)
    time_differences = data['time_difference'].dropna().astype(int) / 3600
    plt.hist(time_differences, bins=np.arange(0, time_differences.max() + 1, 1))
    plt.xlabel('Time difference (hours)')
    plt.ylabel('Frequency')
    plt.title('Distribution of time differences between rocks')
    plt.show()


# Main function
if __name__ == "__main__":
    main()
