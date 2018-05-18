# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import sys
import os

class configFile:
    def __init__(self, path):
        self.path = path
    def open(self):
        self.pathFile = open(self.path, "r")
    def pathsToArray(self):
        self.pathsArray = []
        for eachLine in self.pathFile:
            self.pathsArray.append(eachLine)
        return(self.pathsArray)
    def fileNames(self):
        nameArray = []
        elementArray = []
        for eachElement in self.pathsArray:
            elementArray = eachElement.split("/")
            nameArray.append(elementArray[len(elementArray) - 1])
        return(nameArray)
    def close(self):
        self.pathFile.close()

class parser:
    def __init__(self, path, splitter):
        self.path = path
        self.splitter = splitter
    def open(self):
        self.inputFile = open(self.path, "r")
    def parseData(self):
        i = int(0)
        outputArray = []
        self.unitsArray = []
        XArray = []
        YArray = []
        for eachLine in self.inputFile:
            i += 1
            if (i == 6):
                print (eachLine)
                lineArray = eachLine.split(self.splitter)
                self.unitsArray.append(lineArray[0])
                self.unitsArray.append(lineArray[1])
            elif(i >= 8):
                print(eachLine)
                lineArray = eachLine.split(self.splitter)
                print(lineArray[0])
                print(lineArray[1])
                XArray.append(lineArray[0])
                YArray.append(lineArray[1])
        outputArray.append(XArray)
        outputArray.append(YArray)
        return(outputArray)
    def units(self):
        return(self.unitsArray)
    def close(self):
        self.inputFile.close()

class graphComposer:

    def __init__(self, pathStr, XArray, YArray):
        self.pathStr = pathStr
        self.XArray = XArray
        self.YArray = YArray
        figArray = self.pathStr.split("/")
        self.figName = figArray[len(figArray) - 1]
    def composeLabels(self, XText, XUnit, YText, YUnit):
        self.XLabel = str(XText + " " + "[" + XUnit + "]")
        self.YLabel = str(YText + " " + "[" + YUnit + "]")
    def composeTitle(self, title):
        self.title = str(title)
    def composeLegend(self):
        self.legendText = str("Source: " + self.figName)
    def generateGraph(self):
        plt.xlabel(self.XLabel)
        plt.ylabel(self.YLabel)
        plt.title(self.title)
        plt.plot(self.XArray, self.YArray, label = self.legendText)
        plt.legend()
        currentFig = plt.gcf()
        plt.show()
        fileName = self.figName.split(".")
        name = fileName[0]
        currentFig.savefig(name)

def main():
	configPath = sys.argv[1]
	XLabelText = sys.argv[2]
	YLabelText = sys.argv[3]
	Title = sys.argv[4]
	Splitter = "\t"
	#Splitter = (sys.argv[5])
	print(sys.argv[5])
	
	pathsFile = configFile(configPath)
	pathsFile.open()
	pathsArray = pathsFile.pathsToArray()
	nameArray = pathsFile.fileNames()
	pathsFile.close()
	
	
	i = int(0)
	for eachElement in pathsArray:
	    dirArray = eachElement.split("\n")
	    directory = dirArray[0]
	    print (directory)
	    parse = parser(directory, Splitter)
	    parse.open()
	    plotArray = parse.parseData()
	    unitsArray = parse.units()
	    parse.close()
	    graph = graphComposer(nameArray[i], plotArray[0], plotArray[1])
	    graph.composeLabels(XLabelText, unitsArray[0], YLabelText, unitsArray[1])
	    graph.composeTitle(Title)
	    graph.composeLegend()
	    graph.generateGraph()
	    i += 1
	
main()