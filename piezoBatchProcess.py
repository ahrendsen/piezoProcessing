# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 10:33:14 2021

@author: karla
"""

import os
import datetime
from piezoProcess import processFile
import pandas as pd

homeDir = os.path.expanduser("~")
photosDir = os.path.join(homeDir, "Desktop", "gitSpace", "piezoprocessing",
                         "data")

files = os.scandir(photosDir)
os.chdir(photosDir)

voltages = [0,10.05]
spacing = 400
resultsv1 = []
files = list(files)

for file in files[::len(voltages)]:
    res = processFile(file, spacing, photosDir, photosDir)
    resultsv1.append(res)

df1 = pd.DataFrame(resultsv1, columns=['First Minimum Position V1',
                                       'Second Minimum Position V1'])
df1.insert(0, 'Voltage 1(V)', voltages[0])

resultsv2 = []
for file in files[1::len(voltages)]:
    res = processFile(file, spacing, photosDir, "outDir")
    resultsv2.append(res)

df2 = pd.DataFrame(resultsv2, columns=['First Minimum Position V2',
                                       'Second Minimum Postion V2'])
df2.insert(0, 'Voltage 2(V)', voltages[1])

dfAll = df1.join(df2)

dfAll.to_excel(os.path.join(photosDir,"excelTest.xlsx"))