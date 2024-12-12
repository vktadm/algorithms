class Stack:
    """
    Двойной стек.
    """

    def __init__(self, size):
        self.data = [None] * size
        self.length = 0
        self.size = size

        # Задаем указатели за пределами
        self.top_left = -1
        self.top_right = self.size

    def pop_left(self):
        """
        Извлекает элемент из стека слева.
        """
        if self.top_left >= 0:
            value = self.data[self.top_left]
            self.top_left -= 1
            self.length -= 1
            return value

    def pop_right(self):
        """
        Извлекает элемент из стека справа.
        """
        # Добавьте ваш код тут

        if self.top_right < self.size:
            value = self.data[self.top_right]
            self.top_right += 1
            self.length -= 1
            return value

    def push_left(self, value):
        """
        Добавляет элемент со значением value в стек слева
        """
        # Проверяем заполненность стека.
        if self.length == self.size:
            raise OverflowError

        # Смещаем указатель.
        self.top_left += 1

        # Увеличиваем длину
        self.length += 1

        # Добавляем новый элемент.
        self.data[self.top_left] = value

    def push_right(self, value):
        # Проверяем заполненность стека.
        if self.length == self.size:
            raise OverflowError

        # Смещаем указатель.
        self.top_right -= 1

        # Увеличиваем длину
        self.length += 1

        # Добавляем новый элемент.
        self.data[self.top_right] = value

    def is_left_empty(self):
        """
        Пустая ли левая часть стека?
        """
        return self.top_left == -1

    def is_right_empty(self):
        """
        Пустая ли правая часть стека?
        """
        return self.top_right == self.size

    def clear(self):
        self.top_left = -1
        self.top_right = self.size


def quicksort(array):
    """
    Основная функция сортировки.
    Принимает только массив array.
    """
    # Создаем списки (два списка нужно заменить на один стек на базе класса Stack).
    buf = Stack(len(array) - 1)
    do_quicksort(array, buf, 0, len(array) - 1)


def do_quicksort(array, buf, start, end):
    """
    Быстрая сортировка c использованием двух стеков.
    Нужно реализовать алгоритм с использованием одного двойного стека.
    """

    if start >= end:
        return

    divider = array[start]

    # Помещаем элементы до и после от разделителя.
    i = start + 1
    while i < end + 1:
        if array[i] < divider:
            buf.push_left(array[i])
        else:
            buf.push_right(array[i])
        i += 1

    # Помещаем элементы до разделителя обратно в массив.
    index = start
    while not buf.is_left_empty():
        array[index] = buf.pop_left()
        index += 1

    # Вставляем разделитель.
    array[index] = divider

    # Запоминаем, что это средняя точка.
    midpoint = index

    # Добавляем элементы после разделителя,
    index += 1
    while not buf.is_right_empty():
        array[index] = buf.pop_right()
        index += 1

    # Сортируем две половинки массива.
    do_quicksort(array, buf, start, midpoint - 1)
    do_quicksort(array, buf, midpoint + 1, end)

array = [13, 7, 8, 2, 11, 5, 9, 10, 15]
quicksort(array)
print(array)