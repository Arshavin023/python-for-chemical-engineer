print('''A cylindrical rod with a length L and diameter D is attached to a hot wall with temperature of Ts as depicted below. The ambient air temperature is constant at Tu. Heat transfer coefficient between rod surface to air is h.he diameter of the rod is small enough so we could ignore the radial temperature distribution in the rod. The rod is made of material that has a heat capacity of Cp, density ρ and heat conductivity k.Solve the equation using Method of Lines (MOL) and show the temperature distribution.''')

print('Use Finite difference to evaluate the temperature distribution along the length of the rod')
print(' '*30)
print('Equation: 𝜕^2T/𝜕𝑥^2 − (2ℎ/𝑘𝑅)(𝑇 − 𝑇𝑢) = (𝜌.𝑐𝑝/k)(𝑘𝜕𝑇𝜕𝑡)')
print(' '*30)
print('''Boundary condition:
o 𝑡 = 0; 𝑥 = 𝑥; 𝑇 = 𝑇𝑢
o 𝑡 = 𝑡; 𝑥 = 0; 𝑇 = 𝑇𝑠
o 𝑡 = 𝑡; 𝑥 = 𝐿; −𝑘(𝜕𝑇/𝜕𝑥) = h𝑇''')

#Import Libraries
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

#Parameters
k=.2
h=7e-4
D=1
L=20
Ts=400
Ta=30
rho=2.7
cp=.2
t=60

#Define arrays
Nx=15
x=np.linspace(0,L,Nx)
dx=x[1]-x[0]
Nt=11
tline=np.linspace(0,t,Nt)
Ti=np.ones(Nx)*Ta

# Define Functions
def PDE(T,t):
    alpha=1/(k/cp/rho)
    dTdt=np.zeros(len(T))
    T[0]=Ts
    T[-1]=(4*T[-2]-T[-3]+2*h*dx/k*Ta)/(3+2*h*dx/k)
    for i in range(1,Nx-1):
        dTdt[i]=alpha*(T[i+1]-2*T[i]+T[i-1])/dx**2-\
            alpha*2*h/k/(D/2)*(T[i]-Ta)
    return dTdt

T = odeint(PDE,Ti,tline)

T[:,0]=Ts
T[:,-1]=(4*T[:,-2]-T[:,-3]+2*h*dx/k*Ta)/(3+2*h*dx/k)

#Plotting
plt.figure(0)
for i in range(0,Nt):
    plt.plot(x,T[i,:])
plt.xlabel('Position; cm')
plt.ylabel('Temperature; $^{o}$C')
plt.grid()

plt.figure(1)
plt.imshow(T,cmap='jet',extent=[0,L,t,0],aspect=L/t)
plt.xlabel('Position; cm')
plt.ylabel('Times; s')
plt.colorbar(label='Temperature; $^{o}$C')
plt.grid()