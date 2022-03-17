def recursive_sum(array):
    """write a functions that recieve a list and output the sum of the elements.
    exercise 4.1
    """
    #define a base case
    if len(array) == 1:
        return array[0]
    else: #recursion case
        return array[0] + recursive_sum(array[1:])    

def recursive_count_items(array):
    """write a function that counts elements of a list in a recursive way.
    exercise 4.2
    """
    # define a base case
    if len(array) == 1:
        return 1
    else: #recurive count
        return 1 + recursive_count_items(array[1:])

def recursive_max_value(array):
    """write a function that finds the greatest value in a list in a recursive way
    exercise 4.3
    """
    # define a base case
    if len(array) == 1:
        return array[0]
    else:
        max_value = recursive_max_value(array[1:])
        return max_value if max_value > array[0] else array[0]