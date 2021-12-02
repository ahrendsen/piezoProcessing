# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 10:33:14 2021

@author: karla
"""

import os
import datetime
from piezoProcess import processFile

homeDir = os.path.expanduser("~")
photosDir = os.path.join(homeDir, "Desktop", "gitSpace", "piezoprocessing",
                         "data")

files = os.scandir(photosDir)
os.chdir(photosDir)

spacing = 400
results = []
for file in files:
    res = processFile(file, spacing, photosDir, "outDir")
    results.append(res)

