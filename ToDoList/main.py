import tkinter as tk
from tkinter import filedialog
from tkinter import font
from tkinter import ttk
import random

def add_task():
    task = entry_task.get()
    if task:
        todo_list.insert(tk.END, task)
        entry_task.delete(0, tk.END)

def remove_task():
    try:
        index = todo_list.curselection()[0]
        todo_list.delete(index)
    except IndexError:
        pass

def view_tasks():
    tasks = todo_list.get(0, tk.END)
    if tasks:
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
    else:
        print("No tasks in the list.")

def submit_tasks():
    tasks = todo_list.get(0, tk.END)
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, 'w') as file:
            for task in tasks:
                file.write(task + '\n')

def display_quote():
    with open('quotes.txt', 'r') as file:
        quotes = file.readlines()
        if quotes:
            random_quote = random.choice(quotes)
            quote_label.config(text=f'"{random_quote.strip()}"', font=('italic', 10))

root = tk.Tk()
custom_font = font.Font(family="Comic Sans MS", size=10)
root.title("To-Do List")

style = ttk.Style()
style.theme_use('clam')

quote_frame = ttk.Frame(root)
quote_frame.pack(side=tk.TOP, padx=10, pady=10)

quote_label = ttk.Label(quote_frame, text="", font=('italic', 10))
quote_label.pack()

display_quote()  # Display initial quote when the window opens


frame_input = ttk.Frame(root)
frame_input.pack(side=tk.TOP, padx=10, pady=5)

label_task = ttk.Label(frame_input, text="Enter Task", font=custom_font)
label_task.grid(row=0, column=0, padx=5, pady=5)

entry_task = ttk.Entry(frame_input, width=30)
entry_task.grid(row=1, column=0, padx=5, pady=5)



frame_list = ttk.Frame(root, borderwidth=2, relief=tk.RIDGE)
frame_list.pack(side=tk.RIGHT, padx=10, pady=5)

todo_list = tk.Listbox(frame_list, width=40, height=10, font=custom_font, borderwidth=2, relief=tk.SUNKEN)
todo_list.pack()

button_add = ttk.Button(root, text="Add Task", width=15, command=add_task)
button_add.pack(side=tk.TOP, padx=10, pady=5)

button_remove = ttk.Button(root, text="Remove Task", width=15, command=remove_task)
button_remove.pack(side=tk.TOP, padx=10, pady=5)

button_view = ttk.Button(root, text="View Tasks", width=15, command=view_tasks)
button_view.pack(side=tk.TOP, padx=10, pady=5)

button_submit = ttk.Button(root, text="Submit Tasks", width=15, command=submit_tasks)
button_submit.pack(side=tk.TOP, padx=10, pady=5)

root.mainloop()
