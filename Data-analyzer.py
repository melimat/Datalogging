# -*- coding: utf-8 -*-
import sys


class dataSet:

	def __init__(self, path, splitter):
		self.path = path
		self.splitter = splitter
		self.dataFile = open(self.path)

	def readData(self):
		i = int(0)
		self.unitsArray = []
		self.timeArray = []
		self.dataArray = []
		for eachLine in self.dataFile:
			i += 1
			lineArray = eachLine.split(self.splitter)
			if(i == 6):
				self.unitsArray.append(str(lineArray[0]))
				self.unitsArray.append(str(lineArray[1]))
			elif (i >= 8):
				self.timeArray.append(int(lineArray[0]))
				self.dataArray.append(int(lineArray[1]))

	def minMax(self):
		returnArray = []
		self.maxArray = []
		self.minArray = []
		self.maxValue = int(self.dataArray[0])
		self.minValue = int(self.dataArray[0])
		self.maxTime = int()
		self.minTime = int()

		i = int(0)
		for eachElement in self.dataArray:
			print(("Data: " + str(eachElement) + " ; Time: " + str(self.timeArray[i])))

			if (eachElement <= self.minValue):
				self.minValue = eachElement
				self.minTime = self.timeArray[i]
			if (eachElement >= self.maxValue):
				self.maxValue = eachElement
				self.maxTime = self.timeArray[i]
			i += 1
		print(("MaxValue: " + str(self.maxValue) + " ; MinValue: " + str(self.minValue)))

		self.minArray.append(self.minValue)
		self.minArray.append(self.minTime)
		self.maxArray.append(self.maxValue)
		self.maxArray.append(self.maxTime)
		returnArray.append(self.minArray)
		returnArray.append(self.maxArray)
		return(returnArray)

	def units(self):
		return(self.unitsArray)

	def trend(self):
		self.difference = self.dataArray[0] - (self.dataArray[len(self.dataArray) - 1])
		return (self.difference)

	def startEnd(self):
		startEndArray = []
		startValue = self.dataArray[0]
		endValue = self.dataArray[len(self.dataArray) - 1]
		startEndArray.append(startValue)
		startEndArray.append(endValue)
		return(startEndArray)



def main():
	path = sys.argv[1]
	print(("Path: " + path))
	data = dataSet(path, "\t")
	data.readData()
	minMaxArray = data.minMax()
	unitsArray = data.units()
	startEndArray = data.startEnd()
	minArray = minMaxArray[0]
	maxArray = minMaxArray[1]
	if (startEndArray[0] < startEndArray[1]):
		print("Trend: rising")
	elif (startEndArray[0] > startEndArray[1]):
		print("Trend: falling")
	print(("MinValue: " + str(minArray[0]) + " " + unitsArray[1] + " ; at time: " + str(minArray[1]) + " " + unitsArray[0]))
	print(("MaxValue: " + str(maxArray[0]) + " " + unitsArray[1] + " ; at time: " + str(maxArray[1]) + " " + unitsArray[0]))

main()
