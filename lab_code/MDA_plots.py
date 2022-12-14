#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 11:31:21 2021

@author: macbook
"""

import MDAnalysis as mda

u = mda.Universe('md_nopbc.pdb', "md_nopbc.xtc")
rna = u.select_atoms("nucleic")

protein = u.select_atoms("protein")
RNA = u.select_atoms("nucleic")
SAM = u.select_atoms("resname SAM")
calphas = protein.select_atoms("name CA")


from MDAnalysis.analysis.rms import RMSF
from MDAnalysis.analysis.rms import RMSD
import plotly.graph_objects as go 
import plotly.express as px 

rmsfer_protein = RMSF(calphas, verbose=True).run()
rmsfer_RNA = RMSF(RNA, verbose=True).run()
rmsfer_SAM = RMSF(SAM, verbose=True).run()

rmsd_protein = RMSD(calphas, calphas).run(start=1)
rmsd_protein=rmsd_protein.results.rmsd[0:-2].T
rmsd_RNA = RMSD(RNA, RNA).run(start=1)
rmsd_RNA=rmsd_RNA.results.rmsd[0:-2].T
rmsd_SAM = RMSD(SAM,  SAM).run(start=1)
rmsd_SAM=rmsd_SAM.results.rmsd[0:-2].T

import matplotlib.pyplot as plt
plt.figure(1)
wyk_protein=plt.plot(calphas.resnums, rmsfer_protein.results.rmsf)
plt.xlabel("Residue")
plt.ylabel("RMSF [nm]")
plt.figure(2)
wyk_RNA=plt.plot(RNA.resnums, rmsfer_RNA.results.rmsf)
plt.xlabel("Residue")
plt.ylabel("RMSF [nm]")
plt.figure(3)
wyk_SAM=plt.plot(SAM.ids, rmsfer_SAM.results.rmsf)
plt.xlabel("Atom")
plt.ylabel("RMSF [nm]")
plt.figure(4)
wyk_protein=plt.plot(calphas.resnums, rmsfer_protein.results.rmsf)
wyk_RNA=plt.plot(RNA.resnums, rmsfer_RNA.results.rmsf)
plt.xlabel("Residue")
plt.ylabel("RMSF [nm]")
plt.figure(5)
wyk_rmsd_protein=plt.plot(rmsd_protein[1], rmsd_protein[2])
plt.xlabel("times [ns]")
plt.ylabel("RMSD_protein [nm]")
plt.figure(6)
wyk_rmsd_RNA=plt.plot(rmsd_RNA[1], rmsd_RNA[2])
plt.xlabel("times [ns]")
plt.ylabel("RMSD_RNA [nm]")
plt.figure(7)
wyk_rmsd_SAM=plt.plot(rmsd_SAM[1], rmsd_SAM[2])
plt.xlabel("times [ns]")
plt.ylabel("RMSD_SAM [nm]")

fig=go.Figure()
fig.add_trace(go.Scatter( x=calphas.resnums, y=rmsfer_protein.results.rmsf, name='RMSF_protein'))
fig.add_trace(go.Scatter( x=RNA.resnums, y=rmsfer_RNA.results.rmsf,name='RMSF_RNA'))
fig.add_trace(go.Scatter( x=SAM.ids, y=rmsfer_SAM.results.rmsf,name='RMSF_SAM'))
fig.add_trace(go.Scatter( x=calphas.resnums, y=rmsfer_protein.results.rmsf,name='RMSF_protein_RNA'))
fig.update_layout(title='RMSF' ,
                   xaxis_title='Residue',
                   yaxis_title='RMSF [A]')
fig.show()

fig.write_html("/Users/macbook/dyn6/RMSF.html")

fig=go.Figure()
fig.add_trace(go.Scatter( x=rmsd_protein[1], y=rmsd_protein[2], name='RMSD_protein'))
fig.add_trace(go.Scatter( x=rmsd_RNA[1], y=rmsd_RNA[2],name='RMSD_RNA'))
fig.add_trace(go.Scatter( x=rmsd_SAM[1], y=rmsd_SAM[2],name='RMSD_SAM'))
fig.update_layout(title='RMSD' ,
                   xaxis_title='time',
                   yaxis_title='RMSD [A]')
fig.show()

fig.write_html("/Users/macbook/dyn6/RMSD.html")

























