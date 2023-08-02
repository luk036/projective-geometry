from projective_geometry.pg_common import dot_product, cross_product


def test_dot_product():
    assert dot_product([1, 2, 3], [4, 5, 6]) == 32


def test_cross_product():
    assert cross_product([1, 2, 3], [4, 5, 6]) == [-3, 6, -3]
