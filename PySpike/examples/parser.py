""" parser.py

Created by Jonathan Lim to process data from MATLAB

"""


from __future__ import print_function

import numpy as np
import matplotlib.pyplot as plt

import pyspike as spk

import os
FOLDER_PATH = "C:\\Users\\jonat\\PycharmProjects\\PySpike\\examples\\data from brewer's lab"
DATA_PATH = os.path.join(FOLDER_PATH, "test.txt")

with open(DATA_PATH) as f:
    rawData = f.read()

rawData = rawData.split('\n')
for i in rawData.

    rawData.append(i)

'''plt.figure()
plt.plot(x, np.abs(y), '-k', "test")

plt.xlabel("Time (ms)")
plt.ylabel("Voltage (µV)")
plt.legend(loc="upper left")

plt.show()'''