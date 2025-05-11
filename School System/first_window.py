from tkinter import *
from Student.second_window import SecondWindow
from Administration.Lecturer_Login import LecLoginForm


class FirstWindow:

    def __init__(self, master):
        self.master = master
        self.master.title("WELCOME TO BELGIUM CAMPUS STUDENT & LECTURER MANAGEMENT SYSTEM")
        self.master.geometry('400x300')


        self.create_form()

    def create_form(self):
        Label(self.master, text="Please select what you are logging in as:" , font =('Arial', 16, 'bold' )).pack(pady=20)

        Button(self.master, text="Lecturer", command=self.lecturer).pack(pady=20) #button for lecturer login
        Button(self.master, text="Student", command=self.student).pack(pady=20)

    def student(self):
        self.master.destroy()

        sec_master = Tk()
        SecondWindow(sec_master)
        sec_master.mainloop()

    def lecturer(self):
        self.master.destroy()

        lec_master = Tk()
        LecLoginForm(lec_master)
        lec_master.mainloop()
