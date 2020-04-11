import pandas as pd 
import tkinter as tk
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg



def plotPie(inpString=""):
	df = pd.read_excel("1.xlsx")
	if(inpString!=''):
		df= df[df[inpString] == 'Yes']
	labels =list(set(df['Department']))
	departmentValues=[0]*len(labels)

	for j,i in enumerate(labels):
		departmentValues[j]=(list(df.Department).count(i))
	values=departmentValues


	explode = list()
	for k in labels:
	    explode.append(0.1)


	root= tk.Tk()
	actualFigure = plt.figure(figsize=(5,5), dpi=100)
	actualFigure.suptitle("Participation Stats", fontsize = 22)
	pie = plt.pie(values, labels=labels, explode=explode, shadow=True, autopct='%1.1f%%')
	plt.legend(pie[0], labels, loc="upper corner")	
	canvas = FigureCanvasTkAgg(actualFigure, root)
	canvas.get_tk_widget().pack()
	root.mainloop()