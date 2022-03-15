from typing import List
def find_lowest_index(array: List[int]):
    lowest_value = array[0]
    lowest_value_index = 0
    for i in range(1, len(array)):
        if array[i] < lowest_value:
            lowest_value = array[i]
            lowest_value_index = i
    return lowest_value_index

def selection_sort_algo(array: List[int]):
    new_array = []
    for _ in range(len(array)):
        get_lowest_index = find_lowest_index(array)
        new_array.append(array.pop(get_lowest_index))
    return new_array
