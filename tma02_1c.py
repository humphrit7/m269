def binary_search(a_list, first, last, target):
    """Return the position where target is or should be inserted.

    Assume 0 <= first < len(a_list) and last < len(a_list).
    Assume a_list[first] <= a_list[first+1] <= ... <= a_list[last]
    if first <= last.
    """
    while first <= last:
        middle = (first + last) // 2
        if a_list[middle] == target:
            return middle
        if target < a_list[middle]:
            last = middle - 1
        else:
            first = middle + 1
    return first


def insertion_sort(a_list):
    """Sort a_list in ascending order.

    Use insertion sort with binary search.
    """
    if len(a_list)>1:
        for index in range(0, len(a_list)):
            value = a_list[index]
            newPosition = binary_search(a_list, 0, index, value)
            a_list.insert(newPosition, a_list.pop(index))




items = [5]
insertion_sort(items)
print(items)


items = [4, 3, 2, 1]
insertion_sort(items)
print(items)

items = [1, 2, 3, 4]
insertion_sort(items)
print(items)

items = [4, 2, 3, 1]
insertion_sort(items)
print(items)