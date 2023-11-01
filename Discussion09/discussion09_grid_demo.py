import numpy as np 
import matplotlib.pyplot as plt
import time

### Lets make a grid
x = np.linspace(-3,3,100)
y = np.linspace(-3,3,200)
xx, yy = np.meshgrid(x,y)
print(xx.shape)
print(xx)

### Note the axes are in index!!!
### Also note the aspect ratio
plt.imshow(xx)
plt.show()

### Should give elliptical contours
z = np.sqrt(xx**2+yy**2/4)

fig, axes = plt.subplots(nrows=1,ncols=1,figsize=(8,8))
# axes.contourf(z)
# plt.show()

### Lets get the x and y values in there
# axes.contour(xx,yy,z, levels=[1,2])
# plt.show()

### What about image data? use extent
axes.imshow(z, extent=[np.min(x),np.max(x),np.min(y),np.max(y)])
plt.show()


### Want ticks at center of pixels!
xspace = np.abs(np.diff(x))[0]/2.
yspace = np.abs(np.diff(y))[0]/2.
axes.imshow(z, extent=[np.min(x)-xspace,np.max(x)+xspace,np.min(y)-yspace,np.max(y)+yspace])
plt.show()