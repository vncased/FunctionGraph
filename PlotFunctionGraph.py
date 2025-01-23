import numpy as np
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def pg(func, x_min, x_max, y_min, y_max):
    try:
        x_min = float(x_min)
        x_max = float(x_max)

        if x_min == x_max:
            x_max = x_min + 0.1

        x = np.linspace(x_min, x_max, 400)
    except ValueError:
        result_label.config(text="Ошибка: некорректные границы X")
        return

    try:
        y = eval(func,
                 {"x": x, "sin": np.sin, "cos": np.cos, "tan": np.tan, "exp": np.exp, "log": np.log, "sqrt": np.sqrt,
                  "**": np.power, "abs": np.abs})
    except Exception as e:
        result_label.config(text=f"Ошибка в функции: {e}")
        return

    try:
        y_min = float(y_min)
        y_max = float(y_max)

        if y_min == y_max:
            y_max = y_min + 0.1

        ax.set_ylim(y_min, y_max)
    except ValueError:
        result_label.config(text="Ошибка: некорректные границы Y")
        return

    color = next(color_cycle)
    ax.plot(x, y, label=func, color=color)
    ax.set_title(f'{func}')
    ax.set_xlabel('x')
    ax.set_ylabel('y')

    ax.grid(True)
    ax.legend()

    ax.set_xlim(x_min, x_max)

    canvas.draw()


def ul(language):
    global label, x_min_label, x_max_label, y_min_label, y_max_label, result_label, button, close_button
    if language == "ru":
        label.config(text="Y = F(X):")
        x_min_label.config(text="X min:")
        x_max_label.config(text="X max:")
        y_min_label.config(text="Y min:")
        y_max_label.config(text="Y max:")
        result_label.config(text="")
        button.config(text="Построить график")
        close_button.config(text="Закрыть")
    elif language == "en":
        label.config(text="Y = F(X):")
        x_min_label.config(text="X min:")
        x_max_label.config(text="X max:")
        y_min_label.config(text="Y min:")
        y_max_label.config(text="Y max:")
        result_label.config(text="")
        button.config(text="Plot Graph")
        close_button.config(text="Close")


def obc():
    func = combo.get()
    x_min = x_min_entry.get()
    x_max = x_max_entry.get()
    y_min = y_min_entry.get()
    y_max = y_max_entry.get()

    pg(func, x_min, x_max, y_min, y_max)


def on_close():
    root.destroy()


def focus_next_widget(event):
    event.widget.tk_focusNext().focus()


def on_enter(event):
    if event.widget == combo:
        x_min_entry.focus()
    elif event.widget == x_min_entry:
        x_max_entry.focus()
    elif event.widget == x_max_entry:
        y_min_entry.focus()
    elif event.widget == y_min_entry:
        y_max_entry.focus()
    elif event.widget == y_max_entry:
        obc()


def on_arrow_key(event):
    widget = event.widget
    if event.keysym == 'Up' or event.keysym == 'Down':
        widget.tk_focusNext().focus()


def on_min_to_max(event):
    if event.widget == x_min_entry:
        x_max_entry.delete(0, END)
        x_max_entry.insert(0, x_min_entry.get().replace("-", ""))
    elif event.widget == y_min_entry:
        y_max_entry.delete(0, END)
        y_max_entry.insert(0, y_min_entry.get().replace("-", ""))


root = Tk()
root.title("График функций")


menu_bar = Menu(root)
root.config(menu=menu_bar)

language_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Language", menu=language_menu)
language_menu.add_command(label="Русский", command=lambda: ul("ru"))
language_menu.add_command(label="English", command=lambda: ul("en"))


fig, ax = plt.subplots(figsize=(6, 4))
color_cycle = iter(
    ["blue", "green", "red", "purple", "orange", "brown", "pink", "gray", "cyan", "magenta", "lime", "teal", "gold"])

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().grid(row=0, column=0, padx=10, pady=10, rowspan=12)


label = Label(root, text="Y = F(X):")
label.grid(row=0, column=1, padx=10, pady=10, sticky="w")

functions = [
    'sin(x)', 'cos(x)', 'tan(x)', 'exp(x)', 'log(x)',
    'x - 2', 'x * 2', 'x ** 2', 'sin(x) * cos(2 * x)',
    'x ** 3', 'sin(x) + cos(x)', 'log(x + 10)',
    'exp(x) - exp(-x)', 'sqrt(abs(x))'
]
combo = ttk.Combobox(root, values=functions)
combo.set('sin(x)')
combo.grid(row=1, column=1, padx=10, pady=5, sticky="w")

x_min_label = Label(root, text="X min:")
x_min_label.grid(row=2, column=1, padx=10, pady=5, sticky="w")
x_min_entry = Entry(root)
x_min_entry.insert(0, "-10")
x_min_entry.grid(row=3, column=1, padx=10, pady=5, sticky="w")

x_max_label = Label(root, text="X max:")
x_max_label.grid(row=4, column=1, padx=10, pady=5, sticky="w")
x_max_entry = Entry(root)
x_max_entry.insert(0, "10")
x_max_entry.grid(row=5, column=1, padx=10, pady=5, sticky="w")

y_min_label = Label(root, text="Y min:")
y_min_label.grid(row=6, column=1, padx=10, pady=5, sticky="w")
y_min_entry = Entry(root)
y_min_entry.insert(0, "-10")
y_min_entry.grid(row=7, column=1, padx=10, pady=5, sticky="w")

y_max_label = Label(root, text="Y max:")
y_max_label.grid(row=8, column=1, padx=10, pady=5, sticky="w")
y_max_entry = Entry(root)
y_max_entry.insert(0, "10")
y_max_entry.grid(row=9, column=1, padx=10, pady=5, sticky="w")

result_label = Label(root, text="", fg="red")
result_label.grid(row=10, column=1, padx=10, pady=5, sticky="w")

button = Button(root, text="Построить график", command=obc)
button.grid(row=11, column=1, pady=20, sticky="w")

close_button = Button(root, text="Закрыть", command=on_close)
close_button.grid(row=12, column=1, pady=10, sticky="w")


combo.bind("<Return>", focus_next_widget)
x_min_entry.bind("<Return>", focus_next_widget)
x_max_entry.bind("<Return>", focus_next_widget)
y_min_entry.bind("<Return>", focus_next_widget)
y_max_entry.bind("<Return>", on_enter)

x_min_entry.bind("<Up>", on_arrow_key)
x_min_entry.bind("<Down>", on_arrow_key)
x_max_entry.bind("<Up>", on_arrow_key)
x_max_entry.bind("<Down>", on_arrow_key)
y_min_entry.bind("<Up>", on_arrow_key)
y_min_entry.bind("<Down>", on_arrow_key)
y_max_entry.bind("<Up>", on_arrow_key)
y_max_entry.bind("<Down>", on_arrow_key)

x_min_entry.bind("<KeyRelease>", on_min_to_max)
y_min_entry.bind("<KeyRelease>", on_min_to_max)

root.mainloop()
