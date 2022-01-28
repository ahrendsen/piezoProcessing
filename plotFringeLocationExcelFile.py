# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 12:52:33 2022

This file plots the summary data that

piezoBatchProcess.py

outputs.

Specifically, it compares two different outputs of piezoBatchProcess.py
that were obtained using a moving average for one dataset and no moving average
for the second dataset.
@author: karla
"""

import os
import pandas as pd

homeDir = os.path.expanduser("~")

# Load in one dataset and make the index a variable so we have 
# a monotonic variable to plot on
analysisDir = os.path.join(homeDir, "OneDrive - University of Nebraska-Lincoln",
                         "BoxMigrationUNL", "Gay Group",
                         "Project - Chiral Piezo", "analysis", 
                         "longDrift_2021-11-24", "analysis")
df = pd.read_excel(os.path.join(analysisDir, 'longDrift.xlsx'))
df.reset_index(inplace=True)

# Import the second dataset.
analysisDir = os.path.join(homeDir, "OneDrive - University of Nebraska-Lincoln",
                         "BoxMigrationUNL", "Gay Group",
                         "Project - Chiral Piezo", "analysis", 
                         "longDrift_2021-11-24", "analysis_100PointSmooth")
df2 = pd.read_excel(os.path.join(analysisDir, 'longDrift.xlsx'))

# Join the datasets together on columns, so that we can compare then.
df3 = pd.concat([df,df2], axis='columns')

# Name the columns, because we have duplicate names that make plotting
# difficult. Also I want the auto generated plot labels to be descriptive.
df3.columns = ['index', 'fn_1', 'v_1', 'Raw Min.', 'p2_1', 
               'fn_2', 'v_2', '100 Pixel Smoothing', 'p2_2']

# Plot The second minimum locations.
df3.plot('index', ['p2_1', 'p2_2'], title="Data Smoothing Comparison")
# Plot the first minimum locations.
df3.plot('index', ['Raw Min.', '100 Pixel Smoothing'], 
         title="Data Smoothing Comparison")
