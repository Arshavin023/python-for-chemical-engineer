# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 20:34:57 2021

@author: Azis
"""

from scipy.optimize import newton
import numpy as np

def myfun(x):
    F=np.exp(-x)-x
    return F

xguess=1
result=newton(myfun,xguess)

print(result)

print(myfun(result))