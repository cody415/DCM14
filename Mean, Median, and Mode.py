import pandas as pd
import numpy as np
import statistics as stats

from google.colab import files
uploaded = files.upload()

data = pd.read_csv('Titanic Dataset.csv')

print("First 5 Records of Dataset")
print(data.head())

print("\nVariable Types:")
print(data.dtypes)

print("\nNumerical Variables:")
print(data.select_dtypes(include=['int64', 'float64']).columns)

print("\nCategorical Variables:")
print(data.select_dtypes(include=['object']).columns)

mean_age = np.mean(data['Age'])
print("\nMean value of Age =", mean_age)

mean_fare = np.mean(data['Fare'])
print("Mean value of Fare =", mean_fare)

median_age = np.median(data['Age'])
print("\nMedian value of Age =", median_age)

median_fare = np.median(data['Fare'])
print("Median value of Fare =", median_fare)

mode_age = stats.mode(data['Age'])
print("\nMode value of Age =", mode_age)

mode_class = stats.mode(data['Pclass'])
print("Mode value of PClass =", mode_class)

mode_gender = data['Gender'].value_counts().index[0]
print("\nMode value of Gender =", mode_gender)

print("\nDataset Analysis Completed Successfully!")
print("Age and Fare are Numerical Variables.")
print("Gender is a Categorical Variable.")
print("Mean shows the average value.")
print("Median shows the middle value.")
print("Mode shows the most frequent value.")
