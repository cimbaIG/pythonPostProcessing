import matplotlib
import numpy as np
import pylab as plt

#Change font type and font size in axis labels
matplotlib.rcParams.update({'legend.markerscale': 1.5, 'legend.handlelength': 1, 'legend.frameon': 0, 'legend.handletextpad': 1 , 'font.size': 18,'font.family':'Times New Roman'})

#matplotlib.rcParams['text.usetex'] = True
#matplotlib.rcParams['text.latex.unicode'] = True
matplotlib.rcParams['mathtext.fontset'] = 'stix'
matplotlib.rcParams['font.family'] = 'STIXGeneral'

################################################### Rural terrain ###################################################

sr5000_rural = np.loadtxt('SL1_stressResidual_5000_rural.dat')
sr10000_rural = np.loadtxt('SL1_stressResidual_10000_rural.dat')
sr15000_rural = np.loadtxt('SL1_stressResidual_15000_rural.dat')
sr20000_rural = np.loadtxt('SL1_stressResidual_20000_rural.dat')
sr25000_rural = np.loadtxt('SL1_stressResidual_25000_rural.dat')
sr30000_rural = np.loadtxt('SL1_stressResidual_30000_rural.dat')
sr35000_rural = np.loadtxt('SL1_stressResidual_35000_rural.dat')
sr40000_rural = np.loadtxt('SL1_stressResidual_40000_rural.dat')
sr45000_rural = np.loadtxt('SL1_stressResidual_45000_rural.dat')
sr50000_rural = np.loadtxt('SL1_stressResidual_50000_rural.dat')
sr55000_rural = np.loadtxt('SL1_stressResidual_55000_rural.dat')
sr60000_rural = np.loadtxt('SL1_stressResidual_60000_rural.dat')
sr65000_rural = np.loadtxt('SL1_stressResidual_65000_rural.dat')
sr70000_rural = np.loadtxt('SL1_stressResidual_70000_rural.dat')
sr75000_rural = np.loadtxt('SL1_stressResidual_75000_rural.dat')
sr80000_rural = np.loadtxt('SL1_stressResidual_80000_rural.dat')
sr85000_rural = np.loadtxt('SL1_stressResidual_85000_rural.dat')
sr90000_rural = np.loadtxt('SL1_stressResidual_90000_rural.dat')
sr95000_rural = np.loadtxt('SL1_stressResidual_95000_rural.dat')
sr100000_rural = np.loadtxt('SL1_stressResidual_100000_rural.dat')
sr105000_rural = np.loadtxt('SL1_stressResidual_105000_rural.dat')
sr110000_rural = np.loadtxt('SL1_stressResidual_110000_rural.dat')
sr115000_rural = np.loadtxt('SL1_stressResidual_115000_rural.dat')
sr120000_rural = np.loadtxt('SL1_stressResidual_120000_rural.dat')
sr125000_rural = np.loadtxt('SL1_stressResidual_125000_rural.dat')

ruralNumCorrections = np.arange(1,24.01,1)

diff5000_rural = np.zeros(np.size(sr5000_rural[:,1]))
for i in range(0,np.size(sr5000_rural[:,1])):
    diff5000_rural[i] = pow(sr5000_rural[i,1],2)

diff10000_rural = np.zeros(np.size(sr10000_rural[:,1]))
for i in range(0,np.size(sr10000_rural[:,1])):
    diff10000_rural[i] = pow(sr10000_rural[i,1],2)

diff15000_rural = np.zeros(np.size(sr15000_rural[:,1]))
for i in range(0,np.size(sr15000_rural[:,1])):
    diff15000_rural[i] = pow(sr15000_rural[i,1],2)

diff20000_rural = np.zeros(np.size(sr20000_rural[:,1]))
for i in range(0,np.size(sr20000_rural[:,1])):
    diff20000_rural[i] = pow(sr20000_rural[i,1],2)

diff25000_rural = np.zeros(np.size(sr25000_rural[:,1]))
for i in range(0,np.size(sr25000_rural[:,1])):
    diff25000_rural[i] = pow(sr25000_rural[i,1],2)

diff30000_rural = np.zeros(np.size(sr30000_rural[:,1]))
for i in range(0,np.size(sr30000_rural[:,1])):
    diff30000_rural[i] = pow(sr30000_rural[i,1],2)

