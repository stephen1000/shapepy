""" Lines in 3D space """

from shapepy.pieces import Point
from typing import List, Optional


class Line(object):
    """ A pair of points """

    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end

    def trace(
        self,
        number: Optional[int] = 10,
        interval: Optional[float] = None,
        inclusive: bool = True,
    ) -> List[Point]:
        """ Return points between ``Line.start`` and ``Line.end``. Default behavior is to return 11 total points, ``self.start``,
        ``self.end``, and 9 points evenly distributed in-between the two (e.g. for points (0, 0, 0) and (20,20,20) the 
        return would be [(0,0,0), (2,2,2), (4, 4, 4), (6, 6, 6), (8, 8, 8), (10, 10, 10), (12,12,12), (14,14,14), (16,16,16),
        (18,18,18), (20,20,20)])

        :param number: Number of points to return. Default 10. 
        """
        points: List[Point] = [self.start]
        if number and interval:
            points
        elif number:
            points
        elif interval:
            points
        else:
            raise ValueError("One of `number` or `interval` must be specified")

        if inclusive:
            points.append(self.end)
        return points

