# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt

#fileDirectory = str(input("Here type your logfile directory: "))
fileDirectory = "/home/melimat/Dev/Python/log.txt"

global logfile
logfile = file(fileDirectory, "r")


def plotFunction():
    data = logfile.read()
    dataArray = data.split("\n")
    time = int(0)
    plotData = []
    timeData = []
    for eachLine in dataArray:
        if (len(eachLine) > 1):
            time += 1
            plotData.append(eachLine)
            timeData.append(time)
    plt.plot(timeData, plotData)
    plt.title("Logged data graph")
    plt.xlabel("Time")
    plt.ylabel("Data")
    plt.show()

plotFunction()

