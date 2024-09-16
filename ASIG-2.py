import numpy as np
# Generate two synthetic 1xM feature vectors with M=10
vector_X = np.array([2, 4, 4, 4, 5, 5, 7, 9, 6, 8])
vector_Y = np.array([1, 3, 5, 2, 4, 6, 8, 7, 5, 9])

# Number of elements
M = len(vector_X)
# Calculate means
mean_X = np.sum(vector_X) / M
mean_Y = np.sum(vector_Y) / M

# Calculate covariance using the formula
covariance = np.sum((vector_X - mean_X) * (vector_Y - mean_Y)) / M
print(f"Vector X: {vector_X}")
print(f"Vector Y: {vector_Y}")
print(f"Covariance between X and Y: {covariance}")
