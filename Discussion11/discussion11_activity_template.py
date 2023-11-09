import numpy as np
from astropy.io import fits


### Auto load table
### Load and print autoread_table.txt. Notice that the 
### column heads include units, but the loaded file doesn't use
### the astropy unit system. Add the units to the columns that
### need them, then print the table again

### Manual load table
### manualread_table.txt has the same information as the previous
### file, but also some extra header info that will need to be skipped
### when reading. While you're at it, at load time, change the column
### names to not have units, and add astropy units. Also make sure 
### that the eccentric column is saved as a boolean, rather than
### a string. Save this new table. 



### Load the NGC7469 spectrum. The flux and wavelength
### are in separate FITS extensions. The wavelength is in
### micron, and the flux in Jy (check the headers). 
### Convert the flux to erg/cm^2/s/Hz and plot it.
### See here for an example of converting flux units:
### https://docs.astropy.org/en/stable/units/equivalencies.html



### Load the one of the nspec FITS file in the folder
### The header contains an MJD timestamp. Convert this to
### UTC and print it.


### The RA/Dec are stored in sexagesimal. Convert these to
### decimal and print


### Write a function that will take a list of filenames and 
### return a table of the UT time and decimal RA/Dec. Use
### this function on the files in the discussion folder and
### print the table. Can you use a list comprehension to 
### make the filenames?


### Paste a screenshot of your termianl output into the slides
### and upload the PDF