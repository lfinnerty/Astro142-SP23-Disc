import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
### Make a noisy time series 
times = np.linspace(1,100,1000)
fluxes = np.random.normal(loc=3*np.sin(2*np.pi*times/3.2),scale=1.0)

plt.plot(times,fluxes)
plt.xlabel('Time')
plt.ylabel('Flux')
plt.show()

### It seems dangerous to have two variables - if we change the order of
### fluxes but not times (or delete an element, etc), then the points
### won't match. Make a structured array to contain times and fluxes



### Define a function that takes this strucutred array and plots
### the time series


### This data is sinusoidal, so we can use the fourier transform
### to find the frequency. For example:
### If you don't know what a fourier transform is, go to
### https://numpy.org/doc/stable/reference/routines.fft.html 
### and skim the background information section
power = np.fft.fft(fluxes)
freqs = np.fft.fftfreq(times.size, times[1]-times[0])
print(power.dtype)
plt.plot(freqs, power.real, label='Real component')
plt.plot(freqs, power.imag, label='Imaginary component')
plt.axvline(1/3.2, color='r', linestyle='--', label='True frequency')
plt.xlabel('Frequency')
plt.ylabel('Power')
plt.legend()
plt.show()

### Write a function that takes a structured array of 
### times and fluxes (that you defined above), and returns
### a structured array of frequency and power. Use this function
### to reproduce the above plot
### Think about how to handle the complex part of the fft return






### Now a different example. 
### Making/using a boolean array as a mask
### 