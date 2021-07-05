
from scipy.optimize import fsolve
import numpy as np

F = np.zeros(2)
x = [5,8]

def func(x):
    F[0] = np.exp(-(np.exp(-x[0]+x[1])))- x[1]*(1+x[0]**2)
    F[1] = x[0]*np.cos(x[1]) + x[1]*np.sin(x[0])-(1/2)
    return F

result = fsolve(func, x)
print(result)




