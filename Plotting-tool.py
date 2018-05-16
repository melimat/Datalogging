# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt

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
    def __init__(self, path):
        self.path = path
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
                lineArray = eachLine.split("\t")
                self.unitsArray.append(lineArray[0])
                self.unitsArray.append(lineArray[1])
            elif(i >= 8):
                print(eachLine)
                lineArray = eachLine.split("\t")
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







pathsFile = configFile("/home/melimat/Documents/CO2/Paths.txt")
pathsFile.open()
pathsArray = pathsFile.pathsToArray()
nameArray = pathsFile.fileNames()
pathsFile.close()


i = int(0)
for eachElement in pathsArray:
    dirArray = eachElement.split("\n")
    directory = dirArray[0]
    print (directory)
    parse = parser(directory)
    parse.open()
    plotArray = parse.parseData()
    unitsArray = parse.units()
    plt.xlabel(unitsArray[0])
    plt.ylabel(unitsArray[1])
    XArray = plotArray[0]
    YArray = plotArray[1]
    plt.plot(XArray, YArray, label = "Source: " + nameArray[i] )
    plt.legend()
    #plt.show()
    picNameArray = nameArray[i].split(".")
    picName = picNameArray[0]
    plt.savefig(picName)
    parse.close()
    i += 1

