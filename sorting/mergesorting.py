def mergesort(array):
    """Prepare to merge sorting."""

    # Create temporary array.
    temp_array = [None] * len(array)
    do_mergesort(array, temp_array, 0, len(array) - 1)


def do_mergesort(array, temp_array, start, end):
    """Merge sorting."""

    # If array contain one item, then it is sorted.
    if start == end:
        return

    # Search middle item.
    midpoint = (start + end) // 2

    # Call sorting for left and right part of array.
    do_mergesort(array, temp_array, start, midpoint)
    do_mergesort(array, temp_array, midpoint + 1, end)

    # Merge two part sorted array.
    left_index = start
    right_index = midpoint + 1
    temp_array_index = left_index
    while (left_index <= midpoint) and (right_index <= end):
        if array[left_index] <= array[right_index]:
            temp_array[temp_array_index] = array[left_index]
            left_index += 1
        else:
            temp_array[temp_array_index] = array[right_index]
            right_index += 1
        temp_array_index += 1

    # Final copy not empty arrays.
    for i in range(left_index, midpoint + 1):
        temp_array[temp_array_index] = array[i]
        temp_array_index += 1
    for i in range(right_index, end + 1):
        temp_array[temp_array_index] = array[i]
        temp_array_index += 1

    for i in range(start, end + 1):
        array[i] = temp_array[i]




data = [8, 7, 2, 4, 9, 6, 1, 5, 3, 10]
mergesort(data)
print(data)