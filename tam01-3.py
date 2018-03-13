def least_common_in_unsorted(integers):
    strings = []
    for number in integers:
        strings.append(str(number))
    stringy = "".join(strings)
    print(stringy)



print(least_common_in_unsorted([-1,0,1,2,-1,2]))
print(least_common_in_unsorted([6,0,0,6,6,0]))
print(least_common_in_unsorted([6,0,0,6,0,6]))