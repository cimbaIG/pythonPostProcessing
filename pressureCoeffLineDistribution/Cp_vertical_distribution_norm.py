import matplotlib
import numpy as np
import pylab as plt

#Change font type and font size in axis labels
matplotlib.rcParams.update({ 'legend.fontsize': 15, 'legend.markerscale': 1, 'legend.handlelength': 1, 'legend.frameon': 0, 'legend.handletextpad': 1 , 'font.size': 18,'font.family':'Times New Roman'})

#matplotlib.rcParams['text.usetex'] = True
#matplotlib.rcParams['text.latex.unicode'] = True
matplotlib.rcParams['mathtext.fontset'] = 'stix'
matplotlib.rcParams['font.family'] = 'STIXGeneral'

Cp_frontSide = np.loadtxt('Cp_vline_frontSide_norm.dat')
Cp_rightSide = np.loadtxt('Cp_vline_rightSide_norm.dat')
Cp_rearSide = np.loadtxt('Cp_vline_rearSide_norm.dat')
Cp_topSide = np.loadtxt('Cp_vline_topSide_norm.dat')
Cp_CastroRobins = np.loadtxt('Castro_and_Robins_vline.dat')
Cp_PatersonApelt = np.loadtxt('Paterson_and_Apelt_vline.dat')
Cp_Lim = np.loadtxt('Lim_et_al_vline.dat')

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
plt.plot(Cp_frontSide[:,0], Cp_frontSide[:,3], '-', markeredgecolor='none', markerfacecolor='k', linewidth='2', color='k')
plt.plot(Cp_rightSide[:,0], Cp_rightSide[:,3], '-', markeredgecolor='none', markerfacecolor='k', linewidth='2', color='k')
plt.plot(Cp_rearSide[:,0], Cp_rearSide[:,3], '-', markeredgecolor='none', markerfacecolor='k', linewidth='2', color='k') 
plt.plot(Cp_topSide[:,0], Cp_topSide[:,3], '-', markeredgecolor='none', markerfacecolor='k', linewidth='2', color='k', label = r'CFD')
plt.plot(Cp_CastroRobins[:,0], Cp_CastroRobins[:,1], 'o', markeredgecolor='k', markerfacecolor='none', label = r'CR')
plt.plot(Cp_PatersonApelt[:,0], Cp_PatersonApelt[:,1], 'v', markeredgecolor='k', markerfacecolor='none', label = r'PA')
plt.plot(Cp_Lim[:,0], Cp_Lim[:,1], 's', markeredgecolor='k', markerfacecolor='none', label = r'L')
plt.xlabel(r'', fontname="Times New Roman", fontsize=24)
plt.ylabel(r'$C_{p}$', fontname="Times New Roman", fontsize=24)
plt.ylim(-2.0, 1.20)
plt.xlim(0, 4.0)
ax.xaxis.set_ticks(np.arange(0,4.01,0.5))
ax.yaxis.set_ticks(np.arange(-2.0,1.201,0.4))
#plt.xticks([0.0, 0.1, 0.3, 0.4],('','','',''),rotation='horizontal')

xposition = [1, 2, 3, 4]
for xc in xposition:
    plt.axvline(x=xc, color='k', linewidth='1', linestyle='-')
plt.axhline(y=0.0, color='k', linewidth='1.5', linestyle='-')
plt.arrow( 0.48, 0.0, 0.01, 0.0, fc="k", ec="k", head_width=0.05, head_length=0.1 )
plt.arrow( 1.48, 0.0, 0.01, 0.0, fc="k", ec="k", head_width=0.05, head_length=0.1 )   
plt.arrow( 2.48, 0.0, 0.01, 0.0, fc="k", ec="k", head_width=0.05, head_length=0.1 )   
plt.arrow( 3.48, 0.0, 0.01, 0.0, fc="k", ec="k", head_width=0.05, head_length=0.1 )   

plt.text(0.11, 0.94,'Front face',
     horizontalalignment='center',
     verticalalignment='center',
     transform = ax.transAxes)
plt.text(0.37, 0.94,'Top face',
     horizontalalignment='center',
     verticalalignment='center',
     transform = ax.transAxes)
plt.text(0.63, 0.94,'Rear face',
     horizontalalignment='center',
     verticalalignment='center',
     transform = ax.transAxes)
plt.text(0.88, 0.94,'Side face',
     horizontalalignment='center',
     verticalalignment='center',
     transform = ax.transAxes)
plt.text(0.02, 0.58,'A',
     horizontalalignment='center',
     verticalalignment='center',
     transform = ax.transAxes)
plt.text(0.22, 0.58,'B',
     horizontalalignment='center',
     verticalalignment='center',
     transform = ax.transAxes)
plt.text(0.48, 0.65,'C',
     horizontalalignment='center',
     verticalalignment='center',
     transform = ax.transAxes)
plt.text(0.73, 0.65,'D',
     horizontalalignment='center',
     verticalalignment='center',
     transform = ax.transAxes)
plt.text(0.77, 0.65,'E',
     horizontalalignment='center',
     verticalalignment='center',
     transform = ax.transAxes)
plt.text(0.98, 0.65,'F',
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
plt.savefig('Cp_vertical_distribution_norm.png', dpi = 1000, bbox_inches = 'tight')
plt.savefig('Cp_vertical_distribution_norm.pdf', dpi = 1000, bbox_inches = 'tight')   
#Show figure
plt.show()
