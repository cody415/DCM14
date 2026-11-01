import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency
from scipy.stats import pearsonr

from google.colab import files
uploaded = files.upload()

data = pd.read_csv('Bestseller Books.csv')

print(data.head())

print("\nNull Values in Dataset")
print(data.isnull().sum())

data.fillna(method='ffill', inplace=True)

print("\nFrequency of Genre")
print(data['Genre'].value_counts())

data['Rating Category'] = pd.cut(data['User Rating'],
                                 bins=[0, 4.5, 5],
                                 labels=['Good', 'Excellent'])

print("\nUser Rating Categories")
print(data[['User Rating', 'Rating Category']].head())

num_data = data.select_dtypes(include=['int64', 'float64'])

print("\nSkewness of Numerical Features")
for column in num_data.columns:
    print(column, "=", data[column].skew())

contingency_table = pd.crosstab(data['Rating Category'], data['Genre'])

chi2, p, dof, expected = chi2_contingency(contingency_table)

print("\nAssociation between User Rating and Genre")
print("Chi-Square Statistic =", chi2)
print("P-value =", p)

correlation, p_value = pearsonr(data['User Rating'], data['Price'])

print("\nAssociation between User Rating and Price")
print("Correlation Coefficient =", correlation)
print("P-value =", p_value)
