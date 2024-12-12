def interpolation_search(array, value):
    """
    Возвращает индекс значения value в массиве array.
    Если в массиве более одного искомого элемента,
    то функция не гарантирует, что найденный будет первым.
    Возвращает -1 если элемент не найден.
    """
    min_index = 0
    max_index = len(array) - 1
    while min_index <= max_index:

        # Проверяем равенство индексов, а также наличие элемента.
        if min_index == max_index:
            if array[min_index] == value:
                return min_index
            return -1

        # Поиск среднего элемента.
        middle_index = min_index + (max_index - min_index) * \
              (value - array[min_index]) // (array[max_index] - array[min_index])

        if (middle_index < min_index) or (middle_index > max_index):
            return -1

        # Продолжаем поиск или возвращаем найденный индекс.
        if array[middle_index] < value:
            min_index = middle_index + 1
        elif array[middle_index] > value:
            max_index = middle_index - 1
        else:
            return middle_index

    # Если к этому шагу ничего не нашли, то возвращаем -1.
    return -1
