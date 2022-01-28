
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
# For plot image inset
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
import os
import datetime
import numpy as np
import bottleneck as bn 


def process_file(filename, fringe_width, input_folder, output_folder,
                 graph_output=False):
    print('Processing Image:' + filename)
    image = skimage.io.imread(os.path.join(input_folder, filename))
    # skimage.io.imshow(image)
    # line = measure.profile_line(image,[50,0],[50,400], mode='constant', order=)
    """linewidth = 160 because we want to capture 2/3 of the fringe pattern,
    the edges are more susceptible to noise.
    """
    imageHeight = len(image)
    imageWidth = len(image[0])
    
    yMidpoint = imageHeight/2 
    xMidpoint = imageWidth/2
    
    # Here we take the profile of the image with a VERTICAL line.
    # This allows us to determine the y coordinate of the center
    # of the Gaussian beam. Since this examines the whole image, it takes
    # some time to run. In the future, if this is used with the batch
    # provess program it should probably be put in a 
    # different function and run on just the first image in a sequence to 
    # retrieve the desired y position, then use that same value for all of
    # the images.
    line2 = measure.profile_line(image,
                                [0, xMidpoint], # (x,y) of start of line
                                [imageHeight, xMidpoint], # (x,y) of end
                                linewidth = imageWidth,
                                mode='constant', order=1)
    
    line2 = line2[:,0] # Note: this line just takes the red pixel data
    
    # Here we can visualize the vertical Gaussian profile of the beam.
    # fig2, ax2 = plt.subplots()
    # ax2.scatter(range(len(line2)), line2)
    
    y_max_intensity_location = np.argmax(line2)
    
    profile_linewidth = 500  # This is the total width i.e. distance up plus
                             # distance down. The larger this is, the more
                             # time it takes to process each image. Using
                             # nearly the entire image (3000), takes something
                             # like 26 seconds to process a single image,
                             # but it results in much smoother data. This is
                             # comapred to 5 seconds for a linewidth of 120.
                             
    profile_y = y_max_intensity_location
    line = measure.profile_line(image,
                                [profile_y, 0],
                                [profile_y, imageWidth],
                                linewidth = profile_linewidth,
                                mode='constant', order=5)
    line = line[:,0] # Note: this line just takes the red pixel data
    # Here, you can "smooth" the data by taking a moving average.
    # the window parameter tells you how many elements you take in the 
    # average. The min_count allows it to use a single point at the edges
    # as the average.
    line = bn.move_mean(line, window=1, min_count=1)
    fig, ax = plt.subplot_mosaic([['top', 'top'],
                                  ['bottom_left', 'bottom_right']],
                                 constrained_layout=True)
    ax['top'].scatter(range(len(line)), line)
    ax['top'].set_title("Full Plot: " + os.path.basename(filename))
    ax['bottom_left'].scatter(range(len(line)), line)
    ax['bottom_left'].set_title("First Minimum")
    ax['bottom_right'].scatter(range(len(line)), line)
    ax['bottom_left'].set_title("First Minimum")
    
    # Make an inset of the actual image on the upper plot
    axins = inset_axes(ax['top'], width=1.35, height=.9, loc='upper left')
    axins.tick_params(labelleft=False, labelbottom=False)
    axins.imshow(image)
    axins.axhspan(profile_y - profile_linewidth/2,
                  profile_y + profile_linewidth/2,
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


    graph_name = str.replace(filename, ".JPG", "_graph.png")
    if(graph_output):
        fig.savefig(os.path.join(output_folder, graph_name))

    return([filename, min_1, min_2])

homeDir = os.path.expanduser("~")
photosDir = os.path.join(homeDir, "gitSpace", "piezoprocessing",
                          "data")

file = os.path.join(photosDir, "DSC_0068.JPG")
process_file(file, 500, photosDir, photosDir)
