"""
A point in 3D Space
"""


class Point(object):
    """ A point in 3D space """

    def __init__(self, x: int = 0, y: int = 0, z: int = 0):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other: object):
        """ Add two points' coordinates together """
        if not isinstance(other, Point):
            raise TypeError("`other` must be of type `Point`!")
        return Point(x=self.x + other.x, y=self.y + other.y, z=self.z + other.z)

    def __iter__(self):
        """ Loop over self.coordinates """
        for coordinate in [self.x, self.y, self.z]:
            yield coordinate

    def __eq__(self, other: object):
        """ True if the other point has the same coordinates """
        if not isinstance(other, Point):
            raise TypeError("`other` must be of type `Point`!")
        return all(_ for _ in (self.x == other.x, self.y == other.y, self.z == other.z))

