from tkinter import *
from tkinter import ttk, messagebox
from DataHandler import DatabaseInteraction

dbObj = DatabaseInteraction("BCData.db")

class AdminWindow :
    def __init__(self, window, lecNum):
        self.window = window
        self.window.title("LECTURER DASHBOARD")
        self.window.geometry('1000x600')

        # Create main frame
        self.main_frame = Frame(window)
        self.main_frame.pack(fill=BOTH, expand=True, padx=20, pady=20)

        # Title
        title = Label(self.main_frame, text="LECTURER DASHBOARD", font=('Arial', 20, 'bold'))
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
        self.edit_student_frame = None

        self.lecNum = int(lecNum)
        # collect input
        self.tStuName = StringVar()
        self.tStuSur = StringVar()
        self.tModCode = StringVar()
        self.tModName = StringVar()
        self.tStuNum = StringVar()
        self.tMarks = StringVar()

        #complete
    def create_buttons(self):
        # View Marks Button
        view_marks_btn = Button(self.button_frame, text="View Student Information", command=self.show_marks,
                                width=20, height=2, bg='#4CAF50', fg='white')
        view_marks_btn.pack(side=LEFT, padx=10)

        view_marks_btn = Button(self.button_frame, text="Add new Student", command=self.add_new,
                                width=20, height=2, bg='#4CAF50', fg='white')
        view_marks_btn.pack(side=LEFT, padx=10)

        search_btn = Button(self.button_frame, text="Search Student", command=self.search_student,
                                width=20, height=2, bg='#4CAF50', fg='white')
        search_btn.pack(side=LEFT, padx=10)

        # Add Module Button
        add_module_btn = Button(self.button_frame, text="Add Module", command=self.show_add_module,
                                width=20, height=2, bg='#2196F3', fg='white')
        add_module_btn.pack(side=LEFT, padx=10)

        show_module_btn = Button(self.button_frame, text="Show Module", command=self.show_module,
                                width=20, height=2, bg='#4CAF50', fg='white')
        show_module_btn.pack(side=LEFT, padx=10)



        # Edit Student Button
        edit_student_btn = Button(self.button_frame, text="Edit Student Info", command=self.show_edit_student,
                                  width=20, height=2, bg='#FFC107', fg='black')
        edit_student_btn.pack(side=LEFT, padx=10)

        # Delete Module Button
        delete_module_btn = Button(self.button_frame, text="Delete", command=self.delete_module,
                                   width=20, height=2, bg='#f44336', fg='white')
        delete_module_btn.pack(side=LEFT, padx=10)

    def show_marks(self):

        # Clear any existing frames
        self.clear_frames()

        # Create marks frame
        self.marks_frame = Frame(self.table_frame)
        self.marks_frame.pack(fill=BOTH, expand=True)

        # Create Treeview
        columns = ( 'Student Number', 'Student Name', 'Student Surname', 'Module Code', 'Module Name', 'Marks')
        tree = ttk.Treeview(self.marks_frame, columns=columns, show='headings')

        # Set column headings
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=150)

        displayD =  dbObj.fetchData()
        # display content
        for item in displayD:
            tree.insert('', END, values=item)

        # Add scrollbar
        scrollbar = ttk.Scrollbar(self.marks_frame, orient=VERTICAL, command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)

        # Pack the treeview and scrollbar
        tree.pack(side=LEFT, fill=BOTH, expand=True)
        scrollbar.pack(side=RIGHT, fill=Y)



        view_studs = Button(self.marks_frame, text="View All Students", command=self.view_students,
                            bg='#f44336', fg='white')
        view_studs.pack(pady=20)

        #complete

    def view_students(self):
        self.clear_frames()



         # Create marks frame
        self.marks_frame = Frame(self.table_frame)
        self.marks_frame.pack(fill=BOTH, expand=True)

        # Create Treeview
        columns = ('Student Number', 'Student Name', 'Student Surname', 'Email', 'Course')
        tree = ttk.Treeview(self.marks_frame, columns=columns, show='headings')

        # Set column headings
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=150)

        displayD = dbObj.view_all()
        # display content
        for item in displayD:
            tree.insert('', END, values=item)

        # Add scrollbar
        scrollbar = ttk.Scrollbar(self.marks_frame, orient=VERTICAL, command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)

        # Pack the treeview and scrollbar
        tree.pack(side=LEFT, fill=BOTH, expand=True)
        scrollbar.pack(side=RIGHT, fill=Y)

        view_studs = Button(self.marks_frame, text="View All Students", command=self.view_students,
                            bg='#f44336', fg='white')
        view_studs.pack(pady=20)

    def add_new(self):
        # Clear any existing frames
        self.clear_frames()

        # Create edit student frame
        self.edit_student_frame = Frame(self.table_frame)
        self.edit_student_frame.pack(fill=BOTH, expand=True, pady=20)

        # Enter desired stu # to delete
        Label(self.edit_student_frame, text="Enter Student Number:").pack()
        StuNum_Entry = Entry(self.edit_student_frame, textvariable= self.tStuNum)
        StuNum_Entry.pack(pady=5)

        Label(self.edit_student_frame, text="Enter Student Name:").pack()
        StuName_Entry = Entry(self.edit_student_frame, textvariable= self.tStuName)
        StuName_Entry.pack(pady=5)

        Label(self.edit_student_frame, text="Enter Student Surname:").pack()
        StuSurname_Entry = Entry(self.edit_student_frame,textvariable= self.tStuSur)
        StuSurname_Entry.pack(pady=5)

        Label(self.edit_student_frame, text="Enter Module Code:").pack()
        ModCode_Entry = Entry(self.edit_student_frame, textvariable= self.tModCode)
        ModCode_Entry.pack(pady=5)

        Label(self.edit_student_frame, text="Enter Module Name:").pack()
        ModName_Entry = Entry(self.edit_student_frame, textvariable= self.tModName)
        ModName_Entry.pack(pady=5)

        Label(self.edit_student_frame, text="Enter Marks:").pack()
        Marks_Entry = Entry(self.edit_student_frame, textvariable= self.tMarks)
        Marks_Entry.pack(pady=5)

        # Add a search and delete button
        new_Stu = Button(self.edit_student_frame, text="Add a new Student", command=self.add_new_student,
                            bg='#f44336', fg='white')
        new_Stu.pack(pady=5)

        #complete

    def add_new_student(self):
        try:
            # Attempt to get and convert all field values
            iStuNum = int(self.tStuNum.get())
            sStuName = self.tStuName.get()
            sStuSurname = self.tStuSur.get()
            sModCode = self.tModCode.get()
            sModName = self.tModName.get()
            rMarks = float(self.tMarks.get())

            # Ensure all fields are filled
            if not (sStuName and sStuSurname and sModCode and sModName):
                raise ValueError("All fields must be filled!")

            # Insert the data if everything is valid
            dbObj.insertData(iStuNum, sStuName, sStuSurname, sModCode, sModName, rMarks)
            messagebox.showinfo("Success", f"Student {iStuNum} has been added successfully!")

        except ValueError as ve:
            messagebox.showerror("Error", str(ve))
        except Exception:
            messagebox.showerror("Error", "Invalid input! Please enter valid data.")

    def search_student(self):
        # Clear any existing frames
        self.clear_frames()

        # Create delete module frame
        self.marks_frame = Frame(self.table_frame)
        self.marks_frame.pack(fill=BOTH, expand=True)

        # Enter desired stu # to delete
        Label(self.marks_frame, text="Enter Student Number:").pack()
        student_name_entry = Entry(self.marks_frame, textvariable=self.tStuNum)
        student_name_entry.pack(pady=20)

        # Add a search
        search_btn = Button(self.marks_frame, text="Search Selected Student #", command=self.search_selected_stu,
                            bg='#f44336', fg='white')
        search_btn.pack(pady=5)

        # Create Treeview to show modules
        columns = ('Student Number', 'Student Name', 'Student Surname', 'Module Code', 'Module Name', 'Marks')
        self.tree = ttk.Treeview(self.marks_frame, columns=columns, show='headings')

        # Set column headings
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=120)

        # Add scrollbar
        scrollbar = ttk.Scrollbar(self.marks_frame, orient=VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)

        # Pack the treeview and scrollbar
        self.tree.pack(side=LEFT, fill=BOTH, expand=True)
        scrollbar.pack(side=RIGHT, fill=Y)

    def search_selected_stu(self):
        try:
            # Convert the student number input to an integer
            iStuNum = int(self.tStuNum.get())
        except ValueError:
            # If conversion fails, show an error message
            messagebox.showerror("Error", "Student Number must be an integer!")
        else:
            # Proceed with the search if conversion was successful
            display = dbObj.search(iStuNum)

            # Check if any records were returned
            if display:
                # If found, display a success message and insert each record into the tree view
                messagebox.showinfo("Success", f"Student {iStuNum} has been found!")
                for record in display:
                    self.tree.insert('', 'end', values=record)
            else:
                # If no records are found, display an error message
                messagebox.showinfo("Error", f"Student {iStuNum} does not exist!")

    def show_add_module(self):
        # Clear any existing frames
        self.clear_frames()

        # Create add module frame
        self.add_module_frame = Frame(self.table_frame)
        self.add_module_frame.pack(fill=BOTH, expand=True, pady=20)

        # Add module form
        Label(self.add_module_frame, text="Add New Module", font=('Arial', 14, 'bold')).pack(pady=10)

        # Module Code
        Label(self.add_module_frame, text="Module Code:").pack()
        code_entry = Entry(self.add_module_frame)
        code_entry.pack(pady=5)

        # Module Name
        Label(self.add_module_frame, text="Module Name:").pack()
        name_entry = Entry(self.add_module_frame)
        name_entry.pack(pady=5)

        # Lecturer Name (Pre-filled for the lecturer)
        Label(self.add_module_frame, text="Lecturer:").pack()
        lecturer_entry = Entry(self.add_module_frame)
        name = dbObj.fetchlecName(self.lecNum)
        lecturer_entry.insert(0, name)  # Example of pre-filled lecturer name
        lecturer_entry.pack(pady=5)

        # Submit button
        submit_btn = Button(self.add_module_frame, text="Add Module",
                            command=lambda: self.submit_module(code_entry.get(), name_entry.get(),
                                                               lecturer_entry.get()),
                            bg='#2196F3', fg='white')
        submit_btn.pack(pady=20)

    def show_edit_student(self):
        # Clear any existing frames
        self.clear_frames()

        # Create edit student frame
        self.edit_student_frame = Frame(self.table_frame)
        self.edit_student_frame.pack(fill=BOTH, expand=True, pady=20)

        Label(self.edit_student_frame, text="Edit Student Information", font=('Arial', 14, 'bold')).pack(pady=10)

        # Student Name
        Label(self.edit_student_frame, text="Enter Student Number:").pack()
        student_name_entry = Entry(self.edit_student_frame, textvariable=self.tStuNum)
        student_name_entry.pack(pady=5)

        # Module
        Label(self.edit_student_frame, text="Module Code:").pack()
        module_entry = Entry(self.edit_student_frame, textvariable=self.tModCode)
        module_entry.pack(pady=5)

        # Marks
        Label(self.edit_student_frame, text="Marks:").pack()
        marks_entry = Entry(self.edit_student_frame, textvariable=self.tMarks)
        marks_entry.pack(pady=5)

        # Submit button to edit student info
        submit_btn = Button(self.edit_student_frame, text="Update Marks",
                            command=lambda: self.submit_student_update(student_name_entry.get(), module_entry.get(), marks_entry.get()),
                            bg='#FFC107', fg='black')
        submit_btn.pack(pady=20)

    def submit_student_update(self, student_name, module, marks):
        if not all([student_name, module, marks]):
            messagebox.showerror("Error", "All fields are required!")
            return

        try:
            # Convert before injecting
            iStuNum = int(self.tStuNum.get())
            sModCode = self.tModCode.get()
            rMarks = float(self.tMarks.get())

            # Ensure marks are within a valid range
            if not (0 <= rMarks <= 100):
                messagebox.showerror("Error", "Marks must be between 0 and 100.")
                return

        except ValueError:
            messagebox.showerror("Error", "Ensure all fields are entered correctly with valid data types.")
            return
        else:
            dbObj.updateData(sModCode, rMarks, iStuNum)
            messagebox.showinfo("Success", f"Marks for {student_name} in {sModCode} have been updated to {marks}!")

    def delete_module(self):
        # Clear any existing frames
        self.clear_frames()

        # Create delete module frame
        self.marks_frame = Frame(self.table_frame)
        self.marks_frame.pack(fill=BOTH, expand=True)

        # Create Treeview to show modules
        columns = ('Module Code', 'Module Name', 'Lecturer')
        self.tree = ttk.Treeview(self.marks_frame, columns=columns, show='headings')

        # Set column headings
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=150)

        # Add scrollbar
        scrollbar = ttk.Scrollbar(self.marks_frame, orient=VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)

        # Pack the treeview and scrollbar
        self.tree.pack(side=LEFT, fill=BOTH, expand=True)
        scrollbar.pack(side=RIGHT, fill=Y)

        # Enter desired Mod to delete
        Label(self.marks_frame, text="Enter Module Code:").pack()
        Mod_Code_Entry = Entry(self.marks_frame, textvariable=self.tModCode)
        Mod_Code_Entry.pack(pady=5)

        # Add a delete button
        delete_btn = Button(self.marks_frame, text="Delete Selected Module", command=self.delete_selected_module,
                            bg='#f44336', fg='white')
        delete_btn.pack(pady=20)

        #Enter desired stu # to delete
        Label(self.marks_frame, text="Enter Student Number:").pack()
        student_name_entry = Entry(self.marks_frame, textvariable=self.tStuNum)
        student_name_entry.pack(pady=5)

        # Add a search and delete button
        delete_btn = Button(self.marks_frame, text="Delete Selected Student #", command=self.delete_selected_student,
                            bg='#f44336', fg='white')
        delete_btn.pack(pady=5)

    def delete_selected_module(self):
        try:
            sMod = self.tModCode.get()
            display = dbObj.search(sMod)

            if display:
                # If found, display a success message and insert each record into the tree view
                messagebox.showinfo("Success", f"Module {sMod} has been found!")
                for record in display:
                    self.tree.insert('', 'end', values=record)
            else:
                # If no records are found, display an error message
                messagebox.showinfo("Error", f"Module {sMod} does not exist!")



        except:
            messagebox.showerror("Error", "Please ensure you have entered all fields.")
            return
        else:
            # Confirm deletion
            confirm = messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete module {sMod}?")
            if confirm:
                dbObj.deleteModData(sMod)
                messagebox.showinfo("Success", f"Module {sMod} deleted successfully!")
            else:
                messagebox.showinfo("Cancelled", "Deletion has been cancelled")

    def delete_selected_student(self):
        try:
            iStuNum = int(self.tStuNum.get())
            display = dbObj.search(iStuNum)

            if display:
                # If found, display a success message and insert each record into the tree view
                messagebox.showinfo("Success", f"Student {iStuNum} has been found!")
                for record in display:
                    self.tree.insert('', 'end', values=record)
            else:
                # If no records are found, display an error message
                messagebox.showinfo("Error", f"Student {iStuNum} does not exist!")




        except:
            messagebox.showerror("Error", "Please ensure you have entered all fields.")
            return
        else:
            # Confirm deletion
            confirm = messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete student: {iStuNum}?")
            if confirm:
                dbObj.deleteStuData(iStuNum)
                messagebox.showinfo("Success", f"Student {iStuNum} has been deleted successfully!")
            else:
                messagebox.showinfo("Cancelled", "Deletion has been cancelled")

    def submit_module(self, code, name, lecturer):
        if not all([code, name, lecturer]):
            messagebox.showerror("Error", "All fields are required!")
            return

        dbObj.addModule(code, name, lecturer)
        messagebox.showinfo("Success", f"Module {code} has been added successfully!")
        self.show_marks()  # Refresh the marks view

    def clear_frames(self):
        # Clear any existing frames in table_frame
        if self.marks_frame:
            self.marks_frame.destroy()
        if self.add_module_frame:
            self.add_module_frame.destroy()
        if self.edit_student_frame:
            self.edit_student_frame.destroy()

    def show_module(self):

        # Clear any existing frames
        self.clear_frames()

        # Create marks frame
        self.marks_frame = Frame(self.table_frame)
        self.marks_frame.pack(fill=BOTH, expand=True)

        # Create Treeview
        columns = ('Module Code', 'Module Name', 'Name')
        tree = ttk.Treeview(self.marks_frame, columns=columns, show='headings')

        # Set column headings
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=150)

        displayD =  dbObj.fetchMod()
        # display content
        for item in displayD:
            tree.insert('', END, values=item)

        # Add scrollbar
        scrollbar = ttk.Scrollbar(self.marks_frame, orient=VERTICAL, command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)

        # Pack the treeview and scrollbar
        tree.pack(side=LEFT, fill=BOTH, expand=True)
        scrollbar.pack(side=RIGHT, fill=Y)