diff35000_rural = np.zeros(np.size(sr35000_rural[:,1]))
for i in range(0,np.size(sr35000_rural[:,1])):
    diff35000_rural[i] = pow(sr35000_rural[i,1],2)

diff40000_rural = np.zeros(np.size(sr40000_rural[:,1]))
for i in range(0,np.size(sr40000_rural[:,1])):
    diff40000_rural[i] = pow(sr40000_rural[i,1],2)

diff45000_rural = np.zeros(np.size(sr45000_rural[:,1]))
for i in range(0,np.size(sr45000_rural[:,1])):
    diff45000_rural[i] = pow(sr45000_rural[i,1],2)

diff50000_rural = np.zeros(np.size(sr50000_rural[:,1]))
for i in range(0,np.size(sr50000_rural[:,1])):
    diff50000_rural[i] = pow(sr50000_rural[i,1],2)

diff55000_rural = np.zeros(np.size(sr55000_rural[:,1]))
for i in range(0,np.size(sr55000_rural[:,1])):
    diff55000_rural[i] = pow(sr55000_rural[i,1],2)

diff60000_rural = np.zeros(np.size(sr60000_rural[:,1]))
for i in range(0,np.size(sr60000_rural[:,1])):
    diff60000_rural[i] = pow(sr60000_rural[i,1],2)

diff65000_rural = np.zeros(np.size(sr65000_rural[:,1]))
for i in range(0,np.size(sr65000_rural[:,1])):
    diff65000_rural[i] = pow(sr65000_rural[i,1],2)

diff70000_rural = np.zeros(np.size(sr70000_rural[:,1]))
for i in range(0,np.size(sr70000_rural[:,1])):
    diff70000_rural[i] = pow(sr70000_rural[i,1],2)

diff75000_rural = np.zeros(np.size(sr75000_rural[:,1]))
for i in range(0,np.size(sr75000_rural[:,1])):
    diff75000_rural[i] = pow(sr75000_rural[i,1],2)

diff80000_rural = np.zeros(np.size(sr80000_rural[:,1]))
for i in range(0,np.size(sr80000_rural[:,1])):
    diff80000_rural[i] = pow(sr80000_rural[i,1],2)

diff85000_rural = np.zeros(np.size(sr85000_rural[:,1]))
for i in range(0,np.size(sr85000_rural[:,1])):
    diff85000_rural[i] = pow(sr85000_rural[i,1],2)

diff90000_rural = np.zeros(np.size(sr90000_rural[:,1]))
for i in range(0,np.size(sr90000_rural[:,1])):
    diff90000_rural[i] = pow(sr90000_rural[i,1],2)

diff95000_rural = np.zeros(np.size(sr95000_rural[:,1]))
for i in range(0,np.size(sr95000_rural[:,1])):
    diff95000_rural[i] = pow(sr95000_rural[i,1],2)

diff100000_rural = np.zeros(np.size(sr100000_rural[:,1]))
for i in range(0,np.size(sr100000_rural[:,1])):
    diff100000_rural[i] = pow(sr100000_rural[i,1],2)

diff105000_rural = np.zeros(np.size(sr105000_rural[:,1]))
for i in range(0,np.size(sr105000_rural[:,1])):
    diff105000_rural[i] = pow(sr105000_rural[i,1],2)

diff110000_rural = np.zeros(np.size(sr110000_rural[:,1]))
for i in range(0,np.size(sr110000_rural[:,1])):
    diff110000_rural[i] = pow(sr110000_rural[i,1],2)

diff115000_rural = np.zeros(np.size(sr115000_rural[:,1]))
for i in range(0,np.size(sr115000_rural[:,1])):
    diff115000_rural[i] = pow(sr115000_rural[i,1],2)

diff120000_rural = np.zeros(np.size(sr120000_rural[:,1]))
for i in range(0,np.size(sr120000_rural[:,1])):
    diff120000_rural[i] = pow(sr120000_rural[i,1],2)

diff125000_rural = np.zeros(np.size(sr125000_rural[:,1]))
for i in range(0,np.size(sr125000_rural[:,1])):
    diff125000_rural[i] = pow(sr125000_rural[i,1],2)

