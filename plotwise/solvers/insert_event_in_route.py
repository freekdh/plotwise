from plotwise.problem.vehicle import Vehicle
from typing import List
from plotwise.problem.demand import Event
from .exceptions import NoSolutionException


class InsertEventInRouteSolver:
    def __init__(self, vehicle: Vehicle):
        """Using a heuristic to insert the event in the route resulting in the least increase in route length.

        Args:
            vehicle (Vehicle): The vehicle that is exercising the route
        """
        self._vehicle = vehicle

    def solve(self, event: Event, route: List[Event]) -> List[Event]:
        if event.capacity > self._vehicle.capacity_limit:
            raise NoSolutionException(
                f"Cannot add {event}, its capacity of {event.capacity} exceeds the vehicle max capacity {self._vehicle.capacity_limit}"
            )
        else:
            # TODO most simple solution now, just append to the end. We are not optimizing the route, just the number of deliveries so this is fine.
            # Of course if the second objective is to also find a short route I would put some more effort here to find a proper place for the pickup.
            return route[:-1] + [event] + [route[-1]]