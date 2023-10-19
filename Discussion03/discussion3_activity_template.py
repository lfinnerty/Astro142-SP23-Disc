import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt
#make change here discussion
def make_change():
    x = 1+2
    return x

def linear_residual(pars, xpts, ypts):
	model = pars[0] + pars[1]*xpts
	return np.sum((ypts-model)**2)

class PolynomialModel():
	pass

class Fitter():
	pass


if __name__ == '__main__':
	### Set the random seed so we get the same random numbers every time
	np.random.seed(42)
	true_pars = [-0.5, 10, 0.1]
	
	### Make the data
	xpts = np.arange(0,101)
	ypts = true_pars[0] + true_pars[1]*xpts + true_pars[2]*xpts**2
	
	### Add noise, +/- 20% error on points
	ypts = np.random.normal(loc=ypts,scale=0.2*np.abs(ypts))

	### Lets do some fitting
	### Make initial guess
	p0 = [0, 1.]
	res = minimize(linear_residual, p0, args=(xpts,ypts))
	print(res.x)
	best_fit = res.x[0] + res.x[1]*xpts 


	plt.scatter(xpts, ypts,color='k', label='Data')
	plt.plot(xpts, best_fit, color='r', label='Linear fit')
	plt.legend()
	plt.show()

	### Try fitting a quadratic instead. Does the current residual
	### function seem like the best way to do this?


	### Try making a class for the model and fitter. What is the advantage
	### of setting it up this way?
