from collections import namedtuple
from typing import Set
from dataclasses import dataclass

Coordinate = namedtuple("Coordinate", "x y")


@dataclass(frozen=True, eq=False)
class Demand:
    deliveries: Set[Coordinate]
    pickups: Set[Coordinate]
