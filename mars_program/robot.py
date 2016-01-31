"""Robot module for coding challenge
"""

from enum import IntEnum
from enum import Enum
from mars_program import grid

class Robot:
    """Robot class is responsible for maintaining knowledge of its own
    position and heading. Refers to encapsulated Grid class to find out
    if a move is valid or not

    Robot expects correct input (grid, int, int, Heading)
    """
    def __init__(self, the_grid, x, y, heading):
        self._grid = the_grid
        if x <= 0:
            self._x_pos = 0
        elif x >= 50:
            self._x_pos = 50
        else:
            self._x_pos = x
        if y <= 0:
            self._y_pos = 0
        elif y >= 50:
            self._y_pos = 50
        else:
            self._y_pos = y
        self._heading = heading
        if the_grid is not None:
            self._state = (State.success if self._grid.in_bounds(x, y)
                           else State.fail)

    @property
    def x(self):
        """x is intended to be readonly outside the class"""
        return self._x_pos

    @property
    def y(self):
        """y is intended to be readonly outside the class"""
        return self._y_pos

    @property
    def heading(self):
        """heading is intended to be readonly outside the class"""
        return self._heading

    @property
    def state(self):
        """state is intended to be readonly outside the class"""
        return self._state

    def _target_x_y_mappings(self):
        """gives the next grid point for the robot based on its current
        position"""
        switch = {
            Heading.north: (self.x, self.y + 1),
            Heading.east: (self.x + 1, self.y),
            Heading.south: (self.x, self.y - 1),
            Heading.west: (self.x - 1, self.y)
            }
        return switch

    def drive_forwards(self):
        """attempts to drive forwards, using the grid as a reference to
        decide how to alter its position and state

        if grid is valid drive into grid

        if grid is invalid and current grid point is scented do not
        drive in

        if grid is invalid and current grid point is not scented, fail

        """
        if self._state == State.fail:
            return self._state
        target = self._target_x_y_mappings().get(self._heading)
        result = self._grid.query_x_y(self, target[0], target[1])
        if result == grid.QueryResult.impassable:
            # don't update position, robot is now dead
            self._state = State.fail
        else:
            if result == grid.QueryResult.passable:
                # update to position if coord wasn't scented
                self._x_pos = target[0]
                self._y_pos = target[1]
            self._state = State.success
        return self._state

    def turn_left(self):
        """Generate a new heading based on current heading. Uses modulo
        calculation for transition from N -> W
        """
        if self._state == State.fail:
            return
        self._heading = Heading((self._heading - 1) % 4)

    def turn_right(self):
        """Generate a new heading based on current heading. Uses modulo
        calculation for transition from W -> N
        """
        if self._state == State.fail:
            return
        self._heading = Heading((self._heading + 1) % 4)

def parse_heading(heading):
    """Helper method for parsing headers into character strings
    """
    if heading == Heading.north:
        return 'N'
    if heading == Heading.east:
        return 'E'
    if heading == Heading.south:
        return 'S'
    if heading == Heading.west:
        return 'W'


class Heading(IntEnum):
    """Enum version of all heading states. If a degree based heading was
    used then would instead use atan2(angle) for normalisation, but all
    direction chages are currently cardinal"""
    __order__ = "north east south west"
    north = 0
    east = 1
    south = 2
    west = 3

class State(Enum):
    """Enum version of states - state is either fail or succeed. Could
    probably also use a simple flag, but using an Enum makes changing
    behaviour easier"""
    fail = 0
    success = 1
