cd ..
cd ..
source /opt/gromacs-2020/bin/GMXRC
cd Trm10/DYNAMIKA/
for i in   {0..50} ;do
cp *ndx DYNAMIKA_${i}/ 
cp mol-co1ns.sh DYNAMIKA_${i}/
cd DYNAMIKA_${i}/
rm *#*
./mol-co1ns.sh
rm *#*
cd ..;done
for i in  {0..50} ;do


mkdir Water/mol-WATER_${i}
cp DYNAMIKA_${i}/mol-co1ns/*.pdb Water/mol-WATER_${i}/
cp Water/nR.py Water/mol-WATER_${i}/
cd Water/mol-WATER_${i}
find . -type f -empty -print -delete
../PyMol/pymol/pymol WB.py
cd ..
;done
