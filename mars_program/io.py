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

def recv_robot_info(input):
    """get the robot initialisers as an XX YY D group where both numeric
    values are 0-59 and D is N | E | S | W. Error message is baked into
    class because it's relative to the regex used"""
    if not hasattr(recv_robot_info, "robot_regex"):
        recv_robot_info.robot_regex = re.compile('[1-5]{0,1}[0-9] [1-5]{0,1}[0-9] [N|E|S|W]')
    result = recv_robot_info.robot_regex.match(input)
    if result is None:
        print('Input invalid - enter data in the form XX YY D' +
              ' where XX, YY are numbers 0-59 and D is a direction')
    return result

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
    io_result = None
    while io_result is None:
        io_result = recv_robot_info(input())
    values = io_result.group().split()
    heading = identify_heading(values)
    return robot.Robot(the_grid, int(values[0]), int(values[1]), heading)

def gen_directions():
    """handles the loop for recv_directions"""
    result = None
    while result is None:
        result = recv_directions(input())
    return result.group()

def recv_directions(input):
    """get the directions to follow from the user as a string of LRF
    symbols. Error message is baked into class because it's relative to
    the regex used"""
    if not hasattr(recv_directions, "direction_regex"):
        recv_directions.direction_regex = re.compile('[F|L|R]{1,100}')
    result = recv_directions.direction_regex.match(input)
    if result is None:
        print('input invalid, enter data as a string of letters' +
                ' F, L, R with no spaces (i.e FFLLLRR)')
    return result
