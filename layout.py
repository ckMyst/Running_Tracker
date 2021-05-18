'''
Connor Kissack
GUI Layout
'''

from tkinter import *
from tkinter.ttk import *
import tkinter as tk
import tkinter.font as ft

# ------------

class newWindow(Toplevel):
    def __init__(self, master=None):
        super().__init__(master=master)
        self.title("Choice of Profile")
        self.geometry("350x400")
        initLabel = Label(self, text="Test")
        initLabel.grid()

# ------------

# Do dropdown menu for Edit, File, Save

key = tk.Tk()
key.title("Running Tracker")
key.geometry("350x460")

initLabel = Label(key, text='Profile')
initLabel.grid()

initButton = Button(key, text="New Profile")
initButton.bind("<Button>", lambda e: newWindow(key))
initButton.grid(row=1, column=1, pady=18)


# key.geometry("350x400")
# key.title("Running Tracker")


# ------------
# Data Visualization Widget

def visualgraph1():
# Font size changed with .configure
    Font = ft.Font(family="Calibre", size=12)
    Label1 = tk.Label(key, text="Visual Graph", borderwidth=0.5, relief="solid", font=Font)
    Font.configure(size="14")
    Label1.grid(row=0, column=0, sticky=NE, ipady=12)

visualgraph1()

# ------------
# Profile Widget



def new_profile2():
    Font = ft.Font(family="Calibre", size=12)
    Label2 = tk.Label(key, text="New Profile", borderwidth=0.5, relief="solid", font=Font)
    Font.configure(size="14")
    Label2.grid(row=0, column=1, padx=176, sticky=NE, ipady=12)

new_profile2()

# ------------
# Welcome Widget

def welcome3():
    Font = ft.Font(family="Calibre", size=12)
    Label3 = tk.Label(key, text='Welcome XXX', borderwidth=0.5, relief="solid", font=Font)
    Font.configure(size="14")
    Label3.grid(row=0, column=1,sticky=W, padx=1, ipadx=36, ipady=12)

welcome3()

# ------------
# Daily Routine Widget

def routine4():
    Font = ft.Font(family="Calibre", size=12)
    Label4 = tk.Label(key, text="Routine", borderwidth=0.5, relief="solid", font=Font)
    Font.configure(size="14")
    Label4.grid( pady=60, ipadx=16, ipady=12)

routine4()

# ------------
# Weather Widget

def weather5():
    Font = ft.Font(family="Calibre", size=12)
    Label3 = tk.Label(key, text='Weather', borderwidth=0.5, relief="solid", font=Font)
    Font.configure(size="14")
    Label3.grid(row=10, column=1, sticky=W, padx=1, ipadx=48, ipady=66)

weather5()

# ------------
# Calendar Widget

def calendar6():
    Font = ft.Font(family="Calibre", size=12)
    Label6 = tk.Label(key, text="Calendar", borderwidth=0.5, relief="solid", font=Font)
    Font.configure(size="14")
    Label6.grid(column=0, row=10, pady=30, ipadx=12, ipady=66, sticky=NE)

calendar6()

# ------------
# Date & Time Widget

def date_time7():
    Font = ft.Font(family="Calibre", size=12)
    Label6 = tk.Label(key, text="Date & Time", borderwidth=0.5, relief="solid", font=Font)
    Font.configure(size="14")
    Label6.grid(row=10, column=1, pady=30, ipady=66, ipadx=12)

date_time7()

def close_window():
    print("Hello World")

close_window()

key.mainloop()