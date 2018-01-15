""" plot.py

Simple example showing how to load and plot spike trains and their distance
profiles.

Copyright 2014, Mario Mulansky <mario.mulansky@gmx.net>

Distributed under the BSD License
"""


from __future__ import print_function

import numpy as np
import matplotlib.pyplot as plt

import pyspike as spk

import os
FOLDER_PATH = "C:\\Users\\jonat\\PycharmProjects\\PySpike\\examples\\data from brewer's lab"
DATA_PATH = os.path.join(FOLDER_PATH, "PySpike_testdata - Copy.txt")

spike_trains = spk.load_spike_trains_from_txt(DATA_PATH,
                                              edges=(0, 4000))
print(spike_trains)

# plot the spike times
'''for (i, spike_train) in enumerate(spike_trains):
    plt.scatter(spike_train, i*np.ones_like(spike_train), marker='|')'''

# profile of the first two spike trains
f = spk.isi_profile(spike_trains, indices=[0, 2])
x, y = f.get_plottable_data()

plt.figure()
plt.plot(x, np.abs(y), '-k')

print(x, y)

print("ISI-distance: %.8f" % f.avrg())

plt.xlabel("Time (ms)")
plt.ylabel("Voltage (µV)")
plt.legend(loc="upper left")

plt.show()