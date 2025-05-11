import sqlite3


class DatabaseInteraction:
    # set up constructor and connection to database
    def __init__(self, db):
        self.conn = sqlite3.connect(db) #connection object to database
        self.cursor = self.conn.cursor()    # cursor object to execute queries

    # define CRUD methods
    def StudentsTblReg(self, stuNum, sName, sSurname, Dob, eMail, Phone, Gender, Address, Pass, Courses):
        self.cursor.execute("INSERT INTO Students VALUES (?,?,?,?,?,?,?,?,?,?)",(stuNum, sName, sSurname, Dob, eMail, Phone, Gender, Address, Pass, Courses))
        self.conn.commit()

    def StuLogTblReg(self, stuNum, stuPass):
        self.cursor.execute("Insert Into StuLoginTbl Values(?,?)", (stuNum,stuPass))
        self.conn.commit()

    def insertData(self, sNum, sName, sSur, sMName, sMCode, rMark):
        self.cursor.execute("INSERT INTO StuDataTbl VALUES (Null, ?,?,?,?,?,?)", (sNum, sName, sSur, sMName, sMCode, rMark))
        self.conn.commit()

    def fetchData(self):
        self.cursor.execute("SELECT StuNum, StuName, StuSurname, ModCode, ModName, Mark FROM StuDataTbl")
        rows = self.cursor.fetchall()   #fetches all rows in a table
        return rows

    def fetchStuData(self, iStuNum):
        self.cursor.execute("SELECT * FROM Students Where StuNum=?", (iStuNum,))
        rows = self.cursor.fetchall()   #fetches all rows in a table
        return rows

    def updateStuData(self, sName, sSur, Dob, email, phone, addy, passwrd, stuNum):
        self.cursor.execute("Update Students Set "
                            "StuName=?,"
                            "StuSurname=?,"
                            "DOB=?,"
                            "eMail=?,"
                            "Phone=?,"
                            "Address=?,"
                            "Password=?"
                            "Where StuNum=?",
                            (sName, sSur, Dob, email, phone, addy, passwrd, stuNum) )
        self.conn.commit()

    def checkExistingStu(self, stuNum):
        self.cursor.execute("SELECT * FROM StuLoginTbl where StuNum=?", (stuNum,))
        rows = self.cursor.fetchall()  # fetches all rows in a table
        return rows

    def search(self, stuNum):
        self.cursor.execute("SELECT StuNum, StuName, StuSurname, ModCode, ModName, Mark FROM StuDataTbl where StuNum=?", (stuNum,))
        row = self.cursor.fetchall()
        return row

    def lecLogin(self, lecNum, lecPass):
        self.cursor.execute('SELECT LecNum, LecPassword FROM LecLoginTbl')
        check = self.cursor.fetchall()

        for i in check:
            NumCol = int(i[0])  # LecNum is an integer
            PassCol = str(i[1]).strip()  # LecPassword is a string, removing whitespace

            # Correct comparison with lecNum as int and lecPass as string
            if lecNum == NumCol and lecPass.strip() == PassCol:
                return "Welcome"

        return "Error"

    def stuLogin(self, stuNum, stuPass):
        self.cursor.execute("SELECT StuNum, StuPassword FROM StuLoginTbl")
        check = self.cursor.fetchall()

        for i in check:
            NumCol = int(i[0])  # LecNum is an integer
            PassCol = str(i[1]).strip()  # LecPassword is a string, removing whitespace

            # Correct comparison with lecNum as int and lecPass as string
            if stuNum == NumCol and stuPass.strip() == PassCol:
                return "Welcome"

        return "Error"

    def updateData(self, sMCode, rMark, sNum):
        self.cursor.execute("UPDATE StuDataTbl SET "
                            "ModCode = ?, "
                            "Mark = ? "
                            "WHERE StuNum = ? AND ModCode = ?",
                            (sMCode, rMark, sNum, sMCode))
        self.conn.commit()

    def deleteStuData(self, sNum):
        self.cursor.execute("DELETE FROM StuDataTbl WHERE StuNum=?", (sNum,))
        self.conn.commit()

    def deleteModData(self, sModCode):
        # Delete from StuDataTbl
        self.cursor.execute("DELETE FROM StuDataTbl WHERE ModCode=?", (sModCode,))

        # Delete from ModTbl
        self.cursor.execute("DELETE FROM ModTbl WHERE ModCode=?", (sModCode,))
        self.conn.commit()

    def addModule(self, modcode, modname, lecname):
        self.cursor.execute("insert into ModTbl values (?,?,?)", (modcode,modname,lecname))
        self.conn.commit()

    def fetchlecName(self, lecnum):
        self.cursor.execute("select Name from LecLoginTbl where LecNum =?", (lecnum,))
        name = self.cursor.fetchone()
        return name

    def fetchMod(self):
        self.cursor.execute("SELECT * FROM ModTbl")
        rows = self.cursor.fetchall()
        return rows

    def view_all(self):
        self.cursor.execute("SELECT StuNum, StuName, StuSurname, eMail, Courses FROM Students")
        rows = self.cursor.fetchall()
        return rows



"""
#DB and TBL Creation
BCconn = sqlite3.connect('BCData.db')

StuDataTbl = BCconn.cursor()
StuLoginTbl = BCconn.cursor()
LecLogTbl = BCconn.cursor()
Students = BCconn.cursor()
ModTbl = BCconn.cursor()

StudentsCommand = ("CREATE TABLE IF NOT EXISTS Students (StuNum INTEGER PRIMARY KEY, "
          "StuName TEXT, StuSurname TEXT, DOB TEXT, eMail TEXT, Phone INTEGER, Gender TEXT,"
                   "Address TEXT, Password TEXT, Courses TEXT)")

Stucommand = ("CREATE TABLE IF NOT EXISTS StuDataTbl (List INTEGER PRIMARY KEY, "
          "StuNum INTEGER, StuName TEXT, StuSurname TEXT, ModCode TEXT, ModName TEXT, Mark REAL)")
#Stucommand = "DROP TABLE IF EXISTS StuDataTbl;"
LecLogCommand2 = "Drop Table if Exists LecLoginTbl"

StuLogCommand = "CREATE TABLE IF NOT EXISTS StuLoginTbl (StuNum INTEGER PRIMARY KEY, StuPassword TEXT)"

LecLogCommand = "CREATE TABLE IF NOT EXISTS LecLoginTbl (LecNum INTEGER PRIMARY KEY, LecPassword TEXT, Name Text)"

ModCommand = "CREATE TABLE IF NOT EXISTS ModTbl (Module_Code TEXT PRIMARY KEY, Module_Name TEXT, Lecture_Name Text)"

StuDataTbl.execute(Stucommand)
StuLoginTbl.execute(StuLogCommand)
LecLogTbl.execute(LecLogCommand)
Students.execute(StudentsCommand)
ModTbl.execute(ModCommand)
"""