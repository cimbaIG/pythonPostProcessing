import matplotlib
import numpy as np
import pylab as plt

#Rxy in rural case - Sample line 1
RxySL1 = np.loadtxt('Rxy_lineX0_norm.txt')
RxySL1 = RxySL1[:,0]
#Rxy in rural case - Sample line 2
RxySL2 = np.loadtxt('Rxy_lineX1_norm.txt')
RxySL2 = RxySL2[:,0]
#Rxy in rural case - Sample line 3
RxySL3 = np.loadtxt('Rxy_lineX2_norm.txt')
RxySL3 = RxySL3[:,0]

Rxy = np.array([RxySL1, RxySL2, RxySL3])
Rxy = Rxy.transpose()
size = np.shape(Rxy)
relRxyError = np.zeros((22,1))

for height in range(0,22):
    maxRxy = max(Rxy[height,:])
    minRxy = min(Rxy[height,:])
    relRxyError[height,0] = ((maxRxy-minRxy)/maxRxy)*100
    if (height == 21):
        print relRxyError
        print np.shape(relRxyError)

averageRxyError = 0 #initialize value
for j in range(0,22):
    averageRxyError += relRxyError[j,0] 
    if (j == 21):
        averageRxyError = averageRxyError/22
        print averageRxyError