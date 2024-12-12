class Array:
    """Линейный ститический массив."""

    def __init__(self, size):
        # Данные массива, изначально массив пустой и все его элементы заполнены None.
        # То есть сразу выделяем массив фиксированного объема.
        self.data = [None] * size

        # Длина заполнненого массива.
        # По умолчанию 0, так как массив пустой.
        self.length = 0

        # Полный размер массива.
        self.size = size

    def append(self, value):
        """
        Добавление нового элемента в конец линейного массива.
        Время работы O(1).
        """
        if self.length == self.size:
            raise OverflowError

        self.data[self.length] = value
        self.length += 1

    def insert(self, index, value):
        """
        Добавление нового элемента со значением value на позицию index.
        """
        if self.length == self.size:
            raise OverflowError

        if self.length <= index:
            self.append(value)
            return

        for i in reversed(range(index, self.length)):
            self.data[i+1] = self.data[i]

        self.data[index] = value
        self.length += 1

    def remove(self, value):
        i = 0
        while i < self.length:
            if self.data[i] == value:
                self.data[i:self.length-1] = self.data[i+1:self.length]
                self.length -= 1
                i -= 1
            i += 1

    def __str__(self):
        """
        Возвращает все элементы массива в виде строки.
        """
        return "[" + ", ".join(map(str, self.data[:self.length])) + "]"

array = Array(10)
print(array.size)
print(array.length)
print(array)

array.append(100)
array.append(100)
array.append(10)
array.append(20)
array.append(30)
array.append(40)
array.append(100)

array.insert(2, 300)
array.insert(0, 100)
array.insert(5, 600)
print(array)

array.remove(100)
print(array)