STD_rural = np.array([ np.sqrt( np.sum(diff5000_rural) / (np.size(sr5000_rural[:,1])) ),
np.sqrt( np.sum(diff10000_rural) / (np.size(sr10000_rural[:,1])) ),
np.sqrt( np.sum(diff15000_rural) / (np.size(sr15000_rural[:,1])) ),
np.sqrt( np.sum(diff20000_rural) / (np.size(sr20000_rural[:,1])) ),
np.sqrt( np.sum(diff25000_rural) / (np.size(sr25000_rural[:,1])) ),
np.sqrt( np.sum(diff30000_rural) / (np.size(sr30000_rural[:,1])) ),
np.sqrt( np.sum(diff35000_rural) / (np.size(sr35000_rural[:,1])) ),
np.sqrt( np.sum(diff40000_rural) / (np.size(sr40000_rural[:,1])) ),
np.sqrt( np.sum(diff45000_rural) / (np.size(sr45000_rural[:,1])) ),
np.sqrt( np.sum(diff50000_rural) / (np.size(sr50000_rural[:,1])) ),
np.sqrt( np.sum(diff55000_rural) / (np.size(sr55000_rural[:,1])) ),
np.sqrt( np.sum(diff60000_rural) / (np.size(sr60000_rural[:,1])) ),
np.sqrt( np.sum(diff65000_rural) / (np.size(sr65000_rural[:,1])) ),
np.sqrt( np.sum(diff70000_rural) / (np.size(sr70000_rural[:,1])) ),
np.sqrt( np.sum(diff75000_rural) / (np.size(sr75000_rural[:,1])) ),
np.sqrt( np.sum(diff80000_rural) / (np.size(sr80000_rural[:,1])) ),
np.sqrt( np.sum(diff85000_rural) / (np.size(sr85000_rural[:,1])) ),
np.sqrt( np.sum(diff90000_rural) / (np.size(sr90000_rural[:,1])) ),
np.sqrt( np.sum(diff95000_rural) / (np.size(sr95000_rural[:,1])) ),
np.sqrt( np.sum(diff100000_rural) / (np.size(sr100000_rural[:,1])) ),
np.sqrt( np.sum(diff105000_rural) / (np.size(sr105000_rural[:,1])) ),
np.sqrt( np.sum(diff110000_rural) / (np.size(sr110000_rural[:,1])) ),
np.sqrt( np.sum(diff115000_rural) / (np.size(sr115000_rural[:,1])) ),
np.sqrt( np.sum(diff120000_rural) / (np.size(sr120000_rural[:,1])) )  ])
#np.sqrt( np.sum(diff125000_rural) / (np.size(sr125000_rural[:,1])) ) ])

################################################### SubUrban terrain ###################################################

sr5000_suburban = np.loadtxt('SL1_stressResidual_5000_suburban.dat')
sr10000_suburban = np.loadtxt('SL1_stressResidual_10000_suburban.dat')
sr15000_suburban = np.loadtxt('SL1_stressResidual_15000_suburban.dat')
sr20000_suburban = np.loadtxt('SL1_stressResidual_20000_suburban.dat')
sr25000_suburban = np.loadtxt('SL1_stressResidual_25000_suburban.dat')
sr30000_suburban = np.loadtxt('SL1_stressResidual_30000_suburban.dat')
sr35000_suburban = np.loadtxt('SL1_stressResidual_35000_suburban.dat')
sr40000_suburban = np.loadtxt('SL1_stressResidual_40000_suburban.dat')
sr45000_suburban = np.loadtxt('SL1_stressResidual_45000_suburban.dat')
sr50000_suburban = np.loadtxt('SL1_stressResidual_50000_suburban.dat')
sr55000_suburban = np.loadtxt('SL1_stressResidual_55000_suburban.dat')
sr60000_suburban = np.loadtxt('SL1_stressResidual_60000_suburban.dat')
sr65000_suburban = np.loadtxt('SL1_stressResidual_65000_suburban.dat')
sr70000_suburban = np.loadtxt('SL1_stressResidual_70000_suburban.dat')
sr75000_suburban = np.loadtxt('SL1_stressResidual_75000_suburban.dat')
sr80000_suburban = np.loadtxt('SL1_stressResidual_80000_suburban.dat')
sr85000_suburban = np.loadtxt('SL1_stressResidual_85000_suburban.dat')
sr90000_suburban = np.loadtxt('SL1_stressResidual_90000_suburban.dat')
sr95000_suburban = np.loadtxt('SL1_stressResidual_95000_suburban.dat')
sr100000_suburban = np.loadtxt('SL1_stressResidual_100000_suburban.dat')
sr105000_suburban = np.loadtxt('SL1_stressResidual_105000_suburban.dat')
sr110000_suburban = np.loadtxt('SL1_stressResidual_110000_suburban.dat')
sr115000_suburban = np.loadtxt('SL1_stressResidual_115000_suburban.dat')
sr120000_suburban = np.loadtxt('SL1_stressResidual_120000_suburban.dat')
sr125000_suburban = np.loadtxt('SL1_stressResidual_125000_suburban.dat')

