import numpy
import matplotlib.pyplot as plt
df = list(numpy.genfromtxt('8.csv', delimiter=','))
lst = []
for i in range(1, len(df)):
    lst.append(df[i][29])
fig, ax = plt.subplots()
fig.set_figwidth(1)
ax.bar([0.0,1.0], [lst.count(0), lst.count(1)])
plt.show()
