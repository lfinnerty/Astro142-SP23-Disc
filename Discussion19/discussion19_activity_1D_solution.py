import numpy as np
import matplotlib.pyplot as plt

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

	r = dt/dx**2
	diff = 1.16
	print(r*diff)

	### Make temperature grid with inital conditions
	temps = 273*np.ones(nx)
	temps[-1] = 77.
	newtemps = np.copy(temps)

	### Let's animate this
	plt.ion()
	plt.plot(xpts, temps)
	### Loop through times and update
	t = 0
	while t < 120:
		for x in range(1, nx-1):
			newtemps[x] = (1-2*r*diff)*temps[x] + r*diff*(temps[x-1]+temps[x+1])
		temps = np.copy(newtemps)
		t+=dt

		plt.plot(xpts, temps)
		plt.ylim(bottom=50,top=300)
		plt.title('Time = '+ str(np.round(t,3)))
		plt.draw()
		plt.pause(0.001)
		plt.clf()