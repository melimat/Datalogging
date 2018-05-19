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
				self.unitsArray.append(lineArray[0])
				self.unitsArray.append(lineArray[1])
			elif (i >= 8):
				self.timeArray.append(lineArray[0])
				self.dataArray.append(lineArray[1])

	def minMax(self):
		returnArray = []
		self.maxArray = []
		self.minArray = []
		self.maxValue = int(self.dataArray[0])
		self.minValue = int()
		self.maxTime = int()
		self.minTime = int()

		i = int(0)
		for eachElement in self.dataArray:
			print(("Data: " + str(eachElement) + " ; Time: " + str(self.timeArray[i])))

			if (i == 1):
				self.minValue = self.dataArray[0]
				self.maxValue = self.dataArray[0]

			if (eachElement < self.minValue):
				self.minValue = eachElement
				self.minTime = self.timeArray[i]
			elif(eachElement > self.maxValue):
				self.maxValue = eachElement
				self.maxTime = self.timeArray[i]
			i += 1

		self.minArray.append(self.minValue)
		self.minArray.append(self.minTime)
		self.maxArray.append(self.maxValue)
		self.maxArray.append(self.maxTime)
		returnArray.append(self.minArray)
		returnArray.append(self.maxArray)
		return(returnArray)

	def units(self):
		return(self.unitsArray)


def main():
	path = sys.argv[1]
	print(("Path: " + path))
	data = dataSet(path, "\t")
	data.readData()
	minMaxArray = data.minMax()
	unitsArray = data.units()
	minArray = minMaxArray[0]
	maxArray = minMaxArray[1]
	print(("MinValue: " + str(minArray[0]) + " " + unitsArray[1] + " ; at time: " + str(minArray[1]) + " " + unitsArray[0]))
	print(("MaxValue: " + str(maxArray[0]) + " " + unitsArray[1] + " ; at time: " + str(maxArray[1]) + " " + unitsArray[0]))

main()