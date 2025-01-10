"""
Размещения и перестановки.
"""
from itertools import permutations as i_permutations

def permutations(elements, k):
    """
    Размещения без повторений.
    """
    if k == 0:
        return [[]]

    result = []

    i = 0
    while i < len(elements):
        element = elements[i]

        # Делаем копию строки и исключаем текущий элемент.
        new_elements = elements[:]
        new_elements.remove(element)

        for suffix in permutations(new_elements, k-1):
            result.append([element] + suffix)
        i += 1

    return result

# Размещения
print(permutations([1, 2, 3, 4, 5], 3))
print(list(i_permutations([1, 2, 3, 4, 5], 3)))