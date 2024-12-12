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


class Queue(Array):
    """
    Очередь на базе статического массива.
    """

    def __init__(self, size):
        super().__init__(size)

        # Задаем начальные позиции
        self.last = 0
        self.first = 0

    def enqueue(self, value):
        """
        Добавляет элемент со значением value в очередь.
        """

        # Проверяем, есть ли место для нового элемента.
        if self.size == self.length:
            raise OverflowError

        # Добавляем значение в массив.
        self.data[self.last] = value

        # Рассчитываем следующий индекс для вставки.
        self.last = (self.last + 1) % self.size

        # Увеличиваем длину.
        self.length += 1

    def dequeue(self):
        """
        Извлекает элемент из очереди.
        """

        # Проверяем, не пустая ли очередь.
        if self.length:
            value = self.data[self.first]

            # Уменьшаем размер.
            self.length -= 1

            # Рассчитываем новое значение первого элемента.
            self.first = (self.first + 1) % self.size

            return value

        return None

queue = Queue(4)
queue.enqueue(7)
queue.enqueue(6)
queue.enqueue(2)
queue.enqueue(1)
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
queue.enqueue(13)
print(queue.dequeue())