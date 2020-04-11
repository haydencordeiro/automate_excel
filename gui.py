import tkinter as tk
from Plot import PlotBar,PlotPie
import pymsgbox
from kap2 import Load_excel


def Plot_Bar():
  try:
    
    PlotBar(e2.get())
  except:
    pymsgbox.alert('You have entered invalid column name!', 'Alert')

def Plot_Pie():
  try:
    PlotPie(e2.get())
  except:
    pymsgbox.alert('You have entered invalid column name!', 'Alert')

def SendMessage():
  





master = tk.Tk()
master.configure(bg='black')
tk.Label(master, text="Message",bg='black',fg="white",font=("Arial", 12)).grid(row=0)
tk.Label(master, text="column name",bg='black',fg="white",font=("Arial", 12)).grid(row=1)
tk.Label(master, text="variable columns",bg='black',fg="white",font=("Arial", 12)).grid(row=2)
tk.Label(master, text="No  variable",bg='black',fg="white",font=("Arial", 12)).grid(row=3)

e1 = tk.Entry(master)
e2 = tk.Entry(master)
e3 = tk.Entry(master)
e4 = tk.Entry(master)


e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
e4.grid(row=3, column=1)


for i in range(10):
  master.columnconfigure(i, weight=2)
  master.rowconfigure(i, weight=2)

tk.Button(master, 
          text='Send', 
          command=SendMessage
          ,bg='#2e3d80',fg="white").grid(row=4, 
                                    column=0,
                                    pady=4)



tk.Button(master, text='Plot Bar', command=Plot_Bar,bg='#2e3d80',fg="white").place(x=100,y=96)
tk.Button(master, text='Plot Pie', command=Plot_Pie,bg='#2e3d80',fg="white").place(x=180,y=96)
# tk.Button(master, 
#           text='Recognise', 
#           command=Recognise).grid(row=3, 
#                                     column=2, 
#                                     sticky=tk.W, 
#                                     pady=4)


# tk.Button(master, 
#           text='Sort Attendance', 
#           command=Sort).grid(row=3, 
#                                     column=3, 
#                                     sticky=tk.W, 
#                                     pady=4)


master.mainloop()

tk.mainloop()

