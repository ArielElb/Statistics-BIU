import numpy as np

def generate_data_set(size, low, high):
    # Generate data set with given size and bounds
    return np.random.uniform(low=low, high=high, size=size)


def calculate_mom_estimator(data_set):
    # Calculate method of moments estimator for the given data set
    b_hat = np.max(data_set)
    return b_hat


def calculate_estimation_error(estimator, true_value):
    # Calculate estimation error
    error = np.abs(estimator - true_value)
    return error


# Set the random seed for reproducibility
np.random.seed(123)

# Generate data sets S1, S2, and S3
S1 = generate_data_set(10, 0, 7)
S2 = generate_data_set(100, 0, 7)
S3 = generate_data_set(1000, 0, 7)

# True parameter value
true_b = 7

# Calculate method of moments estimators for S1
b_hat_S1 = calculate_mom_estimator(S1)

# Calculate method of moments estimators for S2
b_hat_S2 = calculate_mom_estimator(S2)

# Calculate method of moments estimators for S3
b_hat_S3 = calculate_mom_estimator(S3)

# Calculate estimation errors
error_b_S1 = calculate_estimation_error(b_hat_S1, true_b)
error_b_S2 = calculate_estimation_error(b_hat_S2, true_b)
error_b_S3 = calculate_estimation_error(b_hat_S3, true_b)

# Print the estimation errors
print("Estimation Errors:")
print("S1 - Error for b:", error_b_S1)
print("S2 - Error for b:", error_b_S2)
print("S3 - Error for b:", error_b_S3)
