from tkinter import *
from tkcalendar import *

import datetime
#from functions import dateCalculator

class dateCalculator():
	"""docstring for datecalculator"""
	def __init__(self, arg):
		super(datecalculator, self).__init__()
		self.arg = arg

	#Define Function to select the date
	def get_startDate():
	   BtnFecha1.config(text="Start Date" + " " + calStart.get_date())
	   startDate = calStart.get_date()
	   return(startDate)

	   #Define Function to select the date
	def get_endDate():
	   BtnFecha2.config(text="End Date" + " " + calEnd.get_date())
	   endDate = calEnd.get_date()
	   return(endDate)

	def test():
		date1 = dateCalculator.get_startDate()
		date2 = dateCalculator.get_endDate()
		#print(date1)
		#print(date2)
		dateDiff = dateCalculator.diffCalculator(date1,date2)

		alldate,_,_,_,_,_,_ = dateDiff
		_,_,_,_,años,_,_ = dateDiff
		_,_,_,_,_,meses,_ = dateDiff
		_,_,_,_,_,_,dias = dateDiff
		
		

		diffMonths.config(text=str(meses) + " Months")
		diffDays.config(text=str(dias) + " Days")
		diffYears.config(text=str(años) + " Years")
		DiffTotal.config(text=str(alldate))
		return(dateDiff)



	#Calcula años meses y dias de diferencia.
	def diffCalculator(date1_str, date2_str):
		format_str = '%m/%d/%y' # The format
		datetime_obj1 = datetime.datetime.strptime(date1_str, format_str)
		datetime_obj2 = datetime.datetime.strptime(date2_str, format_str)


		daysDiff = str(datetime_obj2-datetime_obj1).split(",")

		if len(daysDiff) > 1:
			#print(daysDiff)

			daysDiff = int((daysDiff[0].split(" "))[0])
			#print(daysDiff)
			if daysDiff >= 0:
				# Calculating years
				years = daysDiff // 365

				total_years = str(years) + " Years!"

				# Calculating months
				months = (daysDiff - years *365) // 30

				total_months = str(months) +" Months!"

				onlymonths = datetime_obj2.month - datetime_obj1.month + 12*(datetime_obj2.year - datetime_obj1.year)
				# Calculating days
				onlydays = daysDiff

				days = (daysDiff - years * 365 - months*30)

				total_days = str(days)+ " Days!"

				diferencia_total = str(total_years)+" "+str(total_months)+" "+str(total_days) 

				return(diferencia_total, total_years, total_months, total_days, years, onlymonths, onlydays)
			else:
				return("Ingresa una fecha posterior a la inicial",0,0,0,0,0,0)
			
		else:
			#print(daysDiff)
			return(0,0,0,0,0,0,0)




#Create an instance of tkinter frame or window
win= Tk()
win.configure(bg='Dark Sea Green')
win.title("Calendar")
win.geometry("630x480")

calStart = Calendar(win, selectmode="day")
calStart.grid(row=2, column= 2,  pady=20)


calEnd= Calendar(win, selectmode="day")
calEnd.grid(row=2, column= 4, pady=20)

title = Label(win, text="TioGeras Date-Diff Calculator", background='sea green')
title.grid(row= 1, column=3)
   
#Create a button to pick the date from the calendar
button= Button(win, text= "Select the start Date", command = dateCalculator.test, background="DeepSkyBlue2")
button.grid(row=3, column=2, pady=20)


button= Button(win, text= "Select the end Date", command = dateCalculator.test, background="FireBrick2")
button.grid(row=3, column=4, pady=20)

#Create Label for displaying selected Date
BtnFecha1= Label(win, text="", background="gray63")
BtnFecha1.grid(row=4, column=2, pady=20)

BtnFecha2= Label(win, text="", background="gray63")
BtnFecha2.grid(row=4, column=4, pady=20)

DiffTotal= Label(win, text="", background="SlateGray2")
DiffTotal.grid(row=6, column=3, pady=20)

diffDays= Label(win, text="", background="SlateGray2")
diffDays.grid(row=3, column=3, pady=20)

diffMonths= Label(win, text="", background="SlateGray2")
diffMonths.grid(row=4, column=3, pady=20)

diffYears= Label(win, text="", background="SlateGray2")
diffYears.grid(row=5, column=3, pady=20)


