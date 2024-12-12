def heapsort(values):
    """
    Пирамидальная сортировка массива.
    """
    # Создаем первоначальную кучу.
    make_heap(values)

    # Помещаем элементы из корня в конец (по одному за раз).
    i = 0
    while i < len(values):
        # Вычисляем последний элемент в куче.
        last = (len(values) - 1) - i

        # Обмениваем значения.
        values[0], values[last] = values[last], values[0]

        # Восстанавливаем кучу.
        remake_heap(values, latest_index=last)

        i += 1


def make_heap(values):
    """
    Преобразовывает массив в кучу.
    """

    # Цикл по всем значениям массива.
    i = 0
    while i < len(values):
        # Перемещение очередного элемента в корень.
        index = i
        while index != 0:
            # Ищем родительских индекс.
            parent_index = (index - 1) // 2

            # Если значение дочернего элемента <= родительскому,
            # то мы прерываем цикл.
            if values[index] <= values[parent_index]:
                break

            # Меняем родительский с дочерним.
            values[index], values[parent_index] = values[parent_index], values[index]

            # Меняем текущий индекс на родителя.
            index = parent_index
        i += 1


def remake_heap(values, latest_index):
    """
    Восстанавливает кучу.
    latest_index - индекс массива, ограничивающий кучу.
    """

    index = 0
    while True:
        # Вычисляем индексы дочерних элементов.
        child1_idx = 2 * index + 1
        child2_idx = 2 * index + 2

        # Если дочерние индексы >= последнему индексу,
        # то используем родительский индекс.
        if child1_idx >= latest_index:
            child1_idx = index
        if child2_idx >= latest_index:
            child2_idx = index

        # Если значение родителя больше детей, то выходим из цикла - куча восстановлена.
        if (values[index] >= values[child1_idx]) and \
           (values[index] >= values[child2_idx]):
            break

        # Вычисляем индекс дочернего элемента для обмена.
        if values[child1_idx] > values[child2_idx]:
            swap_child_idx = child1_idx
        else:
            swap_child_idx = child2_idx

        # Обмен родителя с наибольшим ребенком
        values[index], values[swap_child_idx] = values[swap_child_idx], values[index]

        # Переходим на следующую ветку.
        index = swap_child_idx

array = [7, 8, 1, 2, 10, 14, 5, 6, 11]
heapsort(array)
print(array)