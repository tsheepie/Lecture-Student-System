from tkinter import *
from Student.dashboard import StudentDashboard
from DataHandler import DatabaseInteraction
from tkinter import messagebox

dbObj = DatabaseInteraction("BCData.db")

class LoginForm:
    def __init__(self, master):
        self.master = master
        self.master.title("Student Login")
        self.master.geometry('400x300')

        # Variables
        self.student_id_var = StringVar()
        self.password_var = StringVar()

        # Create form
        self.create_form()

    def create_form(self):
        # Title
        Label(self.master, text="STUDENT LOGIN", font=('Arial', 16, 'bold')).pack(pady=20)

        # Student ID
        Label(self.master, text="Student ID:").pack(pady=5)
        Entry(self.master, textvariable=self.student_id_var).pack(pady=5)

        # Password
        Label(self.master, text="Password:").pack(pady=5)
        Entry(self.master, textvariable=self.password_var, show="*").pack(pady=5)

        # Login Button
        Button(self.master, text="Login", command=self.login).pack(pady=20)

    def login(self):
        try:
            # Get input from GUI fields
            stu_username = int(self.student_id_var.get())  # Convert stu to int before passing
            password = self.password_var.get()

            # Call to dbObj to validate credentials
            logVali = dbObj.stuLogin(stu_username, password)

            if logVali == "Welcome":  # If login is successful
                self.master.destroy()  # Close the login window

                messagebox.showinfo("Welcome", "Welcome to the student dashboard where you can view your marks and edit your courses")
                # Open Lecturer Dashboard
                dashbrd_master = Tk()
                StudentDashboard(dashbrd_master, stu_username)
                dashbrd_master.mainloop()
                return stu_username
            else:
                messagebox.showerror("Login Failed", "Invalid username or password!")

        except ValueError:
            messagebox.showerror("Login Error", "Student Number must be a number!")