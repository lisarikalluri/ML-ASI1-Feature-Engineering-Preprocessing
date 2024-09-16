import numpy as np

# Step 1: Create an MxN matrix (M features, N samples)
M = 5  # Number of features
N = 10  # Number of samples
matrix = np.random.rand(M, N)

# Step 2: Compute the covariance matrix
covariance_matrix = np.cov(matrix)

# Step 3: Compute the correlation matrix
correlation_matrix = np.corrcoef(matrix)

# Display the results
print("Matrix (M x N):")
print(matrix)
print("\nCovariance Matrix (M x M):")
print(covariance_matrix)
print("\nCorrelation Matrix (M x M):")
print(correlation_matrix)
