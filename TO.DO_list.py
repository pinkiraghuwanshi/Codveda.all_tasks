import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get().strip()
    if task:
        tasks_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Enter a task.")

def remove_task():
    try:
        tasks_listbox.delete(tasks_listbox.curselection())
    except:
        messagebox.showwarning("Warning", "Select a task to remove.")

def toggle_complete():
    try:
        index = tasks_listbox.curselection()[0]
        task = tasks_listbox.get(index)
        if "[Done]" in task:
            tasks_listbox.delete(index)
            tasks_listbox.insert(index, task.replace(" [Done]", ""))
        else:
            tasks_listbox.delete(index)
            tasks_listbox.insert(index, task + " [Done]")
    except:
        messagebox.showwarning("Warning", "Select a task.")

def toggle_priority():
    try:
        index = tasks_listbox.curselection()[0]
        task = tasks_listbox.get(index)
        if "[!]" in task:
            tasks_listbox.delete(index)
            tasks_listbox.insert(index, task.replace(" [!]", ""))
        else:
            tasks_listbox.delete(index)
            tasks_listbox.insert(index, "[!] " + task)
    except:
        messagebox.showwarning("Warning", "Select a task.")

def toggle_theme():
    global dark_theme
    if dark_theme:
        window.config(bg="white")
        tasks_listbox.config(bg="white", fg="black")
        dark_theme = False
    else:
        window.config(bg="black")
        tasks_listbox.config(bg="black", fg="white")
        dark_theme = True

# Main window
window = tk.Tk()
window.title("To-Do List")
window.geometry("350x400")

dark_theme = False  # Default light theme

# Entry field
task_entry = tk.Entry(window, width=30)
task_entry.pack(pady=5)

# Buttons
tk.Button(window, text="Add Task", command=add_task).pack(pady=2)
tk.Button(window, text="Remove Task", command=remove_task).pack(pady=2)
tk.Button(window, text="Complete Task", command=toggle_complete).pack(pady=2)
tk.Button(window, text="Important Task", command=toggle_priority).pack(pady=2)
tk.Button(window, text="Toggle Theme", command=toggle_theme).pack(pady=2)

# Task list
tasks_listbox = tk.Listbox(window, width=40, height=12)
tasks_listbox.pack(pady=5)

window.mainloop()
