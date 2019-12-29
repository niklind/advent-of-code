import day4.part2
import pytest


@pytest.mark.parametrize("password, expected",
                         [(112233, True),
                          (123444, False),
                          (111122, True)])
def test_part2(password, expected):
    assert expected == day4.part2.validate_password(password)
