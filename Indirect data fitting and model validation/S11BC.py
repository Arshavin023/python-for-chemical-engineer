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
DSAM=4
xfil1=np.zeros((DSAM,len(xdat)))
plt.figure(0)
for i in range(0,DSAM):
    xfil1[i,:]=sgf(xdat,int(5+i*10),2)
    plt.subplot(2,2,i+1)
    plt.plot(tdat,xfil1[i,:])
    plt.scatter(tdat,xdat,s=50,facecolors='none',edgecolors='r')
    plt.grid()
    plt.xlabel('Time; s')
    plt.ylabel('Conversion')
    plt.legend(['Filtered experimental data','Raw experimental data'],prop={'size': 8})
    plt.tight_layout()

Ntsim=101
tsim=np.linspace(tdat[0],tdat[-1],Ntsim)
k1k2store=np.zeros((2,DSAM))
xstore=np.zeros((Ntsim,DSAM))
plt.figure(1)
for i in range(0,DSAM):
    K1K2=lsq(KFIND,[1,1],args=(tsim,tdat,xfil1[i,:]))
    xres=odeint(OODE,0,tsim,args=(K1K2.x[0],K1K2.x[1]))
    k1k2store[:,i]=10**(-K1K2.x)
    xstore[:,i]=xres.flatten()
    plt.subplot(2,2,i+1)
    plt.plot(tsim,xres)
    plt.scatter(tdat,xfil1[i,:],s=50,facecolors='none',edgecolors='r')
    plt.grid()
    plt.xlabel('Time; s')
    plt.ylabel('Conversion')
    plt.legend(['Simulated data','Filtered experimental data'],prop={'size': 8})
    plt.tight_layout()
exp=np.zeros((len(tdat),DSAM*2))
for i in range(0,DSAM):
    exp[:,i*2]=xfil1[i,:]
    xexp=np.interp(tdat,tsim,xstore[:,i])
    exp[:,i*2+1]=xexp
exp=pd.DataFrame(np.concatenate((DATA,exp),axis=1))
k1k2=pd.DataFrame(k1k2store)
RESULT=pd.ExcelWriter('S11BCR.xlsx',engine='xlsxwriter')
exp.to_excel(RESULT,sheet_name='t vs x')
k1k2.to_excel(RESULT,sheet_name='k1 and k2')
RESULT.save()