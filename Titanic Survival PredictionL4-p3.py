import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from google.colab import files
uploaded = files.upload()

data = pd.read_csv('Titanic Dataset.csv')

data.head(5)

num_data = data.drop(['Name', 'Ticket', 'Cabin', 'Embarked', 'Gender'], axis=1)

labels = ['PassengerId','Survived','Pclass','Age','SibSp','Parch','Fare']

for label in labels:
  plt.boxplot(num_data[label])
  print('Distribution of', label)
  plt.show()

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
num_data = scaler.fit_transform(num_data)
