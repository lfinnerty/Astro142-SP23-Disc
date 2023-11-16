import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize

def gaussian(pars,x):
	a, mu, sig = pars
	return a*np.exp(-0.5*(x-mu)**2/sig**2)

def n_gauss_model(pars, x, n=5):
	model = np.zeros(x.size)
	for i in range(3,3*n+1,3):
		model+=gaussian(pars[i-3:i],x)
	return model

def residual(pars, x, data, errs, n):
	return (data-n_gauss_model(pars,x,n))/errs


### Consider an overlapping set of spectral lines
wvarr = np.linspace(2.08,2.22,num=600)
### Note the noise will be different every time you run the script,
### since we didn' set the random seed. Should that change the outcome?
spec = gaussian([10,2.15,0.001],wvarr)+gaussian([3,2.12,0.01],wvarr)+gaussian([7,2.17,0.005],wvarr)+gaussian([2,2.155,0.02],wvarr)+gaussian([2,2.18,0.01],wvarr)
spec = spec+np.random.normal(scale=1.0,size=spec.size)
errs = np.ones(spec.size)
plt.plot(wvarr,spec)
plt.show()

### Let's say we know there are five lines in the spectrum. There's a 
### model and residual function above. Let's try a least squares fit
x0 = [9,2.14,0.002,4,2.13,0.005,6,2.175,0.004,2.2,2.15,0.04,1.0,2.17,0.02]
result = optimize.least_squares(residual,x0=x0,args=(wvarr,spec,errs,5),max_nfev=1e4)
print(result)
print(result.x)
plt.plot(wvarr,spec)
plt.plot(wvarr, n_gauss_model(result.x,wvarr,n=5))
plt.show()

### That didn't go so great, even though we started close and I increased 
### the maximum iterations! What happens if you change x0?
