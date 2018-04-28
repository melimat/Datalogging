# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt, serial as ser
logger = ser.Serial('/dev/ttyACM0', 9600, timeout=.1)
while True:
    string = logger.readline()[:-2]
    if string:
        print (string)
