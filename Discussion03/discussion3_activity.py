import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt

def calc_residual(pars, modelfunc, xpts, data):
	''' Modelfunc is a callable (function) that takes xpts and makes the model '''
	model = modelfunc(pars,xpts)
	return np.sum((model-data)**2)

def linear_model(pars, xpts):
	return pars[0] + pars[1]*xpts

def quadratic_model(pars,xpts):
	return pars[0]+ pars[1]*xpts + pars[2]*xpts**2

class PolynomialModel():
	def __init__(self, degree, xpts):
		self.degree = degree
		self.xpts = xpts
		self.modpts = np.zeros(self.xpts.size)

	def calc_model(self, coeffs):
		### Re-initialize modpts if already calculated
		if np.sum(np.abs(self.modpts) > 0):
			self.modpts = np.zeros(self.xpts.size)
		### Doing this as a loop lets us handle an arbitrary degree polynomial
		for i in range(self.degree+1):
			self.modpts += coeffs[i]*self.xpts**i

	def get_model(self):
		return self.modpts


class Fitter():
	def __init__(self, xpts, ypts):
		self.xpts = xpts
		self.ypts = ypts
		### Not filling this in yet, but instantiating it
		### for clarity 
		self.coeffs = None

	def calc_residual(self, pars, modelobj):
		### Calculate the ypts using the model object
		modelobj.calc_model(pars)
		model = modelobj.get_model()
		return np.sum((model-self.ypts)**2)

	def fit(self, model):
		### Initial guess is all zeros
		### Check that model and data have same xpts
		### Or maybe change the model class so you don't have 
		### to worry about this
		self.coeffs = np.empty(model.degree+1)
		if np.sum(np.abs(model.xpts-self.xpts) > 1e-14):
			raise InputError('Model x points do not match data!')
		p0 = np.zeros(model.degree+1)
		res = minimize(self.calc_residual, p0, args=(model,))
		self.coeffs = res.x

	def get_best_model(self):
		bestmod_obj = PolynomialModel(self.coeffs.size-1, self.xpts)
		bestmod_obj.calc_model(self.coeffs)
		return bestmod_obj.get_model()



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
	res = minimize(calc_residual, p0, args=(linear_model, xpts, ypts))
	print(res.x)
	best_fit = linear_model(res.x, xpts)

	### Now do quadratic
	p0 = [0, 1., 0.1]
	res2 = minimize(calc_residual, p0, args=(quadratic_model, xpts, ypts))
	print(res2.x)
	best_fit_quad = quadratic_model(res2.x, xpts)


	plt.scatter(xpts, ypts,color='k', label='Data')
	plt.plot(xpts, best_fit, color='r', label='Linear fit')
	plt.plot(xpts, best_fit_quad, color='g', label='Quadratic fit')
	plt.legend()
	plt.show()


	### Make one fitter object
	fitobj = Fitter(xpts, ypts)
	### Now make a model, fit it, and get the best-fit
	linear = PolynomialModel(1,xpts)
	fitobj.fit(linear)
	linear_best = fitobj.get_best_model()

	### Now can just make a new model and refit
	quadratic = PolynomialModel(2, xpts)
	fitobj.fit(quadratic)
	quad_best = fitobj.get_best_model()

	### And again, now with a cubic
	cubic = PolynomialModel(3,xpts)
	fitobj.fit(cubic)
	cubic_best = fitobj.get_best_model()


	plt.scatter(xpts, ypts,color='k', label='Data')
	plt.plot(xpts, linear_best, color='r', label='Linear fit')
	plt.plot(xpts, quad_best, color='g', label='Quadratic fit')
	plt.plot(xpts, cubic_best, color='b', label='Cubic fit')
	plt.legend()
	plt.show()