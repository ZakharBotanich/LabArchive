from random import random
from math import exp
from math import e
import matplotlib.pyplot as plt
def get_net(w, x):
    net = 0
    for i in range(len(w)):
        net += w[i] * x[i]
    return net
def f(net):
    return 1/e * net
def pr(net):
    return 1/e
p = 4
w = []
n = 0.01
for i in range(p + 1):
    w.append(random())
X = []
i = -4
while i <= 4:
    X.append(exp(i))
    i += 0.2
misses = -1
era = 0
eps = 0.02
while misses != 0:
    misses = 0
    for i in range(len(X) - p):
        x = [1] + X[i:i+p]
        net = get_net(w, x)
        y = f(net)
        k = 1
        if abs(X[i+p] - y) >= eps:
            misses += 1
            if y > X[i + p]:
                k = -1
            for j in range(p + 1):
                w[j] += n * k * pr(net) * x[j]
    era += 1

x = X[len(X) - p:]
i = 4
a = []
b1 = []
b2 = []
b3 = []
mse = 0
while i <= 12:
    next_x = f(get_net(w, [1] + x))
    mse += (next_x - exp(i)) ** 2
    a.append(i)
    b1.append(exp(i))
    b2.append(next_x)
    b3.append(mse / len(a))
    x = x[1:] + [next_x]
    i += 0.2
fig, axs = plt.subplots(nrows = 3, ncols = 1)
axs[0].set_title("Исходный график")
axs[0].plot(a, b1)
axs[1].set_title("График прогноза")
axs[1].plot(a, b2)
axs[2].set_title("График метрики MSE")
axs[2].plot(a, b3)
plt.show()
