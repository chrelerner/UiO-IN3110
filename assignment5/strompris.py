#!/usr/bin/env python3
"""
Fetch data from https://www.hvakosterstrommen.no/strompris-api
and visualize it.

Assignment 5
"""

import datetime

import altair as alt
alt.renderers.enable('altair_viewer')
import pandas as pd
import requests
import requests_cache

# install an HTTP request cache
# to avoid unnecessary repeat requests for the same data
# this will create the file http_cache.sqlite
requests_cache.install_cache()


# task 5.1:

def prepare_dict_information(data_dict: dict) -> dict:
    """Fetches the entries 'time_start' and 'NOK_per_kWh' from an API dict.

    This function should only be used in the fetch_day_prices() function.

    Arguments:
        data_dict (dict):
            Dictionary with price-information for
            an hour of the day.
    Returns:
        new_dict (dict):
            Dictionary containing the information
            'time_start' and 'NOK_per_kWh'.
    """
    new_dict = {}
    new_dict['time_start'] = data_dict['time_start']
    new_dict['NOK_per_kWh'] = data_dict['NOK_per_kWh']
    return new_dict


def apply_zero_padding(number: str) -> str:
    """Applies leading zero to number if length is 1.
    """
    if len(number) == 1:
        number = f"0{number}"
    return number


def fetch_day_prices(date: datetime.date = None, location: str = "NO1") -> pd.DataFrame:
    """Fetch one day of data for one location from hvakosterstrommen.no API

    This function will fetch all the prices for one location of one day
    and store these in a dataframe with two column for time and price.
    The dataframe returned should consist of 24 rows of data (24 hours).

    Arguments:
        date (datetime.date):
            The date from which information on prices should be fetched.
        location (str):
            The location from which information on prices should be fetched.
    Returns:
        df (pd.dataframe):
            Table containing the prices throughout a date for a location.
    """
    if date is None:
        date = datetime.date.today()

    # Asserts date is after 2nd of October 2022.
    assertion_date = datetime.date(2022, 10, 2)
    assert date >= assertion_date, f"Expected date after {assertion_date}, got {date}"

    # Fetches the information from the API.
    year, month, day = str(date.year), str(date.month), str(date.day)
    month = apply_zero_padding(month)
    day = apply_zero_padding(day)
    api = "https://www.hvakosterstrommen.no/api"
    url = f"{api}/v1/prices/{year}/{month}-{day}_{location}.json"
    r = requests.get(url)
    if not 200 <= r.status_code < 300:
        raise ValueError(f"Request unsuccessful with status-code: {r.status_code}")

    # Takes the information we want from the API and puts it into a dataframe.
    data = r.json()
    prepared_data = [prepare_dict_information(data_dict) for data_dict in data]
    df = pd.DataFrame.from_dict(prepared_data)
    df["time_start"] = pd.to_datetime(df["time_start"], utc=True).dt.tz_convert("Europe/Oslo")

    return df


# LOCATION_CODES maps codes ("NO1") to names ("Oslo")
LOCATION_CODES = {
    'NO1': 'Oslo',
    'NO2': 'Kristiansand',
    'NO3': 'Trondheim',
    'NO4': 'Tromsø',
    'NO5': 'Bergen',
}

# task 1:


def fetch_prices(
    end_date: datetime.date = None,
    days: int = 7,
    locations=tuple(LOCATION_CODES.keys()),
) -> pd.DataFrame:
    """Fetch prices for multiple days and locations into a single DataFrame

    Arguments:
        end_date (datetime.date):
            The last date to gather information from.
        days (int):
            The number of days to gather information from counted
            backwards from end_date.
    Returns:
        resut_df (pd.DataFrame):
            Pandas dataframe with all the information requested.
    """
    if end_date is None:
        end_date = datetime.date.today()

    number_of_days = datetime.timedelta(days=(days - 1))
    start_date = end_date - number_of_days

    result_df = pd.DataFrame()  # Creates empty dataframe to concatenate results.
    for i in range(days):
        day_counter = datetime.timedelta(days=i)
        correct_date = start_date + day_counter
        for location in locations:
            date_df = fetch_day_prices(correct_date, location)

            # Adds additional columns for location name and code,
            # and concatenates it to 'result_df'.
            date_df['location_code'] = location
            date_df['location'] = LOCATION_CODES[location]
            result_df = pd.concat([result_df, date_df])

    return result_df


# task 5.1:


def plot_prices(df: pd.DataFrame) -> alt.Chart:
    """Plot energy prices over time

    x-axis is time_start
    y-axis is price in NOK
    each location gets its own line on the plot

    Arguments:
        df (pd.DataFrafe):
            Pandas dataframe with the information to plot.
    Returns:
        chart (alt.Chart):
            Plot in the form of an altair chart.
    """
    chart = alt.Chart(df).mark_line().encode(
        x="time_start",
        y="NOK_per_kWh",
        color="location"
    )
    return chart


# Task 5.4


def plot_daily_prices(df: pd.DataFrame) -> alt.Chart:
    """Plot the daily average price

    x-axis should be time_start (day resolution)
    y-axis should be price in NOK

    You may use any mark.

    Make sure to document arguments and return value...
    """
    ...


# Task 5.6

ACTIVITIES = {
    # activity name: energy cost in kW
    ...
}


def plot_activity_prices(
    df: pd.DataFrame, activity: str = "shower", minutes: float = 10
) -> alt.Chart:
    """
    Plot price for one activity by name,
    given a data frame of prices, and its duration in minutes.

    Make sure to document arguments and return value...
    """

    ...


def main():
    """Allow running this module as a script for testing."""
    df = fetch_prices()
    chart = plot_prices(df)
    # showing the chart without requiring jupyter notebook or vs code for example
    # requires altair viewer: `pip install altair_viewer`
    chart.show()


if __name__ == "__main__":
    main()
