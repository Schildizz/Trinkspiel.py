#The file is a first alpha. It only serves as an idea and is not yet functional.

from tkinter import *
import os

def Aufgabe():
    return os.system("")

def Wahrheit():
    return os.system("")


master= Tk()
master.geometry("150x150")

master.configure(bg='light blue')

Button(master, text="Aufgabe", command=Aufgabe).place(x=20, y=20)
Button(master, text="Wahrheit", command=Wahrheit).place(x=25, y=50)


mainloop()
