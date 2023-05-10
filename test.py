import pandas as pd
import numpy as np
from tkinter.filedialog import askopenfilename
import datetime as dt
import dateutil.parser as parser
import datefinder


def select_file():
    file_name = askopenfilename()
    return file_name


def read_file(file_name):
    data = pd.read_csv(file_name)
    print(data.head())
    return data


def date_correction(date_string):
    date = parser.parse(date_string)
    return date.date()


def main():
    a = select_file()
    print(a)
    _ = read_file(a)
    _ = date_correction("03/11/2023")


if __name__ == "__main__":
    main()