import tkinter as tk

class windowclass():
    def __init__(self, master):
        self.master = master
        self.btn = tk.Button(master, text="New Profile", command=self.command)
        self.btn.pack()

    def command(self):
        self.master.withdraw()
        toplevel = tk.Toplevel(self.master)
        toplevel.geometry("350x350")
        app = Demo2(toplevel)

class Demo2:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.quitButton = tk.Button(self.frame, text= 'Quit', width = 25, command = self.close_windows)
        self.quitButton.pack()
        self.frame.pack()
    def close_windows(self):
        self.master.destroy()

root = tk.Tk()
root.title("window")
root.geometry("350x350")
cls = windowclass(root)
root.mainloop()