from time import sleep
import urllib.parse
import pandas as pd 
import tkinter as tk
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib import rcParams
import pymsgbox
rcParams.update({'figure.autolayout': True})

def PlotBar(fileName,inpString=''):

	try:
		df = pd.read_excel(fileName)
	except:
		pymsgbox.alert('You have entered invalid file name!', 'Alert')
		return
	if(inpString!=''):
		df= df[df[inpString] == 'Yes']
	departmentsNames=list(set(df['Department']))
	departmentValues=[0]*len(departmentsNames)

	for j,i in enumerate(departmentsNames):
		departmentValues[j]=(list(df.Department).count(i))

	print(departmentsNames,departmentValues)
	data1 = {'departmentsNames': departmentsNames,
	         'departmentValues': departmentValues
	        }
	df1 = DataFrame(data1,columns=['departmentsNames','departmentValues'])

	root= tk.Tk()

	figure1 = plt.Figure(figsize=(5,5), dpi=100)
	ax1 = figure1.add_subplot(111)
	bar1 = FigureCanvasTkAgg(figure1, root)
	bar1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
	df1 = df1[['departmentsNames','departmentValues']].groupby('departmentsNames').sum()
	df1.plot(kind='bar', legend=True, ax=ax1)
	ax1.set_title('Department Names Vs. {}'.format(inpString))

	root.mainloop()



def PlotPie(fileName,inpString=""):
	try:
		df = pd.read_excel(fileName)
	except:
		pymsgbox.alert('You have entered invalid file name!', 'Alert')
		return 
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