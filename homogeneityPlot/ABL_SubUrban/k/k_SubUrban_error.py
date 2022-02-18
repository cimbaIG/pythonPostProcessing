import matplotlib
import numpy as np
import pylab as plt

#k in rural case - Sample line 1
kSL1 = np.loadtxt('k_lineX0.txt')
kSL1 = kSL1[:,0]
#k in rural case - Sample line 2
kSL2 = np.loadtxt('k_lineX1.txt')
kSL2 = kSL2[:,0]
#k in rural case - Sample line 3
kSL3 = np.loadtxt('k_lineX2.txt')
kSL3 = kSL3[:,0]

k = np.array([kSL1, kSL2, kSL3])
k = k.transpose()
size = np.shape(k)
relkError = np.zeros((51,1))

for height in range(0,51):
    maxk = max(k[height,:])
    mink = min(k[height,:])
    relkError[height,0] = ((maxk-mink)/maxk)*100
    if (height == 50):
        print relkError
        print np.shape(relkError)

averagekError = 0 #initialize value
for j in range(0,51):
    averagekError += relkError[j,0] 
    if (j == 50):
        averagekError = averagekError/51
        print averagekError