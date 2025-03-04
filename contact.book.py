import tkinter as tk
from tkinter import messagebox, simpledialog

# Contact dictionary to store contacts
contacts = {}

# Function to add a new contact
def add_contact():
    name = simpledialog.askstring("Input", "Enter Name:")
    if not name:
        return
    phone = simpledialog.askstring("Input", "Enter Phone Number:")
    email = simpledialog.askstring("Input", "Enter Email:")
    address = simpledialog.askstring("Input", "Enter Address:")
    
    if name and phone:
        contacts[name] = {"Phone": phone, "Email": email, "Address": address}
        messagebox.showinfo("Success", f"Contact {name} added successfully!")
    else:
        messagebox.showerror("Error", "Name and Phone are required!")

# Function to view all contacts
def view_contacts():
    contact_list.delete(0, tk.END)
    for name, details in contacts.items():
        contact_list.insert(tk.END, f"{name} - {details['Phone']}")

# Function to search for a contact
def search_contact():
    query = simpledialog.askstring("Search", "Enter Name or Phone Number:")
    contact_list.delete(0, tk.END)
    
    found = False
    for name, details in contacts.items():
        if query.lower() in name.lower() or query == details["Phone"]:
            contact_list.insert(tk.END, f"{name} - {details['Phone']}")
            found = True
    
    if not found:
        messagebox.showinfo("Not Found", "No matching contact found.")

# Function to update a contact
def update_contact():
    name = simpledialog.askstring("Update", "Enter the contact name to update:")
    if name in contacts:
        phone = simpledialog.askstring("Update", "Enter new Phone Number:", initialvalue=contacts[name]["Phone"])
        email = simpledialog.askstring("Update", "Enter new Email:", initialvalue=contacts[name]["Email"])
        address = simpledialog.askstring("Update", "Enter new Address:", initialvalue=contacts[name]["Address"])
        
        contacts[name] = {"Phone": phone, "Email": email, "Address": address}
        messagebox.showinfo("Success", f"Contact {name} updated successfully!")
        view_contacts()
    else:
        messagebox.showerror("Error", "Contact not found!")

# Function to delete a contact
def delete_contact():
    name = simpledialog.askstring("Delete", "Enter the contact name to delete:")
    if name in contacts:
        del contacts[name]
        messagebox.showinfo("Success", f"Contact {name} deleted successfully!")
        view_contacts()
    else:
        messagebox.showerror("Error", "Contact not found!")

# Function to exit the application
def exit_app():
    root.destroy()

# GUI Window
root = tk.Tk()
root.title("Contact Manager")
root.geometry("400x400")

# Buttons
tk.Button(root, text="Add Contact", command=add_contact, width=20).pack(pady=5)
tk.Button(root, text="View Contacts", command=view_contacts, width=20).pack(pady=5)
tk.Button(root, text="Search Contact", command=search_contact, width=20).pack(pady=5)
tk.Button(root, text="Update Contact", command=update_contact, width=20).pack(pady=5)
tk.Button(root, text="Delete Contact", command=delete_contact, width=20).pack(pady=5)
tk.Button(root, text="Exit", command=exit_app, width=20).pack(pady=5)

# Listbox to display contacts
contact_list = tk.Listbox(root, width=50, height=10)
contact_list.pack(pady=10)

# Run the application
root.mainloop()
