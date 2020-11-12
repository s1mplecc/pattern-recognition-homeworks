# w(1)已知，编写感知器算法程序，求下列模式分类的解向量:

import numpy as np

a = [[0, 0, 0], [1, 0, 0], [1, 0, 1], [1, 1, 0]]
b = [[0, 0, 1], [0, 1, 1], [0, 1, 0], [1, 1, 1]]
w1 = [-1, -2, -2, 0]


def standardize(a, b):
    _np_a = []
    _np_b = []
    for i in a:
        i.append(1)
        _np_a.append(np.array(i))
    for i in b:
        i.append(1)
        _np_b.append(np.array(i) * -1)
    return _np_a, _np_b
    # dot = np.array(a[0]).dot(np.array(w).T)


if __name__ == '__main__':
    np_a, np_b = standardize(a, b)
