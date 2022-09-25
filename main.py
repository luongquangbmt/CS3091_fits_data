from astropy.io import fits
hdul = fits.open('cleanimage1.fits')
import sys


print(hdul[0].header)
print(hdul[0].data)

print(sys.path)