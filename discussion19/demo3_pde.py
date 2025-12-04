import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# damped wave equation

import numpy as np
import matplotlib.pyplot as plt

# solve the wave equation with damping
# u_tt + gamma u_t = c^2 u_xx
# using finite difference method
# central difference in time and space
# u_new[i] = (2u[i] - u_prev[i](1 - gamma dt) + (c dt/dx)^2 (u[i+1] - 2u[i] + u[i-1])) / (1 + gamma dt)
# boundary conditions u(0)=u(L)=0

# Parameters
c = 1.0
gamma = 0.5
L = 1.0
N = 300
dx = L/N
dt = 0.9 * dx/c
steps = 600

x = np.linspace(0, L, N)

# Initial conditions
u = np.sin(np.pi * x)
u_prev = u.copy()  # zero initial velocity

# for each time steps
for n in range(steps):
    u_new = np.empty_like(u)
    u_new[1:-1] = (
        (2*u[1:-1] - u_prev[1:-1] * (1 - gamma*dt)
        + (c*dt/dx)**2 * (u[2:] - 2*u[1:-1] + u[:-2]))
        / (1 + gamma*dt)
    )

    u_new[0] = 0
    u_new[-1] = 0

    u_prev, u = u, u_new

plt.plot(x, u)
plt.title("Damped Wave After t = {:.2f}".format(steps*dt))
plt.show()




# wave propagation in 1D
# u_tt = c^2 u_xx

c = 1.0
L = 1.0
N = 500
dx = L/N
dt = 0.9*dx/c

x = np.linspace(0, L, N)

u = np.exp(-300*(x-0.3)**2)
u_prev = u.copy()

fig, ax = plt.subplots()
line, = ax.plot(x, u)

def update(frame):
    global u, u_prev
    un = np.empty_like(u)
    un[1:-1] = (2*u[1:-1] - u_prev[1:-1] 
                + (c*dt/dx)**2*(u[2:]-2*u[1:-1]+u[:-2]))
    un[0] = un[-1] = 0
    u_prev, u = u, un
    line.set_ydata(u)
    return line,

anim = FuncAnimation(fig, update, frames=600, interval=20)
plt.show()

