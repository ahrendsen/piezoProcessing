# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 10:33:14 2021

@author: karla
"""

# Used for getting lists of filenames and easy
# path name construction.
import os
# Import the function from the piezoProcess.py file.
from image_analyzer_final import process_file
# Import pandas for easy joining of datasets and writing to
# the excel file.
import pandas as pd

# This is a shorthand to get the "Home" directory for the currently
# logged in user.
homeDir = os.path.expanduser("~")
# The location of the foler that you want to process.
photosDir = os.path.join(homeDir, "OneDrive - University of Nebraska-Lincoln",
                         "BoxMigrationUNL", "Gay Group",
                         "Project - Chiral Piezo", "data", "longDrift")
# The location of the foler that you want to process.
analysisDir = os.path.join(homeDir, "Desktop", "gitSpace", "piezoprocessing",
                         "analysis")

# Grab an iterator that contains the files in the folder.
files = os.scandir(photosDir)
# Convert the iterator into a list
files = list(files)

# The voltages at which the data was collected. It is
# assumed that the images will be collected in this order.
# So the first files will be collected at 0 volts, then
# the second at 10.05, then the third at 0 volts again.
voltages = [0]
# The approximate spacing of the fringes, used to set a
# bounds of where the program will search for a minimum.
spacing = 400


# %%
# This cell should be converted into a for each loop
# over the voltages list... but I'm lazy.
resultsv1 = []
# This for loop takes every nth file from the
# files list, where n is the number of voltages.
for file in files[::len(voltages)]:
    res = process_file(file, spacing, photosDir, analysisDir)
    resultsv1.append(res)
# This converts it into a dataframe for easy joining later.
df1 = pd.DataFrame(resultsv1, columns=['First Minimum Position V1',
                                       'Second Minimum Position V1'])
# This adds in a new column where each value is the same
# for each row of the column, and they are all equal to
# voltages[0]
df1.insert(0, 'Voltage 1(V)', voltages[0])


resultsv2 = []
for file in files[1::len(voltages)]:
    res = process_file(file, spacing, photosDir, photosDir)
    resultsv2.append(res)
df2 = pd.DataFrame(resultsv2, columns=['First Minimum Position V2',
                                       'Second Minimum Postion V2'])
df2.insert(0, 'Voltage 2(V)', voltages[1])

# %%

# Joins the two voltage blocks together.
dfAll = df1.join(df2)

# Exports the dataframe as an excel file.
dfAll.to_excel(os.path.join(analysisDir, "longDrift.xlsx"))
