import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from scipy.optimize import least_squares as lsq

Texp=100

DATA=pd.read_excel('S11A.xlsx')
Tsort=DATA.loc[(DATA['T']>=Texp)]
print(Tsort)
istart=Tsort.first_valid_index()
ifinal=Tsort.last_valid_index()
DATA=DATA[istart:ifinal]
DATA=DATA.to_numpy()
tdat=DATA[:,0]
Tdat=DATA[:,1]
CAdat=DATA[:,2]
CBdat=DATA[:,3]

# plt.figure(0)
# plt.plot(tdat,Tdat)
# plt.xlabel('Time; s')
# plt.ylabel('Temperature; $^{o}$C')
# plt.ylim((15,105))
# plt.xlim((-250,5250))
# plt.grid()
# plt.tight_layout()

# plt.figure(1)
# plt.plot(tdat,CAdat)
# plt.xlabel('Time; s')
# plt.ylabel('Concentration of A; mol L$^{-1}$')
# plt.xlim((-250,5250))
# plt.grid()
# plt.tight_layout()

# plt.figure(2)
# plt.plot(tdat,CBdat)
# plt.xlabel('Time; s')
# plt.ylabel('Concentration of B; mol L$^{-1}$')
# plt.xlim((-250,5250))
# plt.grid()
# plt.tight_layout()

def OODE(C,t,k1,k2):
    k1=10**(-k1)
    k2=10**(-k2)
    CA=C[0]
    CB=C[1]
    dCAdt=-k1*CA/(k2+CB)
    dCBdt=k1*CA/(k2+CB)
    return [dCAdt,dCBdt]

def KFIND(PAR,tsim,tdat,CAdat,CBdat):
    k1trial=PAR[0]
    k2trial=PAR[1]
    Csim=odeint(OODE,[CAdat[0],CBdat[0]],tsim,args=(k1trial,k2trial))
    CAcalc=np.interp(tdat,tsim,Csim[:,0])
    CBcalc=np.interp(tdat,tsim,Csim[:,1])
    error=np.concatenate((CAdat-CAcalc,CBdat-CBcalc))
    return error

Ntsim=501
tsim=np.linspace(tdat[0],tdat[-1],Ntsim)
K1K2=lsq(KFIND,[1,1],args=(tsim,tdat,CAdat,CBdat))
Csim=odeint(OODE,[CAdat[0],CBdat[0]],tsim,args=(K1K2.x[0],K1K2.x[1]))
plt.scatter(tdat,CAdat,s=50,facecolors='none',edgecolors='r')
plt.scatter(tdat,CBdat,s=50,facecolors='none',edgecolors='b')
plt.plot(tsim,Csim[:,0],tsim,Csim[:,1],linewidth=3)
plt.xlabel('Time; s')
plt.ylabel('Concentration; mol L$^{-1}$')
plt.legend(['C$_{A}$ simulation','C$_{B}$ simulation',\
            'C$_{A}$ data','C$_{B}$ data'])
plt.grid()