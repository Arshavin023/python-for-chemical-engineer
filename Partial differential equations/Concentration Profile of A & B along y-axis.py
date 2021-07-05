import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

k=.1
Da=3e-5
Db=4e-5
d=3.2e-2
L=200
rho=1
g=1e3
Cbs=60
Ca0=.1
miu=2e-2

Nx=8
x=np.linspace(0,d,Nx)
dx=x[1]-x[0]
Ny=8
y=np.linspace(0,L,Ny)
Cainit=np.ones(Nx)*Ca0
Cbinit=np.zeros(Nx)
Cinit=np.concatenate((Cainit,Cbinit))

def FF(C,y):
    dCady=np.zeros(Nx)
    dCbdy=np.zeros(Nx)
    Ca=C[0:Nx]
    Cb=C[Nx:2*Nx+1]
    Cb[0]=Cbs
    Ca[0]=(-Ca[2]+4*Ca[1])/3
    Cb[-1]=(-Cb[-3]+4*Cb[-2])/3
    Ca[-1]=(-Ca[-3]+4*Ca[-2])/3
    for i in range(1,Nx-1):
        vy=rho*g*d/miu*(x[i]-x[i]**2/2/d)
        dCady[i]=(Da*(Ca[i+1]-2*Ca[i]+Ca[i-1])/dx**2-\
                  k*Ca[i]*Cb[i])/vy
        dCbdy[i]=(Db*(Cb[i+1]-2*Cb[i]+Cb[i-1])/dx**2-\
                  2*k*Ca[i]*Cb[i])/vy
    dCdy=np.concatenate((dCady,dCbdy))
    return dCdy

Cres=odeint(FF,Cinit,y)
Ca=Cres[:,0:Nx]
Cb=Cres[:,Nx:2*Nx+1]
Cb[:,0]=Cbs
Ca[:,0]=(-Ca[:,2]+4*Ca[:,1])/3
Cb[:,-1]=(-Cb[:,-3]+4*Cb[:,-2])/3
Ca[:,-1]=(-Ca[:,-3]+4*Ca[:,-2])/3

plt.figure(1)
plt.imshow(Ca,cmap='jet',extent=(0,d,L,0),aspect=d/L)
plt.colorbar(label='Concentration of A; mol cm$^{-3}$')
plt.ylabel('Vertical Position; cm')
plt.xlabel('Horizontal Position; cm')
plt.tight_layout()
plt.grid()
plt.figure(2)
plt.imshow(Cb,cmap='jet',extent=(0,d,L,0),aspect=d/L)
plt.colorbar(label='Concentration of B; mol cm$^{-3}$')
plt.ylabel('Vertical Position; cm')
plt.xlabel('Horizontal Position; cm')
plt.tight_layout()
plt.grid()