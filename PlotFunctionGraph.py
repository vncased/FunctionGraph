import os
import sys
sys.stderr = open(os.devnull, 'w')


import numpy as np
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from func import functions

def pg(func, x_min, x_max, y_min, y_max):
    try:
        x_min = float(x_min)
        x_max = float(x_max)
        if x_min == x_max:
            x_max = x_min + 0.1
        x = np.linspace(x_min, x_max, 400)
    except:
        return

    try:
        y = eval(func, {"x": x, "sin": np.sin, "cos": np.cos, "tan": np.tan, "exp": np.exp, "log": np.log, "sqrt": np.sqrt, "**": np.power, "abs": np.abs})
    except:
        return

    try:
        y_min = float(y_min)
        y_max = float(y_max)
        if y_min == y_max:
            y_max = y_min + 0.1
        ax.set_ylim(y_min, y_max)
    except:
        return

    ax.plot(x, y, label=func)
    ax.set_title(f'{func}', fontsize=14, fontweight="bold")
    ax.set_xlabel('x', fontsize=12, fontweight="bold")
    ax.set_ylabel('y', fontsize=12, fontweight="bold")
    ax.grid(True)
    ax.legend(fontsize=10)
    ax.set_xlim(x_min, x_max)
    canvas.draw()

def changeInput(*args):
    func = combo.get()
    x_min = x_min_entry.get()
    x_max = x_max_entry.get()
    y_min = y_min_entry.get()
    y_max = y_max_entry.get()
    ax.clear()
    pg(func, x_min, x_max, y_min, y_max)

def zoom(event):
    global ax
    x_min, x_max = ax.get_xlim()
    y_min, y_max = ax.get_ylim()

    if event.keysym == 'plus' or event.keysym == 'equal':
        x_min -= 1
        x_max += 1
        y_min -= 1
        y_max += 1
    elif event.keysym == 'minus':
        x_min += 1
        x_max -= 1
        y_min += 1
        y_max -= 1

    x_min_entry.delete(0, END)
    x_min_entry.insert(0, str(int(x_min)))
    x_max_entry.delete(0, END)
    x_max_entry.insert(0, str(int(x_max)))
    y_min_entry.delete(0, END)
    y_min_entry.insert(0, str(int(y_min)))
    y_max_entry.delete(0, END)
    y_max_entry.insert(0, str(int(y_max)))

    func = combo.get()
    ax.clear()
    pg(func, x_min, x_max, y_min, y_max)
    canvas.draw()

def esc(event):
    root.focus_set()

root = Tk()
root.title("Function Graph")
root.config(bg="#f4f4f4")
style = ttk.Style()
style.theme_use('clam')
root.option_add('*Font', 'Helvetica 12')

fig, ax = plt.subplots(figsize=(9, 7)) 
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().grid(row=0, column=0, padx=10, pady=10, rowspan=12)

input_frame = Frame(root, bg="#f4f4f4")
input_frame.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

label = Label(input_frame, text="Y = F(X):", bg="#f4f4f4", fg="black")
label.grid(row=0, column=0, padx=10, pady=10, sticky="e")


combo = ttk.Combobox(input_frame, values=functions)
combo.set('sin(x)')
combo.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

x_min_label = Label(input_frame, text="X min:", bg="#f4f4f4", fg="black")
x_min_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
x_min_entry = Entry(input_frame)
x_min_entry.insert(0, "-10")
x_min_entry.grid(row=3, column=1, padx=10, pady=5, sticky="ew")

x_max_label = Label(input_frame, text="X max:", bg="#f4f4f4", fg="black")
x_max_label.grid(row=4, column=0, padx=10, pady=5, sticky="e")
x_max_entry = Entry(input_frame)
x_max_entry.insert(0, "10")
x_max_entry.grid(row=5, column=1, padx=10, pady=5, sticky="ew")

y_min_label = Label(input_frame, text="Y min:", bg="#f4f4f4", fg="black")
y_min_label.grid(row=6, column=0, padx=10, pady=5, sticky="e")
y_min_entry = Entry(input_frame)
y_min_entry.insert(0, "-10")
y_min_entry.grid(row=7, column=1, padx=10, pady=5, sticky="ew")

y_max_label = Label(input_frame, text="Y max:", bg="#f4f4f4", fg="black")
y_max_label.grid(row=8, column=0, padx=10, pady=5, sticky="e")
y_max_entry = Entry(input_frame)
y_max_entry.insert(0, "10")
y_max_entry.grid(row=9, column=1, padx=10, pady=5, sticky="ew")

result_label = Label(input_frame, text="", fg="red", bg="#f4f4f4")
result_label.grid(row=10, column=1, padx=10, pady=5, sticky="w")

combo.bind("<KeyRelease>", changeInput)
x_min_entry.bind("<KeyRelease>", changeInput)
x_max_entry.bind("<KeyRelease>", changeInput)
y_min_entry.bind("<KeyRelease>", changeInput)
y_max_entry.bind("<KeyRelease>", changeInput)

root.bind('<plus>', zoom)
root.bind('<equal>', zoom)
root.bind('<minus>', zoom)

root.bind('<Escape>', esc)

changeInput()

root.mainloop()
