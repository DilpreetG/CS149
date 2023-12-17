"""Test the dice module.

Name: YOUR NAME
Date: THE DATE
"""

from dice import roll_dice
from dice import are_valid
from dice import add_values
from dice import num_faces


def test_roll_dice():
    assert roll_dice(5) == ['Q', 'Q', '9', 'J', 'K']
    assert roll_dice(0, 1) == ['9']


def test_are_valid():
    assert are_valid(['A', 'K'])
    assert not are_valid(['1', '2', '3'])


def test_add_values():
    assert add_values(['10', '10', '10', '10']) == 40
    assert add_values([]) == -1


def test_num_faces():
    assert num_faces(['Q', '9', 'Q', '9'], 'Q') == 2
    assert num_faces(None, None) == -1
