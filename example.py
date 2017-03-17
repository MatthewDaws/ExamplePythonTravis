import random
from points import Point
import points

array = [Point(random.random(), random.random()) for _ in range(10)]
p = points.nn.nearest(array, Point(0,0))

print("Closest point to (0,0) in array is {}".format(p))