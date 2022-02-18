import matplotlib
from scipy.interpolate import interp1d
import matplotlib.ticker as ticker
import numpy as np
import pylab as plt

#Change font type and font size in axis labels
matplotlib.rcParams.update({'legend.markerscale': 1.5, 'legend.handlelength': 1, 'legend.frameon': 1, 'legend.handletextpad': 1 , 'font.size': 18,'font.family':'Times New Roman'})
plt.locator_params(tight=True,nbins=2)

#matplotlib.rcParams['text.usetex'] = True
#matplotlib.rcParams['text.latex.unicode'] = True
matplotlib.rcParams['mathtext.fontset'] = 'stix'
matplotlib.rcParams['font.family'] = 'STIXGeneral'

#Define interpolation at sample line 2 in the center of the domain
#readRxy = np.loadtxt('Rxy_lineX1_norm.txt')
#interpolation = interp1d(readRxy[:,0], readRxy[:,1])#, kind='cubic')
#xnew = np.arange(-1.26, -0.6, 1e-3)
#ynew = interpolation(xnew)

#Rxy in rural case - Sample line 1
data1 = np.loadtxt('Rxy_lineX0_norm.txt')

fig1 = plt.figure(1)
ax = plt.axes()
plt.plot(data1[:,0], data1[:,1], 'o', markeredgecolor='none', markerfacecolor='k', label='Rural terrain')
#plt.plot(xnew, ynew, '-', linewidth='1.5', color='k' , label='Cubic spline')
#plt.xlabel('Mean velocity, $\overline{u}/u_\mathrm{ref}$ m/s \n a)', fontname="Times New Roman", fontsize=22)
plt.xlabel(r'$\tau_{zx}(z)/u^2_\tau$', fontname="Times New Roman", fontsize=24)
plt.ylabel(r'$z$, m', fontname="Times New Roman", fontsize=24)
plt.xlim(-1.3, -0.499)
plt.ylim(-0.01, 1.01)
startY, endY = (0, 1.01)
start, end = ax.get_xlim() #fig.get_ylim()
ax.yaxis.set_ticks(np.arange(startY,endY,0.1))
ax.xaxis.set_ticks(np.arange(start,end,0.2))
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
plt.savefig('Rxy_rural_sampleLine1_homogeneity.png', dpi = 250, bbox_inches='tight')
#Show figure
plt.show()

#Rxy in rural case - Sample line 2
data2 = np.loadtxt('Rxy_lineX1_norm.txt')

fig2 = plt.figure(2)
ax = plt.axes()
plt.plot(data2[:,0], data2[:,1], 'o', markeredgecolor='none', markerfacecolor='k')
#plt.plot(xnew, ynew, '-', linewidth='1.5', color='k' , label='Cubic spline')
plt.xlabel(r'$\tau_{zx}(z)/u^2_\tau$', fontname="Times New Roman", fontsize=24)
plt.ylabel(r'$z$, m', fontname="Times New Roman", fontsize=24)
plt.xlim(-1.3, -0.499)
plt.ylim(-0.01, 1.01)
startY, endY = (0, 1.01)
start, end = ax.get_xlim() #fig.get_ylim()
ax.yaxis.set_ticks(np.arange(startY,endY,0.1))
ax.xaxis.set_ticks(np.arange(start,end,0.2))
plt.grid(True)
#plt.legend(numpoints=1, loc=2)

#Get current figure
figure = plt.gcf()
#Set figure size
figure.set_size_inches(5, 5)
#When saving, specify the DPI
plt.savefig('Rxy_rural_sampleLine2_homogeneity.png', dpi = 250, bbox_inches='tight')
#Show figure
plt.show()

#Rxy in rural case - Sample line 3
data3 = np.loadtxt('Rxy_lineX2_norm.txt')

#fig3 = plt.subplot(1,3,3)
fig3 = plt.figure(3)
ax = plt.axes()
plt.plot(data3[:,0], data3[:,1], 'o', markeredgecolor='none', markerfacecolor='k')
#plt.plot(xnew, ynew, '-', linewidth='1.5', color='k' , label='Cubic spline')
plt.xlabel(r'$\tau_{zx}(z)/u^2_\tau$', fontname="Times New Roman", fontsize=24)
plt.ylabel(r'$z$, m', fontname="Times New Roman", fontsize=24)
plt.xlim(-1.3, -0.499)
plt.ylim(-0.01, 1.01)
startY, endY = (0, 1.01)
start, end = ax.get_xlim() #fig.get_ylim()
ax.yaxis.set_ticks(np.arange(startY,endY,0.1))
ax.xaxis.set_ticks(np.arange(start,end,0.2))
plt.grid(True)
#plt.legend(numpoints=1, loc=2)

#Get current figure
figure = plt.gcf()
#Set figure size
figure.set_size_inches(5, 5)
#When saving, specify the DPI
plt.savefig('Rxy_rural_sampleLine3_homogeneity.png', dpi = 250, bbox_inches='tight')
#Show figure
plt.show()