from collections import deque
from binary_tree import root

"""
Обход дерева в ширину.
"""
def wide(root_node):
    # Создаем очередь для хранения дочерних вершин.
    children = deque()

    # Помещаем корень в очередь.
    children.append(root_node)

    # Обрабатываем очередь пока она не станет пустой.
    while children:
        # Извлекаем элемент слева.
        node = children.popleft()

        # Выводим элемент.
        print(node.value, end="  ")

        # Добавляем дочерние вершины в очередь.
        if node.left_child:
            children.append(node.left_child)
        if node.right_child:
            children.append(node.right_child)

if __name__ == '__main__':
    wide(root)