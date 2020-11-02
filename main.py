import numpy as np
from matplotlib import pyplot

x = np.array([[0, 0], [3, 8], [2, 2], [1, 1], [5, 3], [4, 8], [6, 3], [5, 4], [6, 4], [7, 5]])


class KMeans(object):
    def __init__(self, k=3, tolerance=0.0001, max_iter=100):
        self.clf_ = {}
        self.centers_ = {}
        self.k_ = k
        self.tolerance_ = tolerance
        self.max_iter_ = max_iter

    def fit(self, data):
        for i in range(self.k_):
            self.centers_[i] = data[i]  # 先随机选取中心点

        for i in range(self.max_iter_):
            for j in range(self.k_):
                self.clf_[j] = []
            for feature in data:
                distances = []
                for center_point in self.centers_:
                    distances.append(np.linalg.norm(feature - self.centers_[center_point]))
                classification = distances.index(min(distances))
                self.clf_[classification].append(feature)

            prev_centers = dict(self.centers_)
            for c in self.clf_:
                self.centers_[c] = np.average(self.clf_[c], axis=0)


if __name__ == '__main__':
    k_means = KMeans(k=3)
    k_means.fit(x)
    for center in k_means.centers_:
        pyplot.scatter(k_means.centers_[center][0], k_means.centers_[center][1], marker='*', s=150)

    for cat in k_means.clf_:
        for point in k_means.clf_[cat]:
            pyplot.scatter(point[0], point[1], c=('r' if cat == 0 else 'b'))

    pyplot.show()
