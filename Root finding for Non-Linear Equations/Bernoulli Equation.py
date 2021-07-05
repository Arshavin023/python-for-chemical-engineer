# 𝐻𝑚=3718.5−2.3496∙𝑄+7.8474∙〖10〗^(−4)∙𝑄^2−9.5812.〖10〗^(−8)∙𝑄^3
# 𝑄=(𝜋∙〖𝐷𝑝〗^2∙𝑣)/4
# 𝑧_2−𝑧_1+(𝑓∙𝐿𝑒∙𝑣^2)/(2∙𝑔∙𝐷𝑝)−𝐻𝑚=0
# 𝑓=0.0596/〖𝑅𝑒〗^0.215 
# 𝑅𝑒=(𝜌∙𝑣∙𝐷𝑝)/𝜇
# Use formatted printing to show a table of Velocity and Diameter
# Estimate the liquid velocity (v) and flowrate (Q) in the pipe. 
# Plot the value of v for various value of Dp (1<Dp<10 cm) 

import numpy as np
from scipy.optimize import fsolve
import matplotlib.pyplot as plt

p = 1
u = 0.01
g = 981
z1 = 300
z2 = 800
Le = 20000
Dpspan = np.linspace(1,10,10)

#Solver
def bern(v,Dp,Le,g,p,u,z1,z2):    
    Q = (np.pi*Dp**2*v)/4
    h = (3718.5-2.3496*Q)+(7.8474*10**-4)*(Q**2-9.5812*10**-8*10**3)
    Re = (p*v*Dp)/u
    f = 0.0596/Re**0.215
    F = z2-z1+(f*Le*v**2)/(2*g*Dp)-h
    return F

vstore_diameter = np.zeros([len(Dpspan),2])
vguess = 1

for i in range(0, len(Dpspan)):
    Dpnow = Dpspan[i]
    v = fsolve(bern, vguess, args=(Dpnow,Le,g,p,u,z1,z2))
    vstore_diameter[i,0] = v
    vstore_diameter[i,1] = Dpnow

#Formatted Printing
header = ['Velocity(m/s)', 'Diameter(m)']
print('-'*30)
print('{:^10s} {:^14s}'.format(*header))
print('_'*30)

for row in vstore_diameter:
    print('{:^10.2f} {:>10.2f}'.format(*row))
    
# Plotting
plt.plot(Dpspan, vstore_diameter[:,0],'--g',linewidth=2,markersize=2)
plt.xlabel('Diameter(m)')
plt.ylabel('Velocity(m/s)')
plt.grid()


    


    

