"""Main module for application"""
import re

from mars_program import io
from mars_program import robot

def sim_robot(the_robot, directions):
    """execute robot directions character by character"""
    for char in directions:
        if char == 'F':
            the_robot.drive_forwards()
        if char == 'L':
            the_robot.turn_left()
        if char == 'R':
            the_robot.turn_right()

def read_input():
    """wasn't sure if all robots should be processed sequentially after
    input is recieved, or if processing should be done as robots are
    entered. As it stands robots are processed as entered, as no
    terminal was defined.
    """
    the_grid = io.get_grid_info()
    while True:
        the_robot = io.build_robot(the_grid)
        directions = io.gen_directions()

        sim_robot(the_robot, directions)
        print('{:d} {:d} {:s}'.format(the_robot.x, the_robot.y,
                                      robot.parse_heading(the_robot.heading)), end="")
        if the_robot.state == robot.State.fail:
            print(" LOST")
        else:
            print()
        print()

if __name__ == "__main__":
    try:
        read_input()
    except KeyboardInterrupt:
        pass
