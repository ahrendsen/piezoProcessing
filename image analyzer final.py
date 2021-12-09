
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 09:20:23 2021
@author: karla
"""

"""
Modifications made by niko thurs Dec 2 9:55 2021
"""

import skimage
from skimage import measure
import matplotlib.pyplot as plt
import os
import datetime
import numpy as np
"""
homeDir = os.path.expanduser("~")
photosDir = os.path.join(homeDir, "Desktop", "gitSpace", "piezoprocessing",
                         "data")

file = os.path.join(photosDir,
                    "C:\TIm Gay Research\Lab Photos\Camera Data\11_2_photos\DSC_0062.JPG")
"""

def process_file(image_location, fringe_width): 
    #file = (r"C:\TIm Gay Research\Lab Photos\Camera Data\11_2_photos\DSC_0062.JPG")
    file = (image_location)
    image = skimage.io.imread(file)
    skimage.io.imshow(image)
    
    #line = measure.profile_line(image,[50,0],[50,400], mode='constant', order=1)
    
    """linewidth = 160 because we want to capture 2/3 of the fringe pattern,
    the edges are more susceptible to noise.
    """
    
    line = measure.profile_line(image,[len(image)/2,0],[len(image)/2,len(image[0])],
                                       linewidth = 120,mode='constant', order=5)
    line = line[:,0]
    fig, ax = plt.subplots()
    ax.scatter(range(len(line)),line) 
    #ax.scatter(range(len(line)),line[:,1]) 
    print(max(line))
    
    width = fringe_width
    
    """
    1 pixel corresponds to one element of the array
    """
    max_location = np.argmax(line)
    
    #print(max_location)
    
    left = max_location-width
    right = max_location + width
    
    min_1 = np.argmin(line[left:max_location]) + left
    print(min_1)
    
    min_2 = np.argmin(line[max_location:right]) + max_location
    print(min_2)
    return([min_1,min_2])
    

process_file(r"C:\TIm Gay Research\Lab Photos\Camera Data\11_2_photos\DSC_0072.JPG", 500)


