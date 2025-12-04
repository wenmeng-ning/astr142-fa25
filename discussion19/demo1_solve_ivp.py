import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# For a small body orbiting a large mass M
# d2r/dt2 = -GM r / |r|^3
# where r = (x,y,z)

# ==== Physical constants ====
G = 6.67e-11  # m^3 kg^-1 s
M = 6e24  # mass of large mass in kg, here we use Earth mass
GM = G * M

# ==== ODE system ====
def ode_system(t, Y):
    x, y, z, vx, vy, vz = Y
    r = np.sqrt(x**2 + y**2 + z**2)
    ax = -GM * x / r**3
    ay = -GM * y / r**3
    az = -GM * z / r**3
    return [vx, vy, vz, ax, ay, az]

# ==== Initial conditions ====
r0 = np.array([7e6, 0, 0])  # initial position, unit: m
v0 = np.array([0, 7500, 0])  # initial velocity, unit: m/s
Y0 = np.concatenate((r0, v0))

# ==== Solve ODE ====
t_span = (0, 2e4)  # time span for the integration, unit: s
t_eval = np.linspace(t_span[0], t_span[1], 1000)
sol = solve_ivp(ode_system, t_span, Y0, t_eval=t_eval)

# ==== Plot results ====
fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111, projection='3d')
ax.plot(sol.y[0], sol.y[1], sol.y[2], color='tab:orange', label='Orbit trajectory')
ax.scatter([0], [0], [0], color='tab:blue', s=200, label='Central Mass')
ax.set_xlabel('X (m)')
ax.set_ylabel('Y (m)')
ax.set_zlabel('Z (m)')
ax.set_title('Orbit of a Small Body around a Large Mass')
ax.legend()
plt.tight_layout()
plt.show()



