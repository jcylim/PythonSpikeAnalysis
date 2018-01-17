""" parser.py

Created by Jonathan Lim to process data from MATLAB

"""


from __future__ import print_function

import numpy as np
import matplotlib.pyplot as plt

import os
DEFAULT_PATH = os.path.dirname(os.path.realpath(__file__))
FOLDER_PATH = os.path.join(DEFAULT_PATH, "data from brewer's lab")
DATA_PATH = os.path.join(FOLDER_PATH, "test.txt")

with open(DATA_PATH) as f:
    rawData = f.read()

rawData = rawData.split('\n')
data, x, y1, y2, y3, y4, y5, y6, y7, y8, y9, y10, y11, y12, y13, y14, y15, y16, y17, y18, y19 = ([] for i in range(21))

for i in range(len(rawData)):
    if i == 0 or i == 1 or i == 3:
        continue
    data.append(rawData[i])

for i in range(len(data)):
    data[i] = data[i].split("\t")
    if i == 0:
        continue
    x.append(data[i][0])
    y1.append(float(data[i][1]))
    y2.append(float(data[i][2]))
    y3.append(float(data[i][3]))
    y4.append(float(data[i][4]))
    y5.append(float(data[i][5]))
    y6.append(float(data[i][6]))
    y7.append(float(data[i][7]))
    y8.append(float(data[i][8]))
    y9.append(float(data[i][9]))
    y10.append(float(data[i][10]))
    y11.append(float(data[i][11]))
    y12.append(float(data[i][12]))
    y13.append(float(data[i][13]))
    y14.append(float(data[i][14]))
    y15.append(float(data[i][15]))
    y16.append(float(data[i][16]))
    y17.append(float(data[i][17]))
    y18.append(float(data[i][18]))
    y19.append(float(data[i][19]))

#graphing voltage at each electrode
plt.figure()
plt.plot(x, y1, '-b', label=data[0][1])
plt.plot(x, y2, '-g', label=data[0][2])
plt.plot(x, y3, '-r', label=data[0][3])
plt.plot(x, y4, '-c', label=data[0][4])
plt.plot(x, y5, '-m', label=data[0][5])
plt.plot(x, y6, '-y', label=data[0][6])
plt.plot(x, y7, '-k', label=data[0][7])
plt.plot(x, y8, '--b', label=data[0][8])
plt.plot(x, y9, '--g', label=data[0][9])
plt.plot(x, y10, '--r', label=data[0][10])
plt.plot(x, y11, '--c', label=data[0][11])
plt.plot(x, y12, '--m', label=data[0][12])
plt.plot(x, y13, '--y', label=data[0][13])
plt.plot(x, y14, '--k', label=data[0][14])
plt.plot(x, y15, ':b', label=data[0][15])
plt.plot(x, y16, ':g', label=data[0][16])
plt.plot(x, y17, ':r', label=data[0][17])
plt.plot(x, y18, ':c', label=data[0][18])
plt.plot(x, y19, ':m', label=data[0][19])

plt.xlabel("Time (ms)")
plt.ylabel("Voltage (µV)")
plt.ylim(-10, 10)
plt.legend(loc="upper center", ncol=5)
plt.show()