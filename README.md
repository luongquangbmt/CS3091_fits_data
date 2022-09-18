# CS3091_fits_data
from astropy.io import fits
from matplotlib.colors import LogNorm
import matplotlib.pyplot as plt
from astropy.visualization import astropy_mpl_style
plt.style.use(astropy_mpl_style)
from astropy.utils.data import get_pkg_data_filename
import numpy as np

#from astropy.utils.data import download_file
#image_file = download_file('http://data.astropy.org/tutorials/FITS-images/HorseHead.fits', cache=True )

hdu_list = fits.open('.vscode/cleanimage.G10.99.SiO.12m.7m.combined.image.mom0 (2).fits')
hdu_list.info()

image_data = hdu_list[0].data

print(type(image_data))
print(image_data.shape)
print(hdu_list[0].header)


'''
hdu_list.close()

image_data = fits.getdata('.vscode/cleanimage.G10.99.SiO.12m.7m.combined.image.mom0 (2).fits')

print(type(image_data)) # Show the Python type for image_data
print(image_data.shape) # Show the number of pixels per side in the 2-D image

plt.imshow(image_data, cmap='gray')
plt.colorbar()

# To see more color maps
# http://wiki.scipy.org/Cookbook/Matplotlib/Show_colormaps

print('Min:', np.min(image_data))
print('Max:', np.max(image_data))
print('Mean:', np.mean(image_data))
print('Stdev:', np.std(image_data))

plt.imshow(image_data.squeeze())
plt.show()

print(type(image_data.flatten()))
print(image_data.flatten().shape)

histogram = plt.hist(image_data.flatten(), bins='auto')

plt.imshow(image_data, cmap='gray', norm=LogNorm())

# I chose the tick marks based on the histogram above
cbar = plt.colorbar(ticks=[5.e3,1.e4,2.e4])
cbar.ax.set_yticklabels(['5,000','10,000','20,000'])


################################
hdulist = fits.open('.vscode/cleanimage.G10.99.SiO.12m.7m.combined.image.mom0 (2).fits')
hdulist.info()
hdulist = fits.getdata('.vscode/cleanimage.G10.99.SiO.12m.7m.combined.image.mom0 (2).fits', ext=0)
print('.vscode/cleanimage.G10.99.SiO.12m.7m.combined.image.mom0 (2).fits')
plt.figure()
plt.imshow('.vscode/cleanimage.G10.99.SiO.12m.7m.combined.image.mom0 (2).fits', cmap='gray')
plt.colorbar()

'''
