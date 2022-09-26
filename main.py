from data_utils import DataUtils


if __name__ == '__main__':
    du = DataUtils('data/cleanimage.G10.99_Feather_SiO.image.fits')
    du.stats()
    du.squeeze_fits(out_folder='PROCESSED_DATA', out_name='squeezed')
    du.draw_image()

