import argparse
import numpy as np
import matplotlib.pyplot as plt
from astropy.table import Table

### We are further expanding on the particle trajectory example from week 2.
### Modify the script below to allow command line inputs 
### to set the initial parameters of the simulation, such as particle type, charge, mass, initial velocity components, 
### time step, and number of steps.
### 


# ---- Argument Parser Setup ----
parser = argparse.ArgumentParser(description="Calculate and plot the trajectory of charged particles in a magnetic field.")
parser.add_argument("-particle", type=str, default="proton", help="Type of particle: proton, alpha, deuteron")
parser.add_argument("-q", type=float, default=1.6e-19, help="charge of the particle (Coulombs)")
parser.add_argument("-m", type=float, default=1.67e-27, help="mass of the particle (kg)")
parser.add_argument("-v0x", type=float, default=1e7, help="initial velocity in x direction (m/s)")
parser.add_argument("-v0y", type=float, default=1e7, help="initial velocity in y direction (m/s)")
parser.add_argument("-v0z", type=float, default=1e7, help="initial velocity in z direction (m/s)")
parser.add_argument("-dt", type=float, default=1e-10, help="time step in seconds")
parser.add_argument("-steps", type=int, default=10000, help="number of time steps to simulate")
### add more arguments as needed, e.g., magnetic field strength, initial position, etc.

# ---- Parse Arguments ----
args = parser.parse_args()



# ---- Function Definition ----

def acceleration(q, m, v):
    return (q/m) * np.cross(v, B_field)

# use RK4 numerical integration to calculate position at each time step
def rk4_integration(q, m, r0, v0):
    r = np.zeros((steps, 3))
    v = np.zeros((steps, 3))
    r[0], v[0] = r0, v0

    for i in range(steps-1):
        k1_v = acceleration(q, m, v[i])
        k1_r = v[i]

        k2_v = acceleration(q, m, v[i]+0.5*dt*k1_v)
        k2_r = v[i]+0.5*dt*k1_v

        k3_v = acceleration(q, m, v[i]+0.5*dt*k2_v)
        k3_r = v[i]+0.5*dt*k2_v

        k4_v = acceleration(q, m, v[i]+dt*k3_v)
        k4_r = v[i]+dt*k3_v

        v[i+1] = v[i]+(dt/6)*(k1_v+2*k2_v+2*k3_v+k4_v)
        r[i+1] = r[i]+(dt/6)*(k1_r+2*k2_r+2*k3_r+k4_r)

    return r # r includes position information [x,y,z] at each step

def plot_trajectory(r, label, save=True, plot=False, outfile='trajectory.png'):
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(r[:,0], r[:,1], r[:,2], label=label)
    ax.set_title(f'Trajectory of {label} in Magnetic Field')
    ax.set_xlabel('X [m]')
    ax.set_ylabel('Y [m]')
    ax.set_zlabel('Z [m]')
    ax.legend()
    if save:
        plt.savefig(outfile)
    if plot:
        plt.show()

# ---- Main Execution ----

if __name__ == "__main__":
    # Update particle parameters based on command line arguments
    particle_types = {
        "proton": {"q": 1.6e-19, "m": 1.67e-27},
        "alpha": {"q": 2*1.6e-19, "m": 4*1.67e-27},
        "deuteron": {"q": 1.6e-19, "m": 2*1.67e-27}
    }

    if args.particle in particle_types:
        q = particle_types[args.particle]["q"]
        m = particle_types[args.particle]["m"]
    else:
        print(f"particle info: {args.particle}.")
        q = args.q
        m = args.m

    v0 = np.array([args.v0x, args.v0y, args.v0z])
    r0 = np.array([0, 0, 0])  # starting at origin

    B_field = np.array([0, 0, 1])  # Magnetic field (Tesla)
    dt = args.dt
    steps = int(args.steps)
    t = np.linspace(0, steps*dt, steps)

    outfilename = f'{args.particle}_trajectory'
    r_traj = rk4_integration(q, m, r0, v0)
    tab = Table(r_traj, names=('x','y','z'))
    tab.meta['q'] = q
    tab.meta['m'] = m
    tab.meta['v0'] = (args.v0x, args.v0y, args.v0z)
    tab.meta['dt'] = dt
    tab.meta['steps'] = steps   
    tab.write(f'{outfilename}_data.fits', overwrite=True)
    plot_trajectory(r_traj, args.particle.capitalize(), save=True, plot=False, outfile=f'{outfilename}_3d.png')
    
    

    
    