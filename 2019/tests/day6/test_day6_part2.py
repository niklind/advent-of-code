import day6.part2
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
                            'K)L',
                            'K)YOU',
                            'I)SAN'], 4)])
def test_part1(relations, expected):
    assert expected == day6.part2.find_orbits(relations)
