import numpy as np 
import matplotlib.pyplot as plt
import time

### Lets make a figure
samples = np.random.normal(loc=0,scale=1.0,size=2000)

fig, ax = plt.subplots(nrows=1,ncols=1,figsize=(8,8))
ax.hist(samples,bins=20,range=(-4,4))
ax.set_xlabel('Value')
ax.set_ylabel('Number of samples',fontsize=18)
plt.show()