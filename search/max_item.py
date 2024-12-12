import time
from search.tournament_two import tournament_two

# MAX элементы
# Вариант 1 - сравнение элементов
def largest_two(A):
    start_time = time.time()
    first_max, second_max = A[:2]
    if first_max < second_max:
        first_max, second_max = second_max, first_max
    for i in range(2, len(A)):
        if A[i] > first_max:
            first_max, second_max = A[i], first_max
        elif A[i] > second_max:
            second_max = A[i]
    end_time = time.time()
    return first_max, second_max, (end_time - start_time)

# Вариант 2 - сортировка
def sorting_two(A):
    start_time = time.time()
    rez = list(tuple(sorted(A, reverse=True)[0:2]))
    end_time = time.time()
    return rez, (end_time - start_time)

# Вариант 3 - через функцию max, с копированием эл-та
def double_two(A):
    start_time = time.time()
    first_max = max(A)
    copy = list(A)
    copy.remove(first_max)
    second_max = max(copy)
    end_time = time.time()
    return first_max, second_max, (end_time - start_time)

A_str = input('Введите массив целых чисел, используя пробел: ').split()

try:
    A_int = [int(i) for i in A_str]
except ValueError:
    print('Невозможно преобразовать в int. Введите целые числа, без знаков препинания!')
else:
    print(largest_two(A_int))
    print(sorting_two(A_int))
    print(double_two(A_int))
    print(tournament_two(A_int))