import tkinter as tk
from tkinter import ttk

def on_mousewheel(event):
    canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

window = tk.Tk()
window.title("Scrollable Window Example")

# Create a Canvas widget
canvas = tk.Canvas(window)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Create a Scrollbar widget and associate it with the Canvas
scrollbar = ttk.Scrollbar(window, orient=tk.VERTICAL, command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Configure the Canvas to use the Scrollbar
canvas.configure(yscrollcommand=scrollbar.set)

# Create a Frame inside the Canvas to hold the content
frame = ttk.Frame(canvas)
canvas.create_window((0, 0), window=frame, anchor=tk.NW)

# Example content
for i in range(20):
    label = ttk.Label(frame, text=f"Label {i+1}")
    label.pack(pady=5)

# Configure the Canvas to scroll the content
frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
canvas.bind_all("<MouseWheel>", on_mousewheel)

window.mainloop()