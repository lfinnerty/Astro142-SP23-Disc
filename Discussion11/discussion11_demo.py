import numpy as np
from astropy.io import fits
from astropy.io import ascii
import astropy.units as u

data = ascii.read('autoread_table.txt')
data['a (AU)'].unit = u.AU
print(data)