class AVLTreeNode(object):
    def __init__(self, key, value):
        self.key = key      # Ключ.
        self.value = value  # Значение узла (данные).
        self.parent = None  # Родитель для облегчения поворота.
        self.left = None    # Левый потомок.
        self.right = None   # Правый потомок.
        self.height = 1     # Высота поддерева с корнем в данном узле.

    def __str__(self):
        return f"{self.key}: {self.value}"

    @property
    def bf(self):
        """
        Показатель сбалансированности (balance_factor).
        Вычисляется как разница высот левого и правого поддеревьев.
        """
        return self.right_height - self.left_height

    @property
    def left_height(self):
        return self.left.height if self.left is not None else 0

    @property
    def right_height(self):
        return self.right.height if self.right is not None else 0

    def update_height(self):
        """
        Обновляет высоту текущего узла.
        """
        self.height = max(self.left_height, self.right_height) + 1


class AVLTree:
    """
    Класс для управления АВЛ-деревом..
    """

    def insert(self, root, key, value=None):
        """
        Вставляет новый узел с ключом key и значением value в дерево с корнем root.
        Обновляет значения высоты и показателя балансировки затронутых узлов, обновляет родителя.
        Возвращает корень результирующего дерева.
        """
        # Если корня нет (новое дерево), то добавляем его и возвращаем.
        if not root:
            return AVLTreeNode(key, value)

        # Если ключ меньше текущего, то идем в левое поддерево.
        if key < root.key:
            root.left = self.insert(root.left, key, value)
        # Если ключ больше текущего, то идем в правое поддерево.
        else:
            root.right = self.insert(root.right, key, value)

        return self.rebalance(root)  # Ребалансировка корня, если требуется.

    def rebalance(self, root):
        """
        Метод для ребалансировки дерева с корнем root.
        Возвращает корень дерева после ребалансировки.

        4 варианта:
        1) root.bf = 2 and root.right.bf < 0     ==> Правый-левый
        2) root.bf = 2                           ==> Правый-правый
        3) root.bf = -2 and root.left.bf > 0     ==> Левый-правый
        4) root.bf = -2                          ==> Левый-левый
        """
        root.update_height()

        if root.bf == 2:
            if root.right.bf < 0:
                root.right = self.rotate_right(root.right)
            return self.rotate_left(root)
        elif root.bf == -2:
            if root.left.bf > 0:
                root.left = self.rotate_left(root.left)
            return self.rotate_right(root)
        return root

    def rotate_right(self, root):
        new_root = root.left
        root.left = new_root.right  # Ставим C-дерево слева от старого корня.
        new_root.right = root       # Меняем корни местами

        # Обновляем высоты.
        root.update_height()
        new_root.update_height()

        return new_root

    def rotate_left(self, root):
        new_root = root.right
        root.right = new_root.left  # Ставим B-дерево справа от старого корня.
        new_root.left = root        # Меняем корни местами

        # Обновляем высоты.
        root.update_height()
        new_root.update_height()

        return new_root

    def find_min_node(self, root):
        """
        Поиск узла с минимальным ключом в поддереве root.
        Рекурсивный спуск по левой ветке до конца.
        """
        if root.left is not None:
            return self.find_min_node(root.left)
        return root

    def remove_min_node(self, root):
        """
        Удаление узла с минимальным значением из дерева.
        """
        if root.left is None:
            return root.right
        root.left = self.remove_min_node(root.left)
        return self.rebalance(root)

    def remove(self, root, key):
        """
        Удаление узла с ключом key.
        root - это корень дерева.
        """
        if not root:
            return None
        if key < root.key:
            root.left = self.remove(root.left, key)
        elif key > root.key:
            root.right = self.remove(root.right, key)
        else:
            left_child = root.left
            right_child = root.right

            left_child.parent = None
            right_child.parent = None
            del root

            if right_child is None:
                return left_child
            min_node = self.find_min_node(right_child)
            min_node.right = self.remove_min_node(right_child)
            min_node.left = left_child
            return self.rebalance(min_node)
        return self.rebalance(root)


tree = AVLTree()
root = None
for i in range(0, 10000):
    root = tree.insert(root, i, str(i))

print()
