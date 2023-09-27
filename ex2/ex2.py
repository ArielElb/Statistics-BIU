import pandas as pd
import numpy as np

# Load the Tomato.csv file into a pandas DataFrame
df = pd.read_csv("Tomato.csv")

# Convert the "Date" column to a pandas datetime object
df["Date"] = pd.to_datetime(df["Date"])

# Select the rows corresponding to the population (2014-2020)
pop_prices = df[df["Date"].dt.year.between(2014, 2020)]["Average"]

# Select the rows corresponding to the sample (2015)
sample_df = df[df["Date"].dt.year == 2015]
sample_prices = sample_df["Average"]

# Calculate the population STD
pop_std = np.std(pop_prices)

# Calculate the sample STD
sample_std = np.std(sample_prices, ddof=1)

# Calculate the covariance between the minimum and maximum daily prices for the sample
covariance = sample_df["Minimum"].cov(sample_df["Maximum"])

# Calculate the Pearson correlation coefficient between the minimum and maximum daily prices for the sample
if len(sample_df["Minimum"]) == len(sample_df["Maximum"]):
    pearson_corr = sample_df["Minimum"].corr(sample_df["Maximum"])
else:
    pearson_corr = np.nan

# Calculate the Pearson correlation coefficient between the minimum daily prices for the months
# January and February of the sample
jan_min_prices = sample_df[sample_df["Date"].dt.month == 1]["Minimum"]
feb_min_prices = sample_df[sample_df["Date"].dt.month == 2]["Minimum"]
if len(jan_min_prices) == len(feb_min_prices):
    jan_feb_corr = jan_min_prices.corr(feb_min_prices)
else:
    jan_feb_corr = "correlation cannot be calculated because the number of observations in the two samples is different"

# Calculate the weighted variance of the maximum daily prices of years 2013 and 2014
# where the weight of each year is the relative number of days provided in the dataset for that year

# Select the rows corresponding to the maximum daily prices for years 2013 and 2014
max_prices_2013 = df[df["Date"].dt.year == 2013]["Maximum"]
max_prices_2014 = df[df["Date"].dt.year == 2014]["Maximum"]

# Calculate the weights for each year based on the number of days provided in the dataset
weights_2013 = np.ones_like(max_prices_2013) * 156 / (156 + 311)
weights_2014 = np.ones_like(max_prices_2014) * 311 / (156 + 311)

# Combine the prices and weights for both years into a single array
max_prices = np.concatenate([max_prices_2013, max_prices_2014])
weights = np.concatenate([weights_2013, weights_2014])

# Calculate the weighted mean of the maximum daily prices for both years
weighted_mean = np.average(max_prices, weights=weights, axis=None)

# Calculate the weighted variance of the maximum daily prices for both years
weighted_var = np.average((max_prices - weighted_mean) ** 2, weights=weights, axis=None)



# Print the results
print("Population STD:", pop_std)
print("Sample STD:", sample_std)
print("Covariance between minimum and maximum daily prices for the sample:", covariance)
print("Pearson correlation coefficient between minimum and maximum daily prices for the sample:", pearson_corr)
print("Pearson correlation coefficient between minimum daily prices for January and February of the sample:", jan_feb_corr)
print("Weighted variance of the maximum daily prices for years 2013 and 2014:", weighted_var)
