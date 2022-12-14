#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Implementation of BFS algorithm for connection search between N1 atom in G37 and selected atoms
from different amino acids on condidtion that R145 was close enough to guanine 
"""



import __main__
__main__.pymol_argv = [ 'pymol', '-qc'] # Quiet and no GUI
import pip
pip.main(['install', 'pandas'])
pip.main(['install', 'openpyxl'])
import sys
import pymol
import os
import json
import pandas as pd
a_directory = './'
pymol.cmd.reinitialize()
dyst=pd.DataFrame()           
def WB_find(filename):

   plik=sys.argv
   ref = os.path.abspath(f'{a_directory}/{filename}.pdb')
   pymol.cmd.load(ref, 'mol')
   if pymol.cmd.get_distance('(resid 9 and polymer.nucleic) and name N2 and mol',f'mol and i. 226 and name OE1')<5 and pymol.cmd.get_distance('(resid 9 and polymer.nucleic) and mol and name N3', 'mol and i. 226 and name NE2')<6 :
       def wb_a_b (a,b):
    
    
           pymol.cmd.select(f"(mol and resname SOL and name OW) within 3.5 of {a}")
           dyst=pd.DataFrame()
           slownik={}
           slownik['pool']=[]
           slownik['poczatek']=[]
           slownik['nowe']=[]
           sprawdzone=set()
           sciezka={}
           atoms = pymol.cmd.get_model('sele')
           pymol.cmd.iterate('sele','pool.append((ID))', space=slownik)
           pymol.cmd.iterate('sele','poczatek.append((ID))', space=slownik)
           koniec=False
           while slownik['pool'] and koniec == False and len(sprawdzone)<500:
               pierwszy=slownik['pool'].pop(0)
               sprawdzone.add(pierwszy)
               #pymol.cmd.select(f 'id {pierwszy} and mol')
               #print(pierwszy)
               #print(type(pierwszy))	
               if  pymol.cmd.get_distance(f' {b}', 'mol and id ' + str(pierwszy))<4:                    
                   ostatni=pierwszy
                   koniec=True
               else:


                   if len(sprawdzone) == 1:
                     last = '(resid 9 and polymer.nucleic) and name O6 and mol'

                   else:
                     last = 'id   ' + str(list(sprawdzone)[-2])
                   pymol.cmd.select('(mol and resname SOL and name OW)  within 3.7 of id  ' + str(pierwszy)  )
                   #pymol.cmd.set_name('sele', 'new' )
                   #pymol.cmd.select(' new  within 6 of  '+ f'{last}' )
                   pymol.cmd.get_model('sele')
                   pymol.cmd.iterate('sele','nowe.append((ID))', space=slownik)
                   for atom in slownik['nowe']:
                           if atom not in sprawdzone and atom not in slownik['pool']:
					#print atom, sprawdzone
                            slownik['pool'].append(atom)
                            sciezka[atom]=pierwszy
            
           if koniec:
                stream=[]
                i=1
                stream.append(ostatni)
                while ostatni not in slownik['poczatek']:
                    i+=1
                    ostatni=sciezka[ostatni]
                    stream.append(ostatni)
                    print(plik, f"{filename}: stream length: ", i, stream)
                wody=len(stream)
                return wody

       G_37=f'(resid 9 and polymer.nucleic) and name H1 and {filename}'

       D201=f'{filename} and i. 314 and name CG'
       D223=f'{filename} and i. 208 and name CG'
       D98=f'{filename} and i. 293 and name CG'
       D99=f'{filename} and i. 354 and name CG'
       E143=f'{filename} and i. 212 and name CD'
       E148=f'{filename} and i. 219 and name CD'
       E139=f'{filename} and i. 229 and name CD'
       E164=f'{filename} and i. 231 and name CD'



       G_D201=wb_a_b(G_37,D201)
       G_D223=wb_a_b(G_37,D223)
       G_D98=wb_a_b(G_37,D98)
       G_D99=wb_a_b(G_37,D99)

       G_E164=wb_a_b(G_37,E164)
       G_E143=wb_a_b(G_37,E143)
       G_E148=wb_a_b(G_37,E148)
       G_E139=wb_a_b(G_37,E139)
       dyst=pd.DataFrame()
       dyst["file"]=[filename]
       dyst["G_D208"]=[G_D223]
       dyst["G_D314"]=[G_D201]

       dyst["G_D293"]=[G_D98]
       dyst["G_D354"]=[G_D99]
       dyst["G_E231"]=[G_E164]
       dyst["G_E212"]=[G_E143]
       dyst["G_E219"]=[G_E148]
       dyst["G_E229"]=[G_E139]
       #mosty='Guanina-E185:   '+f'{G_E}'+'      Guanina-Y290:    '+f'{G_Y}'+'      Guanina-D201:    '+f'{G_D201}'+'      Guanina-D223:    '+f'{G_D223}'

       #print(Y_E)
       
       return dyst
       #print(G_Y)

dst=pd.DataFrame()
dst["file"]=[]
dst["G_D314"]=[]
dst["G_D208"]=[]
dst["G_E212"]=[]
dst["G_D98"]=[]
dst["G_D99"]=[]
dst["G_E231"]=[]
dst["G_E212"]=[]
dst["G_E219"]=[]
dst["G_E229"]=[]
for filename in os.listdir(a_directory):
    
    filename_we=os.path.splitext(filename)[0]
    if  os.path.splitext(filename)[1] == '.pdb':
        pymol.cmd.reinitialize
        moddir='/Users/macbook/Applications/pymol-svn/modules'
        sys.path.insert(0, moddir)
        os.environ['PYMOL_PATH'] = os.path.join(moddir, 'pymol/pymol_path')
        loading=f'{a_directory}/{filename}'
        import pymol
        pymol.pymol_argv = ['pymol','-qc'] + sys.argv[1:]
        pymol.cmd.load(loading)
        w=WB_find(filename_we)
        print(w)
        dst=pd.DataFrame.append(dst,w)
        print(dst)
        pymol.cmd.reinitialize()
        dst.to_excel('wb_nR.xlsx')
print(dyst)
pymol.cmd.quit()
dst.to_excel('wb_nR.xlsx')





