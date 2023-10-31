import numpy as np 
import matplotlib.pyplot as plt


def example_2D(x, y):
	return (np.sin(x)+np.cos(5*y)) * np.exp(-np.sqrt(x**2+y**2))

### Make a figure plotting example 2D on some (sensible) bounds
### Make sure the x/y labels are right. Consider playing with 
### different color maps as well. Paste a screenshot into the 
### slides



### Now lets do some histograms. First let's make some fake data
x1 = np.random.normal(loc=2,scale=3,size=20)
x2 = np.random.normal(loc=4, scale=0.5,size=20)

### Make a histogram of x1 or x2. Overplot the true distribution
### and the distribution you recover from the samples. Try changing
### the number of samples and see the impact on how well the true
### distribution is recovered. Paste a screenshot into the slides



### If you have more time, start the homework, or try making a 
### 2D histogram with x1 and x2. Try adding extra axes with the
### 1D histograms, and overlay the recovered/true distributions
### on the histograms (similar to what corner does)


