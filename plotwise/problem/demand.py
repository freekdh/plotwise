from collections import namedtuple
from typing import Set, Iterable
from dataclasses import dataclass
from os import path
from warnings import warn
import math
import re

Coordinate = namedtuple("Coordinate", "x y")


class DemandFileLoader:
    def __init__(self, file_path: str, from_line=9):
        """Load from file the events, starting from line 'from_line'

        Args:
            file_path (str): The file path with the events
            from_line (int, optional): Start line to read for events. Defaults to 10.
        """
        assert path.exists(file_path), f"Can't find file {file_path}"
        self._file_path = file_path
        self._from_line = from_line

    def get_events(self) -> Iterable[Coordinate]:
        with open(self._file_path) as file:
            return [
                self._get_event(line)
                for i, line in enumerate(file)
                if i >= self._from_line
            ]

    def _get_event(self, line: str) -> Coordinate:
        customer_number, x, y, demand, read_time, due_date, service_time = line.split()
        return Coordinate(x=int(x), y=int(y))


@dataclass(frozen=True, eq=False)
class Demand:
    deliveries: Set[Coordinate]
    pickups: Set[Coordinate]

    @classmethod
    def from_file_50_50(cls, file_path: str) -> "Demand":
        """Import events from file and split. First 50% of events are deliveries and rest is pickups.
        If number of events is uneven, n_deliveries == n_pickups + 1

        Returns:
            Demand
        """
        demand_file_loader = DemandFileLoader(file_path=file_path)
        events = list(demand_file_loader.get_events())

        if n_events := len(events):
            n_deliveries = math.ceil(n_events / 2)
            deliveries = set(events[:n_deliveries])
            pickups = set(events[n_deliveries:])
        else:
            warn(f"No events found in {file_path}")
            deliveries, pickups = {}, {}

        return cls(deliveries=deliveries, pickups=pickups)
