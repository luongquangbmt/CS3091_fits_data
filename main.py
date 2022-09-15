from astropy.io import fits
import numpy as np

# Set up matplotlib
import matplotlib.pyplot as plt
hdul = fits.open("cleanimage.G10.99.SiO.12m.7m.combined.image.mom0.fits")
print(hdul.info())
image_data = hdul[0].data
print(type(image_data))
print(image_data.shape)
print(hdul[0].header)
hdul.close(0)

plt.imshow(image_data[0,0], cmap='summer')
plt.colorbar()

plt.show()





