def countsort(values, max_value):
    """
    Sorting by counting.
    """

    # Create array-counter.
    counts = [0] * (max_value + 1)

    # Count quantity of values main array.
    for value in values:
        counts[value] += 1

    index = 0
    for i in range(max_value + 1):
        for j in range(counts[i]):
            values[index] = i
            index += 1

def negative_countingsort(values):
    """
    Сортировка подсчетом.
    """

    # Вычисляем max_value.
    max_value = min_value = values[0]
    for value in values[1:]:
        if value > max_value:
            max_value = value
        elif value < min_value:
            min_value = value

    # Создаем массив-счетчик.
    counts = {i: 0 for i in range(min_value, max_value + 1)}

    # Считаем количество значений основного массива.
    for value in values:
        counts[value] += 1

    # Копируем значения обратно в массив.
    index = 0
    for i in range(min_value, max_value + 1):
        for j in range(counts[i]):
            values[index] = i
            index += 1

# def countingsort(values):
#     """
#     Сортировка подсчетом.
#     """
#
#     # Расчет min_value и max_value.
#     min_value = max_value = values[0]
#     for value in values[1:]:
#         if value < min_value:
#             min_value = value
#         if value > max_value:
#             max_value = value
#
#     # Вычисляем размер массива.
#     array_size = abs(min_value) + abs(max_value) + 1
#
#     # Создаем массив-счетчик.
#     # Складываем абсолютные значения min_value и max_value.
#     counts = [0] * array_size
#
#     # Считаем количество значений основного массива.
#     # Делаем сдвиг на величину минимального значения.
#     for value in values:
#         counts[value + abs(min_value)] += 1
#
#     # Копируем значения обратно в массив.
#     index = 0
#     for i in range(array_size):
#         for j in range(counts[i]):
#             values[index] = i - abs(min_value)
#             index += 1

data = [-1, 2, -2, 2, -1, 0, -2, 1, 2, 0, 0, 2, 1, -1, 1, 2, 0]
negative_countingsort(data)
print(data)
