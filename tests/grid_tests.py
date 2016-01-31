from nose.tools import *
from  mars_program import grid
from  mars_program import robot

the_grid = None
the_robot = None

def setup():
    global the_grid
    global the_robot
    the_grid = grid.Grid(10, 10)
    the_robot = robot.Robot(the_grid, 10, 10, robot.Heading.north)

def teardown():
    print ("Teardown")

def test_grid_init_normal():
    x = 10
    y = 20
    the_grid = grid.Grid(x, y)
    assert_equal(x, the_grid.max_x)
    assert_equal(y, the_grid.max_y)

def test_grid_init_low_x():
    x = -5
    y = 20
    the_grid = grid.Grid(x, y)
    assert_equal(0, the_grid.max_x)
    assert_equal(y, the_grid.max_y)

def test_grid_init_low_y():
    x = 10
    y = -5
    the_grid = grid.Grid(x, y)
    assert_equal(x, the_grid.max_x)
    assert_equal(0, the_grid.max_y)

def test_grid_init_high_x():
    x = 100
    y = 20
    the_grid = grid.Grid(x, y)
    assert_equal(50, the_grid.max_x)
    assert_equal(y, the_grid.max_y)

@with_setup(setup, teardown)
def test_query_passable():
    assert_equals(the_grid.query_x_y(the_robot, 9, 9), grid.QueryResult.passable)

@with_setup(setup, teardown)
def test_query_robot_lost():
    assert_equals(the_grid.query_x_y(the_robot, 10, 11),
            grid.QueryResult.impassable)

@with_setup(setup, teardown)
def test_query_robot_scented():
    the_grid._scented.add((the_robot.x, the_robot.y))
    assert_equals(the_grid.query_x_y(the_robot, 10, 11),
            grid.QueryResult.scented)

@with_setup(setup, teardown)
def test_is_in_bounds():
    assert_equals(the_grid.in_bounds(0, 0), True)

@with_setup(setup, teardown)
def test_is_not_in_bounds():
    assert_equals(the_grid.in_bounds(11, 11), False)