suburbanNumCorrections = np.arange(1,24.01,1)

diff5000_suburban = np.zeros(np.size(sr5000_suburban[:,1]))
for i in range(0,np.size(sr5000_suburban[:,1])):
    diff5000_suburban[i] = pow(sr5000_suburban[i,1],2)

diff10000_suburban = np.zeros(np.size(sr10000_suburban[:,1]))
for i in range(0,np.size(sr10000_suburban[:,1])):
    diff10000_suburban[i] = pow(sr10000_suburban[i,1],2)

diff15000_suburban = np.zeros(np.size(sr15000_suburban[:,1]))
for i in range(0,np.size(sr15000_suburban[:,1])):
    diff15000_suburban[i] = pow(sr15000_suburban[i,1],2)

diff20000_suburban = np.zeros(np.size(sr20000_suburban[:,1]))
for i in range(0,np.size(sr20000_suburban[:,1])):
    diff20000_suburban[i] = pow(sr20000_suburban[i,1],2)

diff25000_suburban = np.zeros(np.size(sr25000_suburban[:,1]))
for i in range(0,np.size(sr25000_suburban[:,1])):
    diff25000_suburban[i] = pow(sr25000_suburban[i,1],2)

diff30000_suburban = np.zeros(np.size(sr30000_suburban[:,1]))
for i in range(0,np.size(sr30000_suburban[:,1])):
    diff30000_suburban[i] = pow(sr30000_suburban[i,1],2)

diff35000_suburban = np.zeros(np.size(sr35000_suburban[:,1]))
for i in range(0,np.size(sr35000_suburban[:,1])):
    diff35000_suburban[i] = pow(sr35000_suburban[i,1],2)

diff40000_suburban = np.zeros(np.size(sr40000_suburban[:,1]))
for i in range(0,np.size(sr40000_suburban[:,1])):
    diff40000_suburban[i] = pow(sr40000_suburban[i,1],2)

diff45000_suburban = np.zeros(np.size(sr45000_suburban[:,1]))
for i in range(0,np.size(sr45000_suburban[:,1])):
    diff45000_suburban[i] = pow(sr45000_suburban[i,1],2)

diff50000_suburban = np.zeros(np.size(sr50000_suburban[:,1]))
for i in range(0,np.size(sr50000_suburban[:,1])):
    diff50000_suburban[i] = pow(sr50000_suburban[i,1],2)

diff55000_suburban = np.zeros(np.size(sr55000_suburban[:,1]))
for i in range(0,np.size(sr55000_suburban[:,1])):
    diff55000_suburban[i] = pow(sr55000_suburban[i,1],2)

diff60000_suburban = np.zeros(np.size(sr60000_suburban[:,1]))
for i in range(0,np.size(sr60000_suburban[:,1])):
    diff60000_suburban[i] = pow(sr60000_suburban[i,1],2)

diff65000_suburban = np.zeros(np.size(sr65000_suburban[:,1]))
for i in range(0,np.size(sr65000_suburban[:,1])):
    diff65000_suburban[i] = pow(sr65000_suburban[i,1],2)

diff70000_suburban = np.zeros(np.size(sr70000_suburban[:,1]))
for i in range(0,np.size(sr70000_suburban[:,1])):
    diff70000_suburban[i] = pow(sr70000_suburban[i,1],2)

diff75000_suburban = np.zeros(np.size(sr75000_suburban[:,1]))
for i in range(0,np.size(sr75000_suburban[:,1])):
    diff75000_suburban[i] = pow(sr75000_suburban[i,1],2)

diff80000_suburban = np.zeros(np.size(sr80000_suburban[:,1]))
for i in range(0,np.size(sr80000_suburban[:,1])):
    diff80000_suburban[i] = pow(sr80000_suburban[i,1],2)

