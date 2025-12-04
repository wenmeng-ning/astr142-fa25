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
### You will need to define B field, charge, mass, initial position and velocity, time step, and total steps.
### Then define your function or method to solve the ODE.
### Finally, plot the trajectory in 3D.


# ---- Function Definition ----
### Define your function or method to solve the ODE here
def ode():
    return 

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
    # here are some particles to try
    particle_types = {
        "proton": {"q": 1.6e-19, "m": 1.67e-27},
        "alpha": {"q": 2*1.6e-19, "m": 4*1.67e-27},
        "deuteron": {"q": 1.6e-19, "m": 2*1.67e-27}}

    
    r = solve_ode() # FIXME: call your ODE solver here to get trajectory r(t)
    plot_trajectory() ### FIXME: plot the trajectory here
