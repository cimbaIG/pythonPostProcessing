import matplotlib
from scipy.interpolate import interp1d
import numpy as np
import pylab as plt

#Change font type and font size in axis labels
matplotlib.rcParams.update({'legend.markerscale': 1.5, 'legend.handlelength': 1, 'legend.frameon': 0, 'legend.handletextpad': 1 , 'font.size': 18,'font.family':'Times New Roman'})

#matplotlib.rcParams['text.usetex'] = True
#matplotlib.rcParams['text.latex.unicode'] = True
matplotlib.rcParams['mathtext.fontset'] = 'stix'
matplotlib.rcParams['font.family'] = 'STIXGeneral'

WS_rural = np.loadtxt('WSx_rural_sampleline2.dat')
WS_suburban = np.loadtxt('WSx_suburban_sampleline2.dat')
WS_urban = np.loadtxt('WSx_urban_sampleline2.dat')
print WS_rural
fig1 = plt.figure(1)
ax = plt.axes()
plt.plot(WS_rural[:,1], WS_rural[:,0], 'k-o', markeredgecolor='k', markerfacecolor='none', markeredgewidth=1.5, markersize = 6)
plt.xlabel(r'$WS_{x}(z)$, $\mathrm{m}/\mathrm{s}^2$', fontname="Times New Roman", fontsize=24)
plt.ylabel(r'$z$, m', fontname="Times New Roman", fontsize=24)
plt.xlim(-8, 12)
plt.ylim(0, 1.0)
#plt.legend(numpoints=1, loc=1)

ax1 = plt.axes()
ax1.yaxis.set_ticks(np.arange(0,1.01, 0.2))
ax1.xaxis.set_ticks(np.arange(-8, 12.01, 4))

#Get current figure
figure = plt.gcf()
#Set figure size
figure.set_size_inches(5, 5)
#When saving, specify the DPI
plt.savefig('WSx_distribution_rural.png', dpi = 250, bbox_inches = 'tight')
#Show figure
plt.show()

fig2 = plt.figure(2)
ax = plt.axes()
plt.plot(WS_suburban[:,1], WS_suburban[:,0], 'k-o', markeredgecolor='k', markerfacecolor='none', markeredgewidth=1.5, markersize = 6)
plt.xlabel(r'$WS_{x}(z)$, $\mathrm{m}/\mathrm{s}^2$', fontname="Times New Roman", fontsize=24)
plt.ylabel(r'$z$, m', fontname="Times New Roman", fontsize=24)
plt.xlim(-8, 12)
plt.ylim(0, 1.0)
#plt.legend(numpoints=1, loc=1)

ax2 = plt.axes()
ax2.yaxis.set_ticks(np.arange(0,1.01, 0.2))
ax2.xaxis.set_ticks(np.arange(-8, 12.01, 4))

#Get current figure
figure = plt.gcf()
#Set figure size
figure.set_size_inches(5, 5)
#When saving, specify the DPI
plt.savefig('WSx_distribution_suburban.png', dpi = 250, bbox_inches = 'tight')
#Show figure
plt.show()

fig3 = plt.figure(3)
ax = plt.axes()
plt.plot(WS_urban[:,1], WS_urban[:,0], 'k-o', markeredgecolor='k', markerfacecolor='none', markeredgewidth=1.5, markersize = 6)
plt.xlabel(r'$WS_{x}(z)$, $\mathrm{m}/\mathrm{s}^2$', fontname="Times New Roman", fontsize=24)
plt.ylabel(r'$z$, m', fontname="Times New Roman", fontsize=24)
plt.xlim(-8, 12)
plt.ylim(0, 1.0)
#plt.legend(numpoints=1, loc=1)

ax3 = plt.axes()
ax3.yaxis.set_ticks(np.arange(0, 1.01, 0.2))
ax3.xaxis.set_ticks(np.arange(-8, 12.01, 4))

#Get current figure
figure = plt.gcf()
#Set figure size
figure.set_size_inches(5, 5)
#When saving, specify the DPI
plt.savefig('WSx_distribution_urban.png', dpi = 250, bbox_inches = 'tight')
#Show figure
plt.show()