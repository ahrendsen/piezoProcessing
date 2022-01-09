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
                         "Project - Chiral Piezo", "data",
                         "longDrift_2021-11-24")
# The location of the folder that you want to process.
analysisDir = os.path.join(homeDir, "OneDrive - University of Nebraska-Lincoln",
                         "BoxMigrationUNL", "Gay Group",
                         "Project - Chiral Piezo", "analysis", 
                         "longDrift_2021-11-24", "analysis")


# Grab an iterator that contains the files in the folder.
files = os.scandir(photosDir)
# Convert the iterator into a list
files = list(files)
    

# The voltages at which the data was collected. It is
# assumed that the images will be collected in this order
# in a repeating fashion. For example, if data was collected
# at voltages = [0, 10], the first file in the directory 
# should be at 0 volts, the second at 10, the third at 0,
# and so on to the end of the directory.
voltages = [0]
# The approximate spacing of the fringes, used to set a
# bounds of where the program will search for a minimum.
spacing = 400


allResults = []
# %%
for i in range(len(voltages)):
    results = []
    
    # Make individual folders for the graph image files in the analysis folder.
    analysisDirV = os.path.join(analysisDir, str(voltages[i]))
    if os.path.isdir(analysisDirV) is False:
        os.makedirs(analysisDirV)
          
    # This for loop takes every nth file from the
    # files list, where n is the number of voltages.
    for file in files[i::len(voltages)]:
        res = process_file(os.path.basename(file), spacing, photosDir,
                           analysisDirV, graph_output=True)
        results.append(res)
        
    # This converts it into a dataframe for easy joining later.
    df = pd.DataFrame(results, columns=['Filename', 
                                        'First Minimum Position V= ' + 
                                         str(voltages[i]),
                                         'Second Minimum Position V= ' +
                                         str(voltages[i])])
    # This adds in a new column where each value is the same
    # for each row of the column, and they are all equal to
    # voltages[i]
    df.insert(1, 'Voltage = ' + str(voltages[i]) + ' (V)', voltages[i])
    allResults.append(df)

# Joins the voltage blocks together.
dfAll = pd.concat(allResults, axis='columns')

# Exports the dataframe as an excel file.
dfAll.to_excel(os.path.join(analysisDir, "analysisSummary.xlsx"), index=False)
