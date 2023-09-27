# statistics-ex2
## Analysis of Tomato Prices Dataset
- This code performs various statistical analyses on a dataset containing daily tomato prices over several years. The dataset is stored in a CSV file called Tomato.csv.

## Dependencies
This code requires the following dependencies:

- pandas
- numpy
- Running the code
- To run the code, simply execute the ex1.py file in a Python environment with the required dependencies installed. The output of the various analyses will be printed to the console.

## Analyses performed
This code performs the following statistical analyses on the tomato prices dataset:

- Calculates the population standard deviation of the average daily prices from 2014-2020
- Calculates the sample standard deviation of the average daily prices for the year 2015
- Calculates the covariance between the minimum and maximum daily prices for the sample year (2015)
- Calculates the Pearson correlation coefficient between the minimum and maximum daily prices for the sample year (2015)
- Calculates the Pearson correlation coefficient between the minimum daily prices for the months January and February of the sample year (2015)
- Calculates the weighted variance of the maximum daily prices for years 2013 and 2014, where the weight of each year is the relative number of days provided in the dataset for that year

## Results:
1. Population STD: 16.96395648120897 and Sample STD: 15.624328786411915
2. Covariance between minimum and maximum daily prices for the sample: 242.0955063455063
3. Pearson correlation coefficient between minimum and maximum daily prices for the sample: 0.9864668783905615
4. Pearson correlation coefficient between minimum daily prices for January and February of the sample: correlation cannot be calculated because the number of observations in the two samples is different
5. Weighted variance of the maximum daily prices for years 2013 and 2014: 174.63592054653884



### Author
This code was written by Ariel Elbaz.
