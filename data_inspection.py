#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 13:43:56 2022

@author: troyobernolte

basic script to read fits files, header, data, and plot the image
"""

from astropy.io import fits
import matplotlib.pyplot as plt
import numpy as np
from astrodendro import Dendrogram

#Importing image data
image_file = 'data/cleanimage.G10.99.SiO.12m.7m.combined.image.mom0.fits'
#Access image data. The 1st two dimensions aren't important, we only use the 3rd and 4th
image_data = fits.getdata(image_file, ext=0)[0][0]
hdul = fits.open(image_file)
hdr = hdul[0].header

def show():
    #Show the image we are computing
    plt.figure()
    plt.imshow(image_data, cmap='nipy_spectral', vmin = mean_noise)
    plt.title("Original image")
    plt.colorbar()
    
    
def get_info():
    """Finding the average noise level in the data"""
    data_array = []
    layer = image_data
    #First calculate the mean noise level
    for x in range(400,500):
        for y in range(400,500):
            data_array.append(layer[x][y])
    data = np.array(data_array)
    mean_noise = np.mean(data)
    
    #Now calculate standard deviation within actual data
    data_array = []
    for x in range(100, 400):
        for y in range(90, 410):
            data_array.append(layer[x][y])
    noise_data = np.array(data_array)
    standard = np.std(noise_data)
    return(mean_noise, standard)

info = get_info()
standard = info[1]
mean_noise = info[0]

def compute_dendrogram():
    #deviation and a min_delta of the standard deviation within the actual data
    d = Dendrogram.compute(image_data, min_value= mean_noise + standard, min_delta = standard,
                           min_npix=10)
    d.save_to('dendrogram_clean_image.fits')

d = Dendrogram.load_from('dendrogram_clean_image.fits')

trunk = d.trunk

p = d.plotter()
