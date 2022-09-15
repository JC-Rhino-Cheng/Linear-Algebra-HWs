
# coding: utf-8

# In[3]:

import matplotlib.pyplot as plt
import numpy as np
import scipy.io.wavfile as wf
import scipy.fftpack as fft
import math

# please implement your own restore function, no global variables are allowed to be used
def restore(compressed):
    # inverse dct: idct
    div = 107252 / 0.5
    data0_2 = fft.idct(compressed)/div
    restored = data0_2.astype('int16')

    plt.figure()
    plt.plot(restored)
    plt.show()

    return restored

# data, compressed and restored are expedted to be 1D numpy arrays
def score(data, compressed):
    data = data.astype("float64")
    ratio = (compressed.shape[0] * compressed.itemsize) / (data.shape[0] * data.itemsize)

    restored = restore(compressed).astype('float64')

    if data.shape[0] != restored.shape[0]:
        print('restoration failed!')
        exit(0)

    value = np.inner(data, restored) / (np.linalg.norm(data) * np.linalg.norm(restored))
    radian = np.arccos(value)
    radian = min(radian, 1.57079632679)
    error = np.sin(radian)

    print(ratio)
    print(error)
    print(ratio + error)

# read in the sound data
rate, data = wf.read("sound1.wav")

# data0 is the data from channel 0.
data0 = data[:, 0]

# perform dct
data0_1 = fft.dct(data0)

# do some filtering
data0_1[0:5000] = 0
data0_1[10000:] = 0

# show some plots
plt.plot(data0)
plt.show()

print(data0_1.dtype)
score(data0, data0_1)
