# Root finding
# These knowledge could be applied for EOS
# They could also be applied for mass balance and component balance for different components
# We will use scipy.optimize 

from scipy.optimize import newton
import numpy as np

def myfun(x):
    F = np.exp(-x) - x
    return F

xguess = 1.201
result = newton(myfun, xguess)
print(result)
print(myfun(result))

