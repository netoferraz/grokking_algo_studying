from ch04.divide_and_conquer import recursive_sum
import pytest
@pytest.mark.parametrize('expected, test_input', [(12, [2,4,6]), (5, [5]), (10, [8,2]), (20, [10,5,3,2])])
def test_recursive_sum(expected, test_input):
    assert expected == recursive_sum(test_input)