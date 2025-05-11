from tkinter import *
from tkinter import messagebox
from Administration.Admin_Window import AdminWindow  # Importing the new AdminWindow class
from DataHandler import DatabaseInteraction # Importing db functions

dbObj = DatabaseInteraction("BCData.db")

class LecLoginForm:
    def __init__(self, master):
        self.master = master
        self.master.title("Lecturer Login")
        self.master.geometry('400x300')

        # Variables
        self.lecturer_username_var = StringVar()
        self.password_var = StringVar()

        # Create form
        self.create_form()

    def create_form(self):
        # Title
        Label(self.master, text="LECTURER LOGIN", font=('Arial', 16, 'bold')).pack(pady=20)

        # Lecturer Username
        Label(self.master, text="Lecturer Username:").pack(pady=5)
        Entry(self.master, textvariable=self.lecturer_username_var).pack(pady=5)

        # Password
        Label(self.master, text="Password:").pack(pady=5)
        Entry(self.master, textvariable=self.password_var, show="*").pack(pady=5)

        # Login Button
        Button(self.master, text="Login", command=self.login).pack(pady=20)

    def login(self):
        try:
            # Get input from GUI fields
            lecturer_username = int(self.lecturer_username_var.get())  # Convert stu to int before passing
            password = self.password_var.get()

            # Call to dbObj to validate credentials
            logVali = dbObj.lecLogin(lecturer_username, password)

            if logVali == "Welcome":  # If login is successful
                self.master.destroy()  # Close the login window

                messagebox.showinfo("Welcome", "Welcome to the Lecturer dashboard where you can view and edit student details")
                # Open Lecturer Dashboard
                admin_master = Tk()
                AdminWindow(admin_master, lecturer_username)  # Launch the AdminWindow (Lecturer Dashboard)
                admin_master.mainloop()
            else:
                messagebox.showerror("Login Failed", "Invalid username or password!")

        except ValueError:
            messagebox.showerror("Login Error", "Lecturer Number must be a number!")
