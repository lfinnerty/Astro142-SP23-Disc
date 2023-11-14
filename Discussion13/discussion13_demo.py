import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from scipy import optimize
from scipy import interpolate

def model(pars, xpts):
	''' This is a Gaussian with an arbitrary peak height '''
	return pars[0]*np.exp(-(xpts-pars[1])**2/(2*pars[2])**2)

def lsq_residual(pars, xpts, data):
	return data-model(pars,xpts)

def chi2_residual(pars, xpts, data):
	'''This will do the same thing as least squares'''
	return np.sum((data-model(pars,xpts))**2)

def transcendental_function(x):
	''' This function has no closed-form solution! '''
	return 2*np.cos(x) + x 

if __name__ == '__main__':
	xpts = np.linspace(-2,2,1000)
	### What if we want a sub-portion of a complicated model?
	complicated_model = model([8., 0., 0.2], xpts)+model([3., -1., 0.5], xpts)+model([2., 4, 3], xpts)
	plt.plot(xpts, complicated_model)
	plt.show()

	### Compare interpolation and direct evaluation
	### What happens when we change k?
	spl = interpolate.make_interp_spline(xpts,complicated_model,k=1)
	ival = spl(0)
	print('Interpolated value:', ival)
	true_val = model([8., 0., 0.2], 0)+model([3., -1., 0.5],0)+model([2., 4, 3], 0)
	print('True value:', true_val)
	print('Fractional difference:', np.abs(true_val-ival)/true_val)



	### Now lets do some root finding. We have a function we can't 
	### find the root of analytically. Lets use root_scalar and tell
	### it we think the root is somewhere between -2 and 2
	xpts = np.linspace(-2,2,100)
	plt.plot(xpts, transcendental_function(xpts))
	plt.show()
	### So we're really trying to minimize the absolute value (or the 
	### root of the square) of the function
	root = optimize.root_scalar(transcendental_function,bracket=(-2,2))
	print(root)


	### Let's make a fake spectral line (observed at ludicrous resolution)
	### and ffit to it
	true_model = model([8., 0., 0.2], xpts)
	ypts = true_model+np.random.normal(scale=0.3,size=xpts.size)

	plt.plot(xpts,ypts)
	plt.show()

	### We can do this as a least squares problem. Need to provide a 
	### rough guess to the optimizer. Note that curve_fit wraps this up
	### a bit nicer, but requires a slightly different residual function
	result = optimize.least_squares(lsq_residual, x0=[3,1,0.5], args=(xpts,ypts))
	print(result)
	print('---------------------------------------------------------------')
	### Alternatively, can pass chi2 to minimize
	result2 = optimize.minimize(chi2_residual, x0=[3,1,0.5],args=(xpts,ypts))
	print(result2)
	### That took more evaluations of the residual function, since it 
	### didn't leverage that the problem is least squares

	plt.plot(xpts, ypts, color='k')
	plt.plot(xpts, model(result.x,xpts), label='Fit 1')
	plt.plot(xpts, model(result2.x,xpts),label='Fit 2')
	plt.legend()
	plt.show()




