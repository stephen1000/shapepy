""" Tests for the Point module """
import pytest
from shapepy.pieces.point import Point


@pytest.fixture
def point():
    """ A predefined point """
    return Point(x=1, y=2, z=3)


def test_iter(point: Point):
    """ Assert a point iterates over x, y, and z """
    iterator = (_ for _ in point)
    assert next(iterator) == 1
    assert next(iterator) == 2
    assert next(iterator) == 3
    with pytest.raises(StopIteration):
        next(iterator)


def test_eq(point: Point):
    """ Assert equallity is true when appropriate """
    assert point == Point(1, 2, 3)
    assert point != Point(3, 2, 1)


def test_add(point: Point):
    """ Assert adding two points results in a point with their coordinates added """
    assert point + Point(3, 2, 1) == Point(4, 4, 4)
    assert point + Point(0, 0, 0) == point