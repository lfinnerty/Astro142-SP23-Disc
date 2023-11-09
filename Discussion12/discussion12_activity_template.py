### You'll probably want to import some things, do that before funciton
### definitions

### function definitions at top!!!

if __name__ == '__main__':
	### There's a FITS file with WCS information in this folder. Load the file and 
	### make a plot, with axes in equatorial coodinates. Overlay a galactic 
	### coordinate gird on the plot


	### Here's some names in a target list
	tgtnames = ['HD 189733', 'HD 209458', 'HD 149026', 'WASP-33', 'KELT-9', 'TOI-1518']

	### Write a function that takes a target Kmag and exposure time and 
	### estimates the SNR of a Keck/NIRSPEC seeing-limited observation
	### in the Kband-new filter. Define your functions outside of main!! (why?)

	### Query Simbad for the Kband magnitudes of the listed targets.
	### Use your function to print the SNR in a 300s exposure for each target

