def least_common_in_unsorted(numbers):
    """
    Finds the least common number in an unsorted list of
    integers. If there is more than one number with the
    same frequency, returns the rare number which
    appears last in the list .

    Inputs
    ------
    numbers- list - contains only integers

    Returns
    -------
    integer - the least common, or joint least common
               integer in the list.
    """
    counts = [0] * len(numbers)
    for j in range(len(numbers)):
        for i in range(len(numbers)):
            if numbers[j] == numbers[i]:
                counts[j] += 1
    minimum = len(numbers)
    for count in counts:
        if count < minimum:
            minimum = count
    for i in range(len(counts)-1, -1, -1):
        if counts[i] == minimum:
            return numbers[i]





print(least_common_in_unsorted([1]))
print(least_common_in_unsorted([-1,0,1,2,-1,2]))
print(least_common_in_unsorted([6,0,0,6,6,0]))
print(least_common_in_unsorted([6,0,0,6,0,6]))