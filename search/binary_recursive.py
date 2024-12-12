def binary_search(array, value, min_index=None, max_index=None):
    """
    Возвращает индекс искомого элемента (value) в отсортированном массиве (array).
    Если в массиве более одного искомого элемента,
    то функция не гарантирует, что найденный будет первым.
    Возвращает -1 если элемент не найден.
    """

    # Если это первый запуск, то вычисляем значения min_index и max_index.
    if min_index is None:
        min_index = 0
    if max_index is None:
        max_index = len(array) - 1

    # Вычисляем средний индекс.
    middle_index = (min_index + max_index) // 2

    # Сравниваем искомый элемент с текущим.
    if value == array[middle_index]:
        return middle_index

    # Проверка выхода индексов за пределы.
    if min_index > max_index:
        return -1

    # Обновляем минимум и максимум.
    if value > array[middle_index]:
        min_index = middle_index + 1
    else:
        max_index = middle_index - 1

    # Рекурсивный вызов
    return binary_search(array, value, min_index, max_index)