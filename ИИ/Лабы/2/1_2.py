from random import random
import matplotlib.pyplot as plt
def get_y(out):
    return out >= 0.5
def get_net(w, x):
    return w[1] * x[0] + w[2] * x[1] + w[3] * x[2] + w[4] * x[3] + w[0]
def logic(x1, x2, x3, x4):
    return not x1 or (x2 and x3) or x4
w = [round(random(), 1), round(random(), 1), round(random(), 1), round(random(), 1), round(random(), 1)]
e = []
m = []
era = 1
misses = -1
beta = 10 ** -1
while misses != 0:
    misses = 0
    for i in range(16):
        if i == 1 or i == 3 or i == 5 or i == 6 or i == 15 or i == 13 or i == 11:
            continue
        x1 = i//2//2//2 % 2
        x2 = i//2//2 % 2
        x3 = i//2 % 2
        x4 = i % 2
        y = get_y(get_net(w, [x1, x2, x3, x4]))
        X = logic(x1, x2, x3, x4)
        if y != X:
            w[0] = w[0] + beta * (X - y)
            w[1] = w[1] + beta * (X - y) * x1
            w[2] = w[2] + beta * (X - y) * x2
            w[3] = w[3] + beta * (X - y) * x3
            w[4] = w[4] + beta * (X - y) * x4
    for i in range(16):
        x1 = i//2//2//2 % 2
        x2 = i//2//2 % 2
        x3 = i//2 % 2
        x4 = i % 2
        y = get_y(get_net(w, [x1, x2, x3, x4]))
        X = logic(x1, x2, x3, x4)
        if y != X:
            misses += 1
    era += 1
    e.append(era)
    m.append(misses)
fig, ax = plt.subplots()
plt.plot(e, m)
plt.show()    
