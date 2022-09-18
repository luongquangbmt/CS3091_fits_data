#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 10:50:42 2022

@author: troyobernolte

CS3091 Assignment 2

   QUESTIONS
List the at least 5 keywords and their contents:
    SIMPLE  =                    T / conforms to FITS standard                      
    BITPIX  =                    8 / array data type                                
    NAXIS   =                    0 / number of array dimensions                     
    EXTEND  =                    T  

 Data structure: Data Cube
 Data size, shape: (1, 577, 512, 512)
     First 2 dimensions dont really matter

Summary Statistics from get_statistics() function
    Total pixel count:  151257088
    Minimum is:  -0.2420491
    Maximum is:  0.15555312
    Mean is:  1.8423238e-05
    Median is:  2.5055645e-06
    5th percentile is:  -0.01867481768131256
    95th percentile is:  0.018806135002523663
    NaN count is:  104008424
    Total value-carrying pixels:  47248664
    
Histogram of the data of value-carrying pixels is included in the files of this assignment
        
"""
from astropy.io import fits
from astropy.table import Table
import matplotlib.pyplot as plt
from astropy.visualization import astropy_mpl_style
import numpy as np
import math


image_file = "/Users/troyobernolte/Documents/GitHub/Other Data (not commit)/G10.99.SiO.12m.7m.combined.image.fits"

plt.style.use(astropy_mpl_style)
hdul = fits.open(image_file)
#print(hdul.info())
image_data = fits.getdata(image_file, ext=0)
#print(image_data.shape)

hdr = fits.PrimaryHDU().header

#This code shows a slice of a user defined layer
def show_slice(i):
    photo_data = image_data[0][i]
    plt.figure()
    plt.imshow(photo_data, cmap='gray')
    plt.colorbar()

def get_statistics():
    nan_counter = 0
    data_counter = 0
    data_list = []
    for z in range(image_data[0].shape[0]):
        #cut out layer. This will be a (512, 512) 2d array
        layer = image_data[0][z]
        for x in range(layer.shape[0]):
            for y in range(layer.shape[1]):
                #slicing individual pixels in layer
                pixel = layer[x][y]
                if(math.isnan(pixel)):
                    nan_counter += 1
                else:
                    data_counter += 1
                    data_list.append(pixel)
    data = np.array(data_list)
    #Getting summary statistics
    volume = image_data[0].shape[0] * image_data[0].shape[1] * image_data[0].shape[2]
    print("Total pixel count: ", volume)
    print("Minimum is: ", np.min(data))
    print("Maximum is: ", np.max(data))
    print("Mean is: ", np.mean(data))
    print("Median is: ", np.median(data))
    print("5th percentile is: ", np.percentile(data, 5))
    print("95th percentile is: ", np.percentile(data, 95))
    print("NaN count is: ", nan_counter)
    print("Total value-carrying pixels: ", volume - nan_counter)
    #plotting histogram
    plt.figure()
    plt.hist(data, 50)
    plt.show()
    
        
    
evt_data = Table(hdul[0].data)[0]
""" this is a table with 576 columns. Each column represents a 2D slice of 
the data with size (512, 512)"""
#print(evt_data)

"""Getting histograms"""
def hist(layer):
    """ INCURS THE FOLLOWING ERROR:
    ValueError: setting an array element with a sequence
    """
    hist = plt.hist(evt_data[layer])
    plt.plot(hist)
    plt.savefig()
    plt.show()

def get_info():
    hdu = fits.PrimaryHDU()
    hdu.header