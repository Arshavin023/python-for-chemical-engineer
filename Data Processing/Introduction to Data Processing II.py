import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter as sgl

DATA = pd.read_excel('S11B.xlsx')
DATA = DATA.to_numpy()
tdata = DATA[:,0]
xdata = DATA[:,1]
plt.plot(tdata, xdata)
xdatafiltered = sgl(xdata,21,2)
plt.plot(tdata,xdatafiltered,tdata,xdata, 'o')

