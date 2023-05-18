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
    key_labels = []
    for i, key in enumerate(keys):
        key_label = tk.Label(new_window, text=key, width=20)
        key_labels.append(key_label)
        key_labels[i].grid(row=0, column=i)
    # text = tk.Text(new_window)
    
    # Display the contents of the CSV file in a new window
    
    # text.insert('end', df.to_string(index=False))
    # text.grid(row=0, column=0)


def read_keys(df: pd.DataFrame):
    return list(df.keys())


def main():
    # global root
    # Create the main window
    root = tk.Tk()

    # Add a button to open the CSV file
    open_button = tk.Button(root, text="Open CSV File", command=lambda: open_file(root))
    open_button.grid(row=0, column=0)

    # Run the main event loop
    root.mainloop()

if __name__ == "__main__":
    main()