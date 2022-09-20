#!/usr/bin/env python
# coding: utf-8

from unicodedata import name
import numpy as np
import astropy 
from astropy.io import fits

class DataUtils():
    pass

    def __init__(self, fits_fn):
        print("Initialize the class")
        myfile = fits.open(fits_fn)
        print(myfile[0].header)
        self.fits_hdr = myfile[0].header
        self.fits_data = myfile[0].data
        print(np.shape(self.fits_data))    
    
    def squeeze_fits(self, out_folder='./', out_name='squeezed_fits'):
        my_squeezed_image = self.fits_data.squeeze()
        hdr = self.fits_hdr
        print(np.shape(my_squeezed_image))    
        outfile = out_folder+'/'+out_name+'.fits'
        fits.writeto(outfile, my_squeezed_image, hdr, overwrite=True)
        print('DONE')

def main():
    du = DataUtils('RAWDATA/autoG343.48.contsub.SiO.12m.tc_final.fits')
    du.squeeze_fits(out_folder='PROCCESSEDDATA', out_name='autoG343.48.contsub.SiO.12m.tc_final_squezed')


if __name__ == "__main__":
    main()
