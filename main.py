from astropy.io import fits
import numpy as np

# Set up matplotlib
import matplotlib.pyplot as plt
hdul = fits.open("cleanimage.G10.99.SiO.12m.7m.combined.image.mom0.fits")
print(hdul.info())
image_data = hdul[0].data

print(hdul[0].header)
print(type(image_data))
print(image_data.shape)
print(image_data.mean())
print(image_data.max(axis=0))
print(image_data.max())

print(type(image_data))
print('median:',np.median(image_data))

hdul.close(0)


#Calculate the Standard deviations of the X and Y axis 
non_signal = image_data[400:450,200:300]
print (non_signal)
plt.figure()
plt.imshow(image_data[0,0], cmap='rainbow')
plt.colorbar()

plt.show()



'''
5 Keywords:

-NAXIS1=339

-NAXIS2=367

-BPA=0.7584327537994E+02

-CDELT2=0.5555555555556E-04

-NAXIS3=1

 

Data shape/size:

(339,367,1)

Analysis:

min=-0.05529545

max=0.090962544

std=0.00851118

mean=1.4208172e-05

median=-1.6927841e-05

'''

# This is the start of assignment 3

from astropy.io import fits
from astrodendro import Dendrogram
from collections.abc import Iterable

array = image_data[0,0]

d = Dendrogram.compute(array, min_value=0.01, min_delta=0.001, min_npix=10)
v = d.viewer()
p = d.plotter()
print(d.trunk)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

# Plot the whole tree
p.plot_tree(ax, color='black')


# Add axis labels
ax.set_xlabel("Structure")
ax.set_ylabel("Flux")

plt.show()