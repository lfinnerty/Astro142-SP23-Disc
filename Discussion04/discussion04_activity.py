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


### Alternatively, use np.stack to make a 2D array with times in 
### one column and fluxes in the other. What is are the advantages/
### disadvangages of this vs making a dtype? When would you do 
### one or the other?



### This data is sinusoidal, so we can use the fourier transform
### to find the frequency. For example:
### If you don't know what a fourier transform is, go to
### https://numpy.org/doc/stable/reference/routines.fft.html 
### and skim the background information section
power = np.fft.fft(fluxes)
freqs = np.fft.fftfreq(times.size, times[1]-times[0])
print(power.dtype) ### Note that this is complex, not float!
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






### Often, astronomical data has outliers that need to be cleaned
### numpy arrays make this easy. First, lets make a data array
### with a bad value
arr = np.asarray([10,24,12,0,3,14,7,np.nan,10,12,15,16])
### np.isnan returns an array that's true if the array is nan,
### false otherwise
print('Is arr NaN?', np.isnan(arr))
### We can use this to get an array without nan. Note that ~
### is the python negation operator
clean_arr = arr[~np.isnan(arr)]
print('NaNs removed:', clean_arr)
### Alternatively, we could set NaNs to some filler value
arr[np.isnan(arr)] = 0
print('NaNs set to 0:', arr)
### You can do this kind of indexing with ANY boolean array
### for instance:
arr[arr<10] = np.nan ### set all values < 10 to nan
arr[arr>12] = 20. ### set all values > 12 to 20
print('Set a bunch of values:', arr)


### This is a spectrum that contains some NaN values.
### Use np.interp to replace the NaNs using linear
### interpolation
wave = np.load('WASP33_nov21_wvsol.npy')[5]
fluxes = np.load('WASP33_nov21_rereduced_fluxes_coadded_order_5.npy')
print('Flux array shape:', fluxes.shape)
### This is actually a 2D array (it's a spectral time series)
### Show the image to see the missing values
### Note that python puts 0 at the top of the plot! How can
### you fix this?
plt.imshow(fluxes,aspect=25)
plt.xlabel('Pixel')
plt.ylabel('Frame number')
plt.show()

### We don't trust the NaN values, but leaving them in will mess up
### other steps in the data processing. Use linear interpolation to
### replace the NaNs, but keep track of where they were replaced
### so we can drop those points later.


### Make a plot of the NaN-removed array


### Print the indexes of the replaced NaNs