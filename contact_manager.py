import tkinter as tk
from tkinter import messagebox
class ContactManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.config(bg = "#ecf0f1")
        self.root.title("Contact Manager")
        self.root.geometry("300x300+700+300")
        self.contacts = []

        # UI elements
        self.label = tk.Label(root, text="Contact Manager", font=("system", 20), bg="#2ecc71", fg="#000", pady=10)
        self.label.pack(fill=tk.X,pady=(0,25))

        self.add_button = tk.Button(root,font = ("system 8 bold"), text="Add Contact",width= 24, command=self.add_contact, bg="#2ecc71", fg="#fff", padx=10, pady=10,cursor="hand2")
        self.add_button.pack(pady=5)

        self.view_button = tk.Button(root,font = ("system 8 bold"), text="View Contact List",width= 24, command=self.view_contacts, bg="#2ecc71", fg="#fff", padx=10, pady=10,cursor="hand2")
        self.view_button.pack(pady=5)

        self.view_button = tk.Button(root,font = ("system 8 bold"), text="Search Contact",width= 24, command=self.search_contact_popup, bg="#2ecc71", fg="#fff", padx=10, pady=10,cursor="hand2")
        self.view_button.pack(pady=5)

    def add_contact(self):
        add_window = tk.Toplevel(self.root)
        add_window.title("Add Contact")
        add_window.geometry("300x300+750+300")
        add_window.config(bg = "#ecf0f1")
        txt_font = ("system 8 bold")
        # Add Contact UI elements
        tk.Label(add_window,font=txt_font, text="Name   : ",justify="left",width=12,relief="solid",bg = "#2ecc71",fg = "white",pady=3).grid(row=0, column=0, padx=2, pady=16)
        tk.Label(add_window,font = txt_font, text="Number : ",justify="left",width=12,relief="solid",bg = "#2ecc71",fg = "white",pady = 3).grid(row=1, column=0, padx=2, pady=16)
        tk.Label(add_window,font = txt_font, text="Email  : ",justify="left",width=12,relief="solid",bg = "#2ecc71",fg = "white",pady = 3).grid(row=2, column=0, padx=2, pady=16)
        tk.Label(add_window,font = txt_font, text="Address: ",justify="left",width=12,relief="solid",bg = "#2ecc71",fg = "white",pady = 3).grid(row=3, column=0, padx=2, pady=16)

        name_entry = tk.Entry(add_window)
        phone_entry = tk.Entry(add_window)
        email_entry = tk.Entry(add_window)
        address_entry = tk.Entry(add_window)

        name_entry.grid(row=0, column=1, padx=10, pady=10)
        phone_entry.grid(row=1, column=1, padx=10, pady=10)
        email_entry.grid(row=2, column=1, padx=10, pady=10)
        address_entry.grid(row=3, column=1, padx=10, pady=10)
        
        save_button = tk.Button(add_window, text="Save", command=lambda: self.save_contact(
            name_entry.get(),
            phone_entry.get(),
            email_entry.get(),
            address_entry.get(),
            add_window
        ), bg="#2ecc71", fg="white", padx=10, pady=5)
        save_button.grid(row=4, column=0, columnspan=2, pady=10)


    def save_contact(self, name, phone, email, address, window):
        if name and phone:
            contact = {
                "Name": name,
                "Phone": phone,
                "Email": email,
                "Address": address
            }
            self.contacts.append(contact)
            window.destroy()
        else:
            messagebox.showerror("Error", "Name and Phone Number cannot be Empty.")
    def view_contacts(self):
        view_window = tk.Toplevel(self.root)
        view_window.geometry("400x600")
        view_window.geometry("350x400+750+300")
        view_window.title("Contact List")

        if not self.contacts:
            tk.Label(view_window, text="No contacts available.", pady=10).pack()
        else:
            for i, contact in enumerate(self.contacts):
                contact_info = self.Contact_Information(str(i+1),contact['Name'],contact['Phone'],20,6)
                tk.Label(view_window,font = "system 8 bold", text=contact_info,bg="#2ecc71",fg="#fff", pady=5,relief="solid",justify="left").pack(fill="x",pady=1)

            update_button = tk.Button(view_window,font = "system 8 bold", text="Update Contact",width=20, command= lambda:self.update_contact(view_window), bg="#2ecc71", fg="white", padx=10, pady=5)
            update_button.pack(pady=5)

            delete_button = tk.Button(view_window,font = "system 8 bold", text="Delete Contact",width=20, command= lambda :self.delete_contact(view_window), bg="#2ecc71", fg="white", padx=10, pady=5)
            delete_button.pack(pady=5)
    def Contact_Information(self,ID,name,number, leftWidth, rightWidth):
        contact_info = ('Contact Number: '+ID+" ").center(leftWidth + rightWidth, "-") 
        contact_info +=("\n" + "Name ".ljust(leftWidth, '-') + name.rjust(rightWidth) +'\n')
        contact_info +=("Phone ".ljust(leftWidth, '-') + number.rjust(rightWidth) +'\n')
        return contact_info

    def search_contact_popup(self):
        search_window = tk.Toplevel(self.root)
        search_window.title("Search Contact")
        search_window.geometry("300x200+700+300")

        tk.Label(search_window, text="Enter Name or Phone Number to Search: ").pack(pady=10)
        search_entry = tk.Entry(search_window)
        search_entry.pack(pady=10)

        search_button = tk.Button(search_window, text="Search", command=lambda: self.search_contact(search_entry.get()), bg="#2ecc71", fg="white", padx=10, pady=5)
        search_button.pack(pady=10)


    def search_contact(self,query):
        view_window = tk.Toplevel(self.root)
        view_window.geometry("400x600+730+300")
        view_window.title("Contact List")

        if not query:
            messagebox.showerror("Error", "Please enter a name or phone number to search.")
            return
        search_results = []
        for contact in self.contacts:
            if query.lower() in contact['Name'].lower() or query in contact['Phone']:
                search_results.append(contact)
        if not search_results:
            messagebox.showinfo("Search Results", "No contacts found.")
        
        for i, result in enumerate(search_results):
            contact_info = self.Contact_Information(str(i+1),result['Name'],result['Phone'],20,6)
            if result["Address"]:
                contact_info += "Address".ljust(20, '-') + (result["Address"]).rjust(8) +"\n"
            if result["Email"]:
                contact_info += "Email".ljust(20, '-') + (result["Email"]).rjust(8)
            tk.Label(view_window,font = "system 8 bold", text=contact_info,bg="#2ecc71",fg="#fff", pady=5,relief="solid",justify="left").pack(fill="x",pady=1)
    def update_contact(self,view_screen):
        update_window = tk.Toplevel(self.root)
        update_window.title("Update Contact")
        update_window.geometry("300x200+700+300")

        tk.Label(update_window, text="Enter Contact Number to Update: ").pack(pady=10)
        contact_num_entry = tk.Entry(update_window)
        contact_num_entry.pack(pady=10)
        
        update_button = tk.Button(update_window, text="Update", command=lambda: self.open_update_window((contact_num_entry.get()),update_window,view_screen), bg="#2ecc71", fg="white", padx=10, pady=5)
        update_button.pack(pady=10)

    def open_update_window(self, contact_index,update_screen,view_screen):
        try:
            contact_index = int(contact_index) - 1
            if 0 <= contact_index < len(self.contacts):
                update_window = tk.Toplevel(self.root)
                update_window.title("Update Contact")
                update_window.geometry("380x250+750+300")

                tk.Label(update_window,width=20, text="Name: ",fg="#fff",font= "system 8 bold",justify="left",relief="solid",bg="#2ecc71").grid(row=0, column=0, padx=10, pady=10)
                tk.Label(update_window,width=20, text="Phone Number: ",fg="#fff",font= "system 8 bold",justify="left",relief="solid",bg="#2ecc71").grid(row=1, column=0, padx=10, pady=10)
                tk.Label(update_window,width=20, text="Email: ",fg="#fff",font= "system 8 bold",justify="left",relief="solid",bg="#2ecc71").grid(row=2, column=0, padx=10, pady=10)
                tk.Label(update_window,width=20, text="Address: ",fg="#fff",font= "system 8 bold",justify="left",relief="solid",bg="#2ecc71").grid(row=3, column=0, padx=10, pady=10)

                information = self.contacts[contact_index]
                name_entry = tk.Entry(update_window)
                phone_entry = tk.Entry(update_window)
                email_entry = tk.Entry(update_window)
                address_entry = tk.Entry(update_window)

                name_entry.insert(0,information["Name"])
                phone_entry.insert(0,information["Phone"])
                email_entry.insert(0,information["Email"])
                address_entry.insert(0,information["Address"])

                name_entry.grid(row=0, column=1, padx=10, pady=10)
                phone_entry.grid(row=1, column=1, padx=10, pady=10)
                email_entry.grid(row=2, column=1, padx=10, pady=10)
                address_entry.grid(row=3, column=1, padx=10, pady=10)

                save_button = tk.Button(update_window, text="Save", command=lambda: self.save_updated_contact(
                    contact_index,
                    name_entry.get(),
                    phone_entry.get(),
                    email_entry.get(),
                    address_entry.get(),
                    update_window
                ), bg="#2ecc71", fg="white", padx=10, pady=5)
                save_button.grid(row=4, column=0, columnspan=2, pady=10)
                update_screen.destroy()
                view_screen.destroy()


        except:
            messagebox.showerror("Error", "Invalid contact number.")

    def save_updated_contact(self, contact_index, name, phone, email, address, window):
        self.contacts[contact_index] = {
            "Name": name,
            "Phone": phone,
            "Email": email,
            "Address": address
        }
        window.destroy()
        
    def delete_contact(self,view_screen):
        delete_window = tk.Toplevel(self.root)
        delete_window.title("Delete Contact")
        delete_window.geometry("300x200+700+300")

        tk.Label(delete_window, text="Enter Contact Number to Delete: ").pack(pady=10)
        contact_num_entry = tk.Entry(delete_window)
        contact_num_entry.pack(pady=10)

        delete_button = tk.Button(delete_window, text="Delete", command=lambda: self.delete_selected_contact(int(contact_num_entry.get()) - 1,delete_window,view_screen), bg="#2ecc71", fg="white", padx=10, pady=5)
        delete_button.pack(pady=10)

    def delete_selected_contact(self, contact_index,delete_screen , view_screen):
        if 0 <= contact_index < len(self.contacts,):
            del self.contacts[contact_index]
            view_screen.destroy()
            delete_screen.destroy()
        else:
            messagebox.showerror("Error", "Invalid contact number.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactManagerApp(root)
    root.mainloop()
