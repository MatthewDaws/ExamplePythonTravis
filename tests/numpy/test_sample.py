import points.numpy.sample as sample

def test_sample():
    assert abs(sample.compute_average() - 0.5) < 0.1