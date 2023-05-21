import tkinter as tk
from tkinter import filedialog
import pandas as pd

def open_file(root: tk.Tk):
    # global root
    # Get the file path using the file dialog
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    
    # Read the CSV file using Pandas
    df = pd.read_csv(file_path)

    # create a list of labels for the headers
    new_window = tk.Toplevel(root)
    keys = read_keys(df)
    for i, key in enumerate(keys):
        key_label = tk.Label(new_window, text=key, width=20)
        key_label.grid(row=0, column=i+1)

    row_selected = [tk.BooleanVar() for _ in range(len(df))]
    select_all_var = tk.BooleanVar()
    select_all_button = tk.Checkbutton(new_window, variable=select_all_var, command=lambda: select_all(row_selected, select_all_var))
    select_all_button.grid(row=0, column=0)
    toggle_buttons = []
    for i, row in df.iterrows():
        toggle_button = tk.Checkbutton(new_window, variable=row_selected[i], command=lambda: single_select(row_selected, select_all_var))
        toggle_button.grid(row=i+1, column=0)
        toggle_buttons.append(toggle_button)
        for j, value in enumerate(row):
            key_text = tk.Label(new_window, text=value)
            key_text.grid(row=i+1, column=j+1)   


def select_all(toggle_button_vars: list[tk.BooleanVar], select_all_var: tk.BooleanVar):
    check_all_state = select_all_var.get()
    for var in toggle_button_vars:
        var.set(check_all_state)


def single_select(toggle_button_vars: list[tk.BooleanVar], select_all_var: tk.BooleanVar):
    check_all_state = all(var.get() for var in toggle_button_vars)
    select_all_var.set(check_all_state)


def check_toggles(toggle_button_vars: list[tk.BooleanVar]):
    selected_rows = []
    for i, button_var in enumerate(toggle_button_vars):
        if button_var.get():
            selected_rows.append(i)
    return selected_rows


def read_keys(df: pd.DataFrame):
    return list(df.keys())


def main():
    # Create the main window
    root = tk.Tk()

    # Add a button to open the CSV file
    open_button = tk.Button(root, text="Open CSV File", command=lambda: open_file(root))
    open_button.grid(row=0, column=0)

    # Run the main event loop
    root.mainloop()

if __name__ == "__main__":
    main()