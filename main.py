from plotwise.problem.demand import Demand
from plotwise.problem.vehicle import Vehicle
from plotwise.problem.environment import ProblemEnvironment


def solve_problem(
    demand: Demand, vehicle: Vehicle, problem_environment: ProblemEnvironment
):
    pass


if __name__ == "__main__":
    demand = Demand.from_file_50_50(
        file_path="data/homberger_200_customer_instances/C1_2_1.TXT"
    )
    vehicle = Vehicle(capacity_limit=1000)
    problem_environment = ProblemEnvironment()

    solve_problem(demand, vehicle, problem_environment)