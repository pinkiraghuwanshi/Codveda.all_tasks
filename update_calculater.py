import tkinter as tk

def on_button_click(value):
    """Handles button clicks and updates the entry field."""
    if value == "=":
        try:
            result = eval(entry_var.get())  # Evaluate the expression
            entry_var.set(result)
        except Exception as e:
            entry_var.set("Error")
    elif value == "C":
        entry_var.set("")  # Clear the entry field
    else:
        entry_var.set(entry_var.get() + value)

# Create the main application window
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")

entry_var = tk.StringVar()

# Entry widget for display
entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 20), justify="right", bd=10, relief=tk.RIDGE)
entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=8)

# Calculator button layout
buttons = [
    ("7", "8", "9", "/"),
    ("4", "5", "6", "*"),
    ("1", "2", "3", "-"),
    ("C", "0", "=", "+")
]

# Create and place buttons
for row_index, row_values in enumerate(buttons, start=1):
    for col_index, value in enumerate(row_values):
        btn = tk.Button(root, text=value, font=("Arial", 18), command=lambda v=value: on_button_click(v), width=5, height=2)
        btn.grid(row=row_index, column=col_index, padx=5, pady=5)

# Run the Tkinter event loop
root.mainloop()
