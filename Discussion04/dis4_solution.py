import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

# Make a noisy time series
times = np.linspace(1, 100, 1000)
fluxes = np.random.normal(loc=3 * np.sin(2 * np.pi * times / 3.2), scale=1.0)

# Plot the noisy time series
plt.plot(times, fluxes)
plt.xlabel('Time')
plt.ylabel('Flux')
plt.show()

# Create a structured array to contain times and fluxes

data = np.array( [(times[i], fluxes[i]) for i in range(len(times))], dtype=[('time', float), ('flux', float)] )

# Define a function that takes a structured array and plots the time series
def plot_time_series(data):
    plt.plot(data['time'], data['flux'])
    plt.xlabel('Time')
    plt.ylabel('Flux')
    plt.show()

# Alternatively, use np.stack to make a 2D array with times in one column and fluxes in the other.
# Advantages: Simplicity, no need to define data types.
# Disadvantages: You lose the semantic meaning of the data.
# You'd use this when you just need to manipulate the data as a whole without specific column names.
stacked_data = np.stack((times, fluxes), axis=-1)

# Perform the Fourier Transform to find the frequency
power = np.fft.fft(data['flux'])
freqs = np.fft.fftfreq(data['time'].size, data['time'][1] - data['time'][0])
print(power.dtype)  # Note that this is complex, not float!

# Write a function that takes a structured array and returns a structured array of frequency and power.
def compute_fft(data):
    power = np.fft.fft(data['flux'])
    freqs = np.fft.fftfreq(data['time'].size, data['time'][1] - data['time'][0])
    return np.array(list(zip(freqs, power)), dtype=[('frequency', float), ('power', complex)])

fft_data = compute_fft(data)

# Plot the real and imaginary components of the FFT result
plt.plot(fft_data['frequency'], fft_data['power'].real, label='Real component')
plt.plot(fft_data['frequency'], fft_data['power'].imag, label='Imaginary component')
plt.axvline(1 / 3.2, color='r', linestyle='--', label='True frequency')
plt.xlabel('Frequency')
plt.ylabel('Power')
plt.legend()
plt.show()

# Create an array with a bad value (NaN)
arr = np.asarray([10, 24, 12, 0, 3, 14, 7, np.nan, 10, 12, 15, 16])

# Check for NaN values in the array
print('Is arr NaN?', np.isnan(arr))

# Remove NaN values from the array
clean_arr = arr[~np.isnan(arr)]
print('NaNs removed:', clean_arr)

# Set NaN values to a specific filler value (e.g., 0)
arr[np.isnan(arr)] = 0
print('NaNs set to 0:', arr)

# Set values in the array based on certain conditions
arr[arr < 10] = np.nan  # Set all values < 10 to NaN
arr[arr > 12] = 20.0   # Set all values > 12 to 20.0
print('Set a bunch of values:', arr)

# Load data from files (sample file names)
wave = np.load('WASP33_nov21_wvsol.npy')[5]
fluxes = np.load('WASP33_nov21_rereduced_fluxes_coadded_order_5.npy')
print('Flux array shape:', fluxes.shape)

# Plot the 2D array (image) with NaN values
plt.imshow(fluxes, aspect=25)
plt.xlabel('Pixel')
plt.ylabel('Frame number')
plt.show()
