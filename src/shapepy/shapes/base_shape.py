"""
Common class shared by all shapes
"""

from typing import List
from shapepy.pieces import Point, Line


class BaseShape(object):
    """ Common class shared by all shapes """

    def __init__(self):
        self.verticies: List[Point] = []
        

    def contains(self, point:Point):
        """ Defines whether a point is within the shape. Implement in subclasses to define behavior, """
        return False

    @property
    def edges(self) -> List[Line]:
        """ Return a list of lines between verticies """
        return