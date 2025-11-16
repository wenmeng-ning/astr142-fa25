'''
Here are some quick demos of plotting with matplotlib.
'''

import numpy as np
import matplotlib.pyplot as plt

# --------------------------
# create simple plots
# --------------------------

# make some data
x = np.linspace(0,2*np.pi,200)
y = np.sin(x)

# make plots using add_axes
fig = plt.figure(figsize=(8,6)) # create figure

ax = fig.add_axes([0.1,0.1,0.6,0.7]) # add axes 
ax.plot(x,y)
ax.set_xlim(left=np.min(x),right=np.max(x))
ax.set_ylim(bottom=np.min(y),top=np.max(y))
ax.set_title('sine function')
labels = [str(i)+' rad' for i in range(int(np.max(x)+1))]
ax.set_xticks(np.arange(int(np.max(x))+1), labels=labels)

ax2 = fig.add_axes([0.7,0.1,0.2,0.7]) # add another one
ax2.scatter(x, y, s=5,color='k')
ax2.get_yaxis().set_visible(False)

plt.show()


# --------------------------
# simple histogram
# -------------------------- 
samples = np.random.normal(loc=0,scale=1.0,size=2000)

fig, ax = plt.subplots(nrows=1,ncols=1,figsize=(8,6))
ax.hist(samples, bins=20, range=(-4,4), edgecolor='black')
ax.set_xlabel('Value')
ax.set_ylabel('Number of samples', fontsize=14)

plt.tight_layout()
plt.show()

# --------------------------
# histograms with log scales
# --------------------------
data = np.random.lognormal(mean=0, sigma=1, size=1000)

# Regular histogram with linear bins
fig, ax = plt.subplots(1, 2, figsize=(14, 6))

# Plot regular histogram
ax[0].hist(data, bins=50, color='tab:blue', 
           edgecolor='black')
ax[0].set_title('Linear')
ax[0].set_xlabel('Value')
ax[0].set_ylabel('Frequency')

# Plot histogram with logarithmic bins
log_bins = np.logspace(np.log10(min(data)), 
                       np.log10(max(data)), 50) 
ax[1].hist(data, bins=log_bins, color='tab:orange', 
           edgecolor='black')
ax[1].set_title('Log scaled')
ax[1].set_xlabel('Value')
ax[1].set_ylabel('Frequency')

# Set log scale for the x-axis of the second plot
ax[1].set_xscale('log')

# Display the plots
plt.tight_layout()
plt.show()


# --------------------------
# imshow and contour
# --------------------------
x = np.linspace(-5, 5, 101)
y = np.linspace(-5, 5, 101)
# full coordinate arrays
xx, yy = np.meshgrid(x, y)
zz = np.sqrt(xx**2 + yy**2)

fig, ax = plt.subplots(1, 2, figsize=(12,5))
plt.subplots_adjust(wspace=0.05)

# imshow with contour lines
im0 = ax[0].imshow(zz, extent=[-5,5,-5,5], origin='lower')
ax[0].contour(xx,yy,zz, levels=5, linewidths=2, 
              colors=['black'], alpha=0.4)

# filled contours with contourf
im1 = ax[1].contourf(xx, yy, zz, levels=100)

plt.colorbar(im0)
plt.colorbar(im1)
plt.tight_layout()
plt.show()