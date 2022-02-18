import matplotlib 
from scipy.interpolate import interp1d
import matplotlib.ticker as ticker
import numpy as np
import pylab as plt

#Change font type and font size in axis labels
matplotlib.rcParams.update({'legend.markerscale': 1.5, 'legend.handlelength': 1, 'legend.frameon': 1, 'legend.handletextpad': 1 , 'font.size': 18,'font.family':'Times New Roman'})

#matplotlib.rcParams['text.usetex'] = True
#matplotlib.rcParams['text.latex.unicode'] = True
matplotlib.rcParams['mathtext.fontset'] = 'stix'
matplotlib.rcParams['font.family'] = 'STIXGeneral'

#Define interpolation at sample line 2 in the center of the domain
#readVelocity = np.loadtxt('U_lineX1_norm.txt')
#interpolation = interp1d(readVelocity[:,0], readVelocity[:,1], kind='cubic')
#xnew = np.arange(0, 1.4, 1e-3)
#ynew = interpolation(xnew)

#Mean velocity in rural case - Sample line 1
data1 = np.loadtxt('U_lineX0_norm.txt')

#fig = plt.subplot(1, 3, 1)
fig = plt.figure(1)
ax = plt.axes()
plt.plot(data1[:,0], data1[:,1], 'o', markeredgecolor='none', markerfacecolor='k')#, label='Rural terrain')
#plt.plot(xnew, ynew, '-', linewidth='1.5', color='k' , label='Best fit')
#plt.xlabel('Mean velocity, $\overline{u}/u_\mathrm{ref}$ m/s \n a)', fontname="Times New Roman", fontsize=22)
plt.xlabel(r'$\bar{u}(z)/\bar{u}_\mathrm{ref}$', fontname="Times New Roman", fontsize=24)
plt.ylabel(r'$z$, m', fontname="Times New Roman", fontsize=24)
plt.xlim(-0.015, 1.415)
plt.ylim(-0.01, 1.01)
start, end = (0, 1.01)
ax.yaxis.set_ticks(np.arange(start,end,0.1))
plt.grid(True)
#legend = plt.legend(numpoints=1, loc=2)
#frame = legend.get_frame()
#frame.set_facecolor('white')
#frame.set_linewidth(0)

#Get current figure
figure = plt.gcf()
#Set figure size
figure.set_size_inches(5, 5)
#When saving, specify the DPI
plt.savefig('U_rural_sampleLine1.png', dpi = 250, bbox_inches='tight')
#Show figure
plt.show()

#Mean velocity in rural case - Sample line 2
data2 = np.loadtxt('U_lineX1_norm.txt')

#fig = plt.subplot(1,3,2)
fig = plt.figure(2)
ax = plt.axes()
plt.plot(data2[:,0], data2[:,1], 'o', markeredgecolor='none', markerfacecolor='k')
#plt.plot(xnew, ynew, '-', linewidth='1.5', color='k' , label='Best fit')
plt.xlabel(r'$\bar{u}(z)/\bar{u}_\mathrm{ref}$', fontname="Times New Roman", fontsize=24)
plt.ylabel(r'$z$, m', fontname="Times New Roman", fontsize=24)
plt.xlim(-0.015, 1.415)
plt.ylim(-0.01, 1.01)
#start, end = fig.get_xlim() #fig.get_ylim()
start, end = (0, 1.01)
ax.yaxis.set_ticks(np.arange(start, end, 0.1))
plt.grid(True)
#plt.legend(numpoints=1, loc=2)

#Get current figure
figure = plt.gcf()
#Set figure size
figure.set_size_inches(5, 5)
#When saving, specify the DPI
plt.savefig('U_rural_sampleLine2.png', dpi = 250, bbox_inches='tight')
#Show figure
plt.show()

#Mean velocity in rural case - Sample line 3
data3 = np.loadtxt('U_lineX2_norm.txt')

#fig = plt.subplot(1,3,3)
fig = plt.figure(3)
ax = plt.axes()
plt.plot(data3[:,0], data3[:,1], 'o', markeredgecolor='none', markerfacecolor='k')
#plt.plot(xnew, ynew, '-', linewidth='1.5', color='k' , label='Best fit')
plt.xlabel(r'$\bar{u}(z)/\bar{u}_\mathrm{ref}$', fontname="Times New Roman", fontsize=24)
plt.ylabel(r'$z$, m', fontname="Times New Roman", fontsize=24)
plt.xlim(-0.015, 1.415)
plt.ylim(-0.01, 1.01)
start, end = (0, 1.01)
ax.yaxis.set_ticks(np.arange(start, end, 0.1))
plt.grid(True)
#plt.legend(numpoints=1, loc=2)

#Get current figure
figure = plt.gcf()
#Set figure size
figure.set_size_inches(5, 5)
#When saving, specify the DPI
plt.savefig('U_rural_sampleLine3.png', dpi = 250, bbox_inches='tight')
#Show figure
plt.show()