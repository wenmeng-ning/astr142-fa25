'''
Quick demo on using meshgrid and mgrid.
'''

import numpy as np
import matplotlib.pyplot as plt

# using np.meshgrid
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X1, Y1 = np.meshgrid(x, y)
Z1 = X1**2 + Y1**2

# using np.mgrid
X2, Y2 = np.mgrid[-5:5:0.1, -5:5:0.1] 
Z2 = X2**2 + Y2**2

# plot them just for fun
fig = plt.figure(figsize=(12, 6))

# meshgrid
ax1 = fig.add_subplot(121, projection='3d')
ax1.plot_surface(X1, Y1, Z1, cmap='viridis')
ax1.set_title('meshgrid')
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('Z')

# mgrid
ax2 = fig.add_subplot(122, projection='3d')
ax2.plot_surface(X2, Y2, Z2, cmap='viridis')
ax2.set_title('mgrid')
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_zlabel('Z')

plt.tight_layout()
plt.show()