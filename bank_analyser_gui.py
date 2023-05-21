import tkinter as tk
from tkinter import filedialog, ttk
import pandas as pd


def open_file():
    # reads all the data first
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    data = pd.read_csv(file_path)
    return data


def gui_layout(root: tk.Tk, data: pd.DataFrame):

# TODO: pin the top row
# TODO: put in the summation feature
# TODO: put in a date filter
# TODO: put in a summation graph

    canvas = tk.Canvas(root)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.bind_all("<MouseWheel>", lambda e: canvas.yview_scroll(int(-1 * (e.delta / 120)), "units"))

    display_frame = ttk.Frame(canvas)
    canvas.create_window((0, 0), window=display_frame, anchor=tk.NW)

    keys = list(data.keys())
    print(keys)

    for i, key in enumerate(keys):
        key_label = tk.Label(display_frame, text=key, width=20)
        key_label.grid(row=0, column=i+1)
    
    row_selected = [tk.BooleanVar() for _ in range(len(data))]
    select_all_var = tk.BooleanVar()
    select_all_button = tk.Checkbutton(display_frame, variable=select_all_var, command=lambda: select_all(row_selected, select_all_var))
    select_all_button.grid(row=0, column=0)
    toggle_buttons = []
    for i, row in data.iterrows():
        toggle_button = tk.Checkbutton(display_frame, variable=row_selected[i], command=lambda: single_select(row_selected, select_all_var))
        toggle_button.grid(row=i+1, column=0)
        toggle_buttons.append(toggle_button)
        for j, value in enumerate(row):
            key_text = tk.Label(display_frame, text=value)
            key_text.grid(row=i+1, column=j+1)


    canvas.update_idletasks()
    canvas_width = display_frame.winfo_width()
    canvas.configure(width=canvas_width)
    root.update_idletasks()
    window_width = display_frame.winfo_width() + root.winfo_width() - canvas.winfo_width()
    root.geometry(f"{window_width}x300")


def select_all(toggle_button_vars: list[tk.BooleanVar], select_all_var: tk.BooleanVar):
    check_all_state = select_all_var.get()
    for var in toggle_button_vars:
        var.set(check_all_state)


def single_select(toggle_button_vars: list[tk.BooleanVar], select_all_var: tk.BooleanVar):
    check_all_state = all(var.get() for var in toggle_button_vars)
    select_all_var.set(check_all_state)


def main():
    # try to define all the buttons and stuff here
    data = open_file()
    
    # declare tkinter stuff
    root = tk.Tk()

    # setup gui layout
    gui_layout(root, data)

    # run tkinter stuff
    root.mainloop()


if __name__ == "__main__":
    main()