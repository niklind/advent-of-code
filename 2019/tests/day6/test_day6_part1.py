import day6.part1
import pytest


@pytest.mark.parametrize("relations, expected",
                         [(['COM)B',
                            'B)C',
                            'C)D',
                            'D)E',
                            'E)F',
                            'B)G',
                            'G)H',
                            'D)I',
                            'E)J',
                            'J)K',
                            'K)L'], 42)])
def test_part1(relations, expected):
    assert expected == day6.part1.find_orbits(relations)
