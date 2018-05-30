""" graph.py

Created by Jonathan Lim to process data from MATLAB

"""

from __future__ import print_function

import numpy as np
import math
from sklearn.linear_model import LinearRegression
from scipy import stats
from scipy.stats import norm
import matplotlib.mlab as mlab
from scipy import signal
from nose.tools import *
import matplotlib.pyplot as plt
import struct
import quickspikes as qs
from bokeh.plotting import figure, output_file, show

import os
DEFAULT_PATH = os.path.dirname(os.path.realpath(__file__))

data, x, y, spikeValues, isi, processed_hist, graph_hist = ([] for i in range(7))

def analysis(folder, filename):
    folderPath = "data\\" + folder
    filePath = filename + ".txt"
    FOLDER_PATH = os.path.join(DEFAULT_PATH, folderPath)
    DATA_PATH = os.path.join(FOLDER_PATH, filePath)

    with open(DATA_PATH) as f:
        rawData = f.read()

    rawData = rawData.split('\n')

    for i in range(len(rawData)):
        if i == 0 or i == 1 or i == 3:
            continue
        data.append(rawData[i])

    for i in range(len(data) - 1):
        data[i] = data[i].split("\t")
        if i == 0:
            continue
        x.append(float(data[i][0]))
        y.append(float(data[i][1]))

    prepare4Analysis(filename, y)

def prepare4Analysis(filename, y):
    npyFile = filename + ".npy"
    np.save(npyFile, y)
    thres = -3 * y[3749999]
    loadedData = np.load(npyFile)
    det = qs.detector(thres, 1000)  # quickspikes function
    times = det.send(loadedData)  # quickspikes function
    # spikes = qs.peaks(np.load('A4.npy'), times, 30, 30) #quickspikes function
    # print(spikes)
    for i in range(len(times)):
        if i == (len(times) - 1):
            break
        isi.append(times[i + 1] - times[i])
    #print("Spike Time Indices:", times)
    if len(times) != 0:
        for t in range(len(times)):
            spikeValues.append(y[times[t]])
    #print("Spike Voltage Values:", spikeValues)
    # data filter
    for time in isi:
        if time < 5:
            isi.remove(time)

    isiAnalysis(filename, isi)

#graphing spikes vs ISI histogram (log scale)
def isiAnalysis(filename, isi):
    processed_edges = []
    tempCountValue = 0
    output_file(filename + ".html", title=filename)
    p1 = figure(title="ISI Histogram for" + filename, background_fill_color="#E8DDCB", plot_width=1200, plot_height=850,
                y_axis_type="log", x_axis_type="log")  # y_axis_type="log", x_axis_type="log",
    hist, edges = np.histogram(isi, density=True, bins=np.logspace(np.log10(1), np.log10(100),
                                                                   100))  # hist = y, and edges = x; density=True shows probability
    p1.quad(top=hist, bottom=0.001, left=edges[:-1], right=edges[1:],
            fill_color="#036564", line_color="#033649")
    for value in edges:
        processed_edges.append(int(value))
    count = {i: processed_edges.count(i) for i in processed_edges}
    count = list(count.values())
    processed_edges = list(set(processed_edges))
    processed_edges.remove(1)
    processed_edges.remove(2)
    processed_edges.remove(3)
    processed_edges.remove(4)
    processed_edges.remove(100)
    print(len(processed_edges), processed_edges)
    for i in range(len(count)):
        histSum = 0
        for j in range(count[i]):
            histSum = histSum + hist[tempCountValue + j]
        processed_hist.append(histSum / count[i])
        tempCountValue = tempCountValue + count[i]
        if tempCountValue == 99:
            break
    processed_hist.pop(0)
    processed_hist.pop(1)
    processed_hist.pop(2)
    processed_hist.pop(3)
    print(len(processed_hist), processed_hist)
    logEdges = np.log(processed_edges)
    logHist = np.log(processed_hist)
    slope, intercept, r_value, p_value, std_err = stats.linregress(logEdges, logHist)
    print("slope: ", slope)
    print("intercept: ", intercept)
    graph_hist = np.exp(slope * logEdges + intercept)
    #print(graph_hist)
    # p1.circle(processed_edges, graph_hist, size=10, color="navy", alpha=0.5)
    p1.line(processed_edges, graph_hist, line_color="#D95B43", line_width=6,
            legend="Fitted Line")  # alpha parameter makes the line transparent (e.g. alpha=0.7)
    p1.legend.location = "center_right"
    p1.legend.background_fill_color = "darkgrey"
    p1.xaxis.axis_label = 'ISI (Log-Scaled)'  # label milliseconds
    p1.yaxis.axis_label = 'ISI Probability Distribution (Log-Scaled)'
    show(p1)

# main program
if __name__ == "__main__":
    while 1:
        folder = input("Which chamber would you like to graph? 1) EC 2) DG 3) CA1 4) CA3\n")
        if folder == "EC" or folder == "DG" or folder == "CA1" or folder == "CA3":
            filename = input("Which electrode in " + folder + " would you like to graph?\n")
            if type(filename) != str:
                print("Please input a valid file name.")
            else:
                analysis(folder, filename)
                print("ISI histogram for " + filename + " electrode in " + folder + " generated!\n")
        else:
            print("Please input a valid folder name.")

'''plt.hist(isi, normed=True, bins=np.logspace(np.log10(1), np.log10(100), 100), log=True)
plt.plot(processed_edges, graph_hist, 'r', label='fitted line')
plt.xscale('log')
plt.legend()
plt.show()'''
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
