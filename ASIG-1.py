import numpy as np

# Generate a synthetic 1xN feature vector with N=10
feature_vector = np.array([2, 4, 4, 4, 5, 5, 7, 9, 6, 8])

# Number of elements
N = len(feature_vector)

# Calculate mean using the formula
mean = np.sum(feature_vector) / N

# Calculate variance using the formula
variance = np.sum((feature_vector - mean) ** 2) / N
print(f"Feature Vector: {feature_vector}")
print(f"Mean: {mean}")
print(f"Variance: {variance}")
