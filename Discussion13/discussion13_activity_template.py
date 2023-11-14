import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from scipy import optimize
from scipy import interpolate
from astropy.modeling.functional_models import AiryDisk2D

def model(pars, xpts):
	''' This is a Gaussian with an arbitrary peak height '''
	return pars[0]*np.exp(-(xpts-pars[1])**2/(2*pars[2])**2)

if __name__ == '__main__':
	xpts = np.linspace(-2,2,1000)
	### What if we want a sub-portion of a complicated model?
	complicated_model = model([8., 0., 0.2], xpts)+model([3., -1., 0.5], xpts)+model([2., 4, 3], xpts)
	plt.plot(xpts, complicated_model)
	plt.show()

	### Compare interpolation and direct evaluation
	### What happens when we change k?
	### Use datetime.now() to time a) making the interpolating spline
	### b) evaluating the spline and c) evaluating the function 
	### directly. How do these compare?
	spl = interpolate.make_interp_spline(xpts,complicated_model,k=1)
	ival = spl(0)
	print('Interpolated value:', ival)
	true_val = model([8., 0., 0.2], 0)+model([3., -1., 0.5],0)+model([2., 4, 3], 0)
	print('True value:', true_val)
	print('Fractional difference:', np.abs(true_val-ival)/true_val)
	### Note that for large arrays, a numpy-only model may be faster than
	### using interpolation. This is not generally true for more complicated
	### (and realistic) models


	### Write a function that uses a root finder to solve Kepler's equation,
	### M = E - e*sin(E) for E. Print some demo output


	### Let's do a model fit. Start by adding some noise to the complicated model
	data = complicated_model+np.random.normal(scale=0.8,size=xpts.size)
	### Let's also say we know what the typical errors are (since we do)
	sigs = 0.8*np.ones(xpts.size)
	### We already have a model function. Write the residual function and 
	### perform the fit. Print the result


	### We also want to know the errors in the fit parameters. Use the 
	### returned Jacobian to estimate the errors for the fit parameters.
	### Do any parameters show significant covariance?
	### Recall that the covariance matrix is (J.T dot J)^-1, or 
	### (-H)^-1


	### Let's consider a 2-D model, such as fitting to a stellar PSF
	### Make the grids
	xx, yy = np.meshgrid(np.arange(512),np.arange(512))
	true_model = AiryDisk2D(amplitude=100, x_0=124.3, y_0=417.8, radius=1.6)
	clean_data = true_model(xx, yy)
	print(clean_data.shape)
	noise = np.random.normal(scale=np.sqrt(clean_data.flatten()), size=512**2).reshape((512,512)) 
	noisy_data = clean_data + noise

	plt.imshow(noisy_data, origin='lower')
	plt.show()

	### Write the residual function to fit a model to this data. Make it possible to 
	### easily switch between an Airy and a 2D Gaussian model



