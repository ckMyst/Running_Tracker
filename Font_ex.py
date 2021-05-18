'''
GUI Layout
'''
import tkinter as tk
import tkinter.font as tkFont

gui = tk.Tk()


fontStyle = tkFont.Font(family="Lucida Grande", size=20)

label1 = tk.Label(gui, text="Test", font=fontStyle)

def increase_label_font():
    fontsize = fontStyle['size']
    label1['text'] = fontsize+2
    fontStyle.configure(size=fontsize+2)

def decrease_label_font():
    fontsize = fontStyle['size']
    label1['text'] = fontsize-2
    fontStyle.configure(size=fontsize-2)

buttonExample1 = tk.Button(gui, text="Increase", width=30,
                          command=increase_label_font)
buttonExample2 = tk.Button(gui, text="Decrease", width=30,
                          command=decrease_label_font)

buttonExample1.pack(side=tk.LEFT)
buttonExample2.pack(side=tk.LEFT)
label1.pack(side=tk.RIGHT)

gui.mainloop()

