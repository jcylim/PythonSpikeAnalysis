""" graph.py

Created by Jonathan Lim to process data from MATLAB

"""

from __future__ import print_function

import numpy as np
import matplotlib.pyplot as plt

import os
DEFAULT_PATH = os.path.dirname(os.path.realpath(__file__))
FOLDER_PATH = os.path.join(DEFAULT_PATH, "data\\EC")
DATA_PATH = os.path.join(FOLDER_PATH, "A4.txt")

with open(DATA_PATH) as f:
    rawData = f.read()

rawData = rawData.split('\n')
data, x, y = ([] for i in range(3))

for i in range(len(rawData)):
    if i == 0 or i == 1 or i == 3:
        continue
    data.append(rawData[i])

for i in range(len(data)):
    data[i] = data[i].split("\t")
    if i == 0:
        continue
    x.append(data[i][0])
    y.append(float(data[i][1]))

#graphing voltage at each electrode
'''plt.figure()
plt.plot(x, y, '-b', label=data[0][1])

plt.xlabel("Time (ms)")
plt.ylabel("Voltage (µV)")
#plt.ylim(-10, 10)
plt.legend(loc="upper center")
plt.show()'''