import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter as sgf
from scipy.integrate import odeint
from scipy.optimize import least_squares as lsq

DATA=pd.read_excel('S11B.xlsx')
DATA=DATA.to_numpy()
tdat=DATA[:,0]
xdat=DATA[:,1]

# plt.figure(0)
# plt.scatter(tdat,xdat,s=50,facecolors='none',edgecolors='r')
# plt.grid()
# plt.xlabel('Time; s')
# plt.ylabel('Conversion')
# plt.tight_layout()

def OODE(x,t,k1,k2):
    k1=10**(-k1)
    k2=10**(-k2)
    dxdt=k1*(1-x)/(k2+x)
    return dxdt

def KFIND(PAR,tsim,tdat,xdat):
    k1trial=PAR[0]
    k2trial=PAR[1]
    xsim=odeint(OODE,0,tsim,args=(k1trial,k2trial))
    xcalc=np.interp(tdat,tsim,xsim.flatten())
    error=xcalc-xdat
    return error

xfil=sgf(xdat,45,2)
plt.figure(1)
plt.plot(tdat,xfil)
plt.scatter(tdat,xdat,s=50,facecolors='none',edgecolors='r')
plt.grid()
plt.xlabel('Time; s')
plt.ylabel('Conversion')
plt.legend(['Filtered experimental data','Raw experimental data'],prop={'size': 8})
plt.tight_layout()

Ntsim=101
tsim=np.linspace(tdat[0],tdat[-1],Ntsim)

K1K2=lsq(KFIND,[1,1],args=(tsim,tdat,xfil))
K1K2=K1K2.x
xres=odeint(OODE,0,tsim,args=(K1K2[0],K1K2[1]))
plt.figure(2)
plt.plot(tsim,xres)
plt.scatter(tdat,xfil,s=50,facecolors='none',edgecolors='r')
plt.grid()
plt.xlabel('Time; s')
plt.ylabel('Conversion')
plt.legend(['Simulated data','Filtered experimental data'],prop={'size': 8})
plt.tight_layout()

exp=np.zeros((len(tdat),4))
exp[:,0]=tdat
exp[:,1]=xdat
exp[:,2]=xfil
exp[:,3]=np.interp(tdat,tsim,xres.flatten())
exp=pd.DataFrame(exp)
K1K2=pd.DataFrame(10**(-K1K2))
RESULT=pd.ExcelWriter('S11BR.xlsx',engine='xlsxwriter')
exp.to_excel(RESULT,sheet_name='t vs x')
K1K2.to_excel(RESULT,sheet_name='k1 and k2')
RESULT.save()