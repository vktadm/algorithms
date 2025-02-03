def symmetric(node):
    """
    Симметричный обход дерева (рекурсивный вариант).
    """

    # Добавляем проверку на реальность левого и правого потомков.
    if node.has_left_child:
        symmetric(node.left)
    print(node, end="  ")
    if node.has_right_child:
        symmetric(node.right)


def symmetric_thread(root):
    """
    Симметричный обход прошитого дерева.
    """
    node = root
    via_branch = True

    # Цикл до тех пор, пока справа есть потомок или нить.
    while node is not None:
        # Цикл для спуска по левой ветке с потомками.
        while via_branch and node.left is not None and node.has_left_child:
            node = node.left
        # Обработка узла.
        print(node.value, end="  ")
        # Смотрим на узел справа (потомок или нить.
        via_branch = node.has_right_child
        # Спуск по правой ветке.
        node = node.right


def add_node(root, new_value):
    """
    Добавление нового узла в прошитое дерево.
    """
    node = root

    # Сравниваем новое значение с текущим.
    if new_value < node.value:
        if node.has_left_child:
            # Рекурсивно спускаемся в левую ветку.
            add_node(node.left, new_value)
        else:
            # Создаем новый узел.
            new_node = BinaryNode(new_value)

            # Создаем связи (не узлы) для нового узла.
            new_node.left = node.left
            new_node.right = node

            # Указываем левого потомка для текущего узла.
            node.left = new_node
            node.has_left_child = True
    else:
        if node.has_right_child:
            # Рекурсивно спускаемся в правую ветку.
            add_node(node.right, new_value)
        else:
            # Создаем новый узел.
            new_node = BinaryNode(new_value)

            # Создаем связи (не узлы) для нового узла.
            new_node.right = node.right
            new_node.left = node

            # Указываем правого потомка для текущего узла.
            node.right = new_node
            node.has_right_child = True


class BinaryNode:
    """
    Узел прошитого дерева.
    """

    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

        # Слева потомки или ссылки?
        self.has_left_child = False
        self.has_right_child = False

    def __str__(self):
        return f"{self.value}"

    def __repr__(self):
        return self.__str__()


# Создаем дерево из урока.
root = BinaryNode("E")
node1 = BinaryNode("A")
node2 = BinaryNode("B")
node4 = BinaryNode("D")
node6 = BinaryNode("F")
node7 = BinaryNode("G")
node9 = BinaryNode("I")

node1.right = node2

node2.left = node1
node2.right = node4
node2.has_left_child = True
node2.has_right_child = True

node4.left = node2
node4.right = root

root.left = node2
root.right = node6
root.has_left_child = True
root.has_right_child = True

node6.left = root
node6.right = node9
node6.has_right_child = True

node9.left = node7
node9.has_left_child = True

node7.left = node6
node7.right = node9

# Симметричный обход.
symmetric(root)
print()
symmetric_thread(root)

print()
# Добавление элементов.
add_node(root, "C")
add_node(root, "H")

# Симметричный обход (еще раз).
symmetric(root)
print()
symmetric_thread(root)
