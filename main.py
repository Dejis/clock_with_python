from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title("The clock says you are doing well in your life.  Keep pressing on.")

def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)
        
label = Label(root, font=("ds-digital", 200), background = "black", foreground = "cyan")
label.pack(anchor='center')

time()

mainloop()
