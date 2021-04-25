from collections import namedtuple
from typing import Set, Iterable
from dataclasses import dataclass
from os import path


Coordinate = namedtuple("Coordinate", "x y")


@dataclass(frozen=True, eq=False)
class Demand:
    deliveries: Set[Coordinate]
    pickups: Set[Coordinate]

    @classmethod
    def from_file(cls, file_path: str) -> "Demand":
        demand_file_loader = DemandFileLoader(file_path=file_path)
        deliveries = set(demand_file_loader.get_deliveries())
        pickups = set(demand_file_loader.get_pickups())

        return cls(deliveries=deliveries, pickups=pickups)


class DemandFileLoader:
    def __init__(self, file_path: str):
        assert path.exists(file_path), f"Can't find file {file_path}"

    def get_deliveries(self) -> Iterable[Coordinate]:
        raise NotImplementedError

    def get_pickups(self) -> Iterable[Coordinate]:
        raise NotImplementedError