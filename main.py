from astropy.io import fits # dealing with astronimical data, images
from matplotlib.colors import LogNorm
import matplotlib.pyplot as plt # plots 
from astropy.visualization import astropy_mpl_style
plt.style.use(astropy_mpl_style)
from astropy.utils.data import get_pkg_data_filename
import numpy as np #numerical python -- numerical algebra, matrices 
import pandas as pd #dataframe  operation
from astrodendro import Dendrogram # performs dendrogram analysis on images

hdu_list = fits.open('.vscode/cleanimage.G10.99.SiO.12m.7m.combined.image.mom0 (3).fits')
hdu_list.info()
image_data = hdu_list[0].data
my_squeezed_image = image_data.squeeze();

#-----------------------------------------------------------------------------------------
# dendrogram stuff
#-----------------------------------------------------------------------------------------

d = Dendrogram.compute(my_squeezed_image[0], min_value=0.01, min_delta=.001, min_npix=10)
p = d.plotter()
v = d.viewer()

v.show()
d.trunk

print(d.trunk)
print(p)

fig = plt.figure()
ax =fig.add_subplot(1,1,1)
ax.imshow(image_data[0], origin='lower', interpolation='nearest', cmap=plt.cm.Blues, vmax=4.0)

# Highlight two branches
p.plot_tree(ax, structure=8, color='pink', lw=2, alpha=0.5)
p.plot_tree(ax, structure=24, color='green', lw=2, alpha=0.5)

# Add axis labels
ax.set_xlabel("Structure")
ax.set_ylabel("Flux")
plt.show()


