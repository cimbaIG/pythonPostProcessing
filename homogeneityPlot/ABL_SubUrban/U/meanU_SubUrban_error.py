import matplotlib
import numpy as np
import pylab as plt

#Mean velocity in rural case - Sample line 1
velocitySL1 = np.loadtxt('U_lineX0_norm.txt')
y = velocitySL1[:,1] #Define height y data array
velocitySL1 = velocitySL1[:,0]
#Mean velocity in rural case - Sample line 2
velocitySL2 = np.loadtxt('U_lineX1_norm.txt')
velocitySL2 = velocitySL2[:,0]
#Mean velocity in rural case - Sample line 3
velocitySL3 = np.loadtxt('U_lineX2_norm.txt')
velocitySL3 = velocitySL3[:,0]

velocity = np.array([velocitySL1, velocitySL2, velocitySL3])
velocity = velocity.transpose()
size = np.shape(velocity)
relVelError = np.zeros((51,1))

for height in range(0,51):
    maxVelocity = max(velocity[height,:])
    minVelocity = min(velocity[height,:])
    relVelError[height,0] = ((maxVelocity-minVelocity)/maxVelocity)*100
    if (height == 0):
        relVelError[height,0] = 0. #To avoid dividing by zero
    if (height == 50):
    	print relVelError
        print np.shape(relVelError)

averageVelError = 0 #Initialize value
for j in range(0,51):
    averageVelError += relVelError[j,0]
    if (j == 50):
        averageVelError = averageVelError/51
        print averageVelError