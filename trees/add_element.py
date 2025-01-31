class BinaryNode:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def __str__(self):
        return str(self.value)


def add_node(node, new_value):
    # Сравниваем новое значение с текущим.
    if new_value < node.value:
        # Слева ничего нет - размещаем.
        if node.left_child is None:
            # Создаем новый узел слева.
            node.left_child = BinaryNode(new_value)
        else:
            # Рекурсивно спускаемся в левую ветку.
            add_node(node.left_child, new_value)
    else:
        if node.right_child is None:
            # Создаем новый узел справа.
            node.right_child = BinaryNode(new_value)
        else:
            # Рекурсивно спускаемся в правую ветку.
            add_node(node.right_child, new_value)