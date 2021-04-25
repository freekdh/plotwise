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
    deliveries = set(demand_from_file.deliveries)
    assert len(deliveries) == expected_n_deliveries
    assert demand_from_file.has_delivery_event(x=10, y=137)


@pytest.mark.parametrize(
    "file_path, expected_n_pickups",
    [("data/homberger_200_customer_instances/C1_2_1.TXT", 100)],
)
def test_demand_from_file_pickups(file_path, expected_n_pickups):
    demand_from_file = Demand.from_file_50_50(file_path)
    pickups = set(demand_from_file.pickups)
    assert len(pickups) == expected_n_pickups
    assert demand_from_file.has_pickup_event(x=4, y=23)
