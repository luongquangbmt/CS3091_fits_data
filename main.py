from codecs import charmap_build
from importlib.util import LazyLoader
from locale import normalize
from statistics import stdev
from turtle import pd
from typing import ChainMap
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
from mpl_toolkits.axes_grid1.axes_divider import make_axes_locatable
#from astropy.visualization import astropy_mpl_style
from astropy.io import fits
from mpl_toolkits.mplot3d import Axes3D
import matplotlib as mpl
import math
from astropy.io.fits import getdata
from astropy import wcs
from astrodendro import Dendrogram
from astropy.io import fits
from astropy.io.fits import getdata



#plt.style.use(astropy_mpl_style)


hdul_list = fits.open('DATA\G1099SiO12m7mtpcombined.fits') 
hdul_list.info()
image_data = hdul_list[0].data
print(image_data.shape)
print(hdul_list[0].header)
#hdul_list.close()

#Analysing data

print('Min:', np.min(image_data))
print('Max:', np.max(image_data))
print('Mean:', np.mean(image_data))
print('Stdev:', np.std(image_data))
print('median:',np.median(image_data))
print('5th percentile:',np.percentile(image_data,  5))
print('95th percentile:',np.percentile(image_data, 95))
image_volume = image_data.shape[0] * image_data.shape[1] * image_data.shape[2]
print('Num_of_pixels:', image_volume )

'''
5 Keywords:
-NAXIS1=339
-NAXIS2=367
-BPA=0.7584327537994E+02
-CDELT2=0.5555555555556E-04
-NAXIS3=1

Data shape/size:
(339,367,475)

Analysis:
min=-0.05529545
max=0.090962544
std=0.00851118
mean=1.4208172e-05
median=-1.6927841e-05
5%=-0.01472674198952
95%=0.014760643523186442
n of pixels=59096175
'''

'''
#visualizing plot
plt.imshow(image_data[0], vmin = 0, cmap='rainbow')
plt.colorbar()
plt.show()

#1xrms
plt.imshow(image_data[0], vmin = 0, vmax = np.std(image_data), cmap='rainbow')
plt.colorbar()
plt.show()

#2xrms
plt.imshow(image_data[0], vmin = 0, vmax = np.std(image_data)*2, cmap='rainbow')
plt.colorbar()
plt.show()
'''
#Dendrogram
Dendrogram
d = Dendrogram.compute(image_data[0],   min_value='min', min_npix=20, min_delta=0.1)
p = d.plotter()
v=d.viewer()
v.show()
d.trunk
print(d.trunk)
print(p)
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.imshow(image_data[0], vmin=0, origin='lower', interpolation='nearest', cmap='rainbow')

# Highlight two branches
p.plot_tree(ax, structure=8, color='red', lw=2, alpha=0.5)
p.plot_tree(ax, structure=24, color='orange', lw=2, alpha=0.5)

# Add axis labels
ax.set_xlabel("Structure")
ax.set_ylabel("Flux")
plt.show()




'''
print(type(image_data.flatten()))
print(image_data.flatten().shape)

#histogram full data
image_data_hist = plt.hist(image_data.flatten(), bins='auto')
plt.show()

#part of data
image_squeeze = image_data[0]
data_std = np.std(image_squeeze[50:100,50:150])
image_signal = image_squeeze[50:100,50:150]
print(image_signal.std())
image_signal
plt.figure()
plt.imshow(image_signal, vmin=2*data_std, cmap=mpl.cm.rainbow)
plt.colorbar()
plt.show()

#histogram part of data
image_data_hist_2 = plt.hist(image_signal.flatten(), bins='auto')
plt.show()

#plot spectra
plt.style.use('classic')
spectra=fits.open('DATA\cleanimage.G10.99_Feather_SiO.image.fits')
fig=plt.figure(figsize=(18,16), dpi=80, facecolor='w', edgecolor='k')
spectrum= image_data[350,300,:]
plt.imshow(image_data[0], cmap='rainbow', vmin=np.std(image_data), vmax=350)
plt.clf()
plt.plot(spectrum)
plt.show()

'''



