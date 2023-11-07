import numpy as np
from astropy.io import fits
from astropy.io import ascii
import astropy.units as u

data = ascii.read('autoread_table.txt')
print(data)
### Note that lines are 0 indexed and empty lines removed!
data2 = ascii.read('manualread_table.txt',header_start=4,data_start=5,data_end=13)
print(data2)

data2.write('output.txt',format='latex')