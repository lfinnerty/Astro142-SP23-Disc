import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate 
from astropy.modeling.functional_models import Gaussian1D, Lorentz1D


mfunc = Gaussian1D(amplitude=1,mean=0,stddev=1)
### We know analytically that the integral should be 2*sqrt(pi)
### Note the 2 is from how astropy parameterizes the Gaussian
print('Expect:', np.sqrt(2*np.pi))

### Let's evaluate the model at some sampled points
xpts = np.linspace(-8,8,num=400)
model = mfunc(xpts)

plt.plot(xpts,model)
plt.show()

### Say we want to integrate over an observed spectralq line
### to get the total line flux
i1 = integrate.simpson(model,xpts)
print('Simpson:',i1)
i2 = integrate.trapezoid(model,xpts)
print('Trapezoid:',i2)


### Alternatively, let's use the function - say we have
### a function with a painful integral that we need to evaluate
result = integrate.quad(mfunc,-8,8)
print('Quad:', result[0])
result2 = integrate.romberg(mfunc,-8,8)
print('Romberg:', result2)

### What if we want to solve an IVP? Consider a damped 
### harmonic oscillator: x'' + 2*b*w*x' + w**2 x = 0
### Set y1 = x, y2 = x', so that y1' = y2 and we can 
### write a system: 
### y1' = y2
### y2' = -2*b*w*y2 - w**2 * y1
### And say we start at rest, x' = y2 = 0 and position
### x = y1 = 1

def func(t,y, b, w, a):
	''' This returns a tuple, each entry of which
	is one of our equations'''
	return (y[1], -2*b*w*y[1] - w**2 * y[0] + a*np.sin(t/w))

### Takes a callable, timespan, and initial values. Args 
### keyword takes extra arguments
soln = integrate.solve_ivp(func, (0,100),(1,0),args=(0.05,1., 0.),t_eval=np.linspace(0,100,1000))

plt.plot(soln.t, soln.y[0])
plt.xlabel('Time')
plt.ylabel('Position')
plt.show()

plt.plot(soln.t, soln.y[1])
plt.xlabel('Time')
plt.ylabel('Velocity')
plt.show()