import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from google.colab import files
uploaded = files.upload()

data = pd.read_csv('GooglePlayStore.csv')

print(data.head())

print("\nNull Values in Dataset")
print(data.isnull().sum())

data['User Rating'].fillna(data['User Rating'].mean(), inplace=True)
data['Price'].fillna(data['Price'].mean(), inplace=True)

variance_rating = np.var(data['User Rating'])
std_rating = np.std(data['User Rating'])

print("\nVariance of User Rating =", variance_rating)
print("Standard Deviation of User Rating =", std_rating)

variance_price = np.var(data['Price'])
std_price = np.std(data['Price'])

print("\nVariance of Price =", variance_price)
print("Standard Deviation of Price =", std_price)

plt.figure(figsize=(8,5))
plt.hist(data['User Rating'], bins=np.arange(1, 6, 0.5), color='skyblue', edgecolor='black')
plt.title('Distribution of User Rating')
plt.xlabel('User Rating')
plt.ylabel('Frequency')
plt.show()

plt.figure(figsize=(8,5))
plt.hist(data['Price'], bins=10, color='lightgreen', edgecolor='black')
plt.title('Distribution of Price')
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.show()

print("\nData Distribution Analysis Completed Successfully!")
