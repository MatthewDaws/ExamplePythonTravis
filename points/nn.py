def distance(p1, p2):
    """Return the Euclidean distance between `p1` and `p2`"""
    from math import sqrt
    return sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)

def nearest(search_points, point, k=1):
    """Find the `k`th nearest point in `search_points` to `point`"""
    if k > len(search_points):
        raise Exception("Cannot return {}th nearest point as only {} points in passed array".format(
            k, len(search_points)))
    distances = [ (i, distance(point, p)) for i, p in enumerate(search_points) ]
    distances.sort(key = lambda pair : pair[1])
    index = distances[k-1][0]
    return search_points[index]
