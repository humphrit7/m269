def binary_search(a_list, first, last, target):
    """

    Parameters
    ----------
    a_list - a sorted list of integers
    first - an integer 0<=first<len(a_list)
    last - an integer <len(a_list)
    target - an integer

    Returns
    -------
    The index of a_list where target should be inserted to
    preserve the order of the list - integer
    """
    if first > last:
        return first
    elif (first <= last) and (target > a_list[last]):
        return last + 1
    else:
        middle = first + ((last-first) // 2)
        if a_list[middle] == target:
            return middle
        if target < a_list[middle]:
            return binary_search(a_list, first, middle-1, target)
        else:
            return binary_search(a_list, middle+1, last, target)


print(5, 1, binary_search([2, 5, 8, 11, 17], 0, 4, 5))
print(9, 3, binary_search([2, 5, 8, 11, 17], 0, 4, 9))
print(11, 3, binary_search([2, 5, 8, 11, 17], 0, 4, 11))
print(2,0, binary_search([2, 5, 8, 11, 17], 0, 4, 2))
print(8,2, binary_search([2, 5, 8, 11, 17], 0, 4,8))
print(17,4, binary_search([2, 5, 8, 11, 17], 0, 4, 17))
print(0, 0, binary_search([2, 5, 8, 11, 17], 0, 4, 0))
print(20, 5, binary_search([2, 5, 8, 11, 17], 0, 4, 20))