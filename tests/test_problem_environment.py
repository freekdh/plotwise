from plotwise.problem.demand import Coordinate
from unittest.mock import Mock
import math
from plotwise.problem.environment import ProblemEnvironment


def test_distance():
    problem_environment = ProblemEnvironment(None)

    distance = problem_environment.get_distance(Coordinate(1, 5), Coordinate(-10, 5))
    assert distance == 11

    distance = problem_environment.get_distance(Coordinate(5, 5), Coordinate(0, 0))
    assert distance == math.sqrt(50)
