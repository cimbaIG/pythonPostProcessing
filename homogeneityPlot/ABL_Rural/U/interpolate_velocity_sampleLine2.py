import matplotlib
from scipy.interpolate import interp1d
import numpy as np
import pylab as plt

readVelocity = np.loadtxt('U_lineX1_norm.txt')
interpolation = interp1d(readVelocity[:,0], readVelocity[:,1],  kind='cubic')

xnew = np.linspace(0, 1.3, num=10, endpoint=True)
plt.plot(readVelocity[:,0], readVelocity[:,1], 'o', interpolation(xnew), '--')

plt.show()
