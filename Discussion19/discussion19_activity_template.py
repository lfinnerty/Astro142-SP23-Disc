import numpy as np
import matplotlib.pyplot as plt
from numba import jit
import sys

if __name__ == '__main__':
	### Consider the diffusion equation, partial x/partial t = d*laplace x.
	### Let's say we have a 273 K rod tha we're going to use as a 
	### thermal conductor to get heat out of a 70 K cryogenic dewar.
	### The thermal diffusivity of copper is 1.16. Let's start with
	### 1D

	nt = 1000
	nx = 20
	tpts = np.linspace(0,100,num=nt)
	dt = tpts[1]-tpts[0]
	xpts = np.linspace(0,20., num=nx)
	dx = xpts[1] - xpts[0]

	diff = 1.16
	### Note that there's as stability requirement for the explicit finite differences
	### solution, diff * dt/dx**2 < 0.5. I'd print it here to be sure. What happens if 
	### we're above the stability threshold?
	print(diff*dt/dx**2)

	### Make temperature grid with inital conditions
	temps = 273*np.ones(nx)
	temps[-1] = 77.
	newtemps = np.copy(temps)

	plt.plot(temps)
	plt.show()
	### Let's animate this
	plt.ion()
	plt.plot(xpts, temps)

	### Loop through times and update
	t=0
	while t < 200:
		### FIXME updating temps goes here!


		plt.imshow(temps,origin='lower')
		plt.ylim(bottom=50,top=300)
		plt.title('Time = '+ str(np.round(t,3)))
		plt.draw()
		plt.pause(0.0001)
		plt.clf()