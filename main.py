#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 13:30:25 2022

@author: troyobernolte

runs the homework
"""

from data_utils import *
from data_inspection import *

if __name__ == '__main__':
    #define which structure you want to look at
    structure = 1
    
    #Show the original image
    show()
    #Circle the largest value
    show_peak()
    #show the dendrogram of the image
    show_dendrogram()
    #Highlight a structure within the dendrogram
    highlight(structure)
    #Countour this structure
    contour(structure)
    #Contour all of the leaves
    contour_leaves()
    #Print statistics for the data
    stats()