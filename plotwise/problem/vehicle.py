from dataclasses import dataclass


@dataclass(frozen=True)
class Vehicle:
    capacity_limit: float
