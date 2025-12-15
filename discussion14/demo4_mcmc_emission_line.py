"""
Fit a Gaussian spectral line (amplitude, center, sigma). 
Demo of Metropolis-Hastings.
"""
import numpy as np
import matplotlib.pyplot as plt

# generate synthetic data: Gaussian line + continuum + noise
# simplification of real spectral line fitting
# parameters: amplitude, center, sigma, continuum level
# y = cont + A * exp(-0.5 * ((x - mu)/sigma)^2) + noise
def make_synthetic_line(n=200, seed=42):
    rng = np.random.default_rng(seed)
    x = np.linspace(6000, 6550, n)  # wavelength (Angstrom)
    A_true = 1.2
    mu_true = 6525.3
    sigma_true = 1.8
    cont = 0.5
    y = cont + A_true * np.exp(-0.5 * ((x - mu_true)/sigma_true)**2)
    y += rng.normal(scale=0.08, size=n)
    return x, y, (A_true, mu_true, sigma_true, cont)


# log-probability function
def logp(params, x, y, sigma_noise=0.08):
    A, mu, s, cont = params
    if s <= 0 or A < 0:
        return -np.inf
    model = cont + A * np.exp(-0.5 * ((x-mu)/s)**2)
    resid = y - model
    return -0.5 * np.sum((resid/sigma_noise)**2)

# metropolis-hastings MCMC
def metropolis_hastings(logp, x, y, x0, nsteps=5000, proposal_scales=(0.05,0.1,0.05,0.02)):
    rng = np.random.default_rng(0)
    current = np.array(x0, dtype=float)
    samples = np.zeros((nsteps, len(current)))
    accepts = 0
    for i in range(nsteps):
        prop = current + rng.normal(scale=proposal_scales, size=current.shape)
        lp_cur = logp(current, x, y)
        lp_prop = logp(prop, x, y)
        if np.log(rng.random()) < (lp_prop - lp_cur):
            current = prop
            accepts += 1
        samples[i] = current
    print(f'Acceptance fraction: {accepts/nsteps:.3f}')
    return samples


if __name__ == '__main__':
    x, y, truth = make_synthetic_line()
    # initial guess
    x0 = [0.8, 6524.0, 2.5, 0.4]

    # === Run Metropolis-Hastings MCMC ===
    samples = metropolis_hastings(logp, x, y, x0, nsteps=10000)

    # discard burn-in
    burn = 2000
    s = samples[burn:]

    # trace plot
    fig, axes = plt.subplots(4,1, figsize=(6,8), sharex=True)
    labels = ['A', 'mu', 'sigma', 'continuum']
    for i, ax in enumerate(axes):
        ax.plot(samples[:,i], lw=0.5)
        ax.set_ylabel(labels[i])
    axes[-1].set_xlabel('step')
    plt.suptitle('Metropolis-Hastings Trace Plots')
    plt.tight_layout()
    plt.show()

    # posterior histograms
    fig, axes = plt.subplots(2,2,figsize=(7,6))
    axes = axes.ravel()
    for i, ax in enumerate(axes):
        ax.hist(s[:,i], bins=40, density=True, alpha=0.8,
                label = 'MH samples')
        ax.axvline(truth[i] if i<3 else truth[3], color='tab:orange',
                   label = 'true value')
        ax.set_xlabel(labels[i])
    plt.suptitle('Metropolis-Hastings Posterior Distributions')
    plt.tight_layout()
    plt.show()

    