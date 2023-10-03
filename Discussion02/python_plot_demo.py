### Imports
import numpy as np
import matplotlib.pyplot as plt

### Define functions
def make_plot(arr1, arr2, show=False):
	''' Plots arr2 against arr1

	Arguments:
	arr1 - np.ndarray of x-values
	arr2 - np.ndarray of y-values

	Keyword arguments:
	show - bool, whether to show the plot. Default False

	Returns: plt.figure of the plot
	'''
	### Make the plot
	fig = plt.figure()
	plt.plot(arr1,arr2, color='k')
	### Set axis limits
	plt.xlim(left=np.min(arr1), right=np.max(arr1))
	plt.ylim(bottom=np.min(arr2),top=np.max(arr2))
	### Make labels
	plt.xlabel('X value')
	plt.ylabel('Y value')
	### Show the plot if asked
	if show:
		plt.show()

	return fig


if __name__ == '__main__':
	### This separates code that's run when the script is invoked from
	### function definitions. Code above here will be run when this 
	### file is imported by another python file. Code below this statement
	### will only run if this file is main (i.e. the file being executed)

	xvals = np.linspace(1,100,num=1000)
	yvals = 3*xvals**2 + 4

	### This will show the plot
	make_plot(xvals, yvals, show=True)

	### This will save the figure, which we can then show or modify
	### further
	fig = make_plot(xvals, yvals, show=False)
	### Save the demo plot
	plt.savefig('demo_plot.pdf',bbox_inches='tight')
	plt.show()