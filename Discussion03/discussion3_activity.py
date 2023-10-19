import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt

# Define residual fuction for linear fitting
def linear_residual(pars, xpts, ypts):
	model = pars[0] + pars[1]*xpts
	return np.sum((ypts-model)**2)
 
# Define a new residual function for quadratic fitting
def quadratic_residual(pars, xpts, ypts):
    model = pars[0] + pars[1] * xpts + pars[2] * xpts**2
    return np.sum((ypts - model)**2)


class PolynomialModel:
    def __init__(self, degree):
        self.degree = degree

    def model(self, pars, xpts):
        if self.degree == 1:
            return pars[0] + pars[1] * xpts
        elif self.degree == 2:
            return pars[0] + pars[1] * xpts + pars[2] * xpts**2
        else:
            raise ValueError("Unsupported degree")
class Fitter:
    def __init__(self, model):
        self.model = model

    def fit(self, xpts, ypts, initial_guess):
        res = minimize(self.model_residual, initial_guess, args=(xpts, ypts))
        return res.x

    def model_residual(self, pars, xpts, ypts):
        model_values = self.model.model(pars, xpts)
        return np.sum((ypts - model_values)**2)



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
    # Perform quadratic fitting
    p0_quad = [0, 1., 1.]
    res_quad = minimize(quadratic_residual, p0_quad, args=(xpts, ypts))
    print("Quadratic Fit Parameters:", res_quad.x)
    best_fit_quad = res_quad.x[0] + res_quad.x[1] * xpts + res_quad.x[2] * xpts**2

    plt.scatter(xpts, ypts, color='k', label='Data')
    plt.plot(xpts, best_fit_quad, color='b', label='Quadratic fit')
    plt.legend()
    plt.title('Quadratic Fit')
    plt.show()


	### Try making a class for the model and fitter. What is the advantage
	### of setting it up this way?



# Create a linear model instance
linear_model = PolynomialModel(degree=1)
linear_fitter = Fitter(linear_model)
linear_fit_params = linear_fitter.fit(xpts, ypts, initial_guess=[0, 1.])

# Create a quadratic model instance
quadratic_model = PolynomialModel(degree=2)
quadratic_fitter = Fitter(quadratic_model)
quadratic_fit_params = quadratic_fitter.fit(xpts, ypts, initial_guess=[0, 1., 1.])

print("Linear Fit Parameters (Class-based):", linear_fit_params)
print("Quadratic Fit Parameters (Class-based):", quadratic_fit_params)

# Plot results
best_fit_linear_class = linear_model.model(linear_fit_params, xpts)
best_fit_quad_class = quadratic_model.model(quadratic_fit_params, xpts)

plt.figure()
plt.scatter(xpts, ypts, color='k', label='Data')
plt.plot(xpts, best_fit_linear_class, color='r', label='Linear fit (Class-based)')
plt.plot(xpts, best_fit_quad_class, color='b', label='Quadratic fit (Class-based)')
plt.legend()
plt.title('Class-Based Fitting')
plt.show()
