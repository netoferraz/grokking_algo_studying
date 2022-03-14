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

if __name__ == "__main__":
    abc = binary_search(list(range(1,101)), 7)
    print(abc)