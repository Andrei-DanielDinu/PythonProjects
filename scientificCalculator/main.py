import tkinter as tk
import math

def evaluate(event=None):
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def clear():
    entry.delete(0, tk.END)

def add_to_display(value):
    entry.insert(tk.END, value)

def calculate_trig(trig_func):
    try:
        value = float(entry.get())
        if trig_func == "sin":
            result = math.sin(math.radians(value))
        elif trig_func == "cos":
            result = math.cos(math.radians(value))
        elif trig_func == "tan":
            result = math.tan(math.radians(value))
        elif trig_func == "asin":
            result = math.degrees(math.asin(value))
        elif trig_func == "acos":
            result = math.degrees(math.acos(value))
        elif trig_func == "atan":
            result = math.degrees(math.atan(value))
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def calculate_exp_log(func):
    try:
        if func == "exp":
            result = math.exp(float(entry.get()))
        elif func == "sqrt":
            result = math.sqrt(float(entry.get()))
        elif func == "log":
            result = math.log(float(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def calculate_special_numbers(constant):
    if constant == "pi":
        entry.insert(tk.END, str(math.pi))
    elif constant == "e":
        entry.insert(tk.END, str(math.e))

root = tk.Tk()
root.title("Scientific Calculator")

entry = tk.Entry(root, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=6)

buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
    ("sin", 1, 4), ("cos", 2, 4), ("tan", 3, 4), ("C", 4, 4),
    ("exp", 1, 5), ("sqrt", 2, 5), ("log", 3, 5), ("pi", 4, 5),
    ("asin", 1, 6), ("acos", 2, 6), ("atan", 3, 6), ("e", 4, 6)
]

for (text, row, col) in buttons:
    if text in ("sin", "cos", "tan", "asin", "acos", "atan"):
        btn = tk.Button(root, text=text, command=lambda t=text: calculate_trig(t))
    elif text in ("exp", "sqrt", "log"):
        btn = tk.Button(root, text=text, command=lambda t=text: calculate_exp_log(t))
    elif text in ("pi", "e"):
        btn = tk.Button(root, text=text, command=lambda t=text: calculate_special_numbers(t))
    elif text == "C":
        btn = tk.Button(root, text=text, command=clear)
    elif text == "=":
        btn = tk.Button(root, text=text, command=evaluate)
    else:
        btn = tk.Button(root, text=text, command=lambda t=text: add_to_display(t))
    btn.grid(row=row, column=col)

root.bind('<Return>', evaluate)  # Enter key to evaluate expression
root.mainloop()
