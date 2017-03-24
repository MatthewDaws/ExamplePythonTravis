import numpy as _np

def sample():
    while True:
        x = _np.random.random()
        if _np.random.random() <= x:
            return x

from numpy.random import randint as _randint

def sample2():
    return _randint(low=0, high=10)