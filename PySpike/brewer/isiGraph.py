""" graph.py

Created by Jonathan Lim to process data from MATLAB

"""

from __future__ import print_function

import numpy as np
from nose.tools import *
import matplotlib.pyplot as plt
import struct
import quickspikes as qs
from bokeh.plotting import figure, output_file, show

import os
DEFAULT_PATH = os.path.dirname(os.path.realpath(__file__))
FOLDER_PATH = os.path.join(DEFAULT_PATH, "data\\EC")
DATA_PATH = os.path.join(FOLDER_PATH, "A4.txt")

with open(DATA_PATH) as f:
    rawData = f.read()

rawData = rawData.split('\n')
<<<<<<< HEAD
data, x, y, spikeValues = ([] for i in range(4))
=======
data, x, y = ([] for i in range(3))
testX, testY = ([] for i in range(2))
ba = bytearray()
>>>>>>> 021e8205062983a4f6fb4659330f045a153a9da6

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

<<<<<<< HEAD
np.save('A4.npy', y)
thres = -3*y[3749999]
det = qs.detector(thres, 1000) #quickspikes function
times = det.send(np.load('A4.npy')) #quickspikes function
#spikes = qs.peaks(np.load('A4.npy'), times, 30, 30) #quickspikes function
#print(spikes)
print("Spike Time Indices:", times)
if len(times) != 0:
    for t in range(len(times)):
        spikeValues.append(y[times[t]])
print("Spike Voltage Values:", spikeValues)

#graphing spikes vs ISI histogram
'''output_file("A4.html", title="A4")
p1 = figure(title="ISI Histogram",tools="save",
            background_fill_color="#E8DDCB", plot_width=1200, plot_height=850)
hist, edges = np.histogram(spikeValues, density=False, bins=100) #hist = y, and edges = x; density=False shows probability
p1.quad(top=hist, bottom=0, left=edges[:-1], right=edges[1:],
        fill_color="#036564", line_color="#033649")
p1.legend.location = "center_right"
p1.legend.background_fill_color = "darkgrey"
p1.xaxis.axis_label = 'ISI'
p1.yaxis.axis_label = 'Counts'
show(p1)'''

#graphing spikes vs voltage histogram
'''output_file("A4.html", title="A4")
p1 = figure(title="Amplitude Histogram",tools="save",
            background_fill_color="#E8DDCB", plot_width=1200, plot_height=850)
hist, edges = np.histogram(spikeValues, density=False, bins=100) #hist = y, and edges = x; density=False shows probability
p1.quad(top=hist, bottom=0, left=edges[:-1], right=edges[1:],
        fill_color="#036564", line_color="#033649")
p1.legend.location = "center_right"
p1.legend.background_fill_color = "darkgrey"
p1.xaxis.axis_label = 'Voltage (µV)'
p1.yaxis.axis_label = 'Counts'
show(p1)'''
=======
#graphing dataset with Bokeh
'''output_file("A4.html", title="A4")
p = figure(plot_width=1000, plot_height=700)
p.xaxis.axis_label = "Time (ms)"
p.yaxis.axis_label = "Voltage (µV)"'''
for i in range(10):
    testX.append(x[i])
    testY.append(y[i])
det = qs.detector(0, 100)
print(det)
times = det.send(np.array(testY))
print(det)
'''for val in testY:
    b = struct.pack('f', val)
    print(b)
print("final b: ", b)'''

# add a line renderer
'''p.line(x, y, line_width=2)
show(p)

#graphing dataset with pyplot
plt.figure()
plt.plot(x, y, '-b', label=data[0][1])
plt.xlabel("Time (ms)")
plt.ylabel("Voltage (µV)")
#plt.ylim(-10, 10)
plt.legend(loc="upper center")
plt.show()'''
>>>>>>> 021e8205062983a4f6fb4659330f045a153a9da6
