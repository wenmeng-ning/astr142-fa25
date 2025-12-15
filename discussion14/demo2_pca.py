import numpy as np
import scipy.io as sio
import matplotlib
import matplotlib.pyplot as plt
from numpy.matlib import repmat
from sklearn.preprocessing import normalize

# this functions sorts eigenvalues and eigenvectors
def eigsort(V, eigvals):
    # Sort the eigenvalues from largest to smallest. Store the sorted
    # eigenvalues in the column vector lambd.
    lohival = np.sort(eigvals)
    lohiindex = np.argsort(eigvals)
    lambd = np.flip(lohival)
    index = np.flip(lohiindex)
    Dsort = np.diag(lambd)
    
    # Sort eigenvectors to correspond to the ordered eigenvalues. Store sorted
    # eigenvectors as columns of the matrix vsort.
    M = np.size(lambd)
    Vsort = np.zeros((M, M))
    for i in range(M):
        Vsort[:,i] = V[:,index[i]]
    return Vsort, Dsort

# function to view a column vector as an image
def viewcolumn(columnvector):
    # view images
    plt.imshow(columnvector.reshape([60, 60], order='F'), cmap=plt.get_cmap('gray'))

# normalize columns of a matrix
def normc(Mat):
    return normalize(Mat, norm='l2', axis=0)

# load data
dat = sio.loadmat('demo_data.mat')

# unpack data
faces = dat['faces']
dog = dat['dog']
x = dat['x']

# view a sample face
viewcolumn(faces[:,4])

# pca
faces_mean = np.mean(faces, axis=1, keepdims=True)
# mean-centered data
X = faces - faces_mean
n_faces = faces.shape[1]
# compute covariance matrix
C = np.matmul(X.T,X) / n_faces 
# eigen decomposition
eigvals, eigvecs = np.linalg.eig(C)
# sort eigenvalues and eigenvectors
Vsort, Dsort = eigsort(eigvecs, eigvals)
# compute principal components
eigenfaces = np.matmul(X, Vsort)
eigenfaces = normalize(eigenfaces, axis=0)   # orthonormal basis


# view first 16 principal components
fig, axes = plt.subplots(4,4, figsize=(8,8))
for i in range(4):
    for j in range(4):
        ax = axes[i,j]
        ax.imshow(eigenfaces[:,i*4+j].reshape([60,60], order='F'), cmap=plt.get_cmap('gray'))
        ax.axis('off')
plt.suptitle('First 16 Principal Components')
plt.show()

# reconstruct a face using first k principal components
k = 10
face_index = 10

face = faces[:, face_index:face_index+1]
face_centered = face - faces_mean

coeffs = np.matmul(eigenfaces[:, :k].T, face_centered)
face_recon = faces_mean + np.matmul(eigenfaces[:, :k], coeffs)

# original and reconstructed face
fig, axes = plt.subplots(1,2, figsize=(8,4))
ax = axes[0]
ax.imshow(face.reshape([60,60], order='F'), cmap=plt.get_cmap('gray'))
ax.set_title('Original Face')
ax.axis('off')
ax = axes[1]
ax.imshow(face_recon.reshape([60,60], order='F'), cmap=plt.get_cmap('gray'))
ax.set_title(f'Reconstructed Face (k={k})')
ax.axis('off')
plt.show()

# reconstruct dog image using first k principal components
dog_centered = dog - faces_mean
dog_coeffs = np.matmul(eigenfaces[:, :k].T, dog_centered)
dog_recon = faces_mean + np.matmul(eigenfaces[:, :k], dog_coeffs)

# Plot
fig, axes = plt.subplots(1,2, figsize=(8,4))
axes[0].imshow(dog.reshape(60,60, order='F'), cmap='gray')
axes[0].set_title("Original Dog")
axes[1].imshow(dog_recon.reshape(60,60, order='F'), cmap='gray')
axes[1].set_title("Dog projected into Face Space")
for ax in axes: ax.axis('off')
plt.show()
