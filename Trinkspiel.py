#The file is a first alpha. It only serves as an idea and is not yet functional.

from tkinter import *
import os

def Aufgabe():
    return os.system("")

def Wahrheit():
    return os.system("")


master= Tk()
master.geometry("200x60")

master.configure(bg='light blue')

Button(master, text="Aufgabe", command=os.system('python Test.py')).place(x=20, y=20)
Button(master, text="Wahrheit", command=os.system('python Test.py')).place(x=100, y=20)


mainloop()
