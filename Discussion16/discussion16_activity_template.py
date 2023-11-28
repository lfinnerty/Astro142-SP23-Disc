import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import median_abs_deviation

if __name__ == '__main__':
	orders = [6,7,8]

	for order in orders:
		### Load each order of data
		### Does this need to be a loop or could we use a pool? What might we want
		### to separate out if we use a pool?
		data = np.load('WASP33_nov21_rereduced_fluxes_coadded_order_'+str(order)+'.npy')
		plt.imshow(data,aspect=15,vmin=0,vmax=1e4)
		plt.show()
		### Scale each exposure to a consistent median
		for i in range(data.shape[0]):
			data[i] = data[i]/np.nanmedian(data[i])
		### Now we want to make the median over the time series (y-axis)
		### note that there is a much better way to do this (what is it?)
		medspec = np.ones(data.shape[1])
		for j in range(data.shape[1]):
			medspec[j] = np.nanmedian(data[:,j])
		### Now devide each spectrum in the time series by its median
		for i in range(data.shape[0]):
			data[i] = data[i]/medspec
		### And let's mask outliers
		threshold = 6*median_abs_deviation(data.flatten())
		### There's a MUCH beter way to do this. Hint: array indexing
		for i in range(data.shape[0]):
			for j in range(data.shape[1]):
				if np.abs(data[i,j]-1) > threshold:
					data[i,j] = np.nan


		plt.imshow(data,aspect=15,vmin=0.95,vmax=1.05)
		plt.show()

