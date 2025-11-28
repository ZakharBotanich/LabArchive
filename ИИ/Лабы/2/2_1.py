from random import random
from math import exp
import matplotlib.pyplot as plt
def get_y(out):
    return out >= 0
def p(x):
    if x >= 50:
        return -2
    a = 2 * (exp(2*x) - 1) - 2 * exp(2*x) * (exp(2 * x) + 1)
    b = (exp(2*x) - 1) ** 2
    return a / b
def f(net):
    if net >= 50:
        return 1
    return (exp(2*net) - 1) / (exp(2*net) + 1)
def get_net(w, x):
    return w[1] * x[0] + w[2] * x[1] + w[3] * x[2] + w[4] * x[3] + w[0]
def logic(x1, x2, x3, x4):
    return not x1 or (x2 and x3) or x4
w = [round(random(), 1), round(random(), 1), round(random(), 1), round(random(), 1), round(random(), 1)]
m = []
misses = -1
beta = 10 ** -1
while misses != 0:
    misses = 0
    for i in range(16):
        x1 = i//2//2//2 % 2
        x2 = i//2//2 % 2
        x3 = i//2 % 2
        x4 = i % 2
        net = get_net(w, [x1, x2, x3, x4])
        y = get_y(f(net))
        X = logic(x1, x2, x3, x4)
        if y != X:
            misses += 1
            w[0] = w[0] + beta * p(net) * (y - X)
            w[1] = w[1] + beta * x1 * p(net) * (y - X)
            w[2] = w[2] + beta * x2 * p(net) * (y - X)
            w[3] = w[3] + beta * x3 * p(net) * (y - X)
            w[4] = w[4] + beta * x4 * p(net) * (y - X)
    m.append(misses)
fig, ax = plt.subplots()
e = list(range(1, len(m) + 1)) 
plt.plot(e, m)
plt.show()    
