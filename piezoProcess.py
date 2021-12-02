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

file = os.path.join(photosDir,
                    "test.jpg")
image = skimage.io.imread(file)
skimage.io.imshow(image)

line = measure.profile_line(image,[len(image)/2,0],[len(image)/2,len(image[0])], mode='constant', order=1)
fig, ax = plt.subplots()
ax.scatter(range(len(line)),line[:,1])