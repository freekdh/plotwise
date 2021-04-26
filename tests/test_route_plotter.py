from unittest.mock import Mock
import pytest

from plotwise.problem.demand import Coordinate
from plotwise.route_plotter import plot_route


@pytest.fixture
def test_events():
    return [
        Mock(coordinate=Coordinate(1, 2)),
        Mock(coordinate=Coordinate(5, 1)),
        Mock(coordinate=Coordinate(-10, -3)),
        Mock(coordinate=Coordinate(1, 2)),
    ]


def test_route_plotter(test_events):
    fig, ax = plot_route(test_events)
    fig.savefig("test.png")
