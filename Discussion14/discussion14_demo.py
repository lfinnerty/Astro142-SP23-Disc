import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize

framesize = 2048
xpts = np.arange(2048)
obs = 1 + 0.15*np.sin(2*np.pi*xpts/15.) + np.random.normal(scale=0.05, size=framesize)
sigs = 0.05*np.ones(framesize)
plt.plot(obs)
plt.show()

### Make the model and residual functions
def fringe_model(pars, xpts):
  amp = pars[0]
  freq = pars[1]
  return 1 + amp*np.sin(2*np.pi*xpts/freq)

def residual(pars, xpts, obs, errs):
  return (obs - fringe_model(pars,xpts))/errs

def logl(pars, xpts, obs, errs):
  return np.log(np.sqrt(np.sum(((obs - fringe_model(pars,xpts))/errs)**2)/xpts.size))


### What does our likelihood space look like?
amppts = np.linspace(0.1,0.2,300)
freqpts = np.linspace(14.5,15.5,300)
da = (amppts[1]-amppts[0]) / 2
df = (freqpts[1]-freqpts[0]) / 2
lmap = np.zeros((300,300))
for j, freq in enumerate(freqpts):
  	for i, amp in enumerate(amppts):
   		lmap[j,i] = logl((amp,freq),xpts,obs,sigs)**2
plt.imshow(lmap[::-1], extent=(amppts[0]-da,amppts[-1]+da,freqpts[0]-df,freqpts[-1]+df),aspect='auto')
plt.scatter(0.15,15,color='r')
plt.show()


### Now let's try minimizing
bounds = ((0.1,0.2),(14.5,15.5))
res1 = optimize.minimize(logl, x0 =[0.11,14.99],args=(xpts,obs,sigs), bounds=bounds, method='Powell')
print(res1)

plt.imshow(lmap[::-1], extent=(amppts[0]-da,amppts[-1]+da,freqpts[0]-df,freqpts[-1]+df),aspect='auto')
plt.scatter(0.15,15,color='r')
plt.scatter(res1.x[0], res1.x[1], color='m', label='Minimization 1')
plt.show()

print('----------------------------------------------------------')

res2 = optimize.minimize(logl, x0 =[0.14,15.2],args=(xpts,obs,sigs),bounds=bounds, method='Powell')
print(res2)

plt.imshow(lmap[::-1], extent=(amppts[0]-da,amppts[-1]+da,freqpts[0]-df,freqpts[-1]+df),aspect='auto')
plt.scatter(0.15,15,color='r')
plt.scatter(res1.x[0], res1.x[1], color='m', label='Minimization 1')
plt.scatter(res2.x[0], res2.x[1], color='k', label='Minimization 2')
plt.legend()
plt.show()



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
  sample_stds[i]  = np.std(subsample)
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
