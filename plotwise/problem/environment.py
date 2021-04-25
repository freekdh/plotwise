from typing import Iterable
from math import sqrt
from functools import lru_cache
from plotwise.problem.demand import Coordinate


class ProblemEnvironment:
    @lru_cache(maxsize=None)
    def get_distance(self, coordinate1: Coordinate, coordinate2: Coordinate) -> float:
        d_x = abs(coordinate1.x - coordinate1.x)
        d_y = abs(coordinate1.y - coordinate2.y)
        return sqrt(d_x ** 2 + d_y ** 2)
