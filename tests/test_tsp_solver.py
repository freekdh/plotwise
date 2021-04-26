import pytest
from unittest.mock import Mock

from plotwise.problem.demand import Coordinate
from plotwise.solvers.traveling_salesman_problem import TSPSolver
from plotwise.problem.environment import ProblemEnvironment


@pytest.fixture
def problem_environment():
    depot_coordinate = Coordinate(0, 0)
    return ProblemEnvironment(depot_coordinate)


@pytest.fixture
def tsp_solver(problem_environment):
    return TSPSolver(problem_environment)


def test_solve(tsp_solver):
    location1 = Mock(coordinate=Coordinate(1, 1))
    location2 = Mock(coordinate=Coordinate(-1, 1))
    location3 = Mock(coordinate=Coordinate(1, -1))
    location4 = Mock(coordinate=Coordinate(-1, -1))
    solution = tsp_solver.solve({location1, location2, location3, location4})

    assert {location1, location2, location3, location4}.issubset(set(solution.route))
    assert len(solution.route) == 4 + 2  # two for the origin
