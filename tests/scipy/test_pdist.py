from points import Point
import points.scipy.pdist as pdist

from pytest import approx
import math

def test_distance():
    points = [Point(0, 0), Point(1, 0), Point(0, 1)]
    dists = pdist.distance(points)
    assert dists[0] == approx(1.0)
    assert dists[1] == approx(1.0)
    assert dists[2] == approx(math.sqrt(2))
