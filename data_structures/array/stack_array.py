class Array:
    def __init__(self, size):
        self.data = [None] * size
        self.length = 0
        self.size = size

    def __str__(self):
        """
        Возвращает все элементы массива в виде строки.
        """
        return "[" + ", ".join(map(str, self.data[:self.length])) + "]"


class Stack(Array):
    """
    Стек на базе связного списка.
    """

    def __init__(self, size):
        super().__init__(size)

        # Задаем указатель
        self.top = -1

    def pop(self):
        """
        Извлекает элемент из стека.
        """
        if self.top >= 0:
            value = self.data[self.top]
            self.top -= 1
            return value

    def push(self, value):
        """
        Добавление нового элемента в стек.
        """
        # Проверяем заполненность стека.
        if self.top + 1 == self.size:
            raise OverflowError

        # Смещаем указатель.
        self.top += 1

        # Увеличиваем длину
        self.length += 1

        # Добавляем новый элемент.
        self.data[self.top] = value

    def clear(self):
        """
        Очищает стек.
        """
        self.length = 0
        self.top = -1


    def peek(self):
        """
        Возвращает значение верхнего элемента без его извлечения из стека.
        """
        if self.length:
            return self.data[self.top]


    def count(self):
        """
        Возвращает количество элементов в стеке.
        """
        return self.length


stack = Stack(3)
stack.push(12)
stack.push(7)
stack.push(6)
print(stack.peek())
print(stack.count())
stack.clear()
print(stack.count())
print(stack.peek())