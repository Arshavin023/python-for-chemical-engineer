
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

Nx = 21
Nt = 61
x = np.linspace(0,1,Nx)
dx = x[1]-x[0]
t = np.linspace(0,1,Nt)

def PDE(u,t):
    dudt = np.zeros(len(u))
    u[0] = 0.1
    u[-1] = (4*u[-2]-u[-3])/3
    for i in range(1,len(u)-1):
        dudt[i] = (u[i+1]-2*u[i]+u[i-1])/dx**2
    return dudt

ui = np.zeros(Nx)
u = odeint(PDE,ui,t)

u[:,0] = 0.1
u[:,-1] = (4*u[:,-2]-u[:,-3])/3


plt.figure(0)
plt.title('Temperature distribution of an insulated rod')
plt.imshow(u,cmap='jet',extent=(0,x[-1],t[-1],0),aspect=x[-1]/t[-1])
plt.xlabel('Position')
plt.ylabel('Time')
plt.colorbar(label='Temperature gradient; u')
plt.tight_layout()
plt.grid()

plt.figure(1)
for i in range(0,Nt):
    plt.plot(x,u[i,:])
plt.title('Temperature against Position of an insulated rod')
plt.xlabel('Position; cm')
plt.ylabel('Temperature gradient; u')
plt.tight_layout()

