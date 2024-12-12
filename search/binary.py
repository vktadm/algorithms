def binary_search_classic(array, value):
    """
    Возвращает индекс искомого элемента (value) в отсортированном массиве.
    Если в массиве более одного искомого элемента,
    то функция не гарантирует, что найденный будет первым.
    Возвращает -1 если элемент не найден.
    """

    min_index = 0
    max_index = len(array) - 1
    # Цикл до тех пор, пока min и max не встретятся
    while min_index <= max_index:

        # Вычисляем средний элемент.
        middle_index = (min_index + max_index) // 2

        # Меняем max_index и min_index.
        if value < array[middle_index]:
            max_index = middle_index - 1
        elif value > array[middle_index]:
            min_index = middle_index + 1
        else:
            return middle_index

    # Возвращаем -1 если элемент не найден
    return -1