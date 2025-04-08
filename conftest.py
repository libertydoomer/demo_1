import pytest
from car import Car

@pytest.fixture
def car():
    return Car("Приора", "2007")
