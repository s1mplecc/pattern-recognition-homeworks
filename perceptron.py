import numpy as np


def standardize(_a, _b):
    _np_a = []
    _np_b = []
    for i in _a:
        i.append(1)
        _np_a.append(np.array(i))
    for i in _b:
        i.append(1)
        _np_b.append(np.array(i) * -1)
    return _np_a, _np_b


def perceptron(_np_a, _np_b, _w1):
    print(_np_b)
    data = _np_a + _np_b
    print(data)
    _w = np.array(_w1)
    _end_flag = False
    while not _end_flag:
        _leq_flag = False
        for vector in data:
            dot = _w.dot(vector.T)
            if dot > 0:
                continue
            else:
                _w = _w + vector
                print(_w)
                _leq_flag = True
                continue
        if _leq_flag is True:
            _end_flag = False
            continue
        else:
            _end_flag = True
            print('end')
            break
    return _w


if __name__ == '__main__':
    # w(1)已知，编写感知器算法程序，求下列模式分类的解向量:
    a = [[0, 0, 0], [1, 0, 0], [1, 0, 1], [1, 1, 0]]
    b = [[0, 0, 1], [0, 1, 1], [0, 1, 0], [1, 1, 1]]
    w1 = [-1, -2, -2, 0]

    np_a, np_b = standardize(a, b)
    result = perceptron(np_a, np_b, w1)
    print(result)
