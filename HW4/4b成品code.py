import matplotlib.pyplot as plt
import numpy as np
import numpy.linalg as LA
import math

def getData(fname):
    import csv

    # -------- inner function of getData ------------
    def getValue(s):
        return 0 if not s else float(s) #"if not s" implies an empty string

    # -------- open data file ---------------------     
    with open(fname, newline='') as csvfile:
        # count the lines in CSV file
        N = sum(1 for line in csvfile) #數CSV有幾行
        
        # prepare the space for data
        X = np.zeros((N-1, 3)) #根據數來的N創建相應的N-1x2大小的X矩陣 (N-1是因為第一行的東西是廢棄的)

        # reset the file iterator
        csvfile.seek(0)

        # read the data from CSV file
        rows = csv.DictReader(csvfile)
        # the first line contains the titles
        i = 0
        for row in rows: #for迴圈把檔案裡的所有資訊填入X矩陣裡
            X[i,0] = getValue(row['W'])
            X[i,1] = getValue(row['H'])
            X[i,2] = getValue(row['Z'])
            i = i + 1

    return N-1, X #回傳總共有多少筆資料，以及矩陣

#------------- main -----------------

N, X = getData('data.csv') #接收總共有多少筆資料，以及矩陣

# compute means of W and H and Z
means = np.mean(X, axis= 0) #針對X矩陣的三個row(一個是Height一個是Weight一個是Z)分別計算平均
data_for_preparing_t = np.zeros((N,2)) #創建和一個2-col的矩陣，準備計算t
data_for_preparing_t[:,0] = [w - means[0] for w in X[:,0]]
data_for_preparing_t[:,1] = [h - means[1] for h in X[:,1]]
#data_for_preparing_t[:,2] = [z - means[2] for z in X[:,2]]這是z的東西
        
# compute the covariance matrix Sigma
Sigma_for_preparing_t = np.dot(data_for_preparing_t.T, data_for_preparing_t) #計算作業pdf中的(3)的Sigma矩陣(但還沒弄成平均)，dot是內積的意思
Sigma_for_preparing_t = np.true_divide(Sigma_for_preparing_t, np.full((2, 2), N)) #把Sigma矩陣弄成平均
L_for_preparing_t, U_for_preparing_t = LA.eig(Sigma_for_preparing_t) #程式回傳Sigma_for_preparing_t矩陣的eigenvalues(沒有按照大小排列)到L，並且回傳跟剛剛的eigenvalues有相對應的eigen "unit" vectors到U。

#######
#因為LA.eig回傳的eigenvalue沒有按照大小排列，所以要手動找比較大的
pci_for_t = 0
if (L_for_preparing_t[1]>L_for_preparing_t[0]): pci_for_t = 1
#依據剛剛唯一確定的最大的eigenvalue的編號，找到對應的eigenvector
weight_for_w = U_for_preparing_t[pci_for_t][0] if U_for_preparing_t[pci_for_t][0] > 0 else U_for_preparing_t[pci_for_t][0] * -1
weight_for_h = U_for_preparing_t[pci_for_t][1] if U_for_preparing_t[pci_for_t][1] > 0 else U_for_preparing_t[pci_for_t][1] * -1
#######

#######
#開始計算ti們
t = []
new_X = [] #因為畫圖的需要，所以也需要計算new_X
for i in range(len(X[:,0])):
    ti = X[i,0] * weight_for_w + X[i,1] * weight_for_h
    t.append(ti)
    new_X.append((ti, X[i, 2])) #因為畫圖的需要，所以也需要計算new_X
t_average = sum(t) / len(t) #取ti們的平均
t = np.array(t) #把ti們改成numpy array
new_X = np.array(new_X)
#######



#現在開始準備計算t和z之間的關係
data_for_final = np.zeros((N,2))
data_for_final[:,0] = [ti - t_average for ti in t] #之後畫的t-z圖，因為[0]擺t，所以會是t
data_for_final[:,1] = [z - means[2] for z in X[:,2]] #之後畫的t-z圖，因為[1]擺z，所以會是z
z_average = means[2]#順便把z_average記錄起來，因為之後(為了畫圖，)means的結構會改變
        
# compute the covariance matrix Sigma
Sigma_for_final = np.dot(data_for_final.T, data_for_final) 
Sigma_for_final = np.true_divide(Sigma_for_final, np.full((2, 2), N))
L_for_final, U_for_final = LA.eig(Sigma_for_final) 

#######
pci_for_final = 0
if (L_for_final[1]>L_for_final[0]): pci_for_final = 1
weight_for_t = U_for_final[pci_for_final][0] if U_for_final[pci_for_final][0] > 0 else U_for_final[pci_for_final][0] * -1
weight_for_z = U_for_final[pci_for_final][1] if U_for_final[pci_for_final][1] > 0 else U_for_final[pci_for_final][1] * -1
#######



# 開始畫圖
var = math.sqrt(L_for_final[pci_for_final])/2.
pc = U_for_final[:, pci_for_final]*var

# a is the projected coordinate on the line 
a  = np.dot(data_for_final, U_for_final[:, pci_for_final])
print(a)

# Z is the projected coordinate on the original space
#把means結構修改
means = [];means.append(t_average);means.append(z_average);
means = np.array(means)
A = np.reshape(a, (N, 1))
u = np.reshape(U_for_final[:,pci_for_final], (1, 2))
Z = np.dot(A, u) + np.dot(np.ones((N,1)), np.reshape(means, (1,2)))


# plot the figures  
plt.figure()
plt.plot(new_X[:,0], new_X[:,1], 'bo') 
plt.plot(Z[:,0], Z[:,1], 'kx') 
for i in range(N):
    plt.plot([])
#plt.plot([means[0]-pc[0], means[0]+pc[0]], [means[1]-pc[1], means[1]+pc[1]], 'r-') #(141.7,3)~(145.3,799)
plt.plot([141.7, 145.3], [3, 799], 'r-')
plt.xlabel("t")
plt.ylabel("z")
plt.show()






#我把教授給的原始code放在這邊
#var = math.sqrt(L[pci])/2.
#pc = U[:, pci]*var
#
## a is the projected coordinate on the line 
#a  = np.dot(Y, U[:, pci])
#print(a)
#
## Z is the projected coordinate on the original space
#A = np.reshape(a, (N, 1))
#u = np.reshape(U[:,pci], (1, 2))
#Z = np.dot(A, u) + np.dot(np.ones((N,1)), np.reshape(means, (1,2)))
#
#
## plot the figures 
#plt.figure()
#plt.plot(X[:,0], X[:,1], 'bo') 
#plt.plot(Z[:,0], Z[:,1], 'kx') 
#for i in range(N):
#    plt.plot([])
#plt.plot([means[0]-pc[0], means[0]+pc[0]], [means[1]-pc[1], means[1]+pc[1]], 'r-')
#plt.xlabel("Weight")
#plt.ylabel("Height")
#plt.show()