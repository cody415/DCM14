import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from google.colab import files
uploaded = files.upload()

data = pd.read_csv('Bestseller Books.csv')

print(data.head())

print("\nNull Values in Dataset")
print(data.isnull().sum())

data['Price'].fillna(data['Price'].median(), inplace=True)
data['User Rating'].fillna(data['User Rating'].median(), inplace=True)

q10_price = np.quantile(data['Price'], 0.10)

print("\n10th Percentile of Price =", q10_price)

q1_price = np.quantile(data['Price'], 0.25)
q2_price = np.quantile(data['Price'], 0.50)
q3_price = np.quantile(data['Price'], 0.75)
iqr_price = q3_price - q1_price

print("\nPrice Quartiles")
print("Q1 =", q1_price)
print("Q2 =", q2_price)
print("Q3 =", q3_price)
print("IQR =", iqr_price)

q1_rating = np.quantile(data['User Rating'], 0.25)
q2_rating = np.quantile(data['User Rating'], 0.50)
q3_rating = np.quantile(data['User Rating'], 0.75)
iqr_rating = q3_rating - q1_rating

print("\nUser Rating Quartiles")
print("Q1 =", q1_rating)
print("Q2 =", q2_rating)
print("Q3 =", q3_rating)
print("IQR =", iqr_rating)

plt.figure(figsize=(8,5))
plt.boxplot(data['Price'])
plt.title('Boxplot of Price')
plt.ylabel('Price')
plt.show()

plt.figure(figsize=(8,5))
plt.boxplot(data['User Rating'])
plt.title('Boxplot of User Rating')
plt.ylabel('User Rating')
plt.show()
