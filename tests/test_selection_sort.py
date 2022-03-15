from ch02.selection_sort import find_lowest_index, selection_sort_algo
import pytest
def test_find_lowest_index_last_position():
    input_list = sorted([1,2,3,4,5], reverse=True)
    assert find_lowest_index(input_list) == 4

def test_find_lowest_index_first_position():
    input_list = sorted([1,2,3,4,5])
    assert find_lowest_index(input_list) == 0

@pytest.mark.parametrize("input_list", [[0, 1], [3,2,5,10], [100, 1, 200, 20, 30, 50, 70]])
def test_selection_sort_algo(input_list):
    assertion_list = input_list.copy()
    assert selection_sort_algo(input_list) == sorted(assertion_list)