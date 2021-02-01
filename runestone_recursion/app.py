def recursive_factorial(num):
    """Determine the factorial of a number, recursively.
    
    >>> recursive_factorial(3)
    6
    >>> recursive_factorial(0)
    1

    """

    if num == 0:
        return 1
    
    if num == 1: 
        return num
    
    else:
        return num * recursive_factorial(num - 1)


def reverse_list(lst):
    """Reverse a list, recursively.
    
    >>> reverse_list([])
    []
    >>> reverse_list([1])
    [1]
    >>> reverse_list([1,2,3])
    [3, 2, 1]
    """

    if len(lst) < 2:
        return lst
    
    else:
        return [lst[-1]] + reverse_list(lst[:(len(lst) - 1)])