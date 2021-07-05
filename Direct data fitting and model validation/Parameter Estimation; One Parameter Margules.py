#Fitting is used to fit experimental data into a proposed a model
# The goal is to minimize the error(Yexp-Ysim)
# Objective is to minimize SSE = Sum square of error
# If you have x and y data then its called direct fitting
# If we have only x and a differential Y then its indirect fitting
# Model Equation 𝐺𝐸𝑅𝑇=𝐴∙𝑥1∙𝑥2

import numpy as np
import pandas as pd
from scipy.optimize import minimize
import matplotlib.pyplot as plt

#Loading data
df1 = pd.read_excel('data.xlsx')

#Convert to Numpy
data = df1.to_numpy()

#Extracting data into variables
x1 = data[:,0]
y1 = data[:,1]
T = data[:,2]
p1s = data[:,3]
p2s = data[:,4]
P = 1

#Create arrays for storing data
#Calculate GE/RT from Exp data
x2 = np.zeros(len(x1))
y2 = np.zeros(len(x1))
Gamma1 = np.zeros(len(x1))
Gamma2 = np.zeros(len(x1))
GERTdat = np.zeros(len(x1))

for i in range(0,len(x1)):
    x2[i] = 1-x1[i]
    y2[i] = 1-y1[i]
    Gamma1[i] = y1[i]*P/(x1[i]*p1s[i])
    Gamma2[i] = y2[i]*P/(x2[i]*p2s[i])
    GERTdat[i] = x1[i]*np.log(Gamma1[i])+x2[i]*np.log(Gamma2[i])
    
def F2M(PAR,x1,x2,GERTdat):
    GERTcalc=np.zeros(len(x1))
    for i in range(0,len(x1)):
        GERTcalc[i] = PAR*x1[i]*x2[i]
    res=GERTcalc-GERTdat #This is error
    SSEcalc = sum(res**2)
    return SSEcalc

P2M = minimize(F2M,1,args=(x1,x2,GERTdat))
print(P2M)

#recalculation using optimized parameters
A = P2M.x

GERTcalc = np.zeros(len(x1))
for i in range(0,len(x1)):
    GERTcalc[i]= A*x1[i]*x2[i]
    
print(GERTcalc)
print(GERTdat)
    
plt.scatter(x1,GERTdat,s=50,linewidth=2,facecolors='none',edgecolors ='r')
plt.plot(x1,GERTcalc,'--k')
plt.grid()
plt.ylabel(' RTcalc and GE/ RTdat ')
plt.xlabel('x1')
plt.legend(['One parameter Margules ','Experiment'],loc='best', fontsize=10)

    
    

 
