import matplotlib
from scipy.interpolate import interp1d
import numpy as np
import pylab as plt

#Change font type and font size in axis labels
matplotlib.rcParams.update({'legend.markerscale': 1.5, 'legend.handlelength': 1, 'legend.frameon': 1, 'legend.handletextpad': 1 , 'font.size': 18,'font.family':'Times New Roman'})

#matplotlib.rcParams['text.usetex'] = True
#matplotlib.rcParams['text.latex.unicode'] = True
matplotlib.rcParams['mathtext.fontset'] = 'stix'
matplotlib.rcParams['font.family'] = 'STIXGeneral'

#Define interpolation at sample line 2 in the center of the domain
#readK = np.loadtxt('k_lineX1.txt')
#interpolation = interp1d(readK[:,0], readK[:,1], kind='cubic')
#xnew = np.arange(4.35, 11.4, 1e-03)
#ynew = interpolation(xnew)

#k in rural case - Sample line 1
data1 = np.loadtxt('k_lineX0.txt')

#fig3 = plt.subplot(1, 3, 1)
fig1 = plt.figure(1)
ax = plt.axes()
plt.plot(data1[:,0], data1[:,1], 'D', markeredgecolor='none', markerfacecolor='k', label='Urban terrain')
#plt.plot(xnew, ynew, '-', linewidth='1.5', color='k' , label='Cubic spline')
#plt.xlabel('Mean velocity, $\overline{u}/u_\mathrm{ref}$ m/s \n a)', fontname="Times New Roman", fontsize=22)
plt.xlabel(r'$k(z)$, $\mathrm{m}^2/\mathrm{s}^2$', fontname="Times New Roman", fontsize=24)
plt.ylabel(r'$z$, m', fontname="Times New Roman", fontsize=24)
plt.xlim(4, 12.01)
plt.ylim(-0.01, 1.01)
startY, endY = (0, 1.01)
start, end = ax.get_xlim() #fig.get_ylim()
ax.yaxis.set_ticks(np.arange(startY,endY,0.1))
ax.xaxis.set_ticks(np.arange(start,end,1))
plt.grid(True)
#legend = plt.legend(numpoints=1, loc=1)
#frame = legend.get_frame()
#frame.set_facecolor('white')
#frame.set_linewidth(0)

#Get current figure
figure = plt.gcf()
#Set figure size
figure.set_size_inches(5, 5)
#When saving, specify the DPI
plt.savefig('k_urban_sampleLine1_homogeneity.png', dpi = 250, bbox_inches = 'tight')
#Show figure
plt.show()

#k in rural case - Sample line 2
data2 = np.loadtxt('k_lineX1.txt')

#fig3 = plt.subplot(1,3,2)
fig2 = plt.figure(2)
ax = plt.axes()
plt.plot(data2[:,0], data2[:,1], 'D', markeredgecolor='none', markerfacecolor='k')
#plt.plot(xnew, ynew, '-', linewidth='1.5', color='k' , label='Cubic spline')
plt.xlabel(r'$k(z)$, $\mathrm{m}^2/\mathrm{s}^2$', fontname="Times New Roman", fontsize=24)
plt.ylabel(r'$z$, m', fontname="Times New Roman", fontsize=24)
plt.xlim(4, 12.01)
plt.ylim(-0.01, 1.01)
startY, endY = (0, 1.01)
start, end = ax.get_xlim() #fig.get_ylim()
ax.yaxis.set_ticks(np.arange(startY,endY,0.1))
ax.xaxis.set_ticks(np.arange(start,end,1))
plt.grid(True)
#plt.legend(numpoints=1, loc=1)

#Get current figure
figure = plt.gcf()
#Set figure size
figure.set_size_inches(5, 5)
#When saving, specify the DPI
plt.savefig('k_urban_sampleLine2_homogeneity.png', dpi = 250, bbox_inches = 'tight')
#Show figure
plt.show()

#k in rural case - Sample line 3
data3 = np.loadtxt('k_lineX2.txt')

#fig3 = plt.subplot(1,3,3)
fig3 = plt.figure(3)
ax = plt.axes()
plt.plot(data3[:,0], data3[:,1], 'D', markeredgecolor='none', markerfacecolor='k')
#plt.plot(xnew, ynew, '-', linewidth='1.5', color='k' , label='Cubic spline')
plt.xlabel(r'$k(z)$, $\mathrm{m}^2/\mathrm{s}^2$', fontname="Times New Roman", fontsize=24)
plt.ylabel(r'$z$, m', fontname="Times New Roman", fontsize=24)
plt.xlim(4, 12.01)
plt.ylim(-0.01, 1.01)
startY, endY = (0, 1.01)
start, end = ax.get_xlim() #fig.get_ylim()
ax.yaxis.set_ticks(np.arange(startY,endY,0.1))
ax.xaxis.set_ticks(np.arange(start,end,1))
plt.grid(True)
#plt.legend(numpoints=1, loc=1)

#Get current figure
figure = plt.gcf()
#Set figure size
figure.set_size_inches(5, 5)
#When saving, specify the DPI
plt.savefig('k_urban_sampleLine3_homogeneity.png', dpi = 250, bbox_inches = 'tight')
#Show figure
plt.show()