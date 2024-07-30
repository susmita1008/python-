import tkinter as tk
from tkinter import messagebox, simpledialog

class ContactBook:
    def _init_(self, root):
        self.root = root
        self.root.title("Contact Book")
        
        self.contacts = {}

        # Frames
        self.frame = tk.Frame(self.root)
        self.frame.pack(padx=10, pady=10)

        # Labels and Entries
        self.name_label = tk.Label(self.frame, text="Name")
        self.name_label.grid(row=0, column=0)
        self.name_entry = tk.Entry(self.frame)
        self.name_entry.grid(row=0, column=1)

        self.phone_label = tk.Label(self.frame, text="Phone")
        self.phone_label.grid(row=1, column=0)
        self.phone_entry = tk.Entry(self.frame)
        self.phone_entry.grid(row=1, column=1)

        self.email_label = tk.Label(self.frame, text="Email")
        self.email_label.grid(row=2, column=0)
        self.email_entry = tk.Entry(self.frame)
        self.email_entry.grid(row=2, column=1)

        self.address_label = tk.Label(self.frame, text="Address")
        self.address_label.grid(row=3, column=0)
        self.address_entry = tk.Entry(self.frame)
        self.address_entry.grid(row=3, column=1)

        # Buttons
        self.add_button = tk.Button(self.frame, text="Add Contact", command=self.add_contact)
        self.add_button.grid(row=4, column=0, pady=5)

        self.view_button = tk.Button(self.frame, text="View Contacts", command=self.view_contacts)
        self.view_button.grid(row=4, column=1, pady=5)

        self.search_button = tk.Button(self.frame, text="Search Contact", command=self.search_contact)
        self.search_button.grid(row=5, column=0, pady=5)

        self.update_button = tk.Button(self.frame, text="Update Contact", command=self.update_contact)
        self.update_button.grid(row=5, column=1, pady=5)

        self.delete_button = tk.Button(self.frame, text="Delete Contact", command=self.delete_contact)
        self.delete_button.grid(row=6, column=0, pady=5)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        if name and phone:
            self.contacts[phone] = {"name": name, "email": email, "address": address}
            messagebox.showinfo("Success", "Contact added successfully!")
        else:
            messagebox.showerror("Error", "Name and phone number are required.")

    def view_contacts(self):
        contacts_str = "\n".join([f"{v['name']} - {k}" for k, v in self.contacts.items()])
        messagebox.showinfo("Contact List", contacts_str if contacts_str else "No contacts available.")

    def search_contact(self):
        search_term = simpledialog.askstring("Search", "Enter name or phone number:")
        if search_term:
            found_contacts = [f"{v['name']} - {k}" for k, v in self.contacts.items() if search_term in k or search_term.lower() in v['name'].lower()]
            messagebox.showinfo("Search Results", "\n".join(found_contacts) if found_contacts else "No contacts found.")

    def update_contact(self):
        phone = simpledialog.askstring("Update", "Enter phone number of contact to update:")
        if phone in self.contacts:
            name = simpledialog.askstring("Update", "Enter new name:")
            email = simpledialog.askstring("Update", "Enter new email:")
            address = simpledialog.askstring("Update", "Enter new address:")
            self.contacts[phone] = {"name": name, "email": email, "address": address}
            messagebox.showinfo("Success", "Contact updated successfully!")
        else:
            messagebox.showerror("Error", "Contact not found.")

    def delete_contact(self):
        phone = simpledialog.askstring("Delete", "Enter phone number of contact to delete:")
        if phone in self.contacts:
            del self.contacts[phone]
            messagebox.showinfo("Success", "Contact deleted successfully!")
        else:
            messagebox.showerror("Error", "Contact not found.")

if __name__ == "__main__":
    root = tk.Tk()

    root.mainloop()