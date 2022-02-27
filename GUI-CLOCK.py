# GUI clock using tkinter
from tkinter import *
from tkinter.ttk import *
from time import strftime

root=Tk()
root.title("CLOCK")

def time():
    string=strftime("%H:%M:%S")
    lbl.config(text=string)
    lbl.after(1000,time)

lbl = Label(root,font=("times",40,"bold"),background="purple",foreground="white")

lbl.pack(anchor=CENTER)
time()

mainloop()
