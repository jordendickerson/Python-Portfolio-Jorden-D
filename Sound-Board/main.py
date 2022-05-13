from tkinter import *
from tkinter.ttk import *
from application import *
from settings import *

# MUST INSTALL PYGAME FOR PROGRAM TO WORK
# pip install pygame

def main():
    root = Tk()
    Application.__change_Title__(title)
    app = Application(root)
    root.mainloop()





main()
