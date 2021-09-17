'''
Running Tracker
'''

# ------------------------
import tkinter as tk
import tkinter.font as ft
import csv
# import xlxs
# ------------------------
cmmd = tk.Tk()
cmmd.title("Running Tracker")
cmmd.geometry("350x400")
# ==============================================
class selectProf:
    def __init__(self, master):
        self.commence = master
        self.profBtn1 = tk.Button(master, text="New User", command=self.openWin1)
        self.profBtn1.grid()
        self.profBtn2 = tk.Button(master, text="Existing User", command=self.openWin1)
        self.profBtn2.grid()

    def openWin1(self):
        self.commence.withdraw()
        topWin1 = tk.Toplevel(self.commence)
        topWin1.geometry("350x400")
        newWin1 = infoWin(topWin1)
# ==============================================
class dataEntry:
    def __init__(self, master):
        self.commence = master
#       =======================================
        self.user = tk.Label(master, text="Username")
        self.user.grid(row=2, column=2)

        self.psw = tk.Label(master, text="Password")
        self.psw.grid(row=3, column=2)
#       =======================================
        self.userEnt = tk.Entry(master)
        self.userEnt.grid(row=2, column=3)

        self.pswEnt = tk.Entry(master)
        self.pswEnt.grid(row=3, column=3)
#       ========================================
        self.submit = tk.Button(cmmd, text="Submit", command=self.entryCheck)
        self.submit.grid()

    def entryCheck(self, userEnt):
        self.username = self.userEnt
        self.password = self.pswEnt
        with open('profile_checker.csv', 'rt') as f:
            read = csv.reader(f, delimiter=',')
            for row in read:
                for field in row:
                    if field == self.username and self.password:
                        self.commence.withdraw()
#       ========================================
# ==============================================
class infoWin:
    def __init__(self, master):
        self.commence = master
        self.frame = tk.Frame(self.commence)
        self.frame.grid(row=0, column=0, ipady=4)
#   ============================================
    def profileInfo(self, master):
        self.bmi = tk.Label(master, text="BMI")
        self.bmi.grid(row=2, column=2)

        self.goalBmi = tk.Label(master, text="Goal BMI")
        self.goalBmi.grid(row=3, column=2)

        self.timeInterval1 = tk.Label(master, text="Free Time Interval")
        self.timeInterval1.grid(row=2, column=4)

        self.timeInterval2 = tk.Label(master, text="-")
        self.timeInterval2.grid(row=2, column=6)
#   =======================================
        self.bmiEnt = tk.Entry(master, )
        self.bmiEnt.grid(row=2, column=3)

        self.goalBmiENT = tk.Entry(master, )
        self.goalBmiENT.grid(row=3, column=3)

        self.timeInterval1ENT = tk.Entry(master, )
        self.timeInterval1ENT.grid(row=2, column=5)

        self.timeInterval2ENT = tk.Entry(master, )
        self.timeInterval2ENT.grid(row=2, column=7)
#   =======================================
        self.submit = tk.Button(master, text="Submit", command=self.dataSave)
        self.submit.grid()

        self.exit = tk.Button(master, text="Exit", command=self.openWin2)
        self.exit.grid()
#   =======================================
    def dataSave(self):
        with open('profile_checker.csv', 'a') as f:
            write = csv.writer(f, quoting=csv.QUOTE_ALL)
            write.writerow([self.bmiEnt.get(), self.goalBmiENT.get(), self.timeInterval1ENT.get(), self.timeInterval2ENT.get()])
#   =======================================
    def openWin2(self):
        self.commence.withdraw()
        topWin2 = tk.Toplevel(self.commence)
        topWin2.geometry("350x400")
        newWin2 = mainWin(topWin2)
#   ============================================
class mainWin():
    def __init__(self, master):
        self.commence = master
        self.Font = ft.Font(family="Calibre", size=12)
    def welcome(self, master):
        with open('profile_checker.csv', 'a') as f:
            read = csv.reader()
        self.welcLable = tk.Label(master, text='Welcome ', borderwidth=0.5, relief="solid", font=self.Font)
        self.Font.configure(size="14")
        self.welcLable.grid(row=0, column=1, padx=1, ipadx=36, ipady=12)
# ------------
    def routine4(self, master):
        self.Font = ft.Font(family="Calibre", size=12)
        self.rBtn = tk.Button(master, text="Routine", borderwidth=0.5, relief="solid", font=self.Font)
        self.Font.configure(size="14")
        self.rBtn.grid(pady=60, ipadx=16, ipady=12)
# ------------
    def weather5(self, master):
        self.Font = ft.Font(family="Calibre", size=12)
        self.wBtn = tk.Button(master, text='Weather', borderwidth=0.5, relief="solid", font=self.Font)
        self.Font.configure(size="14")
        self.wBtn.grid(row=10, column=1, padx=1, ipadx=48, ipady=66)
# ------------
    def calendar6(self, master):
        self.Font = ft.Font(family="Calibre", size=12)
        self.calBtn = tk.Button(master, text="Calendar", borderwidth=0.5, relief="solid", font=self.Font)
        self.Font.configure(size="14")
        self.calBtn.grid(column=0, row=10, pady=30, ipadx=12, ipady=66)
# ------------
    def date_time7(self, master):
        self.Font = ft.Font(family="Calibre", size=12)
        self.timeBtn = tk.Button(master, text="Date & Time", borderwidth=0.5, relief="solid", font=self.Font)
        self.Font.configure(size="14")
        self.timeBtn.grid(row=10, column=1, pady=30, ipady=66, ipadx=12)
# ------------
    def exit(self, master):
        self.frame = tk.Frame(self.commence)
        self.exitBtn = tk.Button(master, self.frame, command=self.breakWin)
        self.exitBtn.grid()
# ------------
    def breakWin(self):
        self.commence.destroy()
# ============================================
selection = selectProf(cmmd)
authentication = dataEntry(cmmd)
characteristic = infoWin(cmmd)
interface = mainWin(cmmd)
# ===============================================
cmmd.mainloop()
