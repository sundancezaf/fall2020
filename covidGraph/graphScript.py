
# Zaffy Aleman
# Discussion Assignment 7

import pylab
import math
import numpy as np


'''
For this project I tried to do a simple sine wave. I will have to figure out how to 
smooth it out. 

On the other hand, I had a previous project from Intro. to CS, analyzing Covid-19 data
provided by the New York Times. I then went a bit further and used Pandas to make it 
easier to access the data I wanted to see.
I ended up creating individual dataFrames for the states that included the date, number of Cases,
and number of deaths. I grabbed the current dataFrame for Iowa and saved it into a csv file.
Using that CSV file, I created the second graph to show the growth of cases for the state since
March 23, the date of the first official case.

'''

# This is just an attempt at a sine wave 

def sin1():
	listX,listY = [],[]
	for item in range(-10,10):
		x = item * math.pi
		listX.append(x)
		y = -2*math.sin(item)
		listY.append(y)
		#x = item
		#listX.append(x)
	pylab.plot(listX,listY)
	pylab.show()

sin1()


def IowaCases():
	indexList, dateList, casesList, dailyChangeList = [],[],[],[]
	graphDates, graphCases, graphChanges = [],[],[]
# 
	f = open('IowaCovidCases.csv','r')
	for line in f:
		newLine = line.split(',')
		index = newLine[0]
		date = newLine[1]
		cases = newLine[2]
		dailyChange = newLine[3]
		dateList.append(date)
		casesList.append(cases)
		dailyChangeList.append(dailyChange)

	# Don't want to graph every single day so getting just every 20 day values
	for item in range(1,len(dateList)-1,20):
		graphDates.append(dateList[item])
		graphCases.append(casesList[item])
		graphChanges.append(dailyChangeList[item])


	# This graphs the number of covid cases every 15 days for Iowa since first case
	pylab.xlabel('Date')
	pylab.ylabel('Number of Cases')
	pylab.title('Iowa Covid-19 Cases')
	pylab.plot(graphDates,graphCases)
	pylab.show()	

#IowaCases()

