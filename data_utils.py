import pprint
import numpy as np
from astropy.io import fits
from datetime import datetime

from matplotlib import pyplot as plt


class DataUtils:
    pass

    def __init__(self, fits_fn):
        # print("Initialize the class")
        myfile = fits.open(fits_fn)
        # print(myfile[0].header)
        self.fits_hdr = myfile[0].header
        self.fits_data = myfile[0].data
        # print(np.shape(self.fits_data))

    def squeeze_fits(self, out_folder='./', out_datetime=False, out_name='squeezed_fits'):
        my_squeezed_image = self.fits_data.squeeze()
        hdr = self.fits_hdr
        print(np.shape(my_squeezed_image))
        _out_datetime = f"_{str(datetime.now())}" if out_datetime else ""
        outfile = f"{out_folder}/{out_name}{_out_datetime}.fits"
        fits.writeto(outfile, my_squeezed_image, hdr, overwrite=True)
        self.squeezed_fit = my_squeezed_image

    # returns stats of data & prints it
    def stats(self):
        # Get statistics of data
        x = {
            "size": self.fits_data.size,
            "shape": self.fits_data.shape,
            "min": np.min(self.fits_data),
            "max": np.max(self.fits_data),
            "mean": np.mean(self.fits_data),
            "median": np.median(self.fits_data),
            "percentile_5": np.percentile(self.fits_data, 5),
            "percentile_95": np.percentile(self.fits_data, 95),
            "std": np.std(self.fits_data),
            "NaN_count": np.count_nonzero(np.isnan(self.fits_data))
        }

        pprint.pprint(x)  # pretty print dict
        return x

    def draw_image(self, cmap='gist_ncar'):
        plt.figure()
        data_std = np.std(self.squeezed_fit[0, 100:150, 200:221])
        plt.imshow(self.squeezed_fit[0], vmin=2 * data_std, cmap=cmap)
        plt.colorbar()
        plt.show()
