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
        current = self.top.next_node
        prev = self.top

        if current is None:
            new_node = Node(value)
            self.top.next_node = new_node
            return

        while current is not None and current.next_node.value > value:
            current = current.next_node

        # Вставляем новую ячеку перед current
        new_node = Node(value)
        new_node.next_node = current
        current.next_node = new_node

    def sort(self):
        """Сортируем связанный список методом выбора."""
        # Новый ограничитель для нового списка.
        new_top = Node()

        current = self.top

        # Повторяем пока исходный список не пустой.
        while current.next_node is not None:

            # Ячейка after_me предшествует ячейке с наибольшим элементом.
            max_after_me = current
            max_value = max_after_me.next_node.value

            # Ищем следующий элемент
            after_me = current.next_node
            while after_me.next_node is not None:
                if after_me.next_node.value > max_value:
                    max_after_me = after_me
                    max_value = after_me.next_node.value
                after_me = after_me.next_node

            # Удаляем максимальную ячейку из текущего списка.
            max_node = max_after_me.next_node
            max_after_me.next_node = max_node.next_node

            # Добавлям максимальную ячейку в начало нового списка.
            max_node.next_node = new_top.next_node
            new_top.next_node = max_node

        self.top = new_top

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
lst.append(75)
lst.append(12)
lst.append(28)
lst.append(6)
lst.append(16)
print(lst)

# lst.sort()
# print(lst)