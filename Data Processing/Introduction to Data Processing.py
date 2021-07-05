# Introduction to Data Processing; import/export data, filtering & sort 

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

Texp = 100

DATA = pd.read_excel('S11A.xlsx')

Tsort = DATA.loc[(DATA['T']>=100)]
istart=Tsort.first_valid_index()
ifinal=Tsort.last_valid_index()
DATA=DATA[istart:ifinal]
DATA=DATA.to_numpy()
tdat=DATA[:,0] *3
Tdat=DATA[:,1]
CAdat=DATA[:,2]
CBdat=DATA[:,3]

exp=np.zeros((len(tdat),4))
exp[:,0]=tdat
exp[:,1]=Tdat
exp[:,2]=CAdat
exp[:,3]=CBdat
RESULT=pd.ExcelWriter('S11BR.xlsx',engine='xlsxwriter')
