from astropy.io import fits
from matplotlib.colors import LogNorm
import matplotlib.pyplot as plt
from astropy.visualization import astropy_mpl_style
plt.style.use(astropy_mpl_style)
from astropy.utils.data import get_pkg_data_filename
import numpy as np
import pandas as pd

#----------------------------------------------------------------------------------------------
#Assignment 2
#----------------------------------------------------------------------------------------------

hdu_list = fits.open('.vscode/cleanimage.G10.99.SiO.12m.7m.combined.image.mom0 (2).fits')
hdu_list.info()
image_data = hdu_list[0].data

#Inspect data
#        -  List the at least 5 keywords and their contents
print("The following is the data header:")
print(hdu_list[0].header)

#               What type of data structure do we have?
print(f"The data type is: {type(image_data)}") # doesn't show the type!

#              What is the shape of the data?
print(f"the data shape is: {image_data.shape}")
hdu_list.close()
#              How many pixels are there in total?

#What are min, max, mean, median, standard deviation, 5% percentile,
# 95%percentile, number of NaN pixels of the data?
print("Summary statistics:")
print('Min:', np.min(image_data))
print('Max:', np.max(image_data))
print('Mean:', np.mean(image_data))
print('Stdev:', np.std(image_data))
print('5th percentile: ', np.percentile(image_data, 5))
print('95th percentile: ', np.percentile(image_data, 95))
print(' Number of NaN pixels: ', np.nancumsum(image_data)) #I think this is wrong
 
# 2. Visualize data
#   Package: Using matplotlib, glue, yt  or any others
#   2.1 Make the plot of the data (using imshow)
plt.imshow(image_data.squeeze())
plt.show()

print(type(image_data.flatten()))
print(image_data.flatten().shape)

image_data_hist = plt.hist(image_data.flatten(), bins='auto')
plt.show()

#   2.2 Make the plot of the data (using imshow) but use different noise thresholds (rms), 
# we can use 1xrms, 2xrms to better show the signal. For now, consider rms = standard deviation

#so very confused what any of these words mean


#   2.3 Make the histogram of the data
#         For take-home assigment (Make the histogram of a few slices in the 3rd dimension)   
x = [image_data]
plt.hist(x, bins = 10)
plt.show() 
# what are we making a histogram of???
#doesn't work

#  2.3 Plot the spectra (the 3rd dimension) of a few pixels
#        For take-home assigment (Make the histogram of a few slices in the 3rd dimension)    


#doing the shape stuff
#initialize a dataframe?
df = pd.DataFrame(
	[[21, 72, 67.1],
	[23, 78, 69.5],
	[32, 74, 56.6],
	[52, 54, 76.2]],
	columns=['a', 'b', 'c'])

print('The DataFrame is :\n', df)

#get dataframe shape
shape = df.shape
print('\nDataFrame Shape :', shape)
print('\nNumber of rows :', shape[0])
print('\nNumber of columns :', shape[1])
print("this is the end")
# I don't think it's working....


