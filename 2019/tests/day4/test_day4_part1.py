import day4.part1
import pytest


@pytest.mark.parametrize("password, expected",
                         [(111111, True),
                          (223450, False),
                          (123789, False)])
def test_part1(password, expected):
    assert expected == day4.part1.validate_password(password)
