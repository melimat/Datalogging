# -*- coding: utf-8 -*-
#import matplotlib.pyplot as plt

#inputFilePath = str(input("Here type (paste) your path to source of data (file): "))
inputFilePath = "Z:\Dev\Python\TXT\Dostalova_Havlikova.txt"

labelLine = 6
xLabelText = "Time"
yLabelText = "Concentration of CO2"
graphLabel = "Graph of concentration of CO2"
dataStartLine = 8
splitter = "\t"

def plotFunction(path, xLabelText, yLabelText, graphLabel,  dataStartLine, labelLine, splitter):
    numberOfLine = int()
    xArray = []
    yArray = []
    sourceFile = open(path, "r")
    for eachLine in sourceFile:
        numberOfLine += 1
        print ((numberOfLine, ".", "Line: ", eachLine))
        if (numberOfLine == labelLine):
            line = eachLine
            labelArray = line.split(splitter)
            plt.xlabel(xLabelText + " [" + labelArray[0] + "]")
            plt.ylabel(yLabelText + " [" + labelArray[1] + "]")
            print (line)
        if (numberOfLine >= dataStartLine):
            line = eachLine
            lineArray = line.split("\t")
            xArray.append(lineArray[0])
            yArray.append(lineArray[1])
            print(line)
    plt.plot(xArray, yArray)
    plt.title(graphLabel)
    plt.show()

plotFunction(inputFilePath, xLabelText, yLabelText, graphLabel, dataStartLine, labelLine,splitter)
