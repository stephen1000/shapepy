""" A collection of points with segments between each """
from typing import List, Union

from shapepy.pieces import Point, Segment


class Line(object):
    """ A collection of points with segments between each """

    def __init__(self, points:List[Point]):
        self.points = points

    @property
    def segments(self):
        """ A list of segments between each point in the line """
        for index in range(len(self.points)):
            yield Segment(self.points[index], self.points[index+1])

    def __iter__(self):
        """ Loop over the segments of the line """
        for segment in self.segments:
            yield segment

    def append(self, point:Point):
        """ Add a point to the end of the Line

        :param point: Point to append to the Line
        :type point: shapepy.pieces.point.Point
        """
        self.points.append(point)

    def insert(self, pos:int, point:Point):
        """ Insert ``point`` into the Line at position ``pos``"""
        self.points.insert(pos, point)


