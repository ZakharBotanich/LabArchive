import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import Perceptron
from sklearn.metrics import confusion_matrix
df = pd.read_csv('creditcard.csv')
n = int(len(df) * 0.55) + 1
x_train = []
x_test = []
y_train = []
y_test = []
counter = 0
for i in range(len(df)):
    counter += df.iloc[i, 30]
    if df.iloc[i, 30] == 1 or n > 492 - counter:  
        x_train.append([])
        for j in range(8, 18):
            x_train[-1].append(df.iloc[i, j])
        x_train[-1].append(df.iloc[i,29])
        y_train.append(df.iloc[i, 30])
        n -= 1
    else:
        x_test.append([])
        for j in range(8, 18):
            x_test[-1].append(df.iloc[i, j])
        x_test[-1].append(df.iloc[i,29])
        y_test.append(0)
x_train = np.asarray(x_train)
y_train = np.asarray(y_train)
x_test = np.asarray(x_test)
y_test = np.asarray(y_test)
perceptron = Perceptron().fit(x_train, y_train)
y_predicted = np.asarray(list(map(lambda x: round(x), list(perceptron.predict(x_test)))))
matrix = list(confusion_matrix(y_test, y_predicted))
matrix[0] = list(matrix[0])
if len(matrix[0]) == 1:
    matrix[0].append(0)
if len(matrix) == 1:
    matrix.append([0,0])
table_data = [["TP", matrix[0][0]], ["FN", matrix[1][0]], ["FP", matrix[0][1]], ["TN", matrix[1][1]]]
fig, ax = plt.subplots()
table = ax.table(cellText=table_data, loc='center')
table.set_fontsize(14)
table.scale(1,4)
ax.axis('off')
ax.set_title("Матрица ошибок для Perceptron")
plt.show()
