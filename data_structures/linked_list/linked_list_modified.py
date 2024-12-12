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

    def append(self, value):
        """
        Добавление нового элемента в конец связанного списка.
        Время работы O(N).
        """
        current = self.top
        while current.next_node is not None:
            current = current.next_node

        # Создаем ссылку для последнего элемента на новый.
        current.next_node = Node(value)

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
lst.append(75)
lst.append(12)
lst.append(28)
lst.append(6)

print(lst)