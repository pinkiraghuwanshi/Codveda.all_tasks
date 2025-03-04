import random
import string
import tkinter as tk
from tkinter import messagebox

# Function to generate password
def generate_password():
    try:
        length = int(entry_length.get())
        if length < 4:
            messagebox.showerror("Error", "Password length should be at least 4.")
            return
        
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        
        # Display generated password
        entry_password.delete(0, tk.END)
        entry_password.insert(0, password)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

# Create the main application window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x250")

# Labels and Entry fields
tk.Label(root, text="Enter Password Length:", font=("Arial", 12)).pack(pady=10)
entry_length = tk.Entry(root, font=("Arial", 12))
entry_length.pack()

tk.Button(root, text="Generate Password", font=("Arial", 12), command=generate_password).pack(pady=10)

tk.Label(root, text="Generated Password:", font=("Arial", 12)).pack()
entry_password = tk.Entry(root, font=("Arial", 12), width=30)
entry_password.pack()

# Run the application
root.mainloop()