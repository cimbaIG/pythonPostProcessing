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
#xnew = np.arange(3.06, 8.3, 1e-03)
#ynew = interpolation(xnew)

#k in rural case - Sample line 1
data1 = np.loadtxt('k_lineX0.txt')
#k in rural case - Sample line 2
data2 = np.loadtxt('k_lineX1.txt')
#k in rural case - Sample line 3
data3 = np.loadtxt('k_lineX2.txt')

#fig3 = plt.subplot(1, 3, 1)
fig1 = plt.figure(1)
ax = plt.axes()
plt.plot(data1[:,0], data1[:,1], '.', markeredgecolor='k', markerfacecolor='none', label='SL1')
plt.plot(data2[:,0], data2[:,1], 'x', markeredgecolor='k', markerfacecolor='none', label='SL2')
plt.plot(data3[:,0], data3[:,1], '+', markeredgecolor='k', markerfacecolor='none', label='SL3')
#plt.xlabel('Mean velocity, $\overline{u}/u_\mathrm{ref}$ m/s \n a)', fontname="Times New Roman", fontsize=22)
plt.xlabel(r'$k(z)$, $\mathrm{m}^2/\mathrm{s}^2$', fontname="Times New Roman", fontsize=24)
plt.ylabel(r'$z$, m', fontname="Times New Roman", fontsize=24)
plt.xlim(3, 9.0)
plt.ylim(0, 1.0)
starty, endy = (0, 1.01)
startx, endx = (3, 9.01)
ax.yaxis.set_ticks(np.arange(starty,endy,0.1))
ax.xaxis.set_ticks(np.arange(startx,endx,1))
plt.grid(False)
legend = plt.legend(numpoints=1, loc=1)
frame = legend.get_frame()
frame.set_facecolor('white')
frame.set_linewidth(0)

#Get current figure
figure = plt.gcf()
#Set figure size
figure.set_size_inches(5, 5)
#When saving, specify the DPI
plt.savefig('k_subUrban_homogeneity.png', dpi = 250, bbox_inches = 'tight')
#Show figure
plt.show()