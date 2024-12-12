class Node:
    def __init__(self, value=None):
        self.next_node = None
        self.prev_node = None

        self.value = int(value)

    def __str__(self):
        return str(self.value)


class List:
    """
    Двунаправленный связный список.
    """

    def __init__(self):
        # Голова и хвост
        self.head = None
        self.tail = None

        self.length = 0

    def append(self, value):
        """
        Вставка элемента в конец связного списка.
        """
        new_node = Node(value)

        # Если нет head, значит и нет tail
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.length += 1
            return

        # Вставка элемента и формирование ссылок
        new_node.prev_node = self.tail
        self.tail.next_node = new_node
        self.tail = new_node

        self.length += 1

        return new_node

    def sort(self):
        """
        Сортирует связный список с помощью сортировок вставками.
        """
        current = self.head.next_node

        while current.next_node is not None:
            while current.next_node < current and j >= 0:
                j -= 1
            current = current.next_node

    def __str__(self):
        """
        Возвращает все элементы связного списка в виде строки.
        """
        current = self.head
        values = "["

        while current is not None:
            end = ", " if current.next_node else ""
            values += str(current) + end
            current = current.next_node

        return values + "]"