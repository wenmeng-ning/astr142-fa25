'''
Demo of using PCA for dimensionality reduction 
on synthetic 2D Gaussian data.
'''

import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import pandas as pd
import time

# Generate synthetic data
x, y = np.meshgrid(np.arange(512), np.arange(512))
sig = 40
A = 30

# Create a 2D Gaussian image with noise
image = A*np.exp(-((x-256)**2+(y-256)**2)/(2*sig**2))
noise = np.random.normal(scale=0.6, size=x.shape)
noise += np.random.normal(scale=0.2, size=x.shape)

data = image + noise

plt.imshow(data,origin='lower', cmap='viridis')
plt.title('Synthetic 2D Gaussian Data with Noise')
plt.show()

# flatten and standardize the data
flat_data = data.reshape(-1, 1)  # shape (262144, 1)
scaler = StandardScaler()
flat_scaled = scaler.fit_transform(data)


# use scikit-learn PCA for dimensionality reduction
t_start = time.time()
pca = PCA(n_components=2) 
principal_components = pca.fit_transform(flat_scaled)

# Create a DataFrame with the principal components
pca_data = pd.DataFrame(data=principal_components, 
                        columns=['PC1', 'PC2'])

t_end = time.time()
print(f'PCA computation time: {t_end - t_start:.4f} seconds')

# Display the first few rows of the transformed data
print(pca_data.head())

# Plot the principal components 
fig, ax = plt.subplots(figsize=(8,6))
ax.scatter(pca_data['PC1'], pca_data['PC2'], alpha=0.8)
ax.set_title('PCA of Synthetic 2D Gaussian Data')
ax.set_xlabel('Principal Component 1')
ax.set_ylabel('Principal Component 2')
plt.grid()
plt.show()

# Plot explained variance
explained_variance = pca.explained_variance_ratio_
fig, ax = plt.subplots(1,figsize=(8,6))
ax.bar(range(1, len(explained_variance)+1), explained_variance, alpha=0.7)
ax.set_title('Explained Variance by Principal Components')
ax.set_xlabel('Principal Component')
ax.set_ylabel('Variance Explained')
plt.show() 

# Plot reconstructed data from the first two principal components
reconstructed_data = pca.inverse_transform(principal_components)
reconstructed_data = scaler.inverse_transform(reconstructed_data)
reconstructed_data = reconstructed_data.reshape(512, 512)
plt.imshow(reconstructed_data, origin='lower', cmap='viridis')
plt.title('Reconstructed Data from First Two Principal Components')
plt.show()

# reconstruction difference
difference = data - reconstructed_data
plt.imshow(difference, origin='lower', cmap='viridis')
plt.colorbar()
plt.title('Reconstruction Difference')
plt.show()

# plot histogram of differences
plt.hist(difference.ravel(), bins=50, alpha=0.7)
plt.title('Histogram of Pixel-wise Differences')
plt.xlabel('Difference Value')
plt.ylabel('Frequency')
plt.show()


# using svd for dimensionality reduction
t_start = time.time()
U, S, VT = np.linalg.svd(flat_scaled, full_matrices=False)
# keep first 2 singular values
k = 2
U_k = U[:, :k]
S_k = np.diag(S[:k])
VT_k = VT[:k, :]
t_end = time.time()
print(f'SVD computation time: {t_end - t_start:.4f} seconds')
# reconstruct data
reconstructed_svd = np.dot(U_k, np.dot(S_k, VT_k))
reconstructed_svd = scaler.inverse_transform(reconstructed_svd)
reconstructed_svd = reconstructed_svd.reshape(512, 512)
plt.imshow(reconstructed_svd, origin='lower', cmap='viridis')
plt.title('Reconstructed Data from SVD (k=2)')
plt.show()
# reconstruction difference
difference_svd = data - reconstructed_svd
plt.imshow(difference_svd, origin='lower', cmap='viridis')
plt.colorbar()
plt.title('Reconstruction Difference (SVD)')
plt.show()
# plot histogram of differences
plt.hist(difference_svd.ravel(), bins=50, alpha=0.7)
plt.title('Histogram of reconstruction differences (SVD)')
plt.xlabel('Difference Value')
plt.ylabel('Frequency')
plt.show()
