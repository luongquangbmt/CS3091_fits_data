#!/usr/bin/env python
# coding: utf-8

import numpy as np
import astropy 
from astropy.io import fits as fs

myfile = fs.open('DATA/autoG28.23_SiO.12m.tc_final.fits')

print(myfile[0].header)
print(type(myfile[0].data))
#print(myfile[0].data)

my_image = myfile[0].data

print(my_image)

print(np.shape(my_image))

my_squeezed_image = my_image[0,0]
print(np.shape(my_squeezed_image))
my_squeezed_image = my_image.squeeze()
print(np.shape(my_squeezed_image))

data_std = np.std(my_squeezed_image[100:150,200:221])

print(f"mean of the data {np.mean(my_squeezed_image)}")
print(f"mean of the data {np.max(my_squeezed_image)}")
print(f"min of the data {np.min(my_squeezed_image)}")
print(f"std of the data {data_std}")
#print(f"5% percentile of the data {}")
#print(f"95% percentile of the data {}")

import matplotlib.pyplot as plt
import matplotlib as mpl


plt.figure()
plt.imshow(my_squeezed_image, vmin=2*data_std, cmap=mpl.cm.PuOr)
plt.colorbar()
plt.show()

# Finding area where there is no signal to calculate noise
non_signal = my_squeezed_image[400:450,200:300]
print(non_signal.std())
plt.figure()
plt.imshow(non_signal, vmin=data_std, cmap=mpl.cm.rainbow)
plt.colorbar()
plt.show()
