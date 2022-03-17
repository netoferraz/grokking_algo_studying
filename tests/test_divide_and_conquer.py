from ch04.divide_and_conquer import recursive_sum, recursive_count_items
import pytest
@pytest.mark.parametrize('expected, test_input', [(12, [2,4,6]), (5, [5]), (10, [8,2]), (20, [10,5,3,2])])
def test_recursive_sum(expected, test_input):
    assert expected == recursive_sum(test_input)

@pytest.mark.parametrize('expected, test_input', [(3, [2,4,6]), (1, [5]), (2, [8,2]), (4, [10,5,3,2])])
def test_recursive_count_items(expected, test_input):
    assert expected == recursive_count_items(test_input)