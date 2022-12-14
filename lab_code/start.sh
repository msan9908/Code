python3 -m pip install plotly
python3 -m pip install MDAnalysis
python3 -m pip  install numpy
python3 -m pip  install pandas
cd ..
cd ..
source /opt/gromacs-2020/bin/GMXRC
cd Trm5/DYNAMIKA/
for i in {1..50} ;do
cp md_analysis.py DYNAMIKA_${i}/ 
cp *ndx DYNAMIKA_${i}/ 
cp MDA_plots.py DYNAMIKA_${i}/ 
cp Neighbours.py DYNAMIKA_${i}/ 
cp *.sh DYNAMIKA_${i}/
cd DYNAMIKA_${i}/
rm *#*

echo  28 0 0   |  gmx trjconv -f md.xtc -s md.tpr -o md_nopbc.xtc -pbc cluster -center -n
echo  28 0 0   |  gmx trjconv -f md.xtc -s md.tpr -o md_nopbc.pdb -pbc cluster -center -n -e 0 
python3 MDA_plots.py
python3 mdanalysis.py
python3 Neighbours.py
./pdb.sh
cd .. ;done
