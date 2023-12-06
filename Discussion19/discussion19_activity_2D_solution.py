import numpy as np
import matplotlib.pyplot as plt
from numba import jit
import sys

@jit(nopython=True)
def update_temps(temps,nx):
	newtemps = np.copy(temps)
	for x in range(1, nx-1):
		for y in range(1,nx-1):
			newtemps[y,x] = (1-4*r*diff)*temps[y,x] + r*diff*(temps[y,x-1]+temps[y,x+1] +temps[y-1,x]+temps[y+1,x] )
	return newtemps

if __name__ == '__main__':
	### Here's a 2d example

	nt = 5000
	nx = 20
	tpts = np.linspace(0,1,num=nt)
	dt = tpts[1]-tpts[0]
	xpts = np.linspace(0,1., num=nx)
	dx = xpts[1] - xpts[0]

	r = dt/dx**2
	diff = 1.16
	### Note that stability requirement is stricter in 2D
	print(diff*r)

	### Make temperature grid with inital conditions
	temps = 273*np.ones((nx,nx))
	temps[:,-1] = 77.
	newtemps = np.copy(temps)

	plt.imshow(temps)
	plt.show()
	### Let's animate this
	plt.ion()
	plt.plot(xpts, temps)
	### Loop through times and update
	t=0
	while t < 200:
		newtemps = update_temps(temps, nx)
		txt = 'Delta: ' + str(np.round(np.sum(np.abs(temps-newtemps)),3))
		sys.stdout.write(txt+'\r')
		sys.stdout.flush()
		temps = np.copy(newtemps)
		t+=dt

		plt.imshow(temps,origin='lower')
		# plt.ylim(bottom=50,top=300)
		plt.title('Time = '+ str(np.round(t,3)))
		plt.draw()
		plt.pause(0.0001)
		plt.clf()