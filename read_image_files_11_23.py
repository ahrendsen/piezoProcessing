# -*- coding: utf-8 -*-
"""

#get time stamps from the images and relate fringe shift to time
Created on Tue Nov 23 14:19:12 2021

@author: nstam
"""
import xlrd
import os
import datetime
from matplotlib import pyplot as plt

photos = (r"C:\TIm Gay Research\Lab Photos\Camera Data\11_2_photos")
loc = ("C:\TIm Gay Research\camera interferometer data.xlsx")

pos_1 = []
pos_2 = []
pos_3 = []
pos_4 = []

files = os.scandir(photos)
time =[]
for entry in files:
    time.append(entry.stat().st_mtime)
    
print(time)

import numpy as np
t = np.array(time)
t_x = np.array(time)
t = t[61:105]
t_x = t_x[61:105]
t_0 = t[0]
t_0_x = t_x[0]

for i in range(0, len(t)):
    t[i] = t[i] - t_0
    t_x[i] = t_x[i] - t_0_x

t= t[0::2]
t_x = t_x[1::2]
print(t)


length = 23

wb = xlrd.open_workbook(loc)

sheet = wb.sheet_by_index(0)
 
for i in range (1,length):
    pos_1.append(sheet.cell_value(i, 1))

for i in range(1, length):
    pos_2.append(sheet.cell_value(i,2))
    
for i in range(1, length):
    pos_3.append(sheet.cell_value(i,4))
    
 
for i in range(1, length):
    pos_4.append(sheet.cell_value(i,5))

print(len(t))
print(len(t_x))
print(len(pos_1))

plt.scatter(t, pos_1)

fig, axs = plt.subplots(2,2)
fig.suptitle('Vertically stacked subplots')
axs[0,0].scatter(t, pos_1)
axs[0,1].scatter(t, pos_2)
axs[1,0].scatter(t_x, pos_3)
axs[1,1].scatter(t_x, pos_4)

