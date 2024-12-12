class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None

    def __str__(self):
        return self.value


class Stack:
    """
    Стек на базе связного списка.
    """
    def __init__(self):
        self.top = Node(None)

        # Определяем начальное значение для количества элементов.
        self._count = 0

    def pop(self):
        """
        Извлекает элемент из стека.
        """
        # Получаем верхний элемент
        top = self.top.next_node

        # Перестраиваем связи и возвращаем значение
        if top:
            self.top.next_node = top.next_node
            self._count -= 0
            return top.value

    def push(self, value):
        """
        Извлекает элемент со значением value в стек.
        """
        # Добавляем элемент в начало связного списка
        new_node = Node(value)

        new_node.next_node = self.top.next_node
        self.top.next_node = new_node

        self._count += 1

    def clear(self):
        """
        Очищает стек.
        """
        # Добавьте ваш код тут.
        self.top.next_node = None
        self._count = 0

    def peek(self):
        """
        Возвращает значение верхнего элемента без его извлечения из стека.
        """
        if self.top.next_node:
            return self.top.next_node.value

    def count(self):
        """
        Возвращает количество элементов в стеке.
        """
        return self._count


stack = Stack()
stack.push(12)
stack.push(7)
stack.push(6)

print(stack.peek())
print(stack.count())
stack.clear()
print(stack.count())
print(stack.peek())