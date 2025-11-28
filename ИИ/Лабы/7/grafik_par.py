import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
df = pd.read_csv('creditcard.csv')
lst = []
for i in range(1, 29):
    lst.append("V"+str(i))
sns.pairplot(df[lst])
plt.savefig("grafik.png")
