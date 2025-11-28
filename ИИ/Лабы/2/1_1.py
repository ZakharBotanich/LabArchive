from random import random
import matplotlib.pyplot as plt
def get_y(out):
    if out >= 0.5:
        return 1
    return 0
def get_net(w, x):
    return w[1] * x[0] + w[2] * x[1] + w[3] * x[2] + w[4] * x[3] + w[0]
def logic(x1, x2, x3, x4):
    return not x1 or (x2 and x3) or x4
w = [round(random(), 1), round(random(), 1), round(random(), 1), round(random(), 1), round(random(), 1)]                                                                                         
e = []
m = []
misses = -1
era = 1
beta = 10 ** -1
while misses != 0:
    misses = 0
    for i in range(16):
        x1 = i//2//2//2 % 2
        x2 = i//2//2 % 2
        x3 = i//2 % 2
        x4 = i % 2
        net = get_net(w, [x1, x2, x3, x4])
        y = get_y(net)
        X = logic(x1, x2, x3, x4)
        if y != X:
            misses += 1
            w[0] += (X - y) * beta 
            w[1] += x1 * (X - y)* beta
            w[2] += x2 * (X - y) * beta
            w[3] += x3 * (X - y) * beta
            w[4] += x4 * (X - y) * beta
    e.append(era)
    m.append(misses)
    era += 1
fig, ax = plt.subplots()
plt.plot(e, m)
plt.show()
    

