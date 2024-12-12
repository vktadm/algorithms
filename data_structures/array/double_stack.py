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
    Двойной стек на базе статического массива.
    """
    def __init__(self, size):
        super().__init__(size)
        self.top_left = -1
        self.top_right = size

    def pop_left(self):
        """
        Извлекает элемент из стека слева.
        """
        if self.top_left >= 0:
            value = self.data[self.top_left]
            self.data[self.top_left] = None
            self.top_left -= 1
            self.length -= 1
            return value

    def pop_right(self):
        """
        Извлекает элемент из стека справа.
        """
        if self.top_right < self.size:
            value = self.data[self.top_right]
            self.data[self.top_right] = None
            self.top_right += 1
            self.length -= 1
            return value

    def push_left(self, value):
        """
        Добавляет элемент со значением value в стек слева.
        """
        if self.length == self.size:
            raise OverflowError

        self.top_left += 1
        self.length += 1
        self.data[self.top_left] = value

    def push_right(self, value):
        """
        Добавляет элемент со значением value в стек справа.
        """
        if self.length == self.size:
            raise OverflowError

        self.top_right -= 1
        self.length += 1
        self.data[self.top_right] = value

    def clear(self):
        """
        Очищает стек.
        """
        self.top_right = self.size
        self.top_left = -1

        self.length = 0

    def __str__(self):
        """
        Возвращает все элементы массива в виде строки.
        Используем size, так как массив теперь заполняется с двух сторон.
        """
        return "[" + ", ".join(map(str, self.data[:self.size])) + "]"

stack = Stack(4)
stack.push_left(12)
stack.push_left(7)
stack.push_right(11)
stack.push_right(50)
print(stack)
print(stack.pop_left())
print(stack.pop_left())
print(stack.pop_right())
print(stack.pop_right())
print(stack.pop_right())
print(stack.pop_left())
print(stack)