import tkinter as tk

class MyApp:
    def __init__(self, root):
        self.root = root
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.root, text="Hello, World!")
        self.label.pack()

        self.button = tk.Button(self.root, text="Click Me", command=self.button_click)
        self.button.pack()

    def button_click(self):
        self.label.config(text="Button Clicked!")

# Create the tkinter root window
root = tk.Tk()

# Create an instance of the MyApp class
app = MyApp(root)

# Start the tkinter event loop
root.mainloop()