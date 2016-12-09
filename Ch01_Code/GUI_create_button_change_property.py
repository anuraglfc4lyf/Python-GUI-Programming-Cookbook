'''
Created on Nov 23, 2016

@author: Burkhard A. Meier
'''
#======================
# imports
#======================
import tkinter as tk
from tkinter import ttk

# Create instance
win = tk.Tk()   

# Add a title       
win.title("Python GUI")   

# Modify adding a Label
a_label = ttk.Label(win, text="A Label")
a_label.grid(column=0, row=0)

# Button Click Event Function
def click_me():
    action.configure(text="** I have been Clicked! **")
    a_label.configure(foreground='red')
    a_label.configure(text='A Red Label')

# Adding a Button
action = ttk.Button(win, text="Click Me!", command=click_me)   
action.grid(column=1, row=0)


#======================
# Start GUI
#======================
win.mainloop()