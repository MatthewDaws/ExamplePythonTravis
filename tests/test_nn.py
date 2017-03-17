from points import Point
import points.nn

from pytest import approx
import math


def test_distance():
    p1 = Point(0, 0)
    p2 = Point(1, 0)
    p3 = Point(0, 1)
    p4 = Point(1, 2)

    assert points.nn.distance(p1, p2) == approx(1.0)
    assert points.nn.distance(p1, p3) == approx(1.0)
    assert points.nn.distance(p1, p4) == approx(math.sqrt(5))
    assert points.nn.distance(p2, p4) == approx(2)
    assert points.nn.distance(p3, p4) == approx(math.sqrt(2))
    assert points.nn.distance(p2, p3) == approx(math.sqrt(2))


def test_nearest_1st():
    search_points = [Point(0, 0), Point(1, 0), Point(0, 1), Point(1, 1)]

    assert points.nn.nearest(search_points, Point(0, 0)) == Point(0, 0)
    assert points.nn.nearest(search_points, Point(0.2, 0.2)) == Point(0, 0)
    assert points.nn.nearest(search_points, Point(1.1, 0)) == Point(1, 0)
    assert points.nn.nearest(search_points, Point(0.9, 0.4)) == Point(1, 0)


def test_nearest_nth():
    search_points = [Point(0, 0), Point(1, 0), Point(0, 1), Point(1, 1)]

    assert points.nn.nearest(search_points, Point(0, 0), k=2) in [
        Point(1, 0), Point(0, 1)]
    assert points.nn.nearest(search_points, Point(0.4, 0.2), k=2) == Point(1, 0)
    assert points.nn.nearest(search_points, Point(0, 0), k=4) == Point(1, 1)
