from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors

### Load the file and print basic info
hdulst = fits.open('nspec211121_0140.fits')

print(hdulst.info())

# assert 1==0

### get data and header
hdr = hdulst[0].header
data = hdulst[0].data
print('Header:', hdr)
print('Header target keyword, hdr[\'targname\']:', hdr['targname'])
print('Data:', data)

# assert 1==0

# fig = plt.figure(figsize=(12,10))
# ### Add axes, 1 inch border, square
# ax = fig.add_axes([1/12., 1/10., 0.8*10/12, 0.8])
# ax.imshow(data, origin='lower')

# plt.show()
# assert 1==0

### That colormap is terrible, lets change the map and switch to log scale
fig = plt.figure(figsize=(12,10))
ax = fig.add_axes([1/12., 1/10., 0.8*10/12, 0.8])
### Log norm, min 1, max 1000, grayscale
cnorm = colors.LogNorm(vmin=1,vmax=1e3)
cmap = 'gray'
### Save the returned AxesImage object for the colorbar
im = ax.imshow(data, origin='lower', norm=cnorm, cmap=cmap)
# plt.show()

### Now lets add a colorbar with the same scale
### We're adding an axes to a figure, so we do that in figure coordinates
cax = fig.add_axes([1/12.+0.8*10/12+0.01, 1/10., 1/12., 0.8])
cbar = fig.colorbar(mappable=im, cax=cax)
### Change the font size of the labels
cbar.ax.tick_params(labelsize=14)

# plt.show()
# assert 1==0


### Now lets add some annotations
### start with a patch around some telluric features
from matplotlib.patches import Rectangle
### Note that this takes values in data coordinates!
### This is good if we want to put a box over a certain part of the data,
### but an issue if we want e.g. things to stay in the same place when we
### change the range!
patch = ax.add_patch(Rectangle(xy=(50,150), width=500, height=1800, color='r', alpha=0.2,label='Telluric contamination'))
ax.legend(loc='upper right', frameon=False, fontsize=14)

# plt.show()
# assert 1==0

### We can switch ebtween the axes and data coordinates easily
ax.text(0.5,1.02, 'Do this if set_title placement is bad!', horizontalalignment='center', va='center', transform=ax.transAxes, fontsize=18, weight='bold', color='b')
### But if I want to label part of the data, do that in data coordinates
ax.text(1550, 220, 'This looks like\na cosmic ray!', fontsize=14,color='r')

plt.show()