diff85000_suburban = np.zeros(np.size(sr85000_suburban[:,1]))
for i in range(0,np.size(sr85000_suburban[:,1])):
    diff85000_suburban[i] = pow(sr85000_suburban[i,1],2)

diff90000_suburban = np.zeros(np.size(sr90000_suburban[:,1]))
for i in range(0,np.size(sr90000_suburban[:,1])):
    diff90000_suburban[i] = pow(sr90000_suburban[i,1],2)

diff95000_suburban = np.zeros(np.size(sr95000_suburban[:,1]))
for i in range(0,np.size(sr95000_suburban[:,1])):
    diff95000_suburban[i] = pow(sr95000_suburban[i,1],2)

diff100000_suburban = np.zeros(np.size(sr100000_suburban[:,1]))
for i in range(0,np.size(sr100000_suburban[:,1])):
    diff100000_suburban[i] = pow(sr100000_suburban[i,1],2)

diff105000_suburban = np.zeros(np.size(sr105000_suburban[:,1]))
for i in range(0,np.size(sr105000_suburban[:,1])):
    diff105000_suburban[i] = pow(sr105000_suburban[i,1],2)

diff110000_suburban = np.zeros(np.size(sr110000_suburban[:,1]))
for i in range(0,np.size(sr110000_suburban[:,1])):
    diff110000_suburban[i] = pow(sr110000_suburban[i,1],2)

diff115000_suburban = np.zeros(np.size(sr115000_suburban[:,1]))
for i in range(0,np.size(sr115000_suburban[:,1])):
    diff115000_suburban[i] = pow(sr115000_suburban[i,1],2)

diff120000_suburban = np.zeros(np.size(sr120000_suburban[:,1]))
for i in range(0,np.size(sr120000_suburban[:,1])):
    diff120000_suburban[i] = pow(sr120000_suburban[i,1],2)

diff125000_suburban = np.zeros(np.size(sr125000_suburban[:,1]))
for i in range(0,np.size(sr125000_suburban[:,1])):
    diff125000_suburban[i] = pow(sr125000_suburban[i,1],2)

STD_suburban = np.array([ np.sqrt( np.sum(diff5000_suburban) / (np.size(sr5000_suburban[:,1])) ),
np.sqrt( np.sum(diff10000_suburban) / (np.size(sr10000_suburban[:,1])) ),
np.sqrt( np.sum(diff15000_suburban) / (np.size(sr15000_suburban[:,1])) ),
np.sqrt( np.sum(diff20000_suburban) / (np.size(sr20000_suburban[:,1])) ),
np.sqrt( np.sum(diff25000_suburban) / (np.size(sr25000_suburban[:,1])) ),
np.sqrt( np.sum(diff30000_suburban) / (np.size(sr30000_suburban[:,1])) ),
np.sqrt( np.sum(diff35000_suburban) / (np.size(sr35000_suburban[:,1])) ),
np.sqrt( np.sum(diff40000_suburban) / (np.size(sr40000_suburban[:,1])) ),
np.sqrt( np.sum(diff45000_suburban) / (np.size(sr45000_suburban[:,1])) ),
np.sqrt( np.sum(diff50000_suburban) / (np.size(sr50000_suburban[:,1])) ),
np.sqrt( np.sum(diff55000_suburban) / (np.size(sr55000_suburban[:,1])) ),
np.sqrt( np.sum(diff60000_suburban) / (np.size(sr60000_suburban[:,1])) ),
np.sqrt( np.sum(diff65000_suburban) / (np.size(sr65000_suburban[:,1])) ),
np.sqrt( np.sum(diff70000_suburban) / (np.size(sr70000_suburban[:,1])) ),
np.sqrt( np.sum(diff75000_suburban) / (np.size(sr75000_suburban[:,1])) ),
np.sqrt( np.sum(diff80000_suburban) / (np.size(sr80000_suburban[:,1])) ),
np.sqrt( np.sum(diff85000_suburban) / (np.size(sr85000_suburban[:,1])) ),
np.sqrt( np.sum(diff90000_suburban) / (np.size(sr90000_suburban[:,1])) ),
np.sqrt( np.sum(diff95000_suburban) / (np.size(sr95000_suburban[:,1])) ),
np.sqrt( np.sum(diff100000_suburban) / (np.size(sr100000_suburban[:,1])) ),
np.sqrt( np.sum(diff105000_suburban) / (np.size(sr105000_suburban[:,1])) ),
np.sqrt( np.sum(diff110000_suburban) / (np.size(sr110000_suburban[:,1])) ),
np.sqrt( np.sum(diff115000_suburban) / (np.size(sr115000_suburban[:,1])) ),
np.sqrt( np.sum(diff120000_suburban) / (np.size(sr120000_suburban[:,1])) )  ])
#np.sqrt( np.sum(diff125000_suburban) / (np.size(sr125000_suburban[:,1])) ) ])

