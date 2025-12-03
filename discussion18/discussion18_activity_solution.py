import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# === galaxy rotation curve ===
# Make a simple model of galaxy rotation curve
# by assuming a spherical mass distribution and integrating
# the mass density to get enclosed mass at each radius.

# circular velocity at radius r due to enclosed mass M
def v_circular(r, M):
    G = 6.67430e-11  # m^3 kg^-1 s^-2
    return np.sqrt(G * M / r)

# calculate enclosed mass for a given radius with a exponential density profile
def mass_enclosed(r, rho0, r0):
    integrand = lambda r_prime: 4 * np.pi * r_prime**2 * rho0 * np.exp(-r_prime / r0)
    M, err = quad(integrand, 0, r)
    return M

# ------ Integration and Plotting ------

# For convenience, assume an exponential density profile: rho(r) = rho0*exp(-r/r0)
# This is an extremely simplified model and does not represent real galaxies accurately.
rho0 = 1e7  # in Msun/kpc^3
r0 = 3.0    # in kpc

# For convenience, assume dark matter halo density profile: rho(r) = rho0_dm*exp(-r/r0_dm)
# Commonly used models for dark matter halo density profile include NFW, Einasto, Burkert, etc.
# Here we just use an exponential for simplicity.
# Change rho0_dm and r0_dm to see different effects.
rho0_dm = 1e6  # in Msun/kpc^3
r0_dm = 10.0   # in kpc

radii = np.linspace(1, 30, 1000)  # in kpc
### Find the enclosed mass at each radii and the corresponding velocities
# for convenience, adding a constant central mass
masses = np.array([mass_enclosed(r, rho0, r0)+4e6 for r in radii])  # in Msun
velocities = v_circular(radii * 3e19, masses * 2e30)  # convert kpc to m and Msun to kg
velocities /= 1e3  # convert to km/s

### Now include dark matter halo
masses_dm = np.array([mass_enclosed(r, rho0_dm, r0_dm) for r in radii])  # in Msun
masses_total = masses + masses_dm
velocities_total = v_circular(radii * 3e19, masses_total * 2e30)  # convert kpc to m and Msun to kg
velocities_total /= 1e3  # convert to km/s

# Plot rotation curve
fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(radii, velocities, label='baryonic only', color='tab:blue')
ax.plot(radii, velocities_total, label='baryonic + dark matter', color='tab:red')
ax.set_xlim(0,30)
ax.set_title('Galaxy Rotation Curve')
ax.set_xlabel('Radius [kpc]')
ax.set_ylabel('Velocity [km/s]')
plt.legend()
plt.grid()
plt.savefig('galaxy_rotation_curve.png')
plt.show()


# note: this is a highly simplified model and does not represent real galaxies accurately.
