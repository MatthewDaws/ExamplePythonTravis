from points import Point

def test_attributes_return_correctly():
    p = Point(1,2)
    assert(p.x == 1)
    assert(p.y == 2)

def test_equality():
    p1 = Point(1, 0)
    p2 = Point(0, 1)
    p3 = Point(1, 0)

    assert p1 == p1
    assert p1 == p3
    assert p1 != p2
    assert p1 is not p3