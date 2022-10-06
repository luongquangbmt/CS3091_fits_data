#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 13:31:42 2022

@author: troyobernolte

Purpose: utilities functions
"""

from astropy.io import fits
from data_inspection import get_info
import matplotlib.pyplot as plt
from astrodendro import Dendrogram
from astrodendro.analysis import PPStatistic

#Importing image data
image_file = 'data/cleanimage.G10.99.SiO.12m.7m.combined.image.mom0.fits'
#Access image data. The 1st two dimensions aren't important, we only use the 3rd and 4th
image_data = fits.getdata(image_file, ext=0)[0][0]

d = Dendrogram.load_from('dendrogram_clean_image.fits')

trunk = d.trunk

p = d.plotter()

def highlight(struct_num):
    #shows the dendrogram and highlights a structure. Structure 8&1 is very cool
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

    # Show contour for ``min_value``
    ax.set_xlabel(("Structure {} is highlighted").format(struct_num))
    ax.set_ylabel("Flux")

    # Highlight two branches
    p.plot_tree(ax, color='black', lw=2, alpha=0.5)

    p.plot_tree(ax, structure=[struct_num], color='red', lw=2, alpha=0.5)
    plt.show()
    
def contour(struct):
    """Takes in a structure number and shows the contour of that strucure"""
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.imshow(image_data, origin='lower', interpolation='nearest', cmap=plt.cm.Blues, vmax=4.0)

    # Show contour for ``min_value``
    p.plot_contour(ax, color='black')

    # Highlight given branches
    p.plot_contour(ax, structure=struct, lw=3, colors='red')
    
def contour_leaves():
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.imshow(image_data, origin='lower', interpolation='nearest', cmap=plt.cm.Blues, vmax=4.0)
    p.plot_contour(ax, color='black')
    for leaf in d.leaves:
        p.plot_contour(ax, structure=leaf, colors='red')
        s = PPStatistic(leaf)
        ellipse = s.to_mpl_ellipse(edgecolor='orange', facecolor='none')
        ax.add_patch(ellipse)
        
    

def max_pixel():
    max_value = 0
    peak = None
    for element in trunk:
        local_peak = element.get_peak()
        if local_peak[1] > max_value:
            max_value = local_peak[1]
            peak = local_peak
    return peak

def show_dendrogram():
    d.viewer()
    

def show_peak():
    plt.figure()
    largest = max_pixel()
    x = largest[0][0]
    y = largest[0][1]
    #Get the mean noise from data inspection
    mean_noise = get_info()[1]
    #Show the image with the mean noise as a min value
    plt.imshow(image_data, cmap='nipy_spectral', vmin=mean_noise)
    plt.colorbar()
    #Plot a circle with the cordinates given by finding the max
    circle1 = plt.Circle((x,y), 25, color = 'r', fill = False)
    fig = plt.gcf()
    ax = fig.gca()
    ax.add_patch(circle1)
    plt.title("Image with largest value circled")
    plt.show()
    
def stats():
    stat = PPStatistic(d.trunk[0])
    major_sigma	 = stat.major_sigma	
    print("Major sigma is: ", major_sigma)
    minor_sigma	= stat.minor_sigma	
    print("Minor sigma is: ", minor_sigma)
    position_angle	 = stat.position_angle
    print("Position angle is: ", position_angle)
    radius = stat.radius
    print("Radius is: ", radius)
    area_exact = stat.area_exact
    print("Exact area of structure on the sky is: ", area_exact)
    area_ellipse = stat.area_ellipse
    print("Elipse area is: ", area_ellipse)
    x_cen = stat.x_cen	
    print("Mean position of the structure in the x direction: ", x_cen)
    y_cen = stat.y_cen
    print("Mean position of the structure in the y direction: ", y_cen)
    

    

