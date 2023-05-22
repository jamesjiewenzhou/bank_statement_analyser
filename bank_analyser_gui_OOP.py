import tkinter as tk
from tkinter import filedialog, ttk
import pandas as pd
import numpy as np


class BankingApp:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.file_path = self.open_file()
        self.data = self.read_data()
        print(self.data.head())

    @staticmethod
    def open_file():
        file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        return file_path
    
    def read_data(self):
        return pd.read_csv(self.file_path)
    


def main():
    # declare tkinter object
    root = tk.Tk()
    BankingApp(root)


if __name__ == "__main__":
    main()