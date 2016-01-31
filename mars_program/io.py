"""io functions for mars_program coding challenge"""
import re
from mars_program import grid
from mars_program import robot

def get_grid_info():
    """get the coordinates as an XX YY pair where both values are 0-59"""
    result = None
    while result is None:
        result = re.match('[1-5]{0,1}[0-9] [1-5]{0,1}[0-9]', input())
        if result is None:
            print('Input invalid - enter data in the form XX YY' +
                    ' where XX, YY are numbers 0-59')
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
        if result is None:
            print('Input invalid - enter data in the form XX YY D' +
                  ' where XX, YY are numbers 0-59 and D is a direction')
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
        if result is None:
            print('input invalid, enter data as a string of letters' +
                  ' F, L, R with no spaces (i.e FFLLLRR)')
    return result.group()
