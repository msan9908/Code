#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Implementations of Classical and modified Gram-Schmidt algorithm
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy import linalg



def classical_gram_schmidt(A):
    '''
    Implements classical Gram-Schmidt process https://arnold.hosted.uark.edu/NLA/Pages/CGSMGS.pdf

    Inputs
        A: numpy.ndarray of shape (M, N)
    
    Outputs
        Q: numpy.ndarray of shape (M, N)
        R: numpy.ndarray of shape (N, N)
    '''
    m, n = A.shape
    Q = np.zeros((m, n))
    R = np.zeros((n, n))

    for j in range(n):
        v = A[:, j]

        for i in range(j - 1):
            q = Q[:, i]
            R[i, j] = q.dot(v)
            v = v - R[i, j] * q

        norm = linalg.norm(v,ord=2)
        Q[:, j] = v / norm
        R[j, j] = norm
    return Q, R

def modified_gram_schmidt(A):
    '''
    Implements modified Gram-Schmidt process: https://web.mst.edu/hilgers/classes/CS328/notes/modgs/node2.html

    Inputs
        A: numpy.ndarray of shape (M, N)
    
    Outputs
        Q: numpy.ndarray of shape (M, N)
        R: numpy.ndarray of shape (N, N)
    '''
    A = np.array(A, dtype=np.float64)
    m, n = A.shape
    R = np.zeros((n, n))
    Q = np.empty((m, n))
    for k in range(n):
        R[k, k] = linalg.norm(A[:, k]) 
        if R[k, k] == 0:
            break
        else:
            Q[:, k] = A[:, k] / R[k, k]
            for j in range(k+1,n):
                R[k, j] = Q[:, k].T @ A[:, j]
                A[:, j] = A[:, j] - R[k, j]*Q[:, k]
    return Q, R
A = np.random.rand(9,4)

Qm,Rm = modified_gram_schmidt(A)