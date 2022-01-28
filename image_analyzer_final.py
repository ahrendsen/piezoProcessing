
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 09:20:23 2021
@author: karla
"""

"""
Modifications made by niko thurs Dec 2 9:55 2021
"""

import skimage
from skimage import io
from skimage import measure
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
import os
import datetime
import numpy as np
import bottleneck as bn 

homeDir = os.path.expanduser("~")
photosDir = os.path.join(homeDir, "gitSpace", "piezoprocessing",
                         "data")

file = os.path.join(photosDir, "DSC_0068.JPG")


def process_file(image_location, fringe_width, input_folder, output_folder):
    image = skimage.io.imread(os.path.join(input_folder, image_location))
    # skimage.io.imshow(image)
    # line = measure.profile_line(image,[50,0],[50,400], mode='constant', order=)
    """linewidth = 160 because we want to capture 2/3 of the fringe pattern,
    the edges are more susceptible to noise.
    """
    yCoord = len(image)/2 
    profile_linewidth = 120 # This is the total width i.e. distance up plus 
                             # distance down. The larger this is, the more
                             # time it takes to process each image. Using
                             # nearly the entire image (3000), takes something
                             # like 26 seconds to process a single image,
                             # but it results in much smoother data. This is
                             # comapred to 5 seconds for a linewidth of 120.
    line = measure.profile_line(image,
                                [yCoord, 0],
                                [yCoord, len(image[0])],
                                linewidth = profile_linewidth,
                                mode='constant', order=5)
    line = line[:,0]
    line = bn.move_mean(line, window=1, min_count=1)
    print(line)
    fig, ax = plt.subplot_mosaic([['top', 'top'],
                                  ['bottom_left', 'bottom_right']],
                                 constrained_layout=True)
    ax['top'].scatter(range(len(line)), line)
    ax['top'].set_title("Full Plot: " + os.path.basename(file))
    ax['bottom_left'].scatter(range(len(line)), line)
    ax['bottom_left'].set_title("First Minimum")
    ax['bottom_right'].scatter(range(len(line)), line)
    ax['bottom_left'].set_title("First Minimum")
    
    # Make an inset of the actual image
    axins = inset_axes(ax['top'], width=1.35, height=.9, loc='upper left')
    axins.tick_params(labelleft=False, labelbottom=False)
    axins.imshow(image)
    axins.axhspan(yCoord - profile_linewidth/2,
                  yCoord + profile_linewidth/2,
                  color='yellow',
                  alpha=.5)
    print(max(line))
    
    width = fringe_width
    
    """
    1 pixel corresponds to one element of the array
    """
    max_location = np.argmax(line)
    
    #print(max_location)
    
    left = max_location - width
    right = max_location + width
    
    min_1 = np.argmin(line[left: max_location]) + left
    print(min_1)
    
    min_2 = np.argmin(line[max_location: right]) + max_location
    print(min_2)
    
    ax['top'].axvline(min_1)
    ax['top'].axvline(min_2)
    
    shift = 150
    ax['bottom_left'].set_xlim([min_1 - shift, min_1 + shift])
    ax['bottom_left'].axvline(min_1)

    ax['bottom_right'].set_xlim([min_2 - shift, min_2 + shift])
    ax['bottom_right'].axvline(min_2)
    ax['bottom_right'].set_title("Second Minimum")
    
    return([min_1,min_2])
    

process_file(file, 500, photosDir, photosDir)
