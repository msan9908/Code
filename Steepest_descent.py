#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Implementation of  steepest descent with test for the Rosenbrock function
"""
import numpy as np
import scipy.optimize
import matplotlib.pyplot as plt
import scipy.linalg as la

from scipy.optimize import line_search
from numpy.linalg import norm

global gcount1
gcount1 = 0


def stepest_descent(f,grad,x0,y0,k,max_error=10e-5):
    """Implementation with stoping criteria for the Rosenbrock function where the x* is equal to x=1,y=1"""
    global gcount1
    x = [x0,y0] 
    iters=0
    while norm([x[0]-1,x[1]-1],ord=2) > max_error and iters < k:
        grad_x = grad(x)
        alpha = line_search(f, grad, np.array(x), np.array([- grad_x[0],- grad_x[1]]))
        x[0] = x[0] - grad_x[0]*alpha[0]
        x[1] = x[1] - grad_x[1]*alpha[0]
        gcount1 += 1
        iters += 1
    return x
def Rosenbrock(x):
    R = 100*(x[1] - x[0]**2)**2 + (1-x[0])**2
    return R
def Rosenbrock_grad(x):
    grad_x = 2*(200*x[0]**3 -200*x[0]*x[1] + x[0] -1)
    grad_y = 200*(x[1]-x[0]**2)
    
    return [grad_x, grad_y]


stepest_descent(Rosenbrock, Rosenbrock_grad,0,0,300)

max_k = [10,30, 50,100,150,200,250,300]
result1 = []
error = []
gc_arr1 = []
plt.figure(figsize=(10, 6))
for k in max_k:
    gcount1 = 0
    x,y = stepest_descent(Rosenbrock, Rosenbrock_grad,0,0,k)
    error = norm(Rosenbrock([x,y]))
    result1.append([x,y,k,error])
    gc_arr1.append(gcount1)
    plt.scatter(result1[len(result1)-1][0], result1[len(result1)-1][1],label= f"{k}")
plt.ylim([0,1])
plt.xlim([0,1])
plt.title(label="Convergence plot")
plt.xlabel ('x')
plt.ylabel ('y')
plt.legend(title="Number of iterations")
result1 = np.array(result1)

plt.figure(figsize=(10, 6))


plt.title(label="Norm of error")
plt.plot(result1[:,2],result1[:,3])
plt.xlabel('Step Number')
plt.ylabel('Norm of the error')

