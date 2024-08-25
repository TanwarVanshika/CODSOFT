from tkinter import *
from tkinter import messagebox, simpledialog
import os

# Function to add a task to the list
def add_task():
    task = task_entry.get()
    if task != "":
        task_listbox.insert(END, task)
        task_entry.delete(0, END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

# Function to delete the selected task from the list
def delete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
    except:
        messagebox.showwarning("Warning", "You must select a task.")

# Function to edit the selected task
def edit_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task = task_listbox.get(selected_task_index)
        new_task = simpledialog.askstring("Edit Task", "Edit the task:", initialvalue=task)
        if new_task:
            task_listbox.delete(selected_task_index)
            task_listbox.insert(selected_task_index, new_task)
    except:
        messagebox.showwarning("Warning", "You must select a task.")

# Function to mark the selected task as completed
def mark_task_completed():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task = task_listbox.get(selected_task_index)
        if "(Completed)" not in task:
            task_listbox.delete(selected_task_index)
            task_listbox.insert(END, task + " (Completed)")
        else:
            messagebox.showinfo("Info", "Task is already marked as completed.")
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task.")

# Function to save tasks to a file
def save_tasks():
    tasks = task_listbox.get(0, END)
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")
    messagebox.showinfo("Info", "Tasks saved successfully.")

# Function to load tasks from a file
def load_tasks():
    if os.path.exists("tasks.txt"):
        with open("tasks.txt","r") as file:
            tasks = file.readlines()
            for task in tasks:
                task_listbox.insert(END, task.strip())

# Create the main window
root = Tk()
root.title("To-Do List")
root.geometry("400x400")
root.configure(bg="#f0f0f0")

#Add a title label
title_label = Label(root, text="My To-Do List", font=("Helvetica", 18, "bold"), bg="#f0f0f0", fg="#333")
title_label.pack(pady=10)

# Add an entry box to input new tasks
task_entry = Entry(root, width=50, font=("Helvetica", 12), bg="#fff", fg="#333")
task_entry.pack(pady=10)

# Add a listbox to display tasks
task_listbox = Listbox(root, width=50, height=10)
task_listbox.pack(pady=10)

# Add buttons for various functionalities
button_frame = Frame(root, bg="#f0f0f0")
button_frame.pack(pady=10)

add_button = Button(button_frame, text="Add Task", command=add_task, font=("Helvetica", 12), bg="#4caf50", fg="#fff", padx=10, pady=5)
add_button.pack(side=LEFT, padx=5)

delete_button = Button(button_frame, text="Delete Task", command=delete_task, font=("Helvetica", 12), bg="#f44336", fg="#fff", padx=10, pady=5)
delete_button.pack(side=LEFT, padx=5)

edit_button = Button(button_frame, text="Edit Task", command=edit_task, font=("Helvetica", 12), bg="#ff9800", fg="#fff", padx=10, pady=5)
edit_button.pack(side=LEFT, padx=5)

complete_button = Button(root, text="Mark as Completed", command=mark_task_completed, font=("Helvetica", 12), bg="#2196f3", fg="#fff", padx=10, pady=5)
complete_button.pack(side=LEFT, padx=5)

save_button = Button(root, text="Save Tasks", command=save_tasks, font=("Helvetica", 12), bg="#9c27b0", fg="#fff", padx=10, pady=5)
save_button.pack(side=LEFT, padx=5)

load_button = Button(root, text="Load Tasks", command=load_tasks, font=("Helvetica", 12), bg="#009688", fg="#fff", padx=10, pady=5)
load_button.pack(side=LEFT, padx=5)

# Load tasks when the application starts
load_tasks()

# Run the application
root.mainloop()
