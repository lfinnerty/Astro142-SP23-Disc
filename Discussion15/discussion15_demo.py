import numpy as np
import matplotlib.pyplot as plt


### Jacknife resampling can give us a way to check how good/bad the convergence issues are, and
### how our error estimates are. Say we've run our fits several times, getting a best-fit value
### x each time, and some error estimate from the Jacobian, sig_x. Note the last entry
x_arr = np.array([3.25, 3.12, 3.23, 3.35, 3.18, 3.21, 3.23, 3.26,3.29, 10.1 ])
sig_x_arr = np.array([0.06, 0.05, 0.03, 0.07, 0.06, 0.04, 0.06, 0.02, 0.08, 0.5])
print('Mean:', np.mean(x_arr), 'StDev:', np.std(x_arr))
### Want to know typical measurement uncertainty. Since we took more measurements, our
### uncertainty in the mean should be less than the typical measurement uncertainty
print('Mean measurement error', np.mean(sig_x_arr))
### Last point seems to be messing up statistics (note large sigma compared to each individual)
### measurement. Is there a way to quantify this?
### Let's do a leave-one-out resampling (Jackknife)
sample_means = np.empty(x_arr.size)
sample_stds = np.empty(x_arr.size)
for i in range(x_arr.size):
  subsample = x_arr[np.arange(x_arr.size)!=i]
  sample_means[i] = np.mean(subsample)
  sample_stds[i]  = np.std(subsample)s
  print('Leaving out index', i, 'Mean:', sample_means[i], 'StDev:', sample_stds[i])
### When we omit the last point, the mean and standard deviation change a lot (>10sigma)
### Ideally, omitting any one point wouldn't lead to a significant change, so this 
### strongly suggests something is wrong with the last data point

### We can also assess how good our estimate of the standard deviation is
bias = (x_arr.size-1)*(np.mean(sample_stds) - np.std(x_arr))
print('Standard deviation:', np.std(x_arr), 'Bias:', bias)

### In this case, we massively overestimated because we have an outlier. Let's leave
### that point out and try again
x_arr = x_arr[:-1]
sample_means = np.empty(x_arr.size)
sample_stds = np.empty(x_arr.size)
for i in range(x_arr.size):
  subsample = x_arr[np.arange(x_arr.size)!=i]
  sample_means[i] = np.mean(subsample)
  sample_stds[i]  = np.std(subsample)
  print('Leaving out index', i, 'Mean:', sample_means[i], 'StDev:', sample_stds[i])
bias = (x_arr.size-1)*(np.mean(sample_stds) - np.std(x_arr))
print('Standard deviation:', np.std(x_arr), 'Bias:', bias)
### Now we have a pretty good estimate of the error, though larger than we might expect
### based on the individual measurements. There's some extra scatter in the data! Maybe
### an unmeasured systematic error?
print('Mean measurement error', np.mean(sig_x_arr[:-1]))
