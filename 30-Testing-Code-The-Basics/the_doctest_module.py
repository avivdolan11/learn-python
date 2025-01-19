def sum_of_lists(numbers):
    """ Return sum of all numbers in list
    >>> sum_of_lists([1,2,3])
    6
    >>> sum_of_lists([4,5,6])
    15
    """
    total = 0
    for number in numbers:
        total += number

    return total

if __name__ == "__main__":
    import doctest
    doctest.testmod()