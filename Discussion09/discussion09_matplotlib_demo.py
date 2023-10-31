import numpy as np 
import matplotlib.pyplot as plt
import time

### Lets make a figure
fig = plt.figure(figsize=(8,6))
### This is how the "active" figure is tracked for the plt interface
print(fig.number)
### add an axes. 4-tuple specifies (fractional) left, bottom, width, height values
### This should make an axes instance with a 10% border
ax = fig.add_axes([0.1,0.1,0.8,0.8])

### Now lets plot something on that axis
x = np.linspace(0,2*np.pi,200)
y = np.sin(x)
ax.plot(x,y)
### Just use the pyplot interface to show
plt.show()

### Now lets adjust the limits
ax.set_xlim(left=np.min(x),right=np.max(x))
ax.set_ylim(bottom=np.min(y),top=np.max(y))
ax.set_title('This is a sinusoid')
### Lets change what the axes ticks say
labels = [str(i)+' rad' for i in range(int(np.max(x)+1))]
ax.set_xticks(np.arange(int(np.max(x))+1), labels=labels)
plt.show()

### Lets add another plot along the right side
ax2 = fig.add_axes([0.9,0.1,0.1,0.8])
### And lets plot something
ax2.scatter(x, y, s=5,color='k')
ax2.set_title('This is another plot')
plt.show()

### Lets turn the y axis off
ax2.get_yaxis().set_visible(False)
plt.show()
# plt.close()

### Subplots is a somewhat easier way to do this, if 
### the plots are equal
fig, axs = plt.subplots(nrows=2,ncols=1,figsize=(10,5),sharex=True)
axs[0].plot(x,y)
plt.show()

### Can also use interactive mode - need to make a new figure
### There's an actual animation interface in matplotlib,
### but this works for quick things
# plt.ion()
# fig, axs = plt.subplots(nrows=2,ncols=1,figsize=(10,5),sharex=True)
# axs[0].set_xlim(left=0,right=2*np.pi)
# for i in range(x.size):
# 	axs[0].scatter(x[:i],y[:i],color='r')
# 	axs[1].plot(x[:i],y[:i], color='k')
# 	plt.draw()
# 	plt.pause(0.5)
