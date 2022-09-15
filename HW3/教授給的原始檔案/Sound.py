
# coding: utf-8

# In[3]:


import matplotlib.pyplot as plt
import numpy as np
import scipy.io.wavfile as wf
import scipy.fftpack as fft
import math

# read in the sound data
rate, data = wf.read("sound1.wav")

# data0 is the data from channel 0.
data0 = data[:, 0]

# perform dct
data0_1 = fft.dct(data0)

# do some filtering
data0_1[0:5000] = 0
data0_1[10000:] = 0

# inverse dct: idct
div = 107252/2
data0_2 = fft.idct(data0_1)/div
data0_2 = data0_2.astype('int16')

# write file back
wf.write("sound2.wav", rate, data0_2)

# show some plots
plt.plot(data0)
plt.show()
plt.figure()
plt.plot(data0_2)
plt.show()

