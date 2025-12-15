'''
Simple MCMC demo using Metropolis-Hastings for linear fitting.
'''
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42) # 42 is the answer to life, universe and everything ;)

# Assumed linear model: y = m*x + b
# We generate synthetic data for y = 2.5*x - 1.0 + noise
# Then to recover m and b, we define a log-likelihood function
# and use MCMC to sample from the posterior distribution of (m, b).
# In this demo, we use the Metropolis-Hastings algorithm.
# And we assume uniform priors on m and b within reasonable bounds.
# There is a burn-in period during which the chain is still converging so we discard some initial samples.
# After burn-in, we use the samples to estimate the posterior distributions of m and b.

# ===== Generate synthetic data =====

# true parameters
m_true = 2.5
b_true = -1.0

# generate synthetic data
x = np.linspace(0, 10, 30)
y = m_true * x + b_true + np.random.normal(0, 0.5, size=len(x))

# quick look at the data
plt.scatter(x, y, label="data")
plt.plot(x, m_true*x + b_true, color='r', label="true model")
plt.legend()
plt.show()


# calculate log-likelihood
# how to pick sigma? here we assume we know the noise level
# in real applications, this may not be known and need to be estimated as well
def log_likelihood(m, b, x, y, sigma=0.5):
    model = m * x + b
    return -0.5 * np.sum(((y - model) / sigma)**2)

# uniform prior (m in [-10, 10], b in [-10, 10])
def log_prior(m, b):
    if -10 < m < 10 and -10 < b < 10:
        return 0.0  # log(1)
    return -np.inf  # impossible

# posterior probability (combine prior and likelihood)
def log_posterior(m, b, x, y):
    lp = log_prior(m, b)
    if not np.isfinite(lp):
        return -np.inf # impossible
    return lp + log_likelihood(m, b, x, y)

# MCMC using Metropolis-Hastings
def metropolis_hastings(n_steps=5000, initial_guess = (0,0),proposal_widths=(0.5, 0.5)):
    # starting guess
    m_current, b_current = initial_guess
    m_width, b_width = proposal_widths
    
    samples_m = []
    samples_b = []
    
    logp_current = log_posterior(m_current, b_current, x, y)

    for step in range(n_steps):
        # propose new values
        m_proposal = np.random.normal(m_current, m_width)
        b_proposal = np.random.normal(b_current, b_width)

        logp_proposal = log_posterior(m_proposal, b_proposal, x, y)

        # acceptance probability - r = p(proposal) / p(current)
        r = np.exp(logp_proposal - logp_current)

        # accept proposed or reject and keep current
        if np.random.rand() < r:
            m_current = m_proposal
            b_current = b_proposal
            logp_current = logp_proposal

        # record samples
        samples_m.append(m_current)
        samples_b.append(b_current)

    return np.array(samples_m), np.array(samples_b)


if __name__ == "__main__":
    samples_m, samples_b = metropolis_hastings(n_steps=10000, initial_guess=(2.5,-1), proposal_widths=(0.5,0.5))

    # Discard burn-in
    burn_in = 1000
    samples_m = samples_m[burn_in:]
    samples_b = samples_b[burn_in:]

    # Trace plots to visualize convergence
    plt.figure(figsize=(12,4))
    plt.subplot(1,2,1)
    plt.plot(samples_m)
    plt.title("Trace plot: m")

    plt.subplot(1,2,2)
    plt.plot(samples_b)
    plt.title("Trace plot: b")
    plt.show()

    # Posterior histograms
    plt.figure(figsize=(12,4))
    plt.subplot(1,2,1)
    plt.hist(samples_m[1000:], bins=40)
    plt.title("Posterior of m")

    plt.subplot(1,2,2)
    plt.hist(samples_b[1000:], bins=40)
    plt.title("Posterior of b")
    plt.show()

    print(f"Estimated m: {np.mean(samples_m):.2f} ± {np.std(samples_m):.2f}")
    print(f"Estimated b: {np.mean(samples_b):.2f} ± {np.std(samples_b):.2f}")

    ### try changing the proposal widths, number of steps, and burn-in period
    ### how do these changes affect the results?