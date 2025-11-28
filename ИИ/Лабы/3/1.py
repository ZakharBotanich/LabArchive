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
def TPR(mu, tp, fn):
    if tp <= mu:
        tp *= -1
    if fn <= mu:
        fn *= -1
    return tp / (tp + fn)
def FPR(mu, fp, tn):
    if fp <= mu:
        fp *= -1
    if tn <= mu:
        tn *= -1
    return fp / (tn + fp)
w = [round(random(), 1), round(random(), 1), round(random(), 1), round(random(), 1), round(random(), 1)]                                                                                         
misses = -1
beta = 10 ** -1
metrics = []
while misses != 0:
    misses = 0
    tp = 0
    fn = 0
    fp = 0
    tn = 0
    for i in range(16):
        x1 = i//2//2//2 % 2
        x2 = i//2//2 % 2
        x3 = i//2 % 2
        x4 = i % 2
        net = get_net(w, [x1, x2, x3, x4])
        y = get_y(net)
        X = logic(x1, x2, x3, x4)
        if y == X and y == 1:
            tp += 1
        elif y == X and y == 0:
            fn += 1
        elif y != X and X == 0 and y == 1:
            fp += 1
        else:
            tn += 1
        if y != X:
            misses += 1
            w[0] += (X - y) * beta 
            w[1] += x1 * (X - y)* beta
            w[2] += x2 * (X - y) * beta
            w[3] += x3 * (X - y) * beta
            w[4] += x4 * (X - y) * beta
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    F = 2 * (precision * recall) / (precision + recall)
    if misses != 0:
        ROC = TPR(FPR(3, fp, tn), tp, fn)
    else:
        ROC = 0
    metrics.append([tp, fp, fn, tn, precision, recall, F, ROC])
eras = len(metrics)
names = ["TP", "FP", "FN", "TN", "Precision", "Recall", "F", "ROC-AUC"]
for j in range(8):
    y = []
    for i in range(eras):
        y.append(metrics[i][j])
    x = list(range(1, eras + 1))
    if j == 7:
        AUC = 0
        for k in range(len(y) - 1):
            AUC += 0.5 * (y[k] + y[k + 1])
        print("AUC =", AUC)
    fig, ax = plt.subplots()
    plt.plot(x, y)
    ax.set_title("График метрики " + names[j])
    plt.show()
