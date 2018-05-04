# -*- coding: utf-8 -*-
import serial as ser
#serialPort = str(input("Here type your serial port directory:"))
#filename = str(input("Here type your logfile directory:"))
global times
#times = str(input("How many lines of data you want to collect?: "))
serialPort = "/dev/ttyACM0"
filename = "/home/melimat/Dev/Python/log.txt"
times = 50

global logger
logger = ser.Serial(serialPort, 9600, timeout=.1)

global time
time = int(0)

logfile = file(filename, "w")


def logFunction():
    global time, logger
    while(time <= times):
        time += 1
        data = logger.readline()
        if data:
            logfile.write(data)
            print (data)
logFunction()


