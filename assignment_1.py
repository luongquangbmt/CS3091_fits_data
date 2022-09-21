from astropy.io import fits

import numpy as np
import matplotlib.pyplot as plt
from astropy.visualization import astropy_mpl_style

plt.style.use(astropy_mpl_style)


hdul = fits.open('data/cleanimage.G10.99_Feather_SiO.image.fits')

if __name__ == '__main__':
    hdul.info()
    print(hdul[0])
    data = hdul[0].data[0, :, :]

    # Get statistics of data
    print(f"""
    shape: {data.shape}
    min: {np.min(data)}
    max: {np.max(data)}
    mean: {np.mean(data)}
    median: {np.median(data)}
    std: {np.std(data)}
    """
    )

    plt.figure()

    # reducing noise by binning values in 1 / std of the data
    # ex: 1 / 0.03 = 33 different colors
    bin_count = 10  # int(1 / np.std(data))
    hist = np.histogram(data, bins=bin_count)
    data_ = np.fmin(np.digitize(data, hist[1]), bin_count) / bin_count
    plt.imshow(data_, cmap='gist_ncar')
    plt.colorbar()
    plt.show()

hdul.close()
