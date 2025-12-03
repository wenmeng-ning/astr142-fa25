import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad, trapezoid, simpson


# Example 1: integrate sin(x) from 0 to pi/2
# we expect the result to be -cos(pi/2)+cos(0)=1

n_samples = 10

f = lambda x: np.sin(x)
x = np.linspace(0.0, np.pi/2.0, n_samples)  # sample points
y = f(x) # function values at sample points

# method 1: trapezoidal rule
print(f"trapezoid: {trapezoid(y,x)}")

# method 2: Simpson's rule
print(f"simpson: {simpson(y,x)}")

# method 3: quad function
result, error = quad(f, 0, np.pi/2)
print(f"quad: {result}")

# Plotting trapezoidal rule
fig = plt.figure(figsize=(8, 6))
plt.plot(x, y, color='tab:blue')
plt.vlines(x, 0, y, color='tab:blue', alpha=0.5)
plt.scatter(x, y, color='tab:red', label='Sampled Points')
plt.fill_between(x, 0, y, color='lightblue', alpha=0.5, label='Trapezoid approximation')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()


# Example 2: blackbody radiation over a wavelength range
# Integrate Planck's law from 400 nm to 700 nm at T=5800 K

# Planck function
def B_lambda(lam, T):
    h = 6.626e-34 # unit J*s
    c = 3e8 # unit m/s
    k = 1.381e-23 # unit J/K
    return (2*h*c**2)/(lam**5) / (np.exp(h*c/(lam*k*T)) - 1) # unit W/m^2/m/sr

# integrate from 400 nm to 700 nm
lam = np.linspace(400e-9, 700e-9, 500)

flux_trap = trapezoid(B_lambda(lam, 5800),lam)
flux_quad = quad(B_lambda, 400e-9, 700e-9, args=(5800,))[0]

print(f"Integrating blackbody flux from 400 nm to 700 nm at T=5800 K: \n trapezoid: {flux_trap} W/m^2/sr\n quad: {flux_quad} W/m^2/sr")
