import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

from google.colab import files
uploaded = files.upload()

data = pd.read_csv('Bestseller Books.csv')

print(data.head())

print("\nNull Values in Dataset")
print(data.isnull().sum())

data.fillna(method='ffill', inplace=True)

frequency = data['Genre'].value_counts()

print("\nFrequency of Genre")
print(frequency)

median_genre = data['Genre'].mode()[0]

print("\nMedian Value of Genre =", median_genre)

frequency.plot(kind='bar', color='skyblue')
plt.title('Bar Chart of Genre')
plt.xlabel('Genre')
plt.ylabel('Frequency')
plt.show()

frequency.plot(kind='pie', autopct='%1.1f%%')
plt.title('Pie Chart of Genre')
plt.ylabel('')
plt.show()

num_data = data.select_dtypes(include=['int64', 'float64'])

labels = num_data.columns

for label in labels:
    plt.boxplot(num_data[label])
    print('Distribution of', label)
    plt.show()

scaler = StandardScaler()
scaled_data = scaler.fit_transform(num_data)

scaled_data = pd.DataFrame(scaled_data, columns=num_data.columns)

print("\nStandardized Data")
print(scaled_data.head())
