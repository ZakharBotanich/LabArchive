import numpy
import matplotlib.pyplot as plt
from random import randint
from random import random
from random import shuffle
from math import exp
def get_y(out):
    return out >= 0
def p(x):
    if x >= 30:
        return -2
    a = 2 * (exp(2*x) - 1) - 2 * exp(2*x) * (exp(2 * x) + 1)
    b = (exp(2*x) - 1) ** 2
    return a / b
def f(net):
    if net >= 30:
        return 1
    return (exp(2*net) - 1) / (exp(2*net) + 1)
def get_net(w, x):
    net = 0
    for i in range(30):
        net += w[i] * x[i]
    return net
df = list(numpy.genfromtxt('8.csv', delimiter=','))
lst = []
res = []
for i in range(1, len(df)):
    if df[i][29] == 0:
        c = [1]
        for j in range(29):
            c.append(df[i][j])
        lst.append(c)
        res.append(0)
    else:
        c = [1]
        for j in range(29):
            c.append(df[i][j])
        lst.append(c)
        res.append(1)
for i in range(len(lst)):
    for j in range(1, 30):
        lst[i][j] += 2 * randint(0, 1)
w = []
for i in range(30):
    w.append(random())
beta = 1
misses = -1
era = 1
m1 = []
m2 = []
m3 = []
while era <= 100:
    misses = 0
    tp = 0
    fn = 0
    fp = 0
    tn = 0
    for i in range(len(lst)):
        net = get_net(w, lst[i])
        y = get_y(f(net))
        x = res[i]
        if y == x and y == 1:
            tp += 1
        elif y == x and y == 0:
            fn += 1
        elif y != x and x == 0 and y == 1:
            fp += 1
        else:
            tn += 1
        if y != x:
            misses += 1
            for j in range(30):
                w[j] += beta * lst[i][j] * p(net) * (y - x)
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    accuracy = (len(lst) - misses) / len(lst)
    m1.append(precision)
    m2.append(recall)
    m3.append(accuracy)
    era += 1
fig, ax = plt.subplots()
plt.plot(list(range(1, 101)), m1)
ax.set_title("График Precision")
plt.show()

fig, ax = plt.subplots()
plt.plot(list(range(1, 101)), m2)
ax.set_title("График Recall")
plt.show()

fig, ax = plt.subplots()
plt.plot(list(range(1, 101)), m3)
ax.set_title("График Accuracy")
plt.show()

fig, ax = plt.subplots()
table_data = [["TP", tp], ["FN", fn], ["FP", fp], ["TN", tn]]
table = ax.table (cellText=table_data, loc='center')
table.set_fontsize(14)
table.scale(1,4)
ax.axis('off')
ax.set_title("Матрица ошибок")
plt.show()
