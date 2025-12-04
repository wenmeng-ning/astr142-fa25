import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import root_scalar
import matplotlib.pyplot as plt
import numpy as np

# Here we are solving the boundary value problem (BVP):
# y''(x) + y(x) = 0, with y(0)=0 and y(pi/2)=1
# Exact solution: y(x) = sin(x)

# interval and grid
a = 0
b = np.pi/2
N = 50
x = np.linspace(a, b, N+1)
h = x[1] - x[0] # step size

# ==== Shooting method for BVP ====

def ode_system(x, Y):
    y, dy = Y
    return [dy, -y]  # y'' = -y
def boundary_residual(guess):
    Y0 = [0, guess]  # y(0)=0, y'(0)=guess
    sol = solve_ivp(ode_system, [a, b], Y0, t_eval=[b])
    yb = sol.y[0, -1]  # y(b)
    return yb - 1  # goal: y(b)=1

sol = root_scalar(boundary_residual, bracket=[0, 5], method='bisect')
slope_guess = sol.root
Y0 = [0, slope_guess]
sol = solve_ivp(ode_system, [a, b], Y0, t_eval=np.linspace(a, b, 100))
x_shoot = sol.t
y_shoot = sol.y[0]
fig, ax = plt.subplots(figsize=(8,6))
ax.plot(x_shoot, y_shoot, label="Shooting method solution")
ax.plot(x, np.sin(x), '--', label="Exact sin(x)")
plt.legend()
plt.tight_layout()
plt.show()


# ==== Finite difference method for BVP ====
# in this setup, we approximate y''(x_i) ~= (y_{i+1} - 2y_i + y_{i-1})/h^2
# which means we have f(x,y,y') = -y
# so the matrix A have diagonal elements 2 - h^2, and -1 on upper and lower diagonals
# and the right-hand side vector b is zero except for the last element which is 1 (from boundary condition y(b)=1)

A = np.zeros((N-1, N-1))
bvec = np.zeros(N-1)

for i in range(N-1):
    xi = x[i+1]
    bvec[i] = 0 
    if i > 0:
        A[i,i-1] = -1 # lower diag
    A[i,i] = 2 - h**2  # main diag
    if i < N-2:
        A[i,i+1] = -1  # upper diag

# boundary conditions y(0)=0, y(pi/2)=1
bvec[-1] = 1  # only last equation sees y_N

# solve
y_interior = np.linalg.solve(A, bvec)
y = np.concatenate(([0], y_interior, [1]))

fig, ax = plt.subplots(figsize=(8,6))
ax.plot(x, y, label="Finite difference solution")
ax.plot(x, np.sin(x), '--', label="Exact sin(x)")
plt.legend()
plt.tight_layout()
plt.show()


# ==== Collocation method for BVP ====
from scipy.integrate import solve_bvp

def ode_bvp(x, Y):
    y, dy = Y
    return np.vstack((dy, -y))  # y'' = -y

def bc(Ya, Yb):
    return np.array([Ya[0], Yb[0] - 1])  # y(0)=0, y(pi/2)=1

x_colloc = np.linspace(a, b, 5)
y_guess = np.zeros((2, x_colloc.size))

sol = solve_bvp(ode_bvp, bc, x_colloc, y_guess)

x_plot = np.linspace(a, b, 100)
y_colloc = sol.sol(x_plot)[0]
fig, ax = plt.subplots(figsize=(8,6))
ax.plot(x_plot, y_colloc, label="Collocation method solution")
ax.plot(x, np.sin(x), '--', label="Exact sin(x)")
plt.legend()
plt.tight_layout()
plt.show()
