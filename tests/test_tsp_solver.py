import pytest
from unittest.mock import Mock
from math import pi, sin, cos
from plotwise.problem.demand import Coordinate
from plotwise.solvers.traveling_salesman_problem import TSPSolver
from plotwise.problem.environment import ProblemEnvironment


@pytest.fixture
def problem_environment():
    depot_coordinate = Coordinate(1, 0)
    return ProblemEnvironment(depot_coordinate)


@pytest.fixture
def tsp_solver(problem_environment):
    return TSPSolver(problem_environment)


def test_solve(tsp_solver):
    # Put some locations in a circle. Shortest route should follow the.
    n_locations = 10
    locations = [
        Mock(
            coordinate=Coordinate(
                x=cos(2 * pi * ((i + 0.01) / n_locations)),
                y=sin(2 * pi * ((i + 0.01) / n_locations)),
            )
        )
        for i in range(n_locations - 1)
    ]
    solution = tsp_solver.solve(set(locations))

    assert set(locations).issubset(set(solution.route))
    assert len(solution.route) == len(locations) + 2  # two for the origin

    positions = [solution.route.index(location) for location in locations]

    assert positions == list(range(1, 10, 1)) or positions == list(
        reversed(list(range(1, 10, 1)))
    )