################################################### Urban terrain ###################################################

sr5000_urban = np.loadtxt('SL1_stressResidual_5000_urban.dat')
sr10000_urban = np.loadtxt('SL1_stressResidual_10000_urban.dat')
sr15000_urban = np.loadtxt('SL1_stressResidual_15000_urban.dat')
sr20000_urban = np.loadtxt('SL1_stressResidual_20000_urban.dat')
sr25000_urban = np.loadtxt('SL1_stressResidual_25000_urban.dat')
sr30000_urban = np.loadtxt('SL1_stressResidual_30000_urban.dat')
sr35000_urban = np.loadtxt('SL1_stressResidual_35000_urban.dat')
sr40000_urban = np.loadtxt('SL1_stressResidual_40000_urban.dat')
sr45000_urban = np.loadtxt('SL1_stressResidual_45000_urban.dat')
sr50000_urban = np.loadtxt('SL1_stressResidual_50000_urban.dat')
sr55000_urban = np.loadtxt('SL1_stressResidual_55000_urban.dat')
sr60000_urban = np.loadtxt('SL1_stressResidual_60000_urban.dat')
sr65000_urban = np.loadtxt('SL1_stressResidual_65000_urban.dat')
sr70000_urban = np.loadtxt('SL1_stressResidual_70000_urban.dat')
sr75000_urban = np.loadtxt('SL1_stressResidual_75000_urban.dat')
sr80000_urban = np.loadtxt('SL1_stressResidual_80000_urban.dat')
sr85000_urban = np.loadtxt('SL1_stressResidual_85000_urban.dat')
sr90000_urban = np.loadtxt('SL1_stressResidual_90000_urban.dat')
sr95000_urban = np.loadtxt('SL1_stressResidual_95000_urban.dat')
sr100000_urban = np.loadtxt('SL1_stressResidual_100000_urban.dat')
sr105000_urban = np.loadtxt('SL1_stressResidual_105000_urban.dat')
sr110000_urban = np.loadtxt('SL1_stressResidual_110000_urban.dat')
sr115000_urban = np.loadtxt('SL1_stressResidual_115000_urban.dat')
sr120000_urban = np.loadtxt('SL1_stressResidual_120000_urban.dat')
sr125000_urban = np.loadtxt('SL1_stressResidual_125000_urban.dat')

urbanNumCorrections = np.arange(1,24.01,1)

diff5000_urban = np.zeros(np.size(sr5000_urban[:,1]))
for i in range(0,np.size(sr5000_urban[:,1])):
    diff5000_urban[i] = pow(sr5000_urban[i,1],2)

diff10000_urban = np.zeros(np.size(sr10000_urban[:,1]))
for i in range(0,np.size(sr10000_urban[:,1])):
    diff10000_urban[i] = pow(sr10000_urban[i,1],2)

diff15000_urban = np.zeros(np.size(sr15000_urban[:,1]))
for i in range(0,np.size(sr15000_urban[:,1])):
    diff15000_urban[i] = pow(sr15000_urban[i,1],2)

diff20000_urban = np.zeros(np.size(sr20000_urban[:,1]))
for i in range(0,np.size(sr20000_urban[:,1])):
    diff20000_urban[i] = pow(sr20000_urban[i,1],2)

diff25000_urban = np.zeros(np.size(sr25000_urban[:,1]))
for i in range(0,np.size(sr25000_urban[:,1])):
    diff25000_urban[i] = pow(sr25000_urban[i,1],2)

diff30000_urban = np.zeros(np.size(sr30000_urban[:,1]))
for i in range(0,np.size(sr30000_urban[:,1])):
    diff30000_urban[i] = pow(sr30000_urban[i,1],2)

