from astropy.io import fits
from astropy.visualization import astropy_mpl_style
import matplotlib.pyplot as plt



def main():
  


  hdul =   fits.open('DATA/cleanimage.G10.99.SiO.12m.7m.combined.image.mom0.fits')

  hdul.info()
  hdr = hdul[0].header
  data = hdul[0].data
  
  print(f'Size: {data.size} \nShape: {data.shape} \nMin: {data.min()} \nMax: {data.max()}')

  ##print(f'Max Axis 1: {data.max(axis=3)} \nMin Axis1: {data.min(axis=3)}')
  resizedData = data[0,0,:,:]
  print(f'new Dim: {resizedData.shape}')
  plt.style.use(astropy_mpl_style)
  
  plt.figure()
  plt.imshow(resizedData, cmap = 'gray')
  plt.colorbar()
  plt.show()

  
if __name__ == "__main__":
  main()
