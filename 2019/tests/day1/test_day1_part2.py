import day1.part2
import pytest


@pytest.mark.parametrize("mass, fuel_required",
                         [(14, 2),
                          (1969, 966),
                          (100756, 50346)])
def test_part2(mass: int, fuel_required: int):
    assert fuel_required == day1.part2.fuel_requirement(mass)
