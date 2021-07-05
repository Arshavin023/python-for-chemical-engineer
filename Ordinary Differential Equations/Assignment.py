
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

y10 = 1
y20 = 0.05
IC = np.array([y10,y20])
print(IC)

def myfun(Y,t):
    dYdt=np.zeros(len(IC))
    y1 = Y[0]
    y2 = Y[1]
    dYdt[0] = 0.35*y1+1.6*y1*y2
    dYdt[1] = 0.04*y1*y2-0.15*y2
    return dYdt

tspan = np.linspace(0,100,101)

Y = odeint(myfun,IC,tspan)
print(Y)

plt.figure()
plt.subplot(211)
plt.title('Y against Time')
plt.plot(tspan,Y[:,0],'-b',linewidth=2)
plt.ylabel('Y1')

plt.subplot(212)
plt.plot(tspan,Y[:,1],'-g',linewidth=2)
plt.xlabel('Time(min)')
plt.ylabel('Y2')
