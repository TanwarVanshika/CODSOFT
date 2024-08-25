from tkinter import *
from tkinter import ttk, messagebox
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def on_generate():
    try:
        length = int(entry_length.get())
        if length <= 0:
            raise ValueError("Length must be positive")
        password = generate_password(length)
        entry_password.delete(0, END)
        entry_password.insert(0, password)
    except ValueError as e:
        messagebox.showerror("Invalid Input", str(e))

def on_copy():
    root.clipboard_clear()
    root.clipboard_append(entry_password.get())
    messagebox.showinfo("Copied", "Password copied to clipboard!")

#Create the main window
root = Tk()
root.title("Password Generator")
root.geometry("400x250")
root.resizable(False, False)

#Apply theme
style = ttk.Style(root)
style.theme_use("clam")

#Create and place the widgets
frame = ttk.Frame(root, padding="10")
frame.pack(fill=BOTH, expand=True, pady=5)

#Create and place the widgets
label_length = ttk.Label(frame, text="Enter the desired length for the password: ")
label_length.pack(pady=10)

entry_length = ttk.Entry(frame, font=("Helvetica",12))
entry_length.pack(pady=5)

button_generate = ttk.Button(frame, text="Generate Password", command=on_generate, style="Custom.TButton")
button_generate.pack(pady=10)

separator = ttk.Frame(frame, height=15)
separator.pack()

entry_password = ttk.Entry(frame, width=50, font=("Helvetica",12))
entry_password.pack(pady=5)

button_copy = ttk.Button(frame, text="Copy Password", command=on_copy, style="Custom.TButton")
button_copy.pack(pady=10)

# Add some padding and styling
for widget in frame.winfo_children():
    widget.pack_configure(padx=5, pady=5)

# Custom styles
style.configure("TFrame", background="#333")
style.configure("TLabel", background="#333", foreground="#fff", font=("Helvetica", 12))
style.configure("TEntry", font=("Helvetica", 12))
style.configure("TButton", background="#555", foreground="#fff", font=("Helvetica", 11))

#Run the application
root.mainloop()
