import numpy as np
from matplotlib import pyplot

x = np.array([[0, 0], [3, 8], [2, 2], [1, 1], [5, 3], [4, 8], [6, 3], [5, 4], [6, 4], [7, 5]])


class KMeans(object):
    def __init__(self, k=3, tolerance=0.0001, max_iter=100):
        self._k = k
        self._tolerance = tolerance
        self._max_iter = max_iter
        self.cluster = {}
        self.centers = {}

    def fit(self, data):
        for i in range(self._k):
            self.centers[i] = data[i]  # 先随机选取中心点

        for i in range(self._max_iter):
            for j in range(self._k):
                self.cluster[j] = []
            for feature in data:
                distances = []
                for center_point in self.centers:
                    distances.append(np.linalg.norm(feature - self.centers[center_point]))
                classification = distances.index(min(distances))
                self.cluster[classification].append(feature)

            prev_centers = dict(self.centers)
            for c in self.cluster:
                self.centers[c] = np.average(self.cluster[c], axis=0)


if __name__ == '__main__':
    # 试用K均值法对如下模式分布进行聚类分析。
    # ｛ x1（0, 0）, x2（3, 8）, x3（2, 2）, x4（1, 1）, x5（5, 3）,
    # x6（4, 8）, x7（6, 3）, x8（5, 4）, x9（6, 4）, x10（7, 5）｝

    k_means = KMeans(k=3)
    k_means.fit(x)
    for center in k_means.centers:
        pyplot.scatter(k_means.centers[center][0], k_means.centers[center][1], marker='*',
                       s=150)

    colors = ['r', 'b', 'g']
    print(k_means.cluster)
    for index, cat in enumerate(k_means.cluster):
        print(cat)
        for point in k_means.cluster[cat]:
            pyplot.scatter(point[0], point[1], c=colors[index])

    pyplot.show()
