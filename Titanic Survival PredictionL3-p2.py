import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


from google.colab import files
uploaded = files.upload()

data = pd.read_csv('Titanic Dataset.csv')

data.head(5)

data.isnull().sum()

plt.boxplot(data['Age'])
plt.title('Age distribution')
plt.show()

plt.boxplot(data['Pclass'])
plt.title('Passenger Class distribution')
plt.show()
