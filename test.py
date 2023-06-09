import pandas as pd
import numpy as np
from tkinter.filedialog import askopenfilename
import datetime as dt
from dateutil.parser import parse, ParserError


def select_file():
    file_name = askopenfilename()
    return file_name


def read_file(file_name):
    data = pd.read_csv(file_name)
    print(data.head())
    return data


def return_keys(data: pd.DataFrame):
    return list(data.keys())


def update_dates(data: pd.DataFrame, keys: list):
    keys_copy = [key.lower() for key in keys]
    print(keys_copy)
    date_indices = []
    date_substring = "date"
    for i, key in enumerate(keys_copy):
        if key.find(date_substring) != -1:
            date_indices.append(i)
    
    print(date_indices)
    for index in date_indices:
        new_format_dates = correct_dates(data[keys[index]].copy().to_list())
        data[keys[index]] = new_format_dates
    print(data.head())
        


def correct_dates(dates):
    date_formats = []
    day_first = False
    year_first = False
    for date in dates:
        all_formats = determine_datetime_format(date)
        date_formats.append(all_formats)
    
    for formats in date_formats:
        available_formats = []
        for format in formats:
            if format[:2] == "%Y":
                year_first = True
                break
            elif format[:2] == "%d":
                available_formats.append("%d")
            elif format[:2] == "%m":
                available_formats.append("%m")
        if year_first:
            break
        elif len(available_formats) == 1:
            if available_formats[0] == "%d":
                day_first = True
            break
    
    new_dates = []
    for date in dates:
        new_dates.append(parse(date, yearfirst=year_first, dayfirst=day_first).date())
    
    return new_dates


def determine_datetime_format(datetime_string):
    known_formats = [
        "%Y-%m-%d %H:%M:%S.%f",
        "%Y-%m-%d %H:%M:%S",
        "%Y-%m-%d %H:%M",
        "%Y-%m-%d",
        "%m-%d-%Y %I:%M:%S %p",
        "%m-%d-%Y %I:%M %p",
        "%m-%d-%Y",
        "%m-%d-%y %I:%M:%S %p",
        "%m-%d-%y %I:%M %p",
        "%m-%d-%y",
        "%d-%m-%Y %I:%M:%S %p",
        "%d-%m-%Y %I:%M %p",
        "%d-%m-%Y",
        "%d-%m-%y %I:%M:%S %p",
        "%d-%m-%y %I:%M %p",
        "%d-%m-%y",
        "%m/%d/%Y %I:%M:%S %p",
        "%m/%d/%Y %I:%M %p",
        "%m/%d/%Y",
        "%m/%d/%y %I:%M:%S %p",
        "%m/%d/%y %I:%M %p",
        "%m/%d/%y",
        "%d/%m/%Y %I:%M:%S %p",
        "%d/%m/%Y %I:%M %p",
        "%d/%m/%Y",
        "%d/%m/%y %I:%M:%S %p",
        "%d/%m/%y %I:%M %p",
        "%d/%m/%y",
        "%Y/%m/%d %H:%M:%S.%f",
        "%Y/%m/%d %H:%M:%S",
        "%Y/%m/%d %H:%M",
        "%Y/%m/%d",
    ]
    correct_formats = []
    for format_string in known_formats:
        try:
            dt.datetime.strptime(datetime_string, format_string)
            correct_formats.append(format_string)
        except ValueError:
            pass
    return correct_formats


def main():
    a = select_file()
    print(a)
    data = read_file(a)
    keys = return_keys(data)
    update_dates(data, keys)


if __name__ == "__main__":
    main()