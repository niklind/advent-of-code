import day8.part2
import pytest


@pytest.mark.parametrize("image, height, width, expected",
                         [([0, 2, 2, 2, 1, 1, 2, 2, 2, 2, 1, 2, 0, 0, 0, 0], 2, 2, [[0, 1], [1, 0]])])
def test_part2(image, height, width, expected):
    assert expected == day8.part2.find_layer(image, height, width)
