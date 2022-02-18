import matplotlib
import numpy as np
import pylab as plt

#Change font type and font size in axis labels
matplotlib.rcParams.update({ 'legend.fontsize': 15, 'legend.markerscale': 1, 'legend.handlelength': 1, 'legend.frameon': 0, 'legend.handletextpad': 1 , 'font.size': 18,'font.family':'Times New Roman'})

#matplotlib.rcParams['text.usetex'] = True
#matplotlib.rcParams['text.latex.unicode'] = True
matplotlib.rcParams['mathtext.fontset'] = 'stix'
matplotlib.rcParams['font.family'] = 'STIXGeneral'

Cp_frontSide = np.loadtxt('Cp_hline_frontSide_norm.dat')
Cp_rightSide = np.loadtxt('Cp_hline_rightSide_norm.dat')
Cp_rearSide = np.loadtxt('Cp_hline_rearSide_norm.dat')
Cp_topSide = np.loadtxt('Cp_hline_topSide_norm.dat')
Cp_CastroRobins = np.loadtxt('Castro_and_Robins_hline.dat')
#Cp_Lim = np.loadtxt('Lim_et_al_hline.dat')
Cp_PatersonApelt = np.loadtxt('Paterson_and_Apelt_hline.dat')

fig = plt.figure()
ax = plt.axes()
#for direction in ["left","bottom"]:
#    ax.spines[direction].set_position('zero')
#    ax.spines[direction].set_smart_bounds(False)
#for direction in ["right","top"]:
#    ax.spines[direction].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
#ax.grid(True)
plt.plot(Cp_frontSide[:,0], Cp_frontSide[:,2], '-', markeredgecolor='none', markerfacecolor='k', linewidth='2', color='k')
plt.plot(Cp_rightSide[:,0], Cp_rightSide[:,3], '-', markeredgecolor='none', markerfacecolor='k', linewidth='2', color='k')
plt.plot(Cp_rearSide[:,0], Cp_rearSide[:,3], '-', markeredgecolor='none', markerfacecolor='k', linewidth='2', color='k') 
plt.plot(Cp_topSide[:,0], Cp_topSide[:,3], '-', markeredgecolor='none', markerfacecolor='k', linewidth='2', color='k', label = r'CFD')
plt.plot(Cp_CastroRobins[:,0], Cp_CastroRobins[:,1], 'o', markeredgecolor='k', markerfacecolor='none', label = r'CR')
#plt.plot(Cp_Lim[:,0], Cp_Lim[:,1], 's', markeredgecolor='k', markerfacecolor='none', label = r'Lim et al.')
plt.plot(Cp_PatersonApelt[:,0], Cp_PatersonApelt[:,1], 'v', markeredgecolor='k', markerfacecolor='none', label = r'PA')
plt.xlabel(r'', fontname="Times New Roman", fontsize=24)
plt.ylabel(r'$C_{p}$', fontname="Times New Roman", fontsize=24)
plt.ylim(-1.0, 1)
plt.xlim(0, 2.5)
ax.xaxis.set_ticks(np.arange(0,2.501,0.25))
ax.yaxis.set_ticks(np.arange(-1.1,1.1501,0.25))
#plt.xticks([0.0, 0.1, 0.3, 0.4],('','','',''),rotation='horizontal')

xposition = [0.5, 1.5, 2.0]
for xc in xposition:
    plt.axvline(x=xc, color='k', linewidth='1', linestyle='-')
plt.axhline(y=0.0, color='k', linewidth='1.5', linestyle='-')
plt.arrow( 0.2, 0.0, 0.01, 0.0, fc="k", ec="k", head_width=0.05, head_length=0.1 )
plt.arrow( 0.98, 0.0, 0.01, 0.0, fc="k", ec="k", head_width=0.05, head_length=0.1 )   
plt.arrow( 1.72, 0.0, 0.01, 0.0, fc="k", ec="k", head_width=0.05, head_length=0.1 )   
plt.arrow( 2.2, 0.0, 0.01, 0.0, fc="k", ec="k", head_width=0.05, head_length=0.1 )   

plt.text(0.1, 0.94,'Front face',
     horizontalalignment='center',
     verticalalignment='center',
     transform = ax.transAxes)
plt.text(0.4, 0.94,'Side face',
     horizontalalignment='center',
     verticalalignment='center',
     transform = ax.transAxes)
plt.text(0.9, 0.94,'Top face',
     horizontalalignment='center',
     verticalalignment='center',
     transform = ax.transAxes)
plt.text(0.7, 0.94,'Rear face',
     horizontalalignment='center',
     verticalalignment='center',
     transform = ax.transAxes)
plt.text(0.02, 0.45,'A',
     horizontalalignment='center',
     verticalalignment='center',
     transform = ax.transAxes)
plt.text(0.22, 0.45,'B',
     horizontalalignment='center',
     verticalalignment='center',
     transform = ax.transAxes)
plt.text(0.62, 0.52,'C',
     horizontalalignment='center',
     verticalalignment='center',
     transform = ax.transAxes)
plt.text(0.78, 0.52,'D',
     horizontalalignment='center',
     verticalalignment='center',
     transform = ax.transAxes)
plt.text(0.82, 0.52,'E',
     horizontalalignment='center',
     verticalalignment='center',
     transform = ax.transAxes)
plt.text(0.98, 0.52,'F',
     horizontalalignment='center',
     verticalalignment='center',
     transform = ax.transAxes)

legend = plt.legend(numpoints=1, loc='lower right', frameon=True)
frame = legend.get_frame()
frame.set_facecolor('white')
frame.set_edgecolor('white')
frame.set_linewidth(0)

#Get current figure
figure = plt.gcf()
#Set figure size
figure.set_size_inches(8, 5)
#When saving, specify the DPI
plt.savefig('Cp_horizontal_distribution_norm.png', dpi = 1000, bbox_inches = 'tight')
plt.savefig('Cp_horizontal_distribution_norm.pdf', dpi = 1000, bbox_inches = 'tight')   
#Show figure
plt.show()
