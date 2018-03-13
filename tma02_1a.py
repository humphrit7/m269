import time


def insertion_sort(a_list):
    """Sort a_list in ascending order.

    Use insertion sort with linear search.
    """
    for current_position in range(1, len(a_list)):
        current_value = a_list[current_position]
        position = current_position
        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position = position - 1
        a_list[position] = current_value


# the length of the input list
size = 51200  # CHANGE THIS

# Create a list of integers in descending order (worst-case scenario)
test_list = []
for index in range(size):
    test_list.append(size - index)
# Time the execution of the sorting algorithm
start = time.time()
insertion_sort(test_list)
elapsed = (time.time() - start) * 1000
print(size, 'integers sorted in', int(elapsed), 'milliseconds')