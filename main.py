from itertools import takewhile

from plotwise.problem.demand import Coordinate, Demand, Event
from plotwise.problem.vehicle import Vehicle
from plotwise.problem.environment import ProblemEnvironment
from plotwise.solvers.traveling_salesman_problem import TSPSolver


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


if __name__ == "__main__":
    demand = Demand.from_file_50_50(
        file_path="data/homberger_200_customer_instances/C1_2_1.TXT"
    )
    vehicle = Vehicle(capacity_limit=500)

    deliveries = set(get_deliveries_for_vehicle(demand, vehicle))

    problem_environment = ProblemEnvironment(depot_coordinate=Coordinate(0, 0))

    tsp_solver = TSPSolver(problem_environment, max_seconds=100)
    solution = tsp_solver.solve(deliveries)

    print(solution.route)