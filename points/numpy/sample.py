# Example to import numpy and try to use it

import numpy as _np

def compute_average(samples=1000):
    sam = _np.random.random(size = samples)
    return _np.mean(sam)