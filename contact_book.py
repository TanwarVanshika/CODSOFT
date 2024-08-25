import tkinter as tk
from tkinter import messagebox, simpledialog
from PIL import Image, ImageTk, ImageEnhance

class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactBookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        self.root.geometry("330x600")  # Increased length
        self.contacts = []

        self.create_widgets()

    def create_widgets(self):
        # Load and adjust background image transparency
        self.bg_image = Image.open("background.jpg")
        self.bg_image = self.bg_image.resize((500, 600), Image.LANCZOS)
        enhancer = ImageEnhance.Brightness(self.bg_image)
        self.bg_image = enhancer.enhance(0.3)  # Adjust transparency (0.0 to 1.0)
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)

        self.bg_label = tk.Label(self.root, image=self.bg_photo)
        self.bg_label.place(relwidth=1, relheight=1)

        # Styling
        label_font = ("Helvetica", 12, "bold")
        entry_font = ("Helvetica", 12)
        button_font = ("Helvetica", 12, "bold")

        # Name
        self.name_label = tk.Label(self.root, text="Name", font=label_font, bg="#f0f0f0")
        self.name_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.name_entry = tk.Entry(self.root, font=entry_font)
        self.name_entry.grid(row=0, column=1, padx=10, pady=10)

        # Phone
        self.phone_label = tk.Label(self.root, text="Phone", font=label_font, bg="#f0f0f0")
        self.phone_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.phone_entry = tk.Entry(self.root, font=entry_font)
        self.phone_entry.grid(row=1, column=1, padx=10, pady=10)

        # Email
        self.email_label = tk.Label(self.root, text="Email", font=label_font, bg="#f0f0f0")
        self.email_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.email_entry = tk.Entry(self.root, font=entry_font)
        self.email_entry.grid(row=2, column=1, padx=10, pady=10)

        # Address
        self.address_label = tk.Label(self.root, text="Address", font=label_font, bg="#f0f0f0")
        self.address_label.grid(row=3, column=0, padx=10, pady=10, sticky="w")
        self.address_entry = tk.Entry(self.root, font=entry_font)
        self.address_entry.grid(row=3, column=1, padx=10, pady=10)

        # Buttons
        self.add_button = tk.Button(self.root, text="Add Contact", font=button_font, bg="#4CAF50", fg="white", command=self.add_contact)
        self.add_button.grid(row=4, column=0, columnspan=2, pady=10, ipadx=10)

        self.view_button = tk.Button(self.root, text="View Contacts", font=button_font, bg="#2196F3", fg="white", command=self.view_contacts)
        self.view_button.grid(row=5, column=0, columnspan=2, pady=10, ipadx=10)

        self.search_button = tk.Button(self.root, text="Search Contact", font=button_font, bg="#FF9800", fg="white", command=self.search_contact)
        self.search_button.grid(row=6, column=0, columnspan=2, pady=10, ipadx=10)

        self.update_button = tk.Button(self.root, text="Update Contact", font=button_font, bg="#FFC107", fg="white", command=self.update_contact)
        self.update_button.grid(row=7, column=0, columnspan=2, pady=10, ipadx=10)

        self.delete_button = tk.Button(self.root, text="Delete Contact", font=button_font, bg="#F44336", fg="white", command=self.delete_contact)
        self.delete_button.grid(row=8, column=0, columnspan=2, pady=10, ipadx=10)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()
        contact = Contact(name, phone, email, address)
        self.contacts.append(contact)
        messagebox.showinfo("Success", "Contact added successfully!")

    def view_contacts(self):
        contacts_str = "\n".join([f"Name: {c.name}, Phone: {c.phone}" for c in self.contacts])
        messagebox.showinfo("Contacts", contacts_str)

    def search_contact(self):
        search_term = simpledialog.askstring("Search Contact", "Enter name or phone to search:")
        if search_term:
            results = [c for c in self.contacts if search_term.lower() in c.name.lower() or search_term in c.phone]
            if results:
                contacts_str = "\n".join([f"Name: {c.name}, Phone: {c.phone}, Email: {c.email}, Address: {c.address}" for c in results])
                messagebox.showinfo("Search Results", contacts_str)
            else:
                messagebox.showinfo("Search Results", "No contacts found.")

    def update_contact(self):
        name = simpledialog.askstring("Update Contact", "Enter the name of the contact to update:")
        if name:
            for contact in self.contacts:
                if contact.name.lower() == name.lower():
                    new_name = simpledialog.askstring("Update Contact", "Enter new name:", initialvalue=contact.name)
                    new_phone = simpledialog.askstring("Update Contact", "Enter new phone:", initialvalue=contact.phone)
                    new_email = simpledialog.askstring("Update Contact", "Enter new email:", initialvalue=contact.email)
                    new_address = simpledialog.askstring("Update Contact", "Enter new address:", initialvalue=contact.address)
                    contact.name = new_name
                    contact.phone = new_phone
                    contact.email = new_email
                    contact.address = new_address
                    messagebox.showinfo("Success", "Contact updated successfully!")
                    return
            messagebox.showinfo("Error", "Contact not found.")

    def delete_contact(self):
        name = simpledialog.askstring("Delete Contact", "Enter the name of the contact to delete:")
        if name:
            for i, contact in enumerate(self.contacts):
                if contact.name.lower() == name.lower():
                    del self.contacts[i]
                    messagebox.showinfo("Success", "Contact deleted successfully!")
                    return
            messagebox.showinfo("Error", "Contact not found.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBookApp(root)
    root.mainloop()
