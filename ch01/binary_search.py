from typing import List
def binary_search(array: List[int], item:int):
    """If item exists in array, returns the index otherwise return None"""
    lower = 0
    high = len(array) -1
    while lower <= high:
        middle = (lower+high)//2
        guess = array[middle]
        if guess == item:
            return middle
        elif guess > item:
            #updates the highest position
            high = middle - 1
        else: # middle < item
            #updates the lowest position
            lower = middle + 1
    return None

def binary_search_number_of_steps(array: List[int], item:int):
    """If item exists in array, returns the index and number of steps otherwise return None and number of steps"""
    lower = 0
    high = len(array) -1
    number_of_steps = 0
    while lower <= high:
        middle = (lower+high)//2
        guess = array[middle]
        if guess == item:
            return middle, number_of_steps
        elif guess > item:
            number_of_steps += 1
            #updates the highest position
            high = middle - 1
        else: # middle < item
            number_of_steps += 1
            #updates the lowest position
            lower = middle + 1
    return None, number_of_steps


if __name__ == "__main__":
    item_index, nos = binary_search_number_of_steps(list(range(1,257)), 256)
    print(item_index, nos)