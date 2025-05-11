from tkinter import *
from first_window import FirstWindow
from DataHandler import DatabaseInteraction

dbObj = DatabaseInteraction("BCData.db")

def main():
    master = Tk()
    FirstWindow(master)
    master.mainloop()

if __name__ == "__main__":
    main()

