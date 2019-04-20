#!/usr/bin/env pythone
"""helloWorld.py by StephenCardone
"""
import datetime
import sys

def main():
	inputArgs = sys.argv[1:]	
	if inputArgs == []:
		print("args: currentHours(decimal) , Goal Time(decimal) ")
		sys.exit()
	else:
		calculateTime(inputArgs)
#	currentTime = datetime.datetime.now()
#	print(str(currentTime))

def calculateTime(*args):

	_paramInput = args[0]

	currentHours = float(_paramInput[0]) #decimal
	goalTime = float(_paramInput[1])  #decimal

	remaining = goalTime - currentHours #decimal
	hours = int(remaining)
	remaining = remaining * 60

	mins = remaining %60

	output = "You require: %r hours %r minutes" % (hours, int(mins))
	print(output)

	print(endTime(hours, mins))

def endTime(*args):
	currentTime = datetime.datetime.now()
	hour = currentTime.hour	
	mins = currentTime.minute
	amPm = "pm"
	hour = hour + args[0]
	
	if (hour < 12) | (hour >= 24):
		amPm = "am"

	hour = hour % 12

	mins = mins + int(args[1])
	
	if mins > 60:
		hour = hour + 1
		mins = mins % 60
	output = "You will hit goal at:  %r:%02d %s" % (hour, mins, amPm)
	return output
	

main()
