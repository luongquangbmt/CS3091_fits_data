


import numpy as np
import matplotlib.pyplot as plt
from astropy.visualization import astropy_mpl_style
#from astropy.utils.data import download_file
from astropy.io import fits
plt.style.use(astropy_mpl_style)


hdul_list = fits.open('DATA\G1099SiO12m7mtpcombined.fitsTb.fits') 
hdul_list.info()
image_data = hdul_list[0].data
print(image_data.shape)
hdul_list.close()
print('Min:', np.min(image_data))
print('Max:', np.max(image_data))
print('Mean:', np.mean(image_data))
print('Stdev:', np.std(image_data))


plt.imshow(image_data.squeeze())
plt.show()


print(type(image_data.flatten()))
print(image_data.flatten().shape)

image_data_hist = plt.hist(image_data.flatten(), bins='auto')
plt.show()


















