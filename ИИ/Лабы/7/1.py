import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
df = pd.read_csv('creditcard.csv')
for i in range(7):
    for j in range(31):
        print(df.iloc[i, j], end = " ")
    print()
    print()
print(df.describe())
print("Количество записей в наборе данных, отнесенных к мошенническим транзакциям =", df['Class'].sum())
corr = df.corr().round(3)
corr.style.background_gradient(cmap='coolwarm')
print(corr)
plt.hist(df['Class'])
plt.show()







