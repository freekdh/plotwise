from itertools import takewhile
from copy import copy
from typing import Set, List

from plotwise.problem.demand import Coordinate, Demand, Event
from plotwise.problem.vehicle import Vehicle
from plotwise.problem.environment import ProblemEnvironment
from plotwise.solvers.traveling_salesman_problem import TSPSolver
from plotwise.solvers.insert_event_in_route import InsertEventInRouteSolver
from plotwise.solvers.exceptions import NoSolutionException


def get_deliveries_for_vehicle(demand: Demand, vehicle: Vehicle) -> Event:
    """Sort deliveries by capacity and yield delivery until capacity limit is reached

    Args:
        demand (Demand)
        vehicle (Vehicle)

    Yields:
        Event
    """
    sorted_delivery_by_capacity = sorted(
        (delivery for delivery in demand.deliveries),
        key=lambda delivery: delivery.capacity,
    )

    sum_of_capacity = 0
    for delivery in sorted_delivery_by_capacity:
        if delivery.capacity + sum_of_capacity <= vehicle.capacity_limit:
            sum_of_capacity += delivery.capacity
            yield delivery
        else:
            return


def insert_pickup_event_in_route(
    current_route: List[Event],
    pickups: Set[Event],
    problem_environment: ProblemEnvironment,
):

    insert_event_in_route_solver = InsertEventInRouteSolver()

    best_route = None
    best_route_length = None
    for pickup in pickups:
        try:
            route_with_pickup = insert_event_in_route_solver.solve(
                event=pickup, route=copy(current_route)
            )
            route_length = problem_environment.get_route_distance(route_with_pickup)
            if best_route:
                if route_length < best_route_length:
                    best_route_length = route_length
                    best_route = route_with_pickup
            else:
                best_route_length = route_length
                best_route = route_with_pickup
        except NoSolutionException:
            pass

    return best_route


if __name__ == "__main__":
    demand = Demand.from_file_50_50(
        file_path="data/homberger_200_customer_instances/C1_2_1.TXT"
    )
    vehicle = Vehicle(capacity_limit=500)

    deliveries = set(get_deliveries_for_vehicle(demand, vehicle))

    problem_environment = ProblemEnvironment(depot_coordinate=Coordinate(0, 0))

    tsp_solver = TSPSolver(problem_environment, max_seconds=10)
    solution = tsp_solver.solve(deliveries)

    route_without_pickup = solution.route

    best_route = insert_pickup_event_in_route(
        current_route=route_without_pickup,
        pickups=demand.pickups,
        problem_environment=problem_environment,
    )

    if best_route:
        print(f"The proposed route to take is: {[str(event) for event in best_route]}")
    else:
        print("Could not insert a pickup in the route")
