import tkinter as tk

def toggle_check_all():
    check_all_state = check_all_var.get()
    for var in checkbutton_vars:
        var.set(check_all_state)

def checkbutton_changed():
    check_all_state = all(var.get() for var in checkbutton_vars)
    print(check_all_state)
    check_all_var.set(check_all_state)

window = tk.Tk()
window.title("Checkbutton Column Example")

checkbutton_vars = []
check_all_var = tk.BooleanVar()

check_all_button = tk.Checkbutton(window, text="Check All", variable=check_all_var, command=toggle_check_all)
check_all_button.pack()

for i in range(5):
    var = tk.BooleanVar()
    checkbutton_vars.append(var)
    checkbutton = tk.Checkbutton(window, text=f"Checkbutton {i+1}", variable=var, command=checkbutton_changed)
    checkbutton.pack()

window.mainloop()
