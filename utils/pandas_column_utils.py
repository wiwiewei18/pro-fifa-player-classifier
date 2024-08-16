import pandas as pd


def contain_character(column, character):
    column_in_string = column.astype(str)

    return column_in_string.str.contains(character).any()


def parseable_to_int(column):
    numeric_column = pd.to_numeric(column, errors="coerce")

    return (
        numeric_column.notna().all()
        and (numeric_column == numeric_column.astype(int)).all()
    )


def remove_character(column, character):
    character_to_remove = f"[{character}]"

    return column.str.replace(character_to_remove, "", regex=True)


def convert_currency_to_number(column, currency):
    def currency_to_number(value):
        if isinstance(value, str):
            value = value.replace(currency, "").strip()

            if "K" in value:
                return int(float(value.replace("K", "")) * 1000)
            elif "M" in value:
                return int(float(value.replace("M", "")) * 1000000)
            else:
                return int(value)
        else:
            return value

    return column.apply(currency_to_number)


def convert_feet_to_number_in_meter(column):
    def feet_to_number(value):
        feet, inches = value.split("'")
        feet = int(feet)
        inches = int(inches)

        total_inches = feet * 12 + inches

        meters = total_inches * 0.0254

        return meters

    return column.apply(feet_to_number)


def convert_lbs_to_kg(column):

    def lbs_to_kg(value):
        value_in_int = float(value)
        return value_in_int * 0.453592

    return column.apply(lbs_to_kg)


def convert_date_to_year(column):
    def date_to_year(value):
        if pd.isna(value) or value == "":
            return -1
        if isinstance(value, str):
            try:
                return pd.to_datetime(value).year
            except ValueError:
                return -1

    return column.apply(date_to_year)
