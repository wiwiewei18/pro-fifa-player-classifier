import pandas as pd


def get_percentage(dataframe):
    total_missing_value = dataframe.isnull().sum().sort_values(ascending=False)

    percentage_of_missing_value = (
        dataframe.isnull().sum() / dataframe.isnull().count() * 100
    ).sort_values(ascending=False)

    missing_data_df = pd.concat(
        [total_missing_value, percentage_of_missing_value],
        axis=1,
        keys=["Total", "Percentage"],
    )

    return missing_data_df
