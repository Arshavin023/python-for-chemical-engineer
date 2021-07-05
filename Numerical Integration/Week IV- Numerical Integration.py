# Numerical Integration
# ∫(1−𝑥−4𝑥^3+〖2𝑥〗^5 )𝑑𝑥
# UL = 4
# LL = -2

from scipy.integrate import quad
from scipy.integrate import simps
import numpy as np

def Myfun(x):
    F = 1-x-4*x**3+2*x**5
    return F
Res = quad(Myfun,-2,4)
Y = Res[0] 
print(Y)

#Numerical integration of a dataset
x = np.array([-2,-1,0,1,2,3,4])
y = np.array([-29,4,1,-2,31,376,1789])

I = simps(y,x)
print(I)
