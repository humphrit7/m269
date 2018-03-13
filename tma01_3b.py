def least_common_in_sorted(numbers):
    """
    Finds the least common number in an unsorted list of
    integers. If there is more than one number with the
    same frequency, returns the rare number which
    appears last in the list .

    Inputs
    ------
    numbers - list - contains only integers

    Returns
    -------
    integer - the least common, or joint least common
              integer in the list.
    """
    leastCommon = numbers[0]
    currentCount = 0
    currentNumber = numbers[0]
    lowestCount = len(numbers)
    for i in range(len(numbers)):
        if numbers[i] == currentNumber:
            currentCount += 1
        else:
            if currentCount <= lowestCount:
                lowestCount = currentCount
                leastCommon = currentNumber
            currentNumber = numbers[i]
            currentCount = 1
    if currentCount <= lowestCount:
        leastCommon = currentNumber
    return leastCommon


print(least_common_in_sorted([1, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 5, 5]))
print(least_common_in_sorted([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 5]))
print(least_common_in_sorted([1, 1, 1, 1, 1, 1, 2]))