""" graph.py

Created by Jonathan Lim to process data from MATLAB

"""

from __future__ import print_function

import numpy as np
import matplotlib.pyplot as plt
from bokeh.plotting import figure, output_file, show

import os
DEFAULT_PATH = os.path.dirname(os.path.realpath(__file__))
FOLDER_PATH = os.path.join(DEFAULT_PATH, "data\\EC")
DATA_PATH = os.path.join(FOLDER_PATH, "A4.txt")

with open(DATA_PATH) as f:
    rawData = f.read()

rawData = rawData.split('\n')
data, x, y = ([] for i in range(3))
testX, testY = ([] for i in range(2))

for i in range(len(rawData)):
    if i == 0 or i == 1 or i == 3:
        continue
    data.append(rawData[i])

for i in range(len(data)-1):
    data[i] = data[i].split("\t")
    if i == 0:
        continue
    x.append(float(data[i][0]))
    y.append(float(data[i][1]))

#graphing dataset with Bokeh
output_file("A4.html", title="A4")
p = figure(plot_width=1000, plot_height=700)
p.xaxis.axis_label = "Time (ms)"
p.yaxis.axis_label = "Voltage (µV)"
'''for i in range(4000000):
    testX.append(x[i])
    testY.append(y[i])'''
# add a line renderer
p.line(x, y, line_width=2)
show(p)

#graphing dataset with pyplot
'''plt.figure()
plt.plot(x, y, '-b', label=data[0][1])
plt.xlabel("Time (ms)")
plt.ylabel("Voltage (µV)")
#plt.ylim(-10, 10)
plt.legend(loc="upper center")
plt.show()'''

'''if __name__ == "__main__":
    while 1:
        folder = input("Which chamber would you like to graph? 1) EC 2) DG 3) CA1 4) CA3")
        if type(folder)!= str:
            print("Please input a valid file name.")
        else:
            output_file(filename + ".html", title=filename)
        filename = input("Which electrode would you like to graph? ")
        if type(filename)!= str:
            print("Please input a valid file name.")
        else:
            output_file(filename + ".html", title=filename)'''