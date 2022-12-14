mkdir mol-Table
mkdir mol-Table/zR
mkdir mol-Table/nR
mkdir mol-Table/Razem
for i in {0..50};do
rm short-WATER_${i}/*#*

cp mol-short-WATER_${i}/wb_zR.xlsx mol-Table/zR/short-zR_${i}.xlsx
cp mol-short-WATER_${i}/wb_nR.xlsx mol-Table/nR/short-nR_${i}.xlsx
cp mol-short-WATER_${i}/wb_zR.xlsx mol-Table/Razem/short-zR_${i}.xlsx
cp mol-short-WATER_${i}/wb_nR.xlsx mol-Table/Razem/short-nR_${i}.xlsx;done
cp combine.py mol-Table/zR/combine.py
cp combine.py mol-Table/nR/combine.py
cp combine.py mol-Table/Razem/combine.py
cd mol-Table/zR
rm combine.xlsx
find . -type f -empty -print -delete
python3 combine.py
cd ..
cd nR
rm combine.xlsx
find . -type f -empty -print -delete
python3 combine.py
cd ..
cd Razem
rm combine.xlsx
find . -type f -empty -print -delete
python3 combine.py
cd ..
cd ..
mkdir all-Table
mkdir all-Table/zR
mkdir all-Table/nR
mkdir all-Table/Razem
for i in 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19  20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53;do
rm short-WATER_${i}/*#*

cp short-WATER_${i}/wb_zR.xlsx all-Table/zR/short-zR_${i}.xlsx
cp short-WATER_${i}/wb_nR.xlsx all-Table/nR/short-nR_${i}.xlsx
cp short-WATER_${i}/wb_zR.xlsx all-Table/Razem/short-zR_${i}.xlsx
cp short-WATER_${i}/wb_nR.xlsx all-Table/Razem/short-nR_${i}.xlsx
cp mol-short-WATER_${i}/wb_zR.xlsx all-Table/zR/short-zR_${i}.xlsx
cp mol-short-WATER_${i}/wb_nR.xlsx all-Table/nR/short-nR_${i}.xlsx
cp mol-short-WATER_${i}/wb_zR.xlsx all-Table/Razem/short-zR_${i}.xlsx
cp mol-short-WATER_${i}/wb_nR.xlsx all-Table/Razem/short-nR_${i}.xlsx;done
cp combine.py all-Table/zR/combine.py
cp combine.py all-Table/nR/combine.py
cp combine.py all-Table/Razem/combine.py
cd all-Table/zR
rm combine.xlsx
find . -type f -empty -print -delete
python3 combine.py
cd ..
cd nR
rm combine.xlsx
find . -type f -empty -print -delete
python3 combine.py
cd ..
cd Razem
rm combine.xlsx
find . -type f -empty -print -delete
python3 combine.py
cd ..
