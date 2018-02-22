import numpy as np
import pandas as pd
import os
FOLDER_PATH = os.path.dirname(os.path.realpath(__file__))
DATA_PATH = os.path.join(FOLDER_PATH, "data\EC\A4.txt")

with open(DATA_PATH) as f:
    rawData = f.read()

rawData = rawData.split('\n')
data, y = ([] for i in range(2))

for i in range(len(rawData)):
    if i == 0 or i == 1 or i == 2 or i == 3:
        continue
    data.append(rawData[i])

for i in range(len(data)):
    data[i] = data[i].split("\t")

np.save('test.npy', data)
df = pd.DataFrame(data, columns=['Time(ms)', 'Voltage(µV)'])
filename = os.path.join(FOLDER_PATH, "data\A4.h5")
# Save to HDF5
df.to_hdf(filename, 'data', mode='w', format='table')
del df    # allow df to be garbage collected
print(pd.read_hdf(filename, 'data'))