import matplotlib.pyplot as plt
import numpy as np

# Ekman Spiral
fi = 51 * (np.pi/180)
omega = 0.0862129;

f = 2 * omega * np.sin(fi);   # Coriolis parameter
print "f = ", f

Km = 0.0053 # eddy-viscosity parameter

a0 = np.sqrt(f/(2*Km));
print "a0 = ", a0
hg = 3 # ABL height value
print "hg = ", hg

z = np.linspace(0.001,3,1000)  # Vertical coordinate
print "z = ", z

ug = 15.5
print "ug = ", ug

# Calculate Ekman Spiral
u = ug * ( 1 - np.exp(-a0 * z) * np.cos(a0 * z) )
v = ug * ( np.exp(-a0 * z) * np.sin(a0 * z) ) 
alpha = np.zeros(len(z))
for i in alpha:
    alpha = np.arctan2(v,u) * (180/np.pi)
print "u = ", u
print "v = ", v
print "alpha = ", alpha

np.savetxt("ekman_solution_z.csv", z, delimiter=" ")
np.savetxt("ekman_solution_u.csv", u, delimiter=" ")
np.savetxt("ekman_solution_v.csv", v, delimiter=" ")
np.savetxt("ekman_solution_alpha.csv", alpha, delimiter=" ")

u_ug = np.zeros(len(z))
for i in u_ug:
    u_ug = u/ug
v_ug = np.zeros(len(z))
for i in v_ug:
    v_ug = v/ug
magVel = np.zeros(len(z))
for i in magVel:
    magVel = np.sqrt(u*u+v*v)

a0z = np.zeros(len(z))
for i in z:
    a0z = a0 * z

#uag = np.zeros(len(z))
#vag = np.zeros(len(z))
#for i in uag:
#    uag = u - ug
#print "uag = ", uag
#for i in vag:
#    vag = v - vg
#print "vag = ", vag

#Lettau (1950) results
z_Lettau = np.array([50,
100,
150,
200,
250,
300,
350,
400,
450,
500,
550,
600,
650,
700,
750,
800,
850,
900,
950])

z_Lettau_scale = np.array([0.037509377344336,
0.075018754688672,
0.112528132033008,
0.150037509377344,
0.18754688672168,
0.225056264066016,
0.262565641410353,
0.300075018754689,
0.337584396099025,
0.375093773443361,
0.412603150787697,
0.450112528132033,
0.487621905476369,
0.525131282820705,
0.562640660165041,
0.600150037509377,
0.637659414853713,
0.675168792198049,
0.712678169542386])

u_Lettau_scale = np.array([8.16964285714286,
9.33035714285714,
10.3392857142857,
11.25,
12.0357142857143,
12.7678571428571,
13.3660714285714,
13.9464285714286,
14.5357142857143,
15.0267857142857,
15.4464285714286,
15.8035714285714,
16.0625,
16.2767857142857,
16.4464285714286,
16.6071428571429,
16.6607142857143,
16.6785714285714,
16.625])

v_Lettau_scale = np.array([3.88392857142857,
4.14285714285714,
4.28571428571429,
4.41964285714286,
4.42857142857143,
4.375,
4.26785714285714,
4.10714285714286,
3.83035714285714,
3.57142857142857,
3.3125,
3.00892857142857,
2.74107142857143,
2.4375,
2.16964285714286,
1.83928571428571,
1.51785714285714,
1.16964285714286,
0.8125])

magVel_Lettau_scale = np.zeros(len(z_Lettau_scale))
for i in magVel_Lettau_scale:
    magVel_Lettau_scale = np.sqrt(u_Lettau_scale*u_Lettau_scale+v_Lettau_scale*v_Lettau_scale)
alpha_Lettau_scale = np.zeros(len(z_Lettau_scale))
for i in alpha_Lettau_scale:
    alpha_Lettau_scale = np.arctan2(v_Lettau_scale,u_Lettau_scale) * (180/np.pi)

plt.axis([0,25,0,10])
plt.plot(u[0:len(z)],v[0:len(z)],'b')
plt.plot(u_Lettau_scale[0:len(z_Lettau_scale)],v_Lettau_scale[0:len(z_Lettau_scale)],'o')
plt.axis('square')
plt.grid('off')
plt.show()

#plt.axis([-0.2,1.2,0,4])
#plt.plot(v_ug,a0z,label='v/ug')
#plt.plot(u_ug,a0z,label='u/ug')
#plt.show()

plt.plot(u,z,label='u - Ekman (1905)')
#plt.plot(uag,z,label='uag')
plt.plot(v,z,label='v - Ekman (1905)')
#plt.plot(vag,z,label='vag')
plt.plot(magVel,z,label='magVel - Ekman (1905)')
plt.plot(u_Lettau_scale,z_Lettau_scale,'bo',label='u - Lettau (1950)')
plt.plot(v_Lettau_scale,z_Lettau_scale,'ro',label='v - Lettau (1950)')
plt.plot(magVel_Lettau_scale,z_Lettau_scale,'go',label='magVel - Lettau (1950)')
plt.legend()
plt.show()

plt.plot(alpha,z,label='alpha - Ekman (1905), deg')
plt.plot(alpha_Lettau_scale,z_Lettau_scale,'bo',label='alpha - Lettau (1950), deg')
plt.legend()
plt.show()
