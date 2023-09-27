import numpy as np

def generate_data_set(size):
    # Generate data set with given size
    return np.random.normal(loc=2, scale=np.sqrt(5), size=size)

def calculate_mle(data_set):
    # Calculate maximum likelihood estimators for the given data set
    mu_hat = np.mean(data_set)
    sigma2_hat = np.var(data_set)
    return mu_hat, sigma2_hat

def calculate_estimation_errors(mu_hat, sigma2_hat, true_mu, true_sigma2):
    # Calculate estimation errors
    error_mu = np.abs(mu_hat - true_mu)
    error_sigma2 = np.abs(sigma2_hat - true_sigma2)
    return error_mu, error_sigma2

# Set the random seed for reproducibility
np.random.seed(123)

# Generate data sets S1, S2, and S3
S1 = generate_data_set(10)
S2 = generate_data_set(100)
S3 = generate_data_set(1000)

# Calculate maximum likelihood estimators for S1
mu_hat_S1, sigma2_hat_S1 = calculate_mle(S1)

# Calculate maximum likelihood estimators for S2
mu_hat_S2, sigma2_hat_S2 = calculate_mle(S2)

# Calculate maximum likelihood estimators for S3
mu_hat_S3, sigma2_hat_S3 = calculate_mle(S3)

# True parameter values
true_mu = 2
true_sigma2 = 5

# Calculate estimation errors for S1
error_mu_S1, error_sigma2_S1 = calculate_estimation_errors(mu_hat_S1, sigma2_hat_S1, true_mu, true_sigma2)

# Calculate estimation errors for S2
error_mu_S2, error_sigma2_S2 = calculate_estimation_errors(mu_hat_S2, sigma2_hat_S2, true_mu, true_sigma2)

# Calculate estimation errors for S3
error_mu_S3, error_sigma2_S3 = calculate_estimation_errors(mu_hat_S3, sigma2_hat_S3, true_mu, true_sigma2)

# Print the estimation errors
print("Estimation Errors:")
print("S1 - Error for μ:", error_mu_S1)
print("S1 - Error for σ^2:", error_sigma2_S1)
print("S2 - Error for μ:", error_mu_S2)
print("S2 - Error for σ^2:", error_sigma2_S2)
print("S3 - Error for μ:", error_mu_S3)
print("S3 - Error for σ^2:", error_sigma2_S3)
