# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 20:58:19 2021

@author: Azis
"""
from scipy.optimize import fsolve
import numpy as np

F=np.zeros(2)



def func(x):
    F[0]=x[0] * np.cos(x[1]) - 4
    F[1]=x[1] * x[0] - x[1] - 5
    return F


root = fsolve(func, [1, 1])
print(root)