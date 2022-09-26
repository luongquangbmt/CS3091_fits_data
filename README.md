# CS3091_fits_data: HW 2 v1.0
##### Joe Tannoury

### Change List

- no more assignment_1.py, from now the file to run is main.py
- create a new branch for every HW from now on, with an updated readme file
- make use of data_utils.py from main.py



## How to run

Run main.py



## Python scripts

- **main.py**: runs the homework
- **data_inspection.py**: basic script to read fits files, header, data, and plot the image
- **data_utils.py**: utilities functions
  - **squeeze_fits(out_folder, out_name, out_datetime)**: squeeze the fits dimensions and export new fits files
    - _out_folder_: (optional, default current folder './')
    - _out_name_: (optional, default 'squeezed_fits')
    - _out_datetime_: (optional, True or False, default False) 
  - **stats**: comprehensive stats of the fits data
  - **draw_image(cmap)**: draw
    - _cmap_: (optional, default 'gist_ncar')
