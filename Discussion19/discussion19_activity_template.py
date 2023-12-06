import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
	### Consider the diffusion equation, partial x/partial t = d*laplace x.
	### Let's say we have a 273 K rod tha we're going to use as a 
	### thermal conductor to get heat out of a 70 K cryogenic dewar.
	### The thermal diffusivity of copper is 1.16. Let's start with
	### 1D

	tpts = np.linspace(0,100,num=10000)
	xpts = np.linspace(0,20., num=200)

	