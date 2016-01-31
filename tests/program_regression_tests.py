from nose.tools import *
from mars_program import grid
from mars_program import robot

def test_full_run_single_robot_1():
    """Test case from docs
    5 3
    1 1 E
    RFRFRFRF
    """
    the_grid = grid.Grid(5, 3)
    the_robot = robot.Robot(the_grid, 1, 1, robot.Heading.east)
    the_robot.turn_right()
    the_robot.drive_forwards()
    the_robot.turn_right()
    the_robot.drive_forwards()
    the_robot.turn_right()
    the_robot.drive_forwards()
    the_robot.turn_right()
    the_robot.drive_forwards()
    assert_equals((the_robot.x, the_robot.y), (1, 1))
    assert_equals(the_robot._heading, robot.Heading.east)

    """Test case from docs
    5 3
    3 2 N
    FRRFLLFFRRFLL
    """
    the_robot = robot.Robot(the_grid, 3, 2, robot.Heading.north)
    the_robot.drive_forwards()
    the_robot.turn_right()
    the_robot.turn_right()
    the_robot.drive_forwards()
    the_robot.turn_left()
    the_robot.turn_left()
    the_robot.drive_forwards()
    the_robot.drive_forwards()
    the_robot.turn_right()
    the_robot.turn_right()
    the_robot.drive_forwards()
    the_robot.turn_left()
    the_robot.turn_left()
    assert_equals((the_robot.x, the_robot.y), (3, 3))
    assert_equals(the_robot._heading, robot.Heading.north)


    """Test case from docs
    0 3 W
    LLFFFLFLFL
    """
    the_robot = robot.Robot(the_grid, 0, 3, robot.Heading.west)
    the_robot.turn_left()
    the_robot.turn_left()
    the_robot.drive_forwards()
    the_robot.drive_forwards()
    the_robot.drive_forwards()
    the_robot.turn_left()
    the_robot.drive_forwards()
    the_robot.turn_left()
    the_robot.drive_forwards()
    the_robot.turn_left()
    assert_equals((the_robot.x, the_robot.y), (2, 3))
    assert_equals(the_robot._heading, robot.Heading.south)
