def recursive_sum(array):
    """write a functions that recieve a list and output the sum of the elements."""
    #define a base case
    if len(array) == 1:
        return array[0]
    else: #recursion case
        return array[0] + recursive_sum(array[1:])    
