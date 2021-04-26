from collections import namedtuple
from typing import Set, Iterable
from dataclasses import dataclass
from os import path
from warnings import warn
import math
import re


@dataclass(frozen=True)
class Coordinate:
    x: int
    y: int


@dataclass(frozen=True, eq=False)
class Event:
    coordinate: Coordinate
    capacity: float

    @property
    def x(self):
        return self.coordinate.x

    @property
    def y(self):
        return self.coordinate.y


@dataclass(frozen=True, eq=False)
class Pickup(Event):
    def __str__(self):
        return f"Pickup {self.capacity} @({self.x},{self.y})"


@dataclass(frozen=True, eq=False)
class Delivery(Event):
    def __str__(self):
        return f"Delivery {self.capacity} @({self.x},{self.y})"


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

    def get_events(self) -> Iterable[Event]:
        with open(self._file_path) as file:
            return [
                self._get_event(line)
                for i, line in enumerate(file)
                if i >= self._from_line
            ]

    def _get_event(self, line: str) -> Event:
        customer_number, x, y, demand, read_time, due_date, service_time = line.split()
        coordinate = Coordinate(x=int(x), y=int(y))
        return Event(coordinate=coordinate, capacity=float(demand))


@dataclass(frozen=True, eq=False)
class Demand:
    deliveries: Set[Coordinate]
    pickups: Set[Coordinate]

    def has_delivery_event(self, x: int, y: int) -> bool:
        return any(delivery.x == x and delivery.y == y for delivery in self.deliveries)

    def has_pickup_event(self, x: int, y: int) -> bool:
        return any(pickup.x == x and pickup.y == y for pickup in self.pickups)

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
            event_deliveries = set(events[:n_deliveries])
            event_pickups = set(events[n_deliveries:])
        else:
            warn(f"No events found in {file_path}")
            event_deliveries, event_pickups = {}, {}

        deliveries = {Delivery(**event.__dict__) for event in event_deliveries}
        pickups = {Pickup(**event.__dict__) for event in event_pickups}

        return cls(deliveries=deliveries, pickups=pickups)
