class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def __str__(self):
        return str(self.value)

class List:
    def __init__(self):
        """Ограничитель."""
        self.top = Node()
        self.tail = None

    def append_to_end(self, value):
        """
        Добавление нового элемента в КОНЕЦ связанного списка.
        Время работы O(1).
        """
        current = self.tail
        if current is None:
            current = self.top
        # Создаем ссылку для последнего элемента на новый.
        current.next_node = Node(value)
        self.tail = current.next_node

    def append_to_start(self, value):
        """
        Добавление нового элемента в НАЧАЛО связанного списка.
        Время работы O(1).
        """
        current = Node(value, self.top.next_node)
        self.top.next_node = current

    def append_to(self, value, after_value):
        """
        Добавление нового элемента в ОПРЕДЕЛЕННУЮ позицию связанного списка.
        Время работы O(N).
        """
        current = self.top.next_node
        while current is not None:
            if current.value == after_value:
                new_node = Node(value)
                new_node.next_node = current
                return
            current = current.next_node


    def __str__(self):
        """Возвращаем все элементы связанного списка в виде строк."""
        current = self.top.next_node
        values = '['
        while current is not None:
            end = ',' if current.next_node else ''
            values += str(current) + end
            current = current.next_node
        return values + ']'

lst = List()
lst.append_to_end(12)
lst.append_to_end(28)
lst.append_to_end(6)

lst.append_to_start(115)
lst.append_to_start(45)
lst.append_to_start(75)

lst.append_to(34, 12)
lst.append_to(56, 45)
lst.append_to(99, 75)

print(lst)