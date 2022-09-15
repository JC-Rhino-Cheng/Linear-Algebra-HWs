import matplotlib.pyplot as plt
import numpy as np
import scipy.io.wavfile as wf
import scipy.fftpack as fft
import math

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
rate1, data1_1 = wf.read("Laugh track 1.wav", True)
rate2, data2_1 = wf.read("Tympani roll 1.wav", True)
rate3, data3_1 = wf.read("Navigational Instrument, Loran, sonar, navigator, radar,.wav", True)


# data0 is the data from channel 0.
data1 = data1_1[:]
#data2 = data2_1[:, 0] //因為上面有True，所以改掉會錯，但是因為助教說評分用的聲音檔案的只有單聲道，所以要改成下面那行那樣
data2 = data2_1[:]
data3 = data3_1[:]

# perform dct
data1_1 = fft.dct(data1)
data2_1 = fft.dct(data2)
data3_1 = fft.dct(data3)
## Added code by myself
average1_1 = np.mean(np.abs(data1_1))
average2_1 = np.mean(np.abs(data2_1))
average3_1 = np.mean(np.abs(data3_1))


# do some filtering
threshold1_1 = average1_1 * 0.95;
temp1_1 = []; countZeroes1_1 = 0
temp1_1.append(len(data1_1))
for i in range(len(data1_1)):
    if abs(data1_1[i]) <= threshold1_1:
        countZeroes1_1 += 1
    else:
        if countZeroes1_1 != 0:
            temp1_1.append(0)
            temp1_1.append(countZeroes1_1)
            countZeroes1_1 = 0
        temp1_1.append(data1_1[i])
if countZeroes1_1 != 0:
    temp1_1.append(0)
    temp1_1.append(countZeroes1_1)
done1_1 = np.array(temp1_1)
##############################
threshold2_1 = average2_1 * 0.95;
temp2_1 = []; countZeroes2_1 = 0
temp2_1.append(len(data2_1))
for i in range(len(data2_1)):
    if abs(data2_1[i]) <= threshold2_1:
        countZeroes2_1 += 1
    else:
        if countZeroes2_1 != 0:
            temp2_1.append(0)
            temp2_1.append(countZeroes2_1)
            countZeroes2_1 = 0
        temp2_1.append(data2_1[i])
if countZeroes2_1 != 0:
    temp2_1.append(0)
    temp2_1.append(countZeroes2_1)
done2_1 = np.array(temp2_1)
##############################
threshold3_1 = average3_1 * 0.95;
temp3_1 = []; countZeroes3_1 = 0
temp3_1.append(len(data3_1))
for i in range(len(data3_1)):
    if abs(data3_1[i]) <= threshold3_1:
        countZeroes3_1 += 1
    else:
        if countZeroes3_1 != 0:
            temp3_1.append(0)
            temp3_1.append(countZeroes3_1)
            countZeroes3_1 = 0
        temp3_1.append(data3_1[i])
if countZeroes3_1 != 0:
    temp3_1.append(0)
    temp3_1.append(countZeroes3_1)
done3_1 = np.array(temp3_1)





# show some plots
#plt.plot(data0)
#plt.show()
#data1_2 = score(data1, done1_1)
#data2_2 = score(data2, done2_1)
#data3_2 = score(data3, done3_1)


# write file back
#wf.write("ExampleSound_processed.wav", rate0, data0_2)
#wf.write("1_processed.wav", rate1, data1_2)
#wf.write("2_processed.wav", rate2, data2_2)
#wf.write("3_processed.wav", rate3, data3_2)

# show some plots
#plt.plot(data0)
#plt.show()
#plt.figure()
#plt.plot(data0_2)
#plt.show()


score(data1, done1_1)
score(data2, done2_1)
score(data3, done3_1)
