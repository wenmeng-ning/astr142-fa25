import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# === galaxy rotation curve ===

# circular velocity at radius r due to enclosed mass M
def v_circular(r, M):
    G = 6.67430e-11  # m^3 kg^-1 s^-2
    return np.sqrt(G * M / r)

# calculate enclosed mass for a given radius with a exponential density profile
def mass_enclosed(r, rho0, r0):
    integrand = lambda r_prime: 4 * np.pi * r_prime**2 * rho0 * np.exp(-r_prime / r0)
    ### FIXME: numerical integration
    return M

### Integrate mass density to get enclosed mass

# Assume an exponential density profile: rho(r) = rho0*exp(-r/r0)
rho0 = 1e7  # in Msun/kpc^3
r0 = 3.0    # in kpc

# Assume dark matter halo density profile: rho(r) = rho0_dm*exp(-r/r0_dm)
rho0_dm = 1e6  # in Msun/kpc^3
r0_dm = 10.0   # in kpc

radii = np.linspace(1, 30, 1000)  # in kpc
### Find the enclosed mass at each radii and the corresponding velocities
### Plot rotation curve with and without dark matter
### Compare the plots, and check out figure 2 in this paper arXiv:1810.02131
