from abc import abstractmethod
from mip import Model, xsum, minimize, BINARY, CBC
from dataclasses import dataclass
import networkx as nx
from abc import ABC
from typing import List, Set, Iterable
from itertools import product
from plotwise.problem.environment import ProblemEnvironment
from plotwise.problem.demand import Coordinate, Event


@dataclass(frozen=True)
class TSPSolution:
    route: List


class TSPSolver:
    def __init__(self, problem_environment: ProblemEnvironment):
        self._problem_environment = problem_environment

    def solve(self, places: Set[Event]) -> TSPSolution:
        places = [self._problem_environment.depot] + list(places)
        route = list(self._get_shortest_route(places=places))
        return TSPSolution(route=route)

    def _get_distance(self, location1, location2) -> float:
        return self._problem_environment.get_distance(
            location1.coordinate, location2.coordinate
        )

    def _get_shortest_route(self, places: List[Event]) -> Iterable[Event]:
        """Solves the TSP using the MIP package

        Args:
            places ([Event]): The places that can be visited

        Raises:
            NoSolutionException: If no solution can be found

        Yields:
            [Event]: Events are yielded in order starting with the first station in places
        """

        n = len(places)
        V = set(range(n))

        model = Model(solver_name=CBC)
        x = [[model.add_var(var_type=BINARY) for j in V] for i in V]
        y = [model.add_var() for i in V]

        model.objective = minimize(
            xsum(
                self._get_distance(places[i], places[j]) * x[i][j] for i in V for j in V
            )
        )

        for i in V:
            model += xsum(x[i][j] for j in V - {i}) == 1

        # constraint : enter each city only once
        for i in V:
            model += xsum(x[j][i] for j in V - {i}) == 1

        # subtour elimination
        for (i, j) in product(V - {0}, V - {0}):
            if i != j:
                model += y[i] - (n + 1) * x[i][j] >= y[j] - n

        model.optimize()

        if model.num_solutions:
            yield places[0]
            nc = 0
            while True:
                nc = [i for i in V if x[nc][i].x >= 0.99][0]
                yield places[nc]
                if nc == 0:
                    break
            return
        else:
            raise NoSolutionException("Could not find a solution")


class NoSolutionException(Exception):
    pass
