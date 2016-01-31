from nose.tools import *
from  mars_program import grid
from  mars_program import robot

the_grid = None
def setup():
    the_grid = grid.Grid(10, 10)

def teardown():
    the_grid = None

@with_setup(setup, teardown)
def test_left_loop():
    """Start should equal end if four left turns"""
    the_robot = robot.Robot(the_grid, 0, 0, robot.Heading.north)
    for i in range(0, 4):
        the_robot.turn_left()
    assert_equals(the_robot._heading, robot.Heading.north)

@with_setup(setup, teardown)
def test_right_loop():
    """Start should equal end if four right turns"""
    the_robot = robot.Robot(the_grid, 0, 0, robot.Heading.north)
    for i in range(0, 4):
        the_robot.turn_right()
    assert_equals(the_robot._heading, robot.Heading.north)

def test_left_turn():
    """Turning left from north should yield west"""
    the_robot = robot.Robot(the_grid, 0, 0, robot.Heading.north)
    the_robot.turn_left()
    assert_equals(the_robot._heading, robot.Heading.west)


def test_right_turn():
    """Turning right from north should yield east"""
    the_robot = robot.Robot(the_grid, 0, 0, robot.Heading.north)
    the_robot.turn_right()
    assert_equals(the_robot._heading, robot.Heading.east)

