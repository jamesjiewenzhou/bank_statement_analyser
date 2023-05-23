import tkinter as tk
from tkinter import filedialog, ttk
import pandas as pd
import numpy as np


class BankingApp:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.file_path = self.open_file()
        self.data = self.read_data()
        # print(self.data.head())
        self.header_frame_setup()
        self.header_data()
        self.scrollable_canvas_setup()
        self.display_frame_setup()
        self.display_frame_data()
        self.analysis_frame_setup()
        self.analysis_frame_data()
        self.resize_window()

    @staticmethod
    def open_file():
        file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        return file_path
    
    def read_data(self):
        return pd.read_csv(self.file_path)
    
    def header_frame_setup(self):
        self.header_frame = ttk.Frame(self.root)
        self.header_frame.pack(side=tk.TOP, fill=tk.BOTH)
    
    def header_data(self):
        self.select_all_var = tk.BooleanVar()
        # TODO: add button command and function
        self.select_all_button = tk.Checkbutton(self.header_frame, variable=self.select_all_var, command=None)
        self.select_all_button.grid(row=0, column=0)
        keys = list(self.data.keys())
        for i, key in enumerate(keys):
            key_label = tk.Label(self.header_frame, text=key, width=20)
            key_label.grid(row=0, column=i+1)

    def scrollable_canvas_setup(self):
        self.canvas = tk.Canvas(self.root)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = ttk.Scrollbar(self.canvas, orient=tk.VERTICAL, command=self.canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.canvas.configure(yscrollcommand=scrollbar.set)
        self.canvas.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        self.canvas.bind_all("<MouseWheel>", lambda e: self.canvas.yview_scroll(int(-1 * (e.delta / 120)), "units"))

    def display_frame_setup(self):
        self.display_frame = ttk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.display_frame, anchor=tk.NW)

    def display_frame_data(self):
        self.row_selected = [tk.BooleanVar() for _ in range(len(self.data))]
        for i, row in self.data.iterrows():
            # TODO: update command and write function
            toggle_button = tk.Checkbutton(self.display_frame, variable=self.row_selected[i], command=None)
            toggle_button.grid(row=i+1, column=0)
            for j, value in enumerate(row):
                key_text = tk.Label(self.display_frame, text=value, width=20)
                key_text.grid(row=i+1, column=j+1)

    def analysis_frame_setup(self):
        self.analysis_frame = ttk.Frame(self.root)
        self.analysis_frame.pack(side=tk.TOP, fill=tk.BOTH)

    def analysis_frame_data(self):
        calculate_button = tk.Button(self.analysis_frame, text="Calculate Costs", command=lambda: None)
        calculate_button.grid(row=0, column=0)
        # test_label = tk.Label(self.analysis_frame, text="fuck")
        # test_label.grid(row=0, column=1)

    def resize_window(self):
        self.canvas.update_idletasks()
        canvas_width = self.display_frame.winfo_width()
        self.canvas.configure(width=canvas_width)
        self.root.update_idletasks()
        window_width = canvas_width + self.analysis_frame.winfo_width() + 40
        self.root.geometry(f"{window_width}x300")
    


def main():
    # declare tkinter object
    root = tk.Tk()
    app = BankingApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()