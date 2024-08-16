import numpy as np


def get_upper_and_lower_bounds(column):
    Q1 = column.quantile(0.25)
    Q3 = column.quantile(0.75)

    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    return [upper_bound, lower_bound]


def get_outliers(dataframe, column_name):
    column = dataframe[column_name]

    upper_bound, lower_bound = get_upper_and_lower_bounds(column)

    return dataframe[(column < lower_bound) | (column > upper_bound)]


def remove_outliers(dataframe, column_name):
    column = dataframe[column_name]

    upper_bound, lower_bound = get_upper_and_lower_bounds(column)

    return dataframe[(column >= lower_bound) & (column <= upper_bound)]


def percentile_capping(dataframe, column_name):
    lower_bound = dataframe[column_name].quantile(0.01)
    upper_bound = dataframe[column_name].quantile(0.99)

    return np.clip(dataframe[column_name], lower_bound, upper_bound)


def standard_deviation_capping(dataframe, column_name):
    mean = dataframe[column_name].mean()
    std = dataframe[column_name].std()

    lower_bound = mean - 3 * std  # 3 standard deviations below the mean
    upper_bound = mean + 3 * std  # 3 standard deviations above the mean

    return np.clip(dataframe[column_name], lower_bound, upper_bound)
