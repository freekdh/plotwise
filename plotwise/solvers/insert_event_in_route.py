from typing import List
from plotwise.problem.demand import Event
from .exceptions import NoSolutionException


class InsertEventInRouteSolver:
    def __init__(self):
        pass

    def solve(self, event: Event, route: List[Event]):
        try:
            return route[:-1] + [event] + [route[-1]]
        except AttributeError:
            raise NotImplementedError