from tkinter import *
from tkinter import ttk, messagebox
import re
from DataHandler import DatabaseInteraction

dbObj = DatabaseInteraction("BCData.db")


class StudentDashboard:
    def __init__(self, window, iStuNum):
        self.window = window
        self.window.title("STUDENT DASHBOARD")
        self.window.geometry('1000x600')

        # Create main frame
        self.main_frame = Frame(window)
        self.main_frame.pack(fill=BOTH, expand=True, padx=20, pady=20)

        # Title
        title = Label(self.main_frame, text="STUDENT DASHBOARD", font=('Arial', 20, 'bold'))
        title.pack(pady=20)

        # Buttons frame
        self.button_frame = Frame(self.main_frame)
        self.button_frame.pack(pady=20)

        # Create buttons
        self.create_buttons()

        # Create table frame
        self.table_frame = Frame(self.main_frame)
        self.table_frame.pack(fill=BOTH, expand=True)

        # Initially hide all frames
        self.marks_frame = None
        self.add_module_frame = None
        self.update_frame = None

        # Store student number
        self.StuNum = int(iStuNum)

        # Variables for storing form data
        self.fname_var = StringVar()
        self.lname_var = StringVar()
        self.email_var = StringVar()
        self.mobile_var = StringVar()
        self.address_var = StringVar()
        self.password_var = StringVar()
        self.day = StringVar()
        self.month = StringVar()
        self.year = StringVar()

    def create_buttons(self):
        # View Marks Button
        view_btn = Button(self.button_frame, text="View Marks", command=self.show_marks,
                          width=15, height=2, bg='#4CAF50', fg='white')
        view_btn.pack(side=LEFT, padx=10)

        # Update Info Button
        update_btn = Button(self.button_frame, text="Update Information", command=self.update_info,
                            width=15, height=2, bg='#FFC107', fg='black')
        update_btn.pack(side=LEFT, padx=10)

        # Delete Module Button
        delete_btn = Button(self.button_frame, text="Delete Module", command=self.delete_module,
                            width=15, height=2, bg='#f44336', fg='white')
        delete_btn.pack(side=LEFT, padx=10)

        # Logout Button
        logout_btn = Button(self.button_frame, text="Logout", command=self.logout,
                            width=15, height=2, bg='#FF5733', fg='white')
        logout_btn.pack(side=LEFT, padx=10)

    def logout(self):
        confirm = messagebox.askyesno("Confirm Logout", "Are you sure you want to log out?")
        if confirm:
            self.window.destroy()

    def show_marks(self):
        # Clear any existing frames
        self.clear_frames()

        # Create marks frame
        self.marks_frame = Frame(self.table_frame)
        self.marks_frame.pack(fill=BOTH, expand=True)

        # Create Treeview
        columns = ('Student Number', 'Student Name', 'Student Surname', 'Module Code', 'Module Name', 'Marks')
        tree = ttk.Treeview(self.marks_frame, columns=columns, show='headings')

        # Set column headings
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=150)

        try:
            # Fetch and display student data
            display = dbObj.search(self.StuNum)

            if display:
                messagebox.showinfo("Success", f"Student {self.StuNum} here are your details!")
                for record in display:
                    tree.insert('', END, values=record)
            else:
                messagebox.showinfo("Error", f"Student {self.StuNum} your info is missing, please contact Admin team!")

        except ValueError:
            messagebox.showerror("Error", "Student Number must be an integer!")

        # Add scrollbar
        scrollbar = ttk.Scrollbar(self.marks_frame, orient=VERTICAL, command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)

        # Pack the treeview and scrollbar
        tree.pack(side=LEFT, fill=BOTH, expand=True)
        scrollbar.pack(side=RIGHT, fill=Y)

    def update_info(self):
        # Clear any existing frames
        self.clear_frames()

        # Create update frame
        self.update_frame = Frame(self.table_frame)
        self.update_frame.pack(fill=BOTH, expand=True, pady=20)

        # Title
        Label(self.update_frame, text="Update Information", font=('Arial', 14, 'bold')).pack(pady=10)

        # Create form fields
        self.create_form_field("FIRST NAME", self.fname_var)
        self.create_form_field("LAST NAME", self.lname_var)

        # Date of birth fields
        dob_frame = Frame(self.update_frame)
        dob_frame.pack(fill=X, padx=20, pady=5)
        Label(dob_frame, text="DATE OF BIRTH").pack(side=LEFT)

        day_cb = ttk.Combobox(dob_frame, width=3, textvariable=self.day)
        day_cb['values'] = tuple(str(i).zfill(2) for i in range(1, 32))
        day_cb.pack(side=LEFT, padx=5)

        month_cb = ttk.Combobox(dob_frame, width=10, textvariable=self.month)
        month_cb['values'] = ('January', 'February', 'March', 'April', 'May', 'June',
                              'July', 'August', 'September', 'October', 'November', 'December')
        month_cb.pack(side=LEFT, padx=5)

        year_cb = ttk.Combobox(dob_frame, width=5, textvariable=self.year)
        year_cb['values'] = tuple(range(1990, 2023))
        year_cb.pack(side=LEFT, padx=5)

        self.create_form_field("EMAIL ID", self.email_var)
        self.create_form_field("MOBILE NUMBER", self.mobile_var)
        self.create_form_field("ADDRESS", self.address_var)
        self.create_form_field("PASSWORD", self.password_var, show="*")

        # Buttons frame
        button_frame = Frame(self.update_frame)
        button_frame.pack(pady=20)

        Button(button_frame, text="Update Info", command=self.submit_info,
               bg='#4CAF50', fg='white').pack(side=LEFT, padx=10)
        Button(button_frame, text="Clear Input", command=self.reset_form,
               bg='#f44336', fg='white').pack(side=LEFT, padx=10)

    def create_form_field(self, label_text, variable, show=None):
        frame = Frame(self.update_frame)
        frame.pack(fill=X, padx=20, pady=5)
        Label(frame, text=label_text).pack(side=LEFT)
        Entry(frame, textvariable=variable, show=show).pack(side=LEFT, padx=5)

    def validate_mobile(self, mobile):
        if mobile:
            return len(mobile) == 10 and mobile.isdigit()
        return True

    def validate_email(self, email):
        if email:
            pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
            return re.match(pattern, email)
        return True

    def validate_password(self, password):
        if password:
            return len(password) == 6
        return True

    def submit_info(self):
        check = dbObj.fetchStuData(self.StuNum)

        # Get existing data
        for i in check:
            sName, sSurname = i[1], i[2]
            DOB = i[3]
            sEmail, iPhone = i[4], i[5]
            sAddress = i[7]
            sPassword = i[8]

        # Update with new values if provided
        if self.fname_var.get().strip():
            sName = self.fname_var.get().strip()
        if self.lname_var.get().strip():
            sSurname = self.lname_var.get().strip()
        if all([self.day.get(), self.month.get(), self.year.get()]):
            DOB = f"{self.year.get()}-{self.month.get()}-{self.day.get()}"
        if self.email_var.get().strip():
            sEmail = self.email_var.get().strip()
        if self.mobile_var.get().strip():
            iPhone = self.mobile_var.get().strip()
        if self.address_var.get().strip():
            sAddress = self.address_var.get().strip()
        if self.password_var.get().strip():
            sPassword = self.password_var.get().strip()

        # Validate inputs
        if not self.validate_email(sEmail):
            messagebox.showerror("Error", "Invalid email format!")
            return
        if not self.validate_mobile(iPhone):
            messagebox.showerror("Error", "Mobile number must be 10 digits!")
            return
        if not self.validate_password(sPassword):
            messagebox.showerror("Error", "Password must be 6 characters!")
            return

        # Update database
        dbObj.updateStuData(sName, sSurname, DOB, sEmail, iPhone, sAddress, sPassword, self.StuNum)
        messagebox.showinfo("Success", "Information updated successfully!")
        self.reset_form()

    def reset_form(self):
        # Clear all form fields
        for var in [self.fname_var, self.lname_var, self.email_var, self.mobile_var,
                    self.address_var, self.password_var, self.day, self.month, self.year]:
            var.set("")

    def delete_module(self):
        messagebox.showwarning("Delete Module",
                               "Please contact the administration office to delete modules.\n\n" +
                               "Email: admin@university.com\nPhone: (123) 456-7890")

    def clear_frames(self):
        # Clear any existing frames in table_frame
        if self.marks_frame:
            self.marks_frame.destroy()
        if self.update_frame:
            self.update_frame.destroy()


def main():
    window = Tk()
    dashboard = StudentDashboard(window, "12345")  # Example student number
    window.mainloop()


if __name__ == "__main__":
    main()