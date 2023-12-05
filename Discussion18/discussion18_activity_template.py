import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate 
from astropy.modeling.functional_models import Gaussian1D, Lorentz1D

### For a Gaussian profile, the integrated flux is related to 
### the standard deviation and the line amplitude. Find the
### constant of proportionality in this relationship



### Often, we only have a few pixels covering a full spectral line.
### How many pixels do we need across the entire line for integrating
### the sampled function to be a good match for the true function?
### Does this change if we shift the line center by a fraction of 
### a pixel?
### If we add noise to the sampled line, how does that change the
### reliability of the integrated flux?


### The radiative transfer equation describes how light 
### propegates through a medium:
### dI_nu/ds = j_nu - a_nu * I_nu
### Consider:
def jnu(nu, amp, mean, std):
	mod = Gaussian1D(amplitude=amp, mean=mean, stddev=std)
	return mod(nu)

nus = np.linspace(0,1,30)
jnus = jnu(nus, 10, 0.5,0.08)
plt.plot(nus, jnus)
plt.xlabel('Frequency')
plt.ylabel('Emissivity')
plt.show()


### Solve the radiative transfer equation at each frequency. Set the 
### limits of s to 0 and 1, and make sure it's well sampled. Set I_nu(0) = 1, and 
### use a constant a_nu
### Plot I_nu at s = 0 and s = 1. What happened? What happens if you change
### a_nu? I_nu(0)? 

def func(t, I, j, a):
	return j - a*I

soln = integrate.solve_ivp(func, (0,1),1*np.ones(jnus.size),args=(jnus, 0.5),t_eval=np.linspace(0,1,100))
print(soln.y.shape)
plt.plot(soln.t, soln.y[15])
plt.show()

plt.plot(nus, soln.y[:,-1])
plt.plot(nus, soln.y[:,0])
plt.show()