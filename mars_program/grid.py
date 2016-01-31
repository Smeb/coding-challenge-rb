"""Grid module for coding challenge
"""
from enum import Enum

class Grid:
    """Grid class manages bounds of a square Y x Z grid, where Y can be
    any value between 1 and 50 inclusive

    Grid expects correct input - (Int, Int)
    """

    def __init__(self, x, y):
        if x <= 0:
            self._max_x = 0
        elif x >= 50:
            self._max_x = 50
        else:
            self._max_x = x
        if y <= 0:
            self._max_y = 0
        elif y >= 50:
            self._max_y = 50
        else:
            self._max_y = y
        self._scented = set()

    @property
    def max_x(self):
        """max_x is intended to be readonly outside the class"""
        return self._max_x

    @property
    def max_y(self):
        """max_y is intended to be readonly outside the class"""
        return self._max_y

    def query_x_y(self, robot, new_x, new_y):
        """Informs the robot if the grid square queried is passable,
    scented, or impassable"""
        if self.in_bounds(new_x, new_y):
            return QueryResult.passable
        elif (robot.x, robot.y) in self._scented:
            return QueryResult.scented
        else:
            self._scented.add((robot.x, robot.y))
            return QueryResult.impassable

    def in_bounds(self, x, y):
        """Returns true if x, y tuple are in bounds, false otherwise"""
        return x >= 0 and x <= self.max_x and y >= 0 and y <= self.max_y

class QueryResult(Enum):
    """Three possible states from driving into a square:
    impassable - robot is now doomed
    passable   - robot drives into valid square
    scented    - robot tries to drive off grid but is warned
    """
    impassable = 0
    passable = 1
    scented = 2
