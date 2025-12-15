'''
This is an example using the emcee library 
to fit a Gaussian emission line in synthetic spectral data.
'''

import numpy as np
import matplotlib.pyplot as plt
import emcee
import corner

# generate synthetic data: Gaussian line + continuum + noise
# same as demo4
def make_synthetic_line(n=200, seed=42):
    rng = np.random.default_rng(seed)
    x = np.linspace(6500, 6550, n)  # wavelength (Angstrom)
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

if __name__ == '__main__':
    x, y, truth = make_synthetic_line()
    
    # === Set up and run emcee MCMC ===
    nwalkers = 32
    ndim = 4
    # initial positions of walkers: small Gaussian ball around initial guess
    initial = np.array([0.8, 6524.0, 2.5, 0.4])
    pos = initial + 1e-4 * np.random.randn(nwalkers, ndim)

    # create the sampler
    sampler = emcee.EnsembleSampler(nwalkers, ndim, logp, args=(x, y)) 
    sampler.run_mcmc(pos, 10000, progress=True)


    # discard burn-in
    burn = 1000
    samples = sampler.get_chain(discard=burn, flat=True)

    # Print estimated parameters
    A_mcmc, mu_mcmc, sigma_mcmc, cont_mcmc = np.percentile(samples, 50, axis=0)
    print(f'emcee estimated parameters:')
    print(f'A = {A_mcmc:.3f}, mu = {mu_mcmc:.3f}, sigma = {sigma_mcmc:.3f}, cont = {cont_mcmc:.3f}')
    print(f'true parameters:')
    print(f'A = {truth[0]:.3f}, mu = {truth[1]:.3f}, sigma = {truth[2]:.3f}, cont = {truth[3]:.3f}')
    # Plot data and best-fit model
    fig, ax = plt.subplots(figsize=(10,6))
    ax.scatter(x, y, s=5, label='data')
    model_best = cont_mcmc + A_mcmc * np.exp(-0.5 * ((x - mu_mcmc)/sigma_mcmc)**2)
    ax.plot(x, model_best, color='tab:orange', label='best fit')
    plt.legend()
    fig.savefig('demo5_emcee_best_fit.png')
    plt.show()
    

    # Trace plots
    fig, axes = plt.subplots(ndim, figsize=(10, 7), sharex=True)
    labels = ['A', 'mu', 'sigma', 'cont']
    for i in range(ndim):
        ax = axes[i]
        ax.plot(sampler.get_chain()[:, :, i], alpha=0.3, color='tab:blue')
        ax.set_ylabel(labels[i])
    axes[-1].set_xlabel("step number")
    plt.suptitle('Trace Plots')
    plt.tight_layout()
    fig.savefig('demo5_emcee_trace_plots.png')
    plt.show()
    

    # Posterior histograms
    fig, axes = plt.subplots(2, 2, figsize=(10, 8))
    axes = axes.flatten()
    for i in range(ndim):
        ax = axes[i]
        ax.hist(samples[:, i], bins=30, density=True, alpha=0.7, label='emcee samples')
        ax.axvline(truth[i], color='tab:orange', label='true value')
        ax.set_xlabel(labels[i])
        ax.legend()
    plt.suptitle('Posterior Distributions')
    plt.tight_layout()
    fig.savefig('demo5_emcee_posterior_histograms.png')
    plt.show()
    

    # corner plot
    fig = corner.corner(samples, labels=labels, truths=truth)
    plt.suptitle('Corner Plot')
    fig.savefig('demo5_emcee_corner_plot.png')
    plt.show()
    