# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 09:20:23 2021

@author: karla
"""
import skimage
from skimage import measure
import matplotlib.pyplot as plt
import os
import datetime


homeDir = os.path.expanduser("~")
photosDir = os.path.join(homeDir, "Desktop", "gitSpace", "piezoprocessing",
                         "data")

def processFile(inputFile, spacing, inputDirectory, outputDirectory):
    image = skimage.io.imread(os.path.join(inputDirectory,inputFile))
    
    line = measure.profile_line(image,
                                [len(image)/2,0],[len(image)/2,len(image[0])],
                                mode='constant',
                                linewidth = 60, order=5)
    fig, ax = plt.subplots()
    
    ax.scatter(range(len(line)),line[:,0])
    ax.set_title(inputFile)
    ax.set_xlabel("X Position (pixel)")
    ax.set_ylabel("Intensity")
    
    return [1,2]

