#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Distance analysis and visualization of simulations
"""
import numpy as np
import MDAnalysis as mda
import pandas as pd
from MDAnalysis.analysis.distances import dist
from MDAnalysis.lib.distances import calc_angles


u = mda.Universe('md_nopbc.pdb', "md_nopbc.xtc")

dst_RNA_N_SAM_CH3=[]
dst_RNA_O_R145=[]
dst_RNA_N_E185=[]
dst_RNA_N1_Y290=[]
dst_RNA_N7_R145=[]
dst_RNA_N2_E185=[]
angle=[]
for frame in u.trajectory:
 protein = u.select_atoms("protein")
 RNA = u.select_atoms("nucleic")
 G_id= max(protein.resids)+40
 RNA_g37=RNA.select_atoms(f"resid {G_id}")
 RNA_N1 = RNA_g37.select_atoms("name N1")
 RNA_N7 = RNA_g37.select_atoms("name N7")
 RNA_N2 = RNA_g37.select_atoms("name N2")
 RNA_O = RNA_g37.select_atoms("name O6")
 SAM = u.select_atoms("resname SAM")
 SAM_CH3 = SAM.select_atoms("name CGP")
 calphas = protein.select_atoms("name CA")
 E185 = protein.select_atoms("resnum 184 and name CD")
 E185_CG = protein.select_atoms("resnum 184 and name CG")
 R145_NH = protein.select_atoms("resnum 144 and name NH2")
 R145_NE = protein.select_atoms("resnum 144 and name NE")
 N225 = protein.select_atoms("resnum 264 and name N")

 dst_RNA_N_SAM_CH3.append(float(dist(RNA_N1,SAM_CH3)[2]))
 dst_RNA_O_R145.append(float(dist(RNA_O,R145_NE)[2]))
 dst_RNA_N_E185.append(float(dist(RNA_N1,E185)[2]))
 dst_RNA_N7_R145.append(float(dist(RNA_N7,R145_NH)[2]))
 dst_RNA_N2_E185.append(float(dist(RNA_N2,E185)[2]))
 angle.append(float(np.rad2deg(calc_angles(RNA_N1.positions,E185_CG.positions,E185.positions))))
 
time=[]
df=pd.DataFrame()
min_dst_RNA_O_R145=[]
min_dst_RNA_N7_R145=[]
min_time=[]
min_dst_RNA_N_E185=[]
min_angle=[]


for i in range(len(dst_RNA_N_SAM_CH3)):
    time.append(i)
    if dst_RNA_O_R145[i]<10 and dst_RNA_N7_R145[i]<10 and dst_RNA_N_E185[i]<10:
        print(i)
        print(f"dst_RNA_O_R145:{dst_RNA_O_R145[i]}")
        print(f"dst_RNA_N7_R145:{dst_RNA_N7_R145[i]}" )
        print(f"dst_RNA_N1_E185:{dst_RNA_N_E185[i]}")
        min_dst_RNA_O_R145.append(dst_RNA_O_R145[i])
        min_dst_RNA_N7_R145.append(dst_RNA_N7_R145[i])
        min_time.append(time[i])
        min_dst_RNA_N_E185.append(dst_RNA_N_E185[i])
        min_angle.append(angle[i])

dyst=pd.DataFrame()
dyst["time"]=time
dyst["RNA_N_SAM_CH3"]=dst_RNA_N_SAM_CH3
dyst["RNA_O_R145"]=dst_RNA_O_R145
dyst["RNA_N7_R145"]=dst_RNA_N7_R145
dyst["RNA_N_E185"]=dst_RNA_N_E185
dyst["angle"]=angle


import plotly.graph_objects as go 
import plotly.express as px 


fig=go.Figure()
fig.add_trace(go.Scatter( x=dyst['time'], y=dyst['RNA_N7_R145']))
fig.update_layout(title='dst' ,
                   xaxis_title=' Time [ns]',
                   yaxis_title='Distance ')
fig.show()

fig.write_html("/Users/macbook/dyn1/dst_RNA_N7_R145_whole.html")


fig=go.Figure()
fig.add_trace(go.Scatter( x=dyst.index, y=dyst.RNA_N_SAM_CH3))
fig.update_layout(title='dst' ,
                   xaxis_title=' Time [ns]',
                   yaxis_title='Distance ')
fig.show()

fig.write_html("/Users/macbook/dyn1/dst_RNA_N_SAM_CH3_whole.html")

fig=go.Figure()
fig.add_trace(go.Scatter(x=dyst.index, y=dyst.RNA_O_R145))
fig.update_layout(title='dst' ,
                   xaxis_title=' Time [ns]',
                   yaxis_title='Distance ')
fig.show()

fig.write_html("/Users/macbook/dyn1/RNA_O_R145_whole.html")
fig=go.Figure()
fig.add_trace(go.Scatter( x=dyst.index, y=dyst.RNA_N_E185))
fig.update_layout(title='dst' ,
                   xaxis_title=' Time [ns]',
                   yaxis_title='Distance ')
fig.show()

fig.write_html("/Users/macbook/dyn1/RNA_N_E185_whole.html")
fig=go.Figure()
fig.add_trace(go.Scatter(x=dyst.index, y=dyst.RNA_N_SAM_CH3))
fig.add_trace(go.Scatter(x=dyst.index, y=dyst.RNA_O_R145))
fig.add_trace(go.Scatter(x=dyst.index, y=dyst.RNA_N_E185))
fig.add_trace(go.Scatter(x=dyst.index, y=dyst.RNA_N7_R145))
fig.update_layout(title='dst' ,
                   xaxis_title=' Time [ns]',
                   yaxis_title='Distance ')
fig.show()

fig.write_html("/Users/macbook/dyn1/distance_whole.html")



df2=pd.DataFrame()
min2_dst_RNA_O_R145=[]
min2_dst_RNA_N7_R145=[]
min2_time=[]
min2_dst_RNA_N_E185=[]
min2_angle=[]
df["time"]=min_time
df["RNA_O_R145"]=min_dst_RNA_O_R145
df["RNA_N7_R145"]=min_dst_RNA_N7_R145
df["RNA_N_E185"]=min_dst_RNA_N_E185
df["angle"]=min_angle
df.to_excel("/Users/macbook/dyn1/co10ps.xlsx")
for i in range(len(dst_RNA_N_SAM_CH3)):
    
    if dst_RNA_O_R145[i]<10 and dst_RNA_N7_R145[i]<10 and dst_RNA_N_E185[i]<10  and time[i] % 100==0:
        
        min2_dst_RNA_O_R145.append(float(dst_RNA_O_R145[i]))
        min2_dst_RNA_N7_R145.append(float(dst_RNA_N7_R145[i]))
        min2_time.append(float(time[i]))
        min2_dst_RNA_N_E185.append(float(dst_RNA_N_E185[i]))
        min2_angle.append(float(angle[i]))
df2["time"]=min2_time
df2["RNA_O_R145"]=min2_dst_RNA_O_R145
df2["RNA_N7_R145"]=min2_dst_RNA_N7_R145
df2["RNA_N1_E185"]=min2_dst_RNA_N_E185
df2["angle"]=min2_angle
df2.to_excel("/Users/macbook/dyn1/o10ps.xlsx")

