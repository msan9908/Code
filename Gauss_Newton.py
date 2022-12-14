#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Implementation of the Gauss-Newton Method to fit the model function  F(t,x1,x2)=x1⋅x2^t 
to the data on bacterial population
which grows according to the geometric progression.
"""

import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import norm

def F(t,x_1, x_2):
    f = x_1*x_2**t
    return f

def Jacobian_F(t, x_1, x_2):
    Jacobian = []
    for i in t:
        Jacobian.append([x_2**i, i*x_1*x_2**(i-1)])
    nJacobian = np.array(Jacobian)
    return nJacobian

def residuals_F(y, F,  x_1, x_2):
    residuals = []
    for i in range(len(y)):
        residuals.append([y[i] - F(i ,x_1, x_2)])
    nresiduals = np.array(residuals)
    return nresiduals

def Gauss_Newton(y, F, Jacobian_F, residuals_F, x_1, x_2,  maxits = 1000):
    x = np.array([x_1,x_2]) 
    dx = np.array([1,1])
    t = []
    for j in range(len(y)):
        t.append(j)
    
    i = 0
    residuals = []
    while i < maxits:
        dx = np.array([1,1])

        dx  = np.dot(np.linalg.pinv(-Jacobian_F(t, x[0], x[1])), - residuals_F(y, F,  x[0], x[1]))
        x[0] = x[0] + dx[0] 
        x[1] = x[1] + dx[1] 
        i += 1
    
    Results =  []
    for i in range(len(y)):
        residuals.append([y[i] - F(i ,x[0], x[1])])
        Results.append(F(i ,x[0], x[1]))
    return x, Results, i, residuals


data = [0.19, 0.36, 0.69, 1.3, 2.5, 4.7, 8.5, 14]

P_t = data[1:]
P_t_1 = data[:-1]

    
t = []
for i in range(len(data)):
        t.append(i)


r = data[1]/data[0]
Fitted,Results, i, residuals = Gauss_Newton(data, F, Jacobian_F, residuals_F, data[0], r)




plt.figure(figsize=(10, 6))


plt.title(label="Fitted vs. Observed")
plt.plot(t,Results, label = "Fitted")
plt.plot(t,data, label = "Observed")
plt.xlabel('Time')
plt.ylabel('Data')
plt.legend()


plt.figure(figsize=(10, 6))


plt.title(label="Residuals")
plt.plot(t,np.abs(residuals))
plt.xlabel('Time')
plt.ylabel('Absolute of Residuals')