diff35000_urban = np.zeros(np.size(sr35000_urban[:,1]))
for i in range(0,np.size(sr35000_urban[:,1])):
    diff35000_urban[i] = pow(sr35000_urban[i,1],2)

diff40000_urban = np.zeros(np.size(sr40000_urban[:,1]))
for i in range(0,np.size(sr40000_urban[:,1])):
    diff40000_urban[i] = pow(sr40000_urban[i,1],2)

diff45000_urban = np.zeros(np.size(sr45000_urban[:,1]))
for i in range(0,np.size(sr45000_urban[:,1])):
    diff45000_urban[i] = pow(sr45000_urban[i,1],2)

diff50000_urban = np.zeros(np.size(sr50000_urban[:,1]))
for i in range(0,np.size(sr50000_urban[:,1])):
    diff50000_urban[i] = pow(sr50000_urban[i,1],2)

diff55000_urban = np.zeros(np.size(sr55000_urban[:,1]))
for i in range(0,np.size(sr55000_urban[:,1])):
    diff55000_urban[i] = pow(sr55000_urban[i,1],2)

diff60000_urban = np.zeros(np.size(sr60000_urban[:,1]))
for i in range(0,np.size(sr60000_urban[:,1])):
    diff60000_urban[i] = pow(sr60000_urban[i,1],2)

diff65000_urban = np.zeros(np.size(sr65000_urban[:,1]))
for i in range(0,np.size(sr65000_urban[:,1])):
    diff65000_urban[i] = pow(sr65000_urban[i,1],2)

diff70000_urban = np.zeros(np.size(sr70000_urban[:,1]))
for i in range(0,np.size(sr70000_urban[:,1])):
    diff70000_urban[i] = pow(sr70000_urban[i,1],2)

diff75000_urban = np.zeros(np.size(sr75000_urban[:,1]))
for i in range(0,np.size(sr75000_urban[:,1])):
    diff75000_urban[i] = pow(sr75000_urban[i,1],2)

diff80000_urban = np.zeros(np.size(sr80000_urban[:,1]))
for i in range(0,np.size(sr80000_urban[:,1])):
    diff80000_urban[i] = pow(sr80000_urban[i,1],2)

diff85000_urban = np.zeros(np.size(sr85000_urban[:,1]))
for i in range(0,np.size(sr85000_urban[:,1])):
    diff85000_urban[i] = pow(sr85000_urban[i,1],2)

diff90000_urban = np.zeros(np.size(sr90000_urban[:,1]))
for i in range(0,np.size(sr90000_urban[:,1])):
    diff90000_urban[i] = pow(sr90000_urban[i,1],2)

diff95000_urban = np.zeros(np.size(sr95000_urban[:,1]))
for i in range(0,np.size(sr95000_urban[:,1])):
    diff95000_urban[i] = pow(sr95000_urban[i,1],2)

diff100000_urban = np.zeros(np.size(sr100000_urban[:,1]))
for i in range(0,np.size(sr100000_urban[:,1])):
    diff100000_urban[i] = pow(sr100000_urban[i,1],2)

diff105000_urban = np.zeros(np.size(sr105000_urban[:,1]))
for i in range(0,np.size(sr105000_urban[:,1])):
    diff105000_urban[i] = pow(sr105000_urban[i,1],2)

diff110000_urban = np.zeros(np.size(sr110000_urban[:,1]))
for i in range(0,np.size(sr110000_urban[:,1])):
    diff110000_urban[i] = pow(sr110000_urban[i,1],2)

diff115000_urban = np.zeros(np.size(sr115000_urban[:,1]))
for i in range(0,np.size(sr115000_urban[:,1])):
    diff115000_urban[i] = pow(sr115000_urban[i,1],2)

diff120000_urban = np.zeros(np.size(sr120000_urban[:,1]))
for i in range(0,np.size(sr120000_urban[:,1])):
    diff120000_urban[i] = pow(sr120000_urban[i,1],2)

diff125000_urban = np.zeros(np.size(sr125000_urban[:,1]))
for i in range(0,np.size(sr125000_urban[:,1])):
    diff125000_urban[i] = pow(sr125000_urban[i,1],2)

