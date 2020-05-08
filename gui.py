import tkinter as tk
from Plot import PlotBar, PlotPie
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
  Load_excel(e2.get(), e1.get(), e3.get(), e4.get())

master = tk.Tk()
master.configure(bg='white')
tk.Label(master, text="Message", bg='white',fg="#0A5688", font=("Arial", 12, "bold")).grid(row=0)
tk.Label(master, text="column name", bg='white',fg="#0A5688", font=("Arial", 12, "bold")).grid(row=1)
tk.Label(master, text="variable columns", bg='white',fg="#0A5688", font=("Arial", 12, "bold")).grid(row=2)
tk.Label(master, text="No  variable", bg='white',fg="#0A5688", font=("Arial", 12, "bold")).grid(row=3)

e1 = tk.Entry(master)
e2 = tk.Entry(master)
e3 = tk.Entry(master)
e4 = tk.Entry(master)


e1.grid(row=0, column=1, padx=10, pady=10)
e2.grid(row=1, column=1, padx=10, pady=10)
e3.grid(row=2, column=1, padx=10, pady=10)
e4.grid(row=3, column=1, padx=10, pady=10)

for i in range(10):
    master.columnconfigure(i, weight=2)
    master.rowconfigure(i, weight=2)

tk.Button(master,text='Send',command=SendMessage, bg='#F9D162', fg="#0A5688", font=("Helvetica", 10, "bold"), height=3, width=10, activebackground="#F3954F").grid(row=4,column=0,padx=10, pady=20)
tk.Button(master, text='Plot Bar', command=Plot_Bar,bg='#F9D162', fg="#0A5688", font=("Helvetica", 10, "bold"), height=3, width=10, activebackground="#F3954F").grid(row=4, column=1, padx=10, pady=20)
tk.Button(master, text='Plot Pie', command=Plot_Pie,bg='#F9D162', fg="#0A5688", font=("Helvetica", 10, "bold"), height=3, width=10, activebackground="#F3954F").grid(row=4, column=2, padx=10, pady=20)

master.mainloop()
tk.mainloop()