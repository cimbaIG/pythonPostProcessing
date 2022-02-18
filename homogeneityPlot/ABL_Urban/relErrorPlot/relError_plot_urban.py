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
relVelError = np.zeros((22,1))

for height in range(0,22):
    maxVelocity = max(velocity[height,:])
    minVelocity = min(velocity[height,:])
    relVelError[height,0] = ((maxVelocity-minVelocity)/maxVelocity)*100
    if (height == 0):
        relVelError[height,0] = 0. #To avoid dividing by zero
    if (height == 21):
    	print relVelError
        #print np.shape(relVelError)
maxRelVel = max(relVelError)

averageVelError = 0 #Initialize value
for j in range(0,22):
    averageVelError += relVelError[j,0]
    if (j == 21):
        averageVelError = averageVelError/22
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
relRxyError = np.zeros((22,1))

for height in range(0,22):
    maxRxy = max(Rxy[height,:])
    minRxy = min(Rxy[height,:])
    relRxyError[height,0] = abs(((abs(maxRxy)-abs(minRxy))/abs(maxRxy)))*100
    if (height == 21):
        print relRxyError
        #print np.shape(relRxyError)
maxRelRxy = max(relRxyError)

averageRxyError = 0 #initialize value
for j in range(0,22):
    averageRxyError += relRxyError[j,0] 
    if (j == 21):
        averageRxyError = averageRxyError/22
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
relkError = np.zeros((22,1))

for height in range(0,22):
    maxk = max(k[height,:])
    mink = min(k[height,:])
    relkError[height,0] = ((maxk-mink)/maxk)*100
    if (height == 21):
        print relkError
        #print np.shape(relkError)
maxRelK = max(relkError)

averagekError = 0 #initialize value
for j in range(0,22):
    averagekError += relkError[j,0] 
    if (j == 21):
        averagekError = averagekError/22
        #print averagekError

table = [[averageVelError, averageRxyError, averagekError, maxRelVel, maxRelRxy, maxRelK]]
print tabulate(table, headers=["Average rel. error - Mean U, %", "Average rel. error - Rxy, %", "Average rel. error - k, %", "Maximum relative error - Mean U, %", "Maximum relative error - Rxy, %", "Maximum relative error - k, %"])
file = open('relError_plot_urban.dat','w')
file.write(tabulate(table, headers=["Average rel. error - Mean U, %", "Average rel. error - Rxy, %", "Average rel. error - k, %", "Maximum relative error - Mean U, %", "Maximum relative error - Rxy, %", "Maximum relative error - k, %"]))
file.close()

#Change font type and font size in axis labels
matplotlib.rcParams.update({'legend.markerscale': 1.5, 'legend.handlelength': 1, 'legend.frameon': 0, 'legend.handletextpad': 1 , 'font.size': 16,'font.family':'Times New Roman'})

plt.subplot(1, 3, 1)
plt.plot(relVelError, y, '-D', markeredgecolor='none', markerfacecolor='k', linewidth='2', color='k', label='Urban terrain - \nRelative error, %')
plt.xlabel('a)', fontname="Times New Roman", fontsize=24)
plt.ylabel('y, m', fontname="Times New Roman", fontsize=24)
plt.xlim(-0.01, 0.2)
plt.ylim(-0.01, 1.01)
plt.legend(numpoints=1, loc=3)

fig = plt.subplot(1, 3, 2)
plt.plot(relRxyError, y, '-D', markeredgecolor='none', markerfacecolor='k', linewidth='2', color='k')
plt.xlabel('b)', fontname="Times New Roman", fontsize=24)
#plt.ylabel('y, m', fontname="Times New Roman", fontsize=24)
#plt.xlim(-0.6, 0)
plt.ylim(-0.01, 1.01)
startX, endX = (0, 0.601)
fig.xaxis.set_ticks(np.arange(startX, endX, 0.15))
plt.legend(numpoints=1, loc=1)

plt.subplot(1, 3, 3)
plt.plot(relkError, y, '-D', markeredgecolor='none', markerfacecolor='k', linewidth='2', color='k')
plt.xlabel('c)', fontname="Times New Roman", fontsize=24)
#plt.ylabel('y, m', fontname="Times New Roman", fontsize=24)
plt.xlim(-0.01, 0.5)
plt.ylim(-0.01, 1.01)
plt.legend(numpoints=1, loc=1)

#Get current figure
figure = plt.gcf()
#Set figure size
figure.set_size_inches(16, 7)
#When saving, specify the DPI
plt.savefig('relError_plot_urban.png', dpi = 250, bbox_inches = 'tight')
plt.show()