STD_urban = np.array([ np.sqrt( np.sum(diff5000_urban) / (np.size(sr5000_urban[:,1])) ),
np.sqrt( np.sum(diff10000_urban) / (np.size(sr10000_urban[:,1])) ),
np.sqrt( np.sum(diff15000_urban) / (np.size(sr15000_urban[:,1])) ),
np.sqrt( np.sum(diff20000_urban) / (np.size(sr20000_urban[:,1])) ),
np.sqrt( np.sum(diff25000_urban) / (np.size(sr25000_urban[:,1])) ),
np.sqrt( np.sum(diff30000_urban) / (np.size(sr30000_urban[:,1])) ),
np.sqrt( np.sum(diff35000_urban) / (np.size(sr35000_urban[:,1])) ),
np.sqrt( np.sum(diff40000_urban) / (np.size(sr40000_urban[:,1])) ),
np.sqrt( np.sum(diff45000_urban) / (np.size(sr45000_urban[:,1])) ),
np.sqrt( np.sum(diff50000_urban) / (np.size(sr50000_urban[:,1])) ),
np.sqrt( np.sum(diff55000_urban) / (np.size(sr55000_urban[:,1])) ),
np.sqrt( np.sum(diff60000_urban) / (np.size(sr60000_urban[:,1])) ),
np.sqrt( np.sum(diff65000_urban) / (np.size(sr65000_urban[:,1])) ),
np.sqrt( np.sum(diff70000_urban) / (np.size(sr70000_urban[:,1])) ),
np.sqrt( np.sum(diff75000_urban) / (np.size(sr75000_urban[:,1])) ),
np.sqrt( np.sum(diff80000_urban) / (np.size(sr80000_urban[:,1])) ),
np.sqrt( np.sum(diff85000_urban) / (np.size(sr85000_urban[:,1])) ),
np.sqrt( np.sum(diff90000_urban) / (np.size(sr90000_urban[:,1])) ),
np.sqrt( np.sum(diff95000_urban) / (np.size(sr95000_urban[:,1])) ),
np.sqrt( np.sum(diff100000_urban) / (np.size(sr100000_urban[:,1])) ),
np.sqrt( np.sum(diff105000_urban) / (np.size(sr105000_urban[:,1])) ),
np.sqrt( np.sum(diff110000_urban) / (np.size(sr110000_urban[:,1])) ),
np.sqrt( np.sum(diff115000_urban) / (np.size(sr115000_urban[:,1])) ),
np.sqrt( np.sum(diff120000_urban) / (np.size(sr120000_urban[:,1])) ) ])
#np.sqrt( np.sum(diff125000_urban) / (np.size(sr125000_urban[:,1])) ) ])

################################################### Plot residuals ###################################################

#fig = plt.subplot(1, 3, 1)
fig = plt.figure(1)
ax = plt.axes()
plt.plot(ruralNumCorrections, STD_rural, 'o', markeredgecolor='k', markerfacecolor='none', markersize=8, label=r'Rural terrain')
plt.plot(suburbanNumCorrections, STD_suburban, 's', markeredgecolor='k', markerfacecolor='none', markersize=8, label=r'Suburban terrain')
plt.plot(urbanNumCorrections, STD_urban, '+', markeredgecolor='k', markerfacecolor='none', markersize=8, label=r'Urban terrain')
#plt.plot(xnew, ynew, '-', linewidth='1.5', color='k' , label='Best fit')
#plt.xlabel('Mean velocity, $\overline{u}/u_\mathrm{ref}$ m/s \n a)', fontname="Times New Roman", fontsize=22)
plt.xlabel(r'Correction', fontname="Times New Roman", fontsize=18)
plt.ylabel(r'Standard deviation $\sigma$', fontname="Times New Roman", fontsize=18)
plt.xlim(0, 24.3)
plt.ylim(0.04, 0.28)
starty, endy = (0.04, 0.2801)
startx, endx = (0, 24.01)
ax.yaxis.set_ticks(np.arange(starty,endy,0.04))
ax.xaxis.set_ticks(np.arange(startx,endx,2))
plt.grid(False)
legend = plt.legend(numpoints=1, loc=1)
frame = legend.get_frame()
frame.set_facecolor('white')
frame.set_linewidth(0)

#Get current figure
figure = plt.gcf()
#Set figure size
figure.set_size_inches(8, 5)
#When saving, specify the DPI
plt.savefig('convergenceWS.png', dpi = 250, bbox_inches='tight')
plt.savefig('convergenceWS.pdf', bbox_inches='tight')
#Show figure
plt.show()

################################################################################################################