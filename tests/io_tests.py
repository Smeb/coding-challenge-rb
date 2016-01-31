from nose.tools import *
from mars_program import io

def test_recv_directions():
    """recv_directions should return regex result with group equal to
    input on success"""
    string = "LLLRRFFF"
    result = io.recv_directions(string)
    assert_equals(result.group(), string)

def recv_robot_info():
    """recv_robot_info should return regex result with group equal to
    input on success"""
    string = "10 10 W"
    result = io.recv_robot_info(string)
    assert_equals(result.group(), string)

def test_recv_directions_fail():
    """recv_directions should return None on fail"""
    string = "CHAMPLFLFLFL"
    result = io.recv_directions(string)
    assert_equals(result, None)

def test_recv_robot_info_fail():
    """recv_robot_info should return None on fail"""
    string = "CHAMP 32 21 W"
    result = io.recv_directions(string)
    assert_equals(result, None)
