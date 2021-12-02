# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 09:20:23 2021

@author: karla
"""
import skimage
from skimage import measure
import matplotlib.pyplot as plt
import os


homeDir = os.path.expanduser("~")
photosDir = os.path.join(homeDir, "Desktop", "gitSpace", "piezoprocessing",
                         "data")

# The input file is the image to be analyzed.
# The spacing is the pixels between the maximum and the minimum in the image.
# The input directory is the folder that the input files are located in.
# The output directory is where you want any output data to be saved (not
# curretnly used.)


def processFile(inputFile, spacing, inputDirectory, outputDirectory):
    image = skimage.io.imread(os.path.join(inputDirectory, inputFile))

    line = measure.profile_line(image,
                                [len(image)/2, 0],
                                [len(image)/2, len(image[0])],
                                mode='constant',
                                linewidth=60, order=5)
    fig, ax = plt.subplots()

    ax.scatter(range(len(line)), line[:, 0])
    ax.set_title(inputFile)
    ax.set_xlabel("X Position (pixel)")
    ax.set_ylabel("Intensity")

    return [1, 2]
