def linear_search(values, target):
    """Линейный поиск."""
    i = 0
    while i < len(values):
        if values[i] == target:
            return i
        i += 1
    return -1

def linear_search_sort(values, target):
    """Линейный поиск в отсортированном массиве."""
    i = 0
    while i < len(values):
        if values[i] == target:
            return i
        if values[i] > target:
            return -1
        i += 1
    return -1

def linear_search_enum(values, target):
    for idx, value in enumerate(values):
        if value == target:
            return idx
    return -1

def linear_search_several(values, target):
    idx_list = []
    for idx, value in enumerate(values):
        if value == target:
            idx_list.append(idx)
    if idx_list:
        return idx_list
    return -1

print(linear_search([5, 6, 9, 7, 10, 15], 6))
print(linear_search_sort([1, 3, 5, 7, 5, 6, 7, 8, 9], 4))
print(linear_search_enum([5, 6, 9, 7, 10, 15], 6))
print(linear_search_several([5, 15, 6, 9, 7, 10, 10, 15, 15], 13))