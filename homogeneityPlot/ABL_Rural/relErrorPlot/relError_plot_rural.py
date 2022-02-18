import matplotlib
from scipy.interpolate import interp1d
import numpy as np
import pylab as plt
from tabulate import tabulate

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
relVelError = np.zeros((53,1))

print "Relative Velocity Error data:"
for height in range(0,53):
    maxVelocity = max(velocity[height,:])
    minVelocity = min(velocity[height,:])
    relVelError[height,0] = ((maxVelocity-minVelocity)/maxVelocity)*100
    if (height == 0):
        relVelError[height,0] = 0. #To avoid dividing by zero
    if (height == 52):
    	print relVelError
        #print np.shape(relVelError)
maxRelVelError = max(relVelError)
minRelVeError = min(relVelError)

averageVelError = 0 #Initialize value
for j in range(0,53):
    averageVelError += relVelError[j,0]
    if (j == 52):
        averageVelError = averageVelError/53
        #print averageVelError

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
relRxyError = np.zeros((53,1))

print "Relative Rxy Error data:"
for height in range(0,53):
    maxRxy = max(Rxy[height,:])
    minRxy = min(Rxy[height,:])
    relRxyError[height,0] = abs(((abs(maxRxy)-abs(minRxy))/abs(maxRxy)))*100
    if (height == 52):
        print relRxyError
        #print np.shape(relRxyError)
maxRelRxyError = max(relRxyError)
minRelRxyError = min(relRxyError)

averageRxyError = 0 #initialize value
for j in range(0,53):
    averageRxyError += relRxyError[j,0] 
    if (j == 52):
        averageRxyError = averageRxyError/53
        #print averageRxyError

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
relkError = np.zeros((53,1))

print "Relative k Error data:"
for height in range(0,53):
    maxk = max(k[height,:])
    mink = min(k[height,:])
    relkError[height,0] = ((maxk-mink)/maxk)*100
    if (height == 52):
        print relkError
        #print np.shape(relkError)
maxRelKError = max(relkError)
minRelKError = min(relkError)

averagekError = 0 #initialize value
for j in range(0,53):
    averagekError += relkError[j,0] 
    if (j == 52):
        averagekError = averagekError/53
        #print averagekError

table = [[averageVelError, averageRxyError, averagekError, maxRelVelError, maxRelRxyError, maxRelKError]]
print tabulate(table, headers=["Average rel. error - Mean U, %", "Average rel. error - Rxy, %", "Average rel. error - k, %", "Maximum relative error - Mean U, %", "Maximum relative error - Rxy, %", "Maximum relative error - k, %"])
file = open('relError_plot_rural.dat','w')
file.write(tabulate(table, headers=["Average rel. error - Mean U, %", "Average rel. error - Rxy, %", "Average rel. error - k, %", "Maximum relative error - Mean U, %", "Maximum relative error - Rxy, %", "Maximum relative error - k, %"]))
file.close()

#Change font type and font size in axis labels
matplotlib.rcParams.update({'legend.markerscale': 1.5, 'legend.handlelength': 1, 'legend.frameon': 0, 'legend.handletextpad': 1 , 'font.size': 18,'font.family':'Times New Roman'})

fig = plt.subplot(1, 3, 1)
plt.plot(relVelError, y, '-o', markeredgecolor='none', markerfacecolor='k', linewidth='2', color='k', label='Rural terrain - \nRelative error, %')
plt.xlabel('a)', fontname="Times New Roman", fontsize=24)
plt.ylabel('y, m', fontname="Times New Roman", fontsize=24)
#plt.xlim(-0.01, 0.24)
plt.ylim(-0.01, 1.01)
startX, endX = (0, 0.251)
fig.xaxis.set_ticks(np.arange(startX, endX, 0.05))
plt.legend(numpoints=1, loc=1)

fig = plt.subplot(1, 3, 2)
plt.plot(relRxyError, y, '-o', markeredgecolor='none', markerfacecolor='k', linewidth='2', color='k')
plt.xlabel('b)', fontname="Times New Roman", fontsize=24)
#plt.ylabel('y, m', fontname="Times New Roman", fontsize=24)
plt.xlim(0, 1.5)
startX, endX = (0, 1.501)
plt.ylim(-0.01, 1.01)
fig.xaxis.set_ticks(np.arange(startX, endX, 0.25))
plt.legend(numpoints=1, loc=3)

fig = plt.subplot(1, 3, 3)
plt.plot(relkError, y, '-o', markeredgecolor='none', markerfacecolor='k', linewidth='2', color='k')
plt.xlabel('c)', fontname="Times New Roman", fontsize=24)
#plt.ylabel('y, m', fontname="Times New Roman", fontsize=24)
#plt.xlim(-0.01, 0.8)
startX, endX = (0, 0.801)
plt.ylim(-0.01, 1.01)
fig.xaxis.set_ticks(np.arange(startX, endX, 0.2))
plt.legend(numpoints=1, loc=1)

#Get current figure
figure = plt.gcf()
#Set figure size
figure.set_size_inches(16, 7)
#When saving, specify the DPI
plt.savefig('relError_plot_rural.png', dpi = 250, bbox_inches = 'tight')
plt.show()