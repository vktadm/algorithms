"""
Сочетания без повторений.
"""
from itertools import combinations as i_combinations


def combinations(elements, k):
    if k == 0:
        return [[]]

    result = []

    i = 0
    while i < len(elements):
        for suffix in combinations(elements[i+1:], k - 1):
            result.append([elements[i]] + suffix)
        i += 1

    return result


print(combinations(["A", "B", "C", "D"], 3))
print(list(i_combinations(["A", "B", "C", "D"], 3)))