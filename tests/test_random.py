import points.random as testmod
from unittest.mock import patch

def fixed_random():
    return 0.5

@patch("numpy.random.random", fixed_random)
def test_sample():
    assert( testmod.sample() == 0.5 )

# Somehow I should be able to do this in a more Pythonic way...
class CyclicReturner():
    def __init__(self, buffer):
        self.buffer = buffer
        self.index = -1

    def __call__(self):
        self.index += 1
        if self.index == len(self.buffer):
            self.index = 0
        return self.buffer[self.index]

# These next two tests are, IMHO, genuine tests which exercise the logic in
# "random.py" without worrying about (pseudo-)random number generators.
def test_sample_passes_rejection():
    with patch("numpy.random.random", CyclicReturner([0.7, 0.6])):
        assert( testmod.sample() == 0.7 )

def test_sample_rejects_first_pass():
    with patch("numpy.random.random", CyclicReturner([0.7, 0.8, 0.6, 0.5])):
        assert( testmod.sample() == 0.6 )

def fixed_random_integer(low, high):
    return 5

# In points/random.py we do "from numpy.random import randint as _randint" and so the
# symbol we need to 'patch' is "points.random._randint" and _not_
# "numpy.random.randint".  See "Where to patch", currently at:
#    https://docs.python.org/3/library/unittest.mock.html?highlight=patch#id5
# Notice also that we cannot patch "testmod.randint" as "testmod" is just a
# local name.
#
# By the way, why not just "from numpy.random import randint" ??
# Because then Sphinx will try to create documentation, which involves it getting
# itself into the numpy source code, which doesn't end entirely well.
@patch("points.random._randint", fixed_random_integer)
def test_sample2():
    assert( testmod.sample2() == 5 )
