import matplotlib.pyplot as plt
import numpy as np
import scipy.io.wavfile as wf
import scipy.fftpack as fft
import math
import copy

# please implement your own restore function, no global variables are allowed to be used
def restore(compressed):

    length = compressed[0]
    temp = []
    idx_for_compressed = 1

    while idx_for_compressed < len(compressed):
        if compressed[idx_for_compressed] != 0:
            temp.append(compressed[idx_for_compressed])
            idx_for_compressed += 1
            continue
        else:
            idx_for_compressed += 1
            num = int(compressed[idx_for_compressed])
            list_of_zeroes_to_append = [0 for i in range(num)]  
            temp[len(temp):] = list_of_zeroes_to_append[:]
            idx_for_compressed += 1
            continue


    # inverse dct: idct
    div = length / 0.5
    data0_2 = fft.idct(temp)/div
    restored = data0_2.astype('int16')

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
rate0, exampleSound = wf.read("sound1.wav")

# data0 is the data from channel 0.
data0 = exampleSound[:]

# perform dct
data0_1 = fft.dct(data0)
## Added code by myself
average0_1 = np.mean(np.abs(data0_1))


# do some filtering
#data0_1[0:5000] = 0
#data0_1[10000:] = 0



# show some plots
plt.plot(data0)
plt.show()
data0_2 = restore(data0_1)
plt.figure()
plt.plot(data0_2)
plt.show()

# write file back
#wf.write("ExampleSound_processed.wav", rate0, data0_2)

# show some plots
#plt.plot(data0)
#plt.show()
#plt.figure()
#plt.plot(data0_2)
#plt.show()

