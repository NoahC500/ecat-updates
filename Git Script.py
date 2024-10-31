#!/bin/python3
import datetime
import os
from tkinter import *
from tkinter import Tk

def submit(msgIn):
    msg = msgIn.get(3.0, END)[0:-1]
    now = str(datetime.datetime.now())
    os.system(f"git add . && git commit -a -m \"{now[8:10]}/{now[5:7]}/{now[0:4]} {now[11:16]} - {msg}\" && git push")
    root.destroy()

root = Tk()
root.title("ECAT Updates Git Commit")
frame = Frame(root)
frame.grid()
root.resizable(width=False, height=False)

msgIn = Text(root, width=50, height=10)
msgIn.grid(column=0, row=0)
msgIn.insert(1.0, f"# Lines 1 & 2 are ignored\n# The first line is appended after the date & time\n")

submitBtn = Button(root, width=50, height=1, command=lambda: submit(msgIn), text="Submit")
submitBtn.grid(column=0, row=1)

root.mainloop()
