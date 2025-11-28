import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import AffinityPropagation
from sklearn.decomposition import TruncatedSVD

df = list(np.genfromtxt('8.csv', delimiter=',')[1:2001])
for i in range(len(df)):
    df[i] = df[i][:5]
X = np.asarray(df)

#кластеризация
afprop = AffinityPropagation(max_iter = 150)
afprop.fit(X)
cluster_centers_indices = afprop.cluster_centers_indices_
n_clusters = len(cluster_centers_indices)
P = afprop.predict(X)

#снижение размерности
svd = TruncatedSVD()
a = svd.fit_transform(X)

colors = list(map(lambda x: "#" + hex(x** 2 + 100*x + 1048576)[2:] , P))
plt.scatter(a[:,0], a[:,1], c=colors)
plt.show()

