import pip
pip.main(['install', 'pandas'])
pip.main(['install', 'openpyxl'])
import pandas as pd
import sys
import os
import re
a_directory = './'
#dynamika = []

""" Combines the results of the BFS search from different simulations into one xlsx file """
df  = pd.DataFrame()
def klatkowanie(x):
	x=str(x)
	
	klatka = re.findall(r'\d+',x)[0]
	#print(klatka)
	return klatka


for filename in os.listdir(a_directory):    
   if  os.path.splitext(filename)[1] == '.xlsx':
    filename_we=os.path.splitext(filename)[0]
    dynamika = re.findall(r'\d+',filename_we)
    #if len(filename_we) == 10:
	#	    dynamika = filename_we[-1]
    #else:
	#	    dynamika = filename_we[-2:-1]
    plik = pd.read_excel(filename,engine='openpyxl')
    print(list(plik.columns.values))
    print(dynamika)
    plik['file'].apply(klatkowanie)
    plik.insert(0,'Dynamika',dynamika[0])
    df = pd.DataFrame.append(df,plik)
df.to_excel('combine.xlsx')
    
	

