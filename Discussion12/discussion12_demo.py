from astropy.visualization import quantity_support
import numpy as np
import astropy.units as u
import matplotlib.pyplot as plt
from astropy.io import fits
from astropy.wcs import WCS

times = np.arange(100)*u.s
arr1 = np.arange(100)*u.m
arr2 = 0.5*np.arange(100)*u.cm

with quantity_support():
	plt.plot(times,arr1)
	plt.plot(times,arr2)
	plt.show()

### Now that we're outside the quantity_support
### context, we'll get the default behavior 
### again
plt.plot(times,arr1)
plt.plot(times,arr2)
plt.show()



### Lets load a file and plot it with WCS
hdulst = fits.open('gc_2mass_k.fits')
data = hdulst[0].data
hdr = hdulst[0].header
wcs = WCS(hdr)
ax = plt.subplot(projection=wcs)
plt.imshow(data,origin='lower')
plt.grid(color='white',ls='solid')
plt.xlabel('RA')
plt.ylabel('Dec')
# plt.show()

### Lets overlay a different projection
overlay = ax.get_coords_overlay('galactic')
overlay.grid(color='white', ls='dotted')
overlay[0].set_axislabel('Galactic latitude')
overlay[1].set_axislabel('Galactic longitude')
plt.show()