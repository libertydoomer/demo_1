import pytest
from car import Car


def test_drive(car):
    car.drive(100)
    assert car.mileage == 100


def test_refuel(car):
    car.refuel(10)
    assert car.mileage == 100


@pytest.mark.parametrize("mileage, refuel, expected_mileage", [
    (100, 10, 200),
    (50, 5, 100),
    (0, 20, 200),
])
def test_drive_and_refuel(mileage, refuel, expected_mileage):
    car = Car("Приора", "2007", mileage)
    car.refuel(refuel)
    assert car.mileage == expected_mileage
