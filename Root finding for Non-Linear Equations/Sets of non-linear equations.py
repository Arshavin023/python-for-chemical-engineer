from scipy.optimize import fsolve
import numpy as np

def func(x):
    xspan = np.zeros(2)
    x1 = xspan[0]
    x2 = xspan[1]
    F = np.zeros(2)
    F[0] = np.exp(-(np.exp(-(x[0]+x2))))-x2*(1+x1**2)
    F[1] = x1*np.cos(x2)+x2*np.sin(x1)-(1/2) 
    return F

xguess = 2
result = fsolve(func, ([1.2,1.09]))

print(result)
print(func(result))
