"""Main module for application"""
import re

from mars_program import grid
from mars_program import robot

def get_grid_info():
    """get the coordinates as an XX YY pair where both values are 0-59"""
    result = None
    while result is None:
        result = re.match('[1-5]{0,1}[0-9] [1-5]{0,1}[0-9]', input())
    grid_values = result.group().split()
    # split values and cast to int
    the_grid = grid.Grid(int(grid_values[0]), int(grid_values[1]))
    return the_grid

def get_robot_info():
    """get the robot initialisers as an XX YY D group where both numeric
    values are 0-59 and D is N | E | S | W"""
    if not hasattr(get_robot_info, "robot_regex"):
        get_robot_info.robot_regex = re.compile('[1-5]{0,1}[0-9] [1-5]{0,1}[0-9] [N|E|S|W]')
    result = None
    while result is None:
        result = get_robot_info.robot_regex.match(input())
    return result.group()

def identify_heading(values):
    """maps a letter N E S W to the respective heading - could be done
    with a dict"""
    heading_value = values[2] # input is x y D where D is direction
    if heading_value == 'N':
        return robot.Heading.north
    elif heading_value == 'E':
        return robot.Heading.east
    elif heading_value == 'S':
        return robot.Heading.south
    else:
        return robot.Heading.west


def build_robot(the_grid):
    """return a robot object after getting values from user input"""
    values = get_robot_info().split()
    heading = identify_heading(values)
    return robot.Robot(the_grid, int(values[0]), int(values[1]), heading)

def get_directions():
    """get the directions to follow from the user as a string of LRF
    symbols"""
    if not hasattr(get_directions, "direction_regex"):
        get_directions.direction_regex = re.compile('[F|L|R]{1,100}')
    result = None
    while result is None:
        result = get_directions.direction_regex.match(input())
    return result.group()

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
    the_grid = get_grid_info()
    while True:
        the_robot = build_robot(the_grid)
        directions = get_directions()
        sim_robot(the_robot, directions)
        print('{:d} {:d} {:s}'.format(the_robot.x, the_robot.y,
                                      robot.parse_heading(the_robot.heading)), end="")
        if the_robot.state == robot.State.fail:
            print(" LOST")
        else:
            print()

if __name__ == "__main__":
    try:
        read_input()
    except KeyboardInterrupt:
        pass
    except:
        print('\nSorry - there was an error and your rover was lost' +
              ' on Mars :(')
