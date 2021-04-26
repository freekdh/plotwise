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
    n_locations = 10
    locations = [Mock(coordinate=Coordinate(0, i)) for i in range(n_locations)]
    solution = tsp_solver.solve(set(locations))

    assert set(locations).issubset(set(solution.route))
    assert len(solution.route) == len(locations) + 2  # two for the origin

    positions = [solution.route.index(location) for location in locations]

    assert positions == [
        _ + 1 for _ in range(len(solution.route[1:-1]))
    ] or positions == [_ + 1 for _ in reversed(list(range(len(solution.route[1:-1]))))]
