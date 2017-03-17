# Example which imports scipy

import scipy.spatial as _spatial
import numpy as _np
from .. import point

def _unstack_as_numpy_array(points):
    return _np.array([[p.x, p.y] for p in points])

def distance(points):
    """From an array of `Point`s compute the distances"""
    return _spatial.distance.pdist(_unstack_as_numpy_array(points))