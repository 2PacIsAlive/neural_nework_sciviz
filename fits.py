#!usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
#import fitsio

from astropy.io import fits
		
filename = 'table2.fits'
#data     = fitsio.read(filename)

#fits = fitsio.FITS(filename)

#hdu_list = fits.open(filename)

#print fits[0][:]

#print hdu_list.info()

image_data = fits.getdata(filename)
print image_data.shape
plt.imshow(image_data, cmap='gray')
plt.colorbar()

