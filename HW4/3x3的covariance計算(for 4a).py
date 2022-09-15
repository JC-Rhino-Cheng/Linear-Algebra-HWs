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

# compute means of W and H        
means = np.mean(X, axis= 0) #針對X矩陣的兩個row(一個是Height一個是Weight)分別計算平均
Y = np.zeros((N,3)) #創建和X矩陣一模一樣大小的矩陣，並且(下面兩行)把要計算變異數(a.k.a. 標準差的平方)的資料全部先算好
Y[:,0] = [x - means[0] for x in X[:,0]]
Y[:,1] = [x - means[1] for x in X[:,1]]
Y[:,2] = [x - means[2] for x in X[:,2]]
        
# compute the covariance matrix Sigma
Sigma = np.dot(Y.T, Y) #計算作業pdf中的(3)的Sigma矩陣，dot是內積的意思
Sigma = np.true_divide(Sigma, np.full((3, 3), N))
L, U = LA.eig(Sigma) #程式回傳Sigma矩陣的eigenvalues(沒有按照大小排列)到L，並且回傳跟剛剛的eigenvalues有相對應的eigen unit vectors到U。

#記得用Breakpoint(新增在line53)來追蹤，否則看不到eigenvalue和eigenvector
print(1)