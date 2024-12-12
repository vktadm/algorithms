class Node:
    def __init__(self, value=None, next_node=None, prev_node=None):
        self.value = value
        self.next_node = next_node
        self.prev_node = prev_node

    def __str__(self):
        return str(self.value)

class List:
    def __init__(self):
        """Ограничитель."""
        self.top = Node()

    def append(self, value):
        """Добавление нового элемента в КОНЕЦ связанного списка.
        Время работы O(1)."""
        current = self.top
        while current.next_node is not None:
            current = current.next_node

        new_node = Node(value)
        current.next_node = new_node
        new_node.prev_node = current

    def prepend(self, value):
        """Добавление нового элемента в начало двунаправленного списка."""
        new_node = Node(value, self.top.next_node, self.top)
        if self.top.next_node is not None:
            self.top.next_node.prev_node = new_node
        self.top.next_node = new_node


    def insert(self, after_value, value):
        """Добавление нового элемента value после элемента after_value.
        Время работы O(N)"""
        current = self.top.next_node
        while current is not None:
            if current.value == after_value:
                # Создаем новую ячейку.
                new_node = Node(value, current.next_node, current)
                if current.next_node is not None:
                    # Связываем впереди стоящий элемент с новой ячейкой.
                    current.next_node.prev_node = new_node
                # Связываем предыдущий (текущий) элемент с новой ячейкой.
                current.next_node = new_node
                return
            current = current.next_node


    def delete(self, value):
        """
        Удаление элемента по значению.
        """
        current = self.top.next_node
        while current is not None:
            if current.value == value:
                if current.next_node is not None:
                    current.next_node.prev_node = current.prev_node
                current.prev_node.next_node = current.next_node
                return
            current = current.next_node



    def __str__(self):
        """Возвращаем все элементы связанного списка в виде строк."""
        current = self.top.next_node
        values = '['
        while current is not None:
            end = ', ' if current.next_node else ''
            values += str(current) + end
            current = current.next_node
        return values + ']'

lst = List()

lst.prepend(111)
lst.prepend(114)
lst.prepend(100)

zero = lst.top.next_node.next_node.next_node
print(zero.value)
print(zero.next_node.value)
print(zero.prev_node.value)

# lst.insert(6, 60)
# lst.insert(28, 280)

# lst.delete(111)

print(lst)