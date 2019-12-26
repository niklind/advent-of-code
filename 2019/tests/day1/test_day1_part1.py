import day1.part1
import pytest


@pytest.mark.parametrize("mass, fuel_required",
                         [(12, 2),
                          (14, 2),
                          (1969, 654),
                          (100756, 33583)])
def test_part1(mass: int, fuel_required: int):
    assert fuel_required == day1.part1.fuel_requirement(mass)
