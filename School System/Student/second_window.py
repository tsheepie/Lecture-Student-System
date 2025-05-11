from tkinter import *
from Student.student_registration import StudentRegistrationForm
from Student.student_login import LoginForm

from tkinter import ttk, messagebox
import re


class SecondWindow:

    def __init__(self, master):
        self.master = master
        self.master.title("WELCOME TO BELGIUM CAMPUS STUDENT!")
        self.master.geometry('400x300')

        self.create_form()

    def create_form(self):
        Label(self.master, text="Please select what you are logging in as:", font=('Arial', 16, 'bold')).pack(pady=20)

        Button(self.master, text="Existing Student", command=self.estudent).pack(pady=20)  # button for lecturer login
        Button(self.master, text="New Student", command=self.nstudent).pack(pady=20)

    def nstudent(self):
        self.master.destroy()

        reg_master = Tk()
        StudentRegistrationForm(reg_master)
        reg_master.mainloop()

    def estudent(self):
        self.master.destroy()

        log_master = Tk()
        LoginForm(log_master)
        log_master.mainloop()
