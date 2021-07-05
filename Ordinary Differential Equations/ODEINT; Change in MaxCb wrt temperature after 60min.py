#Solving Ordinary differential equations with odeint where tspan
# 𝐴 → 𝐵 → 𝐶
# The goal is to evaluate the optimum temperature needed to obtain maximum conversion of B
# 𝑘1=𝐴1∙exp(−𝐸1/𝑅𝑇)
# 𝑘2=𝐴2∙exp(−𝐸2/𝑅𝑇)  
#dCa/dt= −𝑘1Ca
#dCb/dt= 𝑘1∙𝐶a−𝑘2Cb
#dCb/dt= 𝑘2∙𝐶b


import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

#Data
Cao = 2
Cbo = 0
Cco = 0
IC = np.array([Cao,Cbo,Cco]) #Initial concentration of Ab,B & C
A1 = 0.145
A2 = 0.05
E1 = 1167.8
E2 = 1580.8
R = 1.987
Tdata = np.linspace(300,450,31)
tspan = np.linspace(0,60,61)
dCdt = np.zeros(3)
Cbmaxstore = np.zeros(len(Tdata))

#Function
def myfun(C,t,T,A1,A2,E1,E2,R):
    Ca,Cb,Cc = C
    k1 = A1*np.exp(-E1/(R*T))
    k2 = A2*np.exp(-E2/(R*T))
    dCAdt = -k1*Ca
    dCBdt= k1*Ca-k2*Cb
    dCCdt= k2*Cb
    
    dCdt = np.array([dCAdt,dCBdt,dCCdt])
    return dCdt

#Solver
for i in range(0,len(Tdata)):
    T = Tdata[i]
    Sol = odeint(myfun,IC,tspan,args=(T,A1,A2,E1,E2,R))
    Cbmax = np.max(Sol[:,1])
    Cbmaxstore[i] = Cbmax

header = ['Temp(*C)', 'Max of Cb after 60min']
A = np.zeros([31,2])
A[:,0] = Tdata
A[:,1] = Cbmaxstore

#Formatted Printing
print(' '*30)
print('Maximum concentration of Cb after 60min for each Temperature')
print('_'*24)
print('{:^10s} {:^16s}'.format(*header))
print('_'*24)
for row in A:
    print('{:^10} {:^16.4F}'.format(*row))
    
#Plotting
plt.plot(Tdata,Cbmaxstore,'o-g',linewidth=2,markersize=5)
plt.title('ODEINT; Plot of MaxCb vs Temp after 60 min')
plt.xlabel('Temp')
plt.ylabel('MaxCb after 60 min')
plt.grid()

    
    



