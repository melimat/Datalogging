# -*- coding: utf-8 -*-
#import matplotlib.pyplot as plt

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
            elementArray = eachElement.split("\\")
            nameArray.append(elementArray[len(elementArray) - 1])
        return(nameArray)
    def close(self):
        self.pathFile.close()

class parser:
    def __init__(self, path):
        self.path = path
    def open(self):
        self.inputFile = open(self.path, "r")
    def parseData(self):
        i = int(0)
        outputArray = []
        XArray = []
        YArray = []
        for eachLine in self.inputFile:
            i += 1
            if(i >= 8):
                print(eachLines)
                lineArray = eachLine.split("\t")
                XArray.append(lineArray[0])
                YArray.append(lineArray[1])
        outputArray.append(XArray)
        outputArray.append(YArray)
        return(outputArray)
    def units(self):
        i = int(0)
        unitsArray = []
        for eachLine in self.inputFile:
            i += 1
            if(i == 6):
                print (eachLine)
                lineArray = eachLine.split("\t")
                unitsArray.append(lineArray[0])
                unitsArray.append(lineArray[1])
        return(unitsArray)
    def close(self):
        self.inputFile.close()







pathsFile = configFile("Z:\Dev\Python\paths.txt")
pathsFile.open()
pathsArray = pathsFile.pathsToArray()
nameArray = pathsFile.fileNames()
pathsFile.close()

for eachElement in pathsArray:
    dirArray = eachElement.split("\n")
    directory = dirArray[0]
    print (directory)
    parse = parser(directory)
    parse.open()
    unitsArray = parse.units()
    plotArray = parse.parseData()
    XArray = plotArray[0]
    YArry = plotArray[1]
    for eachElement in XArray:
        print (eachElement)
    for eachElement in YArray:
        print (eachElement)
    parse.close()
