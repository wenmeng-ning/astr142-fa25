import numpy as np
import matplotlib.pyplot as plt

# ==== Physical constants ====
B_field = np.array([0, 0, 1])  # Magnetic field along Z (Tesla)
dt = 1e-10
steps = int(1e4)
t = np.linspace(0, steps * dt, steps)

# ==== Define particles ====
particles = [
    {
        "label": "Proton",
        "q": 1.6e-19,
        "m": 1.67e-27,
        "v0": np.array([1e7, 1e7, 0.5e7]),
        "r0": np.array([0, 0, 0]),
        "color": "red"
    },
    {
        "label": "Alpha Particle",
        "q": 2*1.6e-19,
        "m": 4*1.67e-27,
        "v0": np.array([1e7, -1e7, 1e7]),
        "r0": np.array([0, 0, 0]),
        "color": "green"
    }]

# ==== ODE solving methods ====

def euler_method(q, m, r0, v0):
    r = np.zeros((steps, 3))
    v = np.zeros((steps, 3))
    r[0], v[0] = r0, v0
    for i in range(steps - 1):
        a = (q/m)*np.cross(v[i], B_field)
        v[i+1] = v[i] + a*dt
        r[i+1] = r[i] + v[i]*dt
    return r

def euler_cromer_method(q, m, r0, v0):
    r = np.zeros((steps, 3))
    v = np.zeros((steps, 3))
    r[0], v[0] = r0, v0
    for i in range(steps - 1):
        a = (q / m) * np.cross(v[i], B_field)
        v[i+1] = v[i] + a*dt
        r[i+1] = r[i] + v[i+1]*dt  # Use updated v
    return r


def acceleration(q, m, v):
        return (q / m) * np.cross(v, B_field)

def rk4_method(q, m, r0, v0):
    r = np.zeros((steps, 3))
    v = np.zeros((steps, 3))
    r[0], v[0] = r0, v0

    for i in range(steps - 1):
        k1_v = acceleration(q, m, v[i])
        k1_r = v[i]

        k2_v = acceleration(q, m, v[i] + 0.5*dt*k1_v)
        k2_r = v[i] + 0.5*dt*k1_v

        k3_v = acceleration(q, m, v[i] + 0.5*dt*k2_v)
        k3_r = v[i] + 0.5*dt*k2_v

        k4_v = acceleration(q, m, v[i] + dt*k3_v)
        k4_r = v[i] + dt*k3_v

        v[i+1] = v[i] + (dt/6)*(k1_v + 2*k2_v + 2*k3_v + k4_v)
        r[i+1] = r[i] + (dt/6)*(k1_r + 2*k2_r + 2*k3_r + k4_r)

    return r

# ==== Run Simulations ====

methods = {
    "Euler": euler_method,
    "Euler-Cromer": euler_cromer_method,
    "RK4": rk4_method,
}

# Store results for plotting
results = {method: [] for method in methods}

for method_name, method_func in methods.items():
    for p in particles:
        r_traj = method_func(p["q"], p["m"], p["r0"], p["v0"])
        results[method_name].append((p["label"], r_traj, p["color"]))

# ==== Plot XY Projections ====

fig, axs = plt.subplots(1, 3, figsize=(18, 5))

for ax, (method_name, particle_data) in zip(axs, results.items()):
    for label, r, color in particle_data:
        ax.plot(r[:, 0], r[:, 1], label=label, color=color, lw=1)
    ax.set_title(f"{method_name} Method")
    ax.set_xlabel("X position (m)")
    ax.set_ylabel("Y position (m)")
    ax.set_aspect('equal')
    ax.grid(True)
    ax.legend()

plt.suptitle("Cyclotron Motion (XY Projection)", fontsize=16)
plt.tight_layout()
plt.show()