import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from google.colab import files
uploaded = files.upload()

data = pd.read_csv('Titanic Dataset.csv')

data.head(5)

sns.set_style('whitegrid')

sns.countplot(x='Survived', data=data)

sns.countplot(x='Gender', hue='Survived', data=data)

sns.countplot(x='Survived', data=data, palette='winter')

sns.countplot(x='Gender', hue='Survived', data=data, palette='winter')

sns.countplot(x='Embarked', data=data)

sns.countplot(x='Embarked', data=data)
plt.xticks(rotation=30, fontsize=20)
plt.show()

