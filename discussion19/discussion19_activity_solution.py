import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# ====== Activity: Solve IVP =========

### We are using this particle trajectory example again.
### This time, write your own ODE solver.
### We have this IVP problem, where there is a B field along Z direction of 1 T.
### A particle of mass m, initial velocity v0, and initial position r0 moves under Lorentz force:
### dv/dt = (q/m) v x B
### Find its trajectory r(t) using your own ODE solver.


# ---- Define arguments----
q = 1.6e-19  # charge in Coulombs
m = 1.67e-27  # mass in kg
B_field = np.array([0, 0, 1])  # Magnetic field in Tesla
r0 = np.array([0, 0, 0])  # initial position in meters
v0 = np.array([1e7, 1e7, 0.5e7])  # initial velocity in m/s
dt = 1e-10
steps = int(1e4)
t_tot = steps * dt

# ---- Function Definition ----
def ode(t, Y):
    x0, y0, z0, vx0, vy0, vz0 = Y
    ax, ay, az = (q/m)*np.cross(np.array([vx0, vy0, vz0]), B_field)
    return np.array([vx0, vy0, vz0, ax, ay, az]) 

def plot_trajectory(r, label, save=True, plot=False):
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(r[:,0], r[:,1], r[:,2], label=label)
    ax.set_title(f'Trajectory of {label} in Magnetic Field')
    ax.set_xlabel('X [m]')
    ax.set_ylabel('Y [m]')
    ax.set_zlabel('Z [m]')
    ax.legend()
    if save:
        plt.savefig(f'{label}_trajectory.png')
    if plot:
        plt.show()

# ---- Main Execution ----

if __name__ == "__main__":
    particle_types = {
        "proton": {"q": 1.6e-19, "m": 1.67e-27},
        "alpha": {"q": 2*1.6e-19, "m": 4*1.67e-27},
        "deuteron": {"q": 1.6e-19, "m": 2*1.67e-27}
    }

    t_eval = np.linspace(0, t_tot, steps)

    sol = solve_ivp(ode, [0, t_tot], np.concatenate((r0, v0)), t_eval=t_eval)
    r = sol.y[:3].T  # Extract position components
    plot_trajectory(r, label="Proton", save=True, plot=True)
    
