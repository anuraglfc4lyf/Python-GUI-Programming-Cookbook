'''
Created on Nov 26, 2016

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

tabControl = ttk.Notebook(win)          # Create Tab Control

tab1 = ttk.Frame(tabControl)            # Create a tab 
tabControl.add(tab1, text='Tab 1')      # Add the tab

tabControl.pack(expand=1, fill="both")  # Pack to make visible

#======================
# Start GUI
#======================
win.mainloop()
