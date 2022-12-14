#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 12 13:55:19 2022

@author: macbook
"""

import numpy as np
import MDAnalysis as mda
import pandas as pd
from MDAnalysis.analysis.bat import BAT
from MDAnalysis.analysis.distances import dist
from MDAnalysis.analysis.distances import between
from MDAnalysis.lib.distances import calc_angles


u = mda.Universe('md_nopbc.pdb', "md_nopbc.xtc")

RNA = u.select_atoms("nucleic")
RNA_g37=RNA.select_atoms("resid 9 and name O6")
Neigh=[]
ID=[]
for frame in u.trajectory:
 Neig=mda.lib.NeighborSearch.AtomNeighborSearch(u.select_atoms("protein or resname SAM"), box=None).search(RNA_g37, radius=4, level='R')
 Neigh.append(Neig.resnames)
 ID.append(Neig.resids)
time=[]
df=pd.DataFrame()
Numb=[]
for i in range(len(Neigh)):
    time.append(i)
    Numb.append(len(Neigh[i]))
Amin=np.zeros([len(time),max(Numb)]).astype(str)
for i in range(len(Neigh)):
    N=Neigh[i]
    I=ID[i]
    for j in range(len(Neigh[i])):
        Amin[i,j]=str(I[j])+N[j]
Amin[Amin == '0.0']=np.nan
AA=np.unique(Amin)
df=pd.DataFrame(Amin)
df["time"]=time

Amino_Acids=np.zeros([len(time),len(AA)])
df2=pd.DataFrame(Amino_Acids)
df2.columns=AA
for a in AA:
    for i in range(len(Neigh)):
        if a in df[i:i+1].values:
            df2.at[i,a]=1
freq=df2.mean()
freq=pd.DataFrame(freq)
freq.columns=['Frequency']
df.to_excel('Neighbours.xlsx')
df2.to_excel('Neighbours_01.xlsx')
freq.to_excel('Summary.xlsx')












