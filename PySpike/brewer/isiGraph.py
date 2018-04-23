""" graph.py

Created by Jonathan Lim to process data from MATLAB

"""

from __future__ import print_function

import numpy as np
from scipy import signal
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
data, x, y, spikeValues, isi = ([] for i in range(5))

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

np.save('A4.npy', y)
thres = -3*y[3749999]
loadedData = np.load('A4.npy')
det = qs.detector(thres, 1000) #quickspikes function
times = det.send(loadedData) #quickspikes function
#spikes = qs.peaks(np.load('A4.npy'), times, 30, 30) #quickspikes function
#print(spikes)
for i in range(len(times)):
    if i == (len(times)-1):
        break
    isi.append(times[i+1] - times[i])
print("Spike Time Indices:", times)
if len(times) != 0:
    for t in range(len(times)):
        spikeValues.append(y[times[t]])
print("Spike Voltage Values:", spikeValues)

#graphing spikes vs ISI histogram (log scale)
output_file("A4.html", title="A4")
p1 = figure(title="ISI Histogram", background_fill_color="#E8DDCB", plot_width=1200, plot_height=850, y_axis_type="log", x_axis_type="log")
hist, edges = np.histogram(isi, density=True, bins=np.logspace(np.log10(1),np.log10(100), 100)) #hist = y, and edges = x; density=True shows probability
p1.quad(top=hist, bottom=0.001, left=edges[:-1], right=edges[1:],
        fill_color="#036564", line_color="#033649")
p1.legend.location = "center_right"
p1.legend.background_fill_color = "darkgrey"
p1.xaxis.axis_label = 'ISI (Log Scale)'
p1.yaxis.axis_label = 'ISI Probability Distribution (Log Scale)'
show(p1)

#graphing spikes vs ISI histogram
'''output_file("A4.html", title="A4")
p1 = figure(title="ISI Histogram", background_fill_color="#E8DDCB", plot_width=1200, plot_height=850)
hist, edges = np.histogram(isi, density=False, bins=10) #hist = y, and edges = x; density=False shows probability
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
