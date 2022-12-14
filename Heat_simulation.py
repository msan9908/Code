#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Simulation of heat distribution in a material based on excercise by Neal Wagner, 
University of Texas, San Antonio, which is a description of a program from the book "A FORTRAN Coloring Book", 
by Roger E. Kaufman, MIT Press,
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation

plate_length = 20
max_iter_time = 100
inner_plate = 6
alpha = 1
delta_x = 1


# Initialize solution: the grid of u(k, i, j)
u = np.empty((max_iter_time, plate_length, plate_length))

# Initial condition everywhere inside the grid
u_initial = 90

# Boundary conditions (fixed temperature)
u_top = 100.0
u_bottom = 32
u_inner = 212

# Set the initial condition
u.fill(u_initial)

# Set the boundary conditions at sides
u[:, :, :1] = u_bottom
u[:, :1, 1:] = u_bottom
u[:, :, (plate_length-1):] = u_bottom
for i in range((inner_plate+2), plate_length,  delta_x):
    u[:, i, :1] = 32 + (100 - 32)/(plate_length - (inner_plate+2) )*(i - (inner_plate+1))
for i in range((inner_plate+2), plate_length,  delta_x):
    u[:, i, (plate_length-1):] = 32 + (100 - 32)/(plate_length - (inner_plate+2) )*(i - (inner_plate+1))
u[:, (inner_plate+1):(2*inner_plate+1), (inner_plate+1):(2*inner_plate+1)] = u_inner
u[:, (plate_length-1):, :] = u_top

sim_grid = range((inner_plate+1),(2*inner_plate+1), delta_x) 
def calculate(u):
    max_dt = 0.6
    k = 0
    while max_dt > 0.5:
            for i in range(1, plate_length-1, delta_x):
                for j in range(1, plate_length-1, delta_x):
                    if i not in sim_grid or j not in sim_grid:
                        u[k + 1, i, j] = 0.25 * (u[k][i+1][j] + u[k][i-1][j] + u[k][i][j+1] + u[k][i][j-1])
            max_dt = np.max(np.abs(np.subtract(u[k + 1, :, :], u[k, :, :])))
            k = k+1
            
    else:
        return u,k

def plotheatmap(u_k, k):
    plt.clf()

    plt.xlabel("x [inch]")
    plt.ylabel("y [inch]")

    plt.pcolormesh(u_k, cmap=plt.cm.jet, vmin=32, vmax=212)
    cbar = plt.colorbar()
    cbar.ax.set_title('Temperature [°F]',fontsize=12)



    return plt



def animate(k):
    plt = plotheatmap(u[k], k)
    
    plt.title(f'Heat distribution at Frame {k}')
u,k = calculate(u)
anim = animation.FuncAnimation(plt.figure(), animate, interval=1, frames=k, repeat=False )
anim.save("heat_equation_solution.gif")

for i in range(20):
        for j in range(20):
            u[:, i, j] = np.random.normal(92, 10)
            u[:, :, :1] = u_bottom
            u[:, :1, 1:] = u_bottom
            u[:, :, (plate_length-1):] = u_bottom
for i in range((inner_plate+2), plate_length,  delta_x):
                u[:, i, :1] = 32 + (100 - 32)/(plate_length - (inner_plate+2) )*(i - (inner_plate+1))
for i in range((inner_plate+2), plate_length,  delta_x):
                    u[:, i, (plate_length-1):] = 32 + (100 - 32)/(plate_length - (inner_plate+2) )*(i - (inner_plate+1))
                    u[:, (inner_plate+1):(2*inner_plate+1), (inner_plate+1):(2*inner_plate+1)] = u_inner
                    u[:, (plate_length-1):, :] = u_top


# Set the initial condition for second simulation

def randomized_u(u):
    
    for i in range(20):
        for j in range(20):
            u[:, i, j] = np.random.normal(92, 10)
            u[:, :, :1] = u_bottom
            u[:, :1, 1:] = u_bottom
            u[:, :, (plate_length-1):] = u_bottom
    for i in range((inner_plate+2), plate_length,  delta_x):
                u[:, i, :1] = 32 + (100 - 32)/(plate_length - (inner_plate+2) )*(i - (inner_plate+1))
    for i in range((inner_plate+2), plate_length,  delta_x):
                    u[:, i, (plate_length-1):] = 32 + (100 - 32)/(plate_length - (inner_plate+2) )*(i - (inner_plate+1))
                    u[:, (inner_plate+1):(2*inner_plate+1), (inner_plate+1):(2*inner_plate+1)] = u_inner
                    u[:, (plate_length-1):, :] = u_top
    return u

k_mean = []

for i in range(30):
    u = np.empty((max_iter_time, plate_length, plate_length))
    u = randomized_u(u)
    u,k = calculate(u)
    k_mean.append(k)
print("Mean of convergence time: ", np.mean(k_mean))
print("Std of convergence time: ", np.std(k_mean))

u = randomized_u(u)
u, k = calculate(u)

anim = animation.FuncAnimation(plt.figure(), animate, interval=1, frames=k, repeat=False )
anim.save("heat_equation_solution2.gif")