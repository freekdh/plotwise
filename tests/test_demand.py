import pytest

from plotwise.problem.demand import Demand, Coordinate


@pytest.fixture(scope="session")
def demand():
    return Demand(
        deliveries={Coordinate(2, 5), Coordinate(-10, -9)}, pickups={Coordinate(1, 1)}
    )


def test_demand(demand):
    pass
