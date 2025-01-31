def symmetric(node):
    """
    Симметричный обход дерева.
    """
    if node.left_child:
        symmetric(node.left_child)
    print(node.value, end="  ")
    if node.right_child:
        symmetric(node.right_child)


class BinaryNode:
    def __init__(self, value, parent=None):
        self.value = value
        self.parent = parent
        self.left_child = None
        self.right_child = None

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return self.__str__()

    def is_left_child(self):
        if self.parent.left_child:
            if self.parent.left_child.value == self.value:
                return True
        return False


def find(node, target):
    """
    Поиск элемента.
    """
    if target == node.value:
        return node

    if target < node.value:
        if node.left_child is None:
            return None
        return find(node.left_child, target)
    else:
        if node.right_child is None:
            return None
        else:
            return find(node.right_child, target)


def delete(node):
    """
    Удаление элемента.
    """
    if node.left_child is None and node.right_child is None:
        # Удаляем вершину без потомков.
        if node.is_left_child():
            node.parent.left_child = None
        else:
            node.parent.right_child = None
    elif node.left_child and node.right_child:
        # Удаляем вершину, у которой два потомка.
        left_child = node.left_child

        # Случай когда у левого потомка нет правого.
        if left_child.right_child is None:
            # Устанавливаем левую ветку.
            left_child.right_child = node.right_child
            node.right_child.parent = left_child

            # Поднимаем вверх.
            left_child.parent = node.parent

            if node.is_left_child():
                node.parent.left_child = left_child
            else:
                node.parent.right_child = left_child
        # Случай, когда у левого потомка есть правый.
        else:
            # Спускаемся вниз
            right_child = left_child.right_child
            while right_child:
                if right_child.right_child:
                    right_child = right_child.right_child
                else:
                    break

            # На этом этапе у нас есть последний правый потомок.
            # Случай, когда у правого потомка нет левого, то есть это терминальная вершина.
            if right_child.left_child is None:
                right_child.right_child = node.right_child
                # node.right_child.parent = right_child

                right_child.left_child = node.left_child

                right_child.parent.right_child = None
            # Случай, когда у правого потомка есть левый.
            else:
                # Помещаем нижнюю левую на место правой.
                right_child.left_child.parent = right_child.parent
                right_child.parent.right_child = right_child.left_child

                # Поднимаем правый вверх - устанавливаем потомки.
                right_child.left_child = node.left_child
                right_child.right_child = node.right_child

            # Последнее перемещение.
            right_child.parent = node.parent

            node.left_child.parent = right_child
            node.right_child.parent = right_child

            if node.is_left_child():
                node.parent.left_child = right_child
            else:
                node.parent.right_child = right_child
    else:
        # Удаляем вершину, у которой один потомок (слева или справа).
        if node.left_child:
            if node.is_left_child():
                node.parent.left_child = node.left_child
            else:
                node.parent.right_child = node.left_child
            # Перестанавливаем родителя.
            node.left_child.parent = node.parent
        else:
            if node.is_left_child():
                node.parent.left_child = node.right_child
            else:
                node.parent.right_child = node.right_child
            # Переустанавливаем родителя.
            node.right_child.parent = node.parent


root = BinaryNode(60)
node2 = BinaryNode(35, parent=root)
node3 = BinaryNode(76, parent=root)
node4 = BinaryNode(21, parent=node2)
node5 = BinaryNode(42, parent=node2)
node6 = BinaryNode(71, parent=node3)
node7 = BinaryNode(89, parent=node3)
node8 = BinaryNode(17, parent=node4)
node9 = BinaryNode(24, parent=node4)
node10 = BinaryNode(68, parent=node6)
node11 = BinaryNode(11, parent=node8)
node12 = BinaryNode(23, parent=node9)
node13 = BinaryNode(28, parent=node9)
node14 = BinaryNode(63, parent=node10)
node15 = BinaryNode(69, parent=node10)
node16 = BinaryNode(26, parent=node13)


root.left_child = node2
root.right_child = node3
node2.left_child = node4
node2.right_child = node5
node3.left_child = node6
node3.right_child = node7
node4.left_child = node8
node4.right_child = node9
node6.left_child = node10
node8.left_child = node11
node9.left_child = node12
node9.right_child = node13
node10.left_child = node14
node10.right_child = node15
node13.left_child = node16

symmetric(root)
print()

delete(find(root, 89))
symmetric(root)
print()

delete(find(root, 71))
symmetric(root)
print()

delete(find(root, 21))
symmetric(root)
print()

delete(find(root, 35))
symmetric(root)