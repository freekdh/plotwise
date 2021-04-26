from plotwise.problem.demand import Coordinate
from unittest.mock import Mock

from plotwise.problem.environment import ProblemEnvironment


def test_distance():
    Mock()
    problem_environment = ProblemEnvironment(None)

    distance = problem_environment.get_distance(Coordinate(1, 5), Coordinate(-10, 5))
    assert distance == 11