import pytest

from plotwise.problem.demand import Demand, Coordinate


@pytest.fixture(scope="session")
def example_demand():
    return Demand(
        deliveries={Coordinate(2, 5), Coordinate(-10, -9)}, pickups={Coordinate(1, 1)}
    )


def test_demand(example_demand):
    pass


@pytest.mark.parametrize(
    "file_path, expected_n_deliveries",
    [("data/homberger_200_customer_instances/C1_2_1.TXT", 101)],
)
def test_demand_from_file_deliveries(file_path, expected_n_deliveries):
    demand_from_file = Demand.from_file_50_50(file_path=file_path)
    assert len(set(demand_from_file.deliveries)) == expected_n_deliveries


@pytest.mark.parametrize(
    "file_path, expected_n_pickups",
    [("data/homberger_200_customer_instances/C1_2_1.TXT", 100)],
)
def test_demand_from_file_pickups(file_path, expected_n_pickups):
    demand_from_file = Demand.from_file_50_50(file_path)
    assert len(set(demand_from_file.pickups)) == expected_n_pickups
