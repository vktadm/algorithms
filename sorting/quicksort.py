def quicksort(array, start, end):
    """
    Быстрая сортировка c использованием двух стеков.
    """

    if start >= end:
        return

    # Используем первый элемент в качестве разделителя.
    # Не самый оптимальный вариант, особенно если массив почти отсортирован.
    divider = array[start]

    # Помещаем элементы до и после от разделителя.
    before, after = [], []
    i = start + 1
    while i < end + 1:
        if array[i] < divider:
            before.append(array[i])
        else:
            after.append(array[i])
        i += 1

    # Помещаем элементы до разделителя обратно в массив.
    index = start
    while len(before) > 0:
        array[index] = before.pop()
        index += 1

    # Вставляем разделитель.
    array[index] = divider

    # Запоминаем, что это средняя точка.
    midpoint = index

    # Добавляем элементы после разделителя,
    index += 1
    while len(after) > 0:
        array[index] = after.pop()
        index += 1

    # Сортируем две половинки массива.
    quicksort(array, start, midpoint - 1)
    quicksort(array, midpoint + 1, end)


data = [7, 8, 9, 4, 6, 5, 10, 3, 2, 1]
# Первый вызов функции, указываем первый и последний элементы массива.
quicksort(data, 0, len(data) - 1)
print(data)