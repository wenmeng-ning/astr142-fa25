'''
This is a demo on working with fits file.
Discussion08 topics outline:
- hdu lists and hdu objects
- accessing info, data and headers
- creating files
'''

from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
from datetime import datetime

# --------------------------------------------
# open and access info 
# --------------------------------------------
file = "m77_jwst.fits"

with fits.open(file) as hdul:
    print(hdul.info())

# --------------------------------------------
# get data and header
# --------------------------------------------
hdr = fits.getheader(file, ext=('SCI', 1))
print(list(hdr.keys()))

dat = fits.getdata(file, ext=('SCI', 1))

plt.imshow(dat, origin='lower', norm=LogNorm())
plt.show()

# --------------------------------------------
# create file
# --------------------------------------------

# example 1 - quick data save
x, y = np.meshgrid(np.linspace(-1,1,512), np.linspace(-1,1,512))
sig = 0.2
A = 1/(2*np.pi*sig**2)
image = np.exp(-(x**2+y**2)/(2*sig**2))

# write data to file
fits.writeto('gaussian.fits', image, overwrite=True)

plt.imshow(image, origin='lower')
plt.show()


# example 2 - save hdulists of hdu objects with data and header
# Create coordinate grid centered at (0,0)
width, height = 512, 512
x = np.linspace(-1, 1, width)
y = np.linspace(-1, 1, height)
X, Y = np.meshgrid(x, y)

# Convert to polar coordinates
R = np.sqrt(X**2 + Y**2)
Theta = np.arctan2(Y, X)

# Define value of z
Z = np.sin(2 * np.pi * R +  Theta)
Z_normalized = ((Z - Z.min()) / (Z.max() - Z.min())) # normalize z
# Display the pattern
plt.imshow(Z_normalized, cmap='gray', origin='lower')
plt.title('Polar Interference Pattern')
plt.axis('off')
plt.show()

# Create a Primary HDU (Header/Data Unit)
hdu = fits.PrimaryHDU(Z_normalized)

# Add header information
hdr = hdu.header
hdr['DATE'] = datetime.utcnow().strftime('%Y-%m-%d')
hdr['FUNCTION'] = 'sin(2*pi*sqrt(x^2 + y^2) + atan2(y,x))'
hdr['COMMENT'] = "discussion08_example"

# Create HDUList and write to file
hdul = fits.HDUList([hdu])
hdul.writeto('discussion08_example.fits', overwrite=True)
