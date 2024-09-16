import numpy as np

# Step 1: Create two 1xN feature vectors
N = 10  # You can change N to any number
vector1 = np.random.rand(N)
vector2 = np.random.rand(N)

# Step 2: Compute the means of the two vectors
mean_vector1 = np.mean(vector1)
mean_vector2 = np.mean(vector2)

# Step 3: Compute the covariance
covariance = np.mean((vector1 - mean_vector1) * (vector2 - mean_vector2))

# Step 4: Compute the standard deviations of the two vectors
std_vector1 = np.std(vector1)
std_vector2 = np.std(vector2)

# Step 5: Compute the correlation
correlation = covariance / (std_vector1 * std_vector2)

# Display the results
print("Vector 1:", vector1)
print("Vector 2:", vector2)
print("Correlation between Vector 1 and Vector 2:", correlation)
