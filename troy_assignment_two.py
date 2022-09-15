#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 10:50:42 2022

@author: troyobernolte

CS3091 Assignment 2
"""

from astropy.io import fits
import matplotlib.pyplot as plt
from astropy.visualization import astropy_mpl_style

image_file = "/Users/troyobernolte/Documents/GitHub/Other Data (not commit)/G10.99.SiO.12m.7m.combined.image.fits"

plt.style.use(astropy_mpl_style)
hdul = fits.open(image_file)
#print(hdul.info())
image_data = fits.getdata(image_file, ext=0)
#print(image_data.shape)

#This code shows a slice of a user defined layer
def show_slice(i):
    photo_data = image_data[0][i]
    plt.figure()
    plt.imshow(photo_data, cmap='gray')
    plt.colorbar()
    
def print_header_info():
    print(hdul.info())

"""Getting histograms"""