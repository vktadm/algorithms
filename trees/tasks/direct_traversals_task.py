class Node:
    """
    Класс узла дерева.
    """

    def __init__(self, value):
        self.value = value
        self.children = []

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self.value)


def direct(node):
    # Начинаем с значения текущего узла
    result = str(node)

    # Перебираем всех детей и добавляем очередного потомка к общему результату.
    for child in node.children:
        result += " " + direct(child)

    return result


# Создаём дерево на основе класса выше
root = Node("a")
node_b = Node("b")
node_c = Node("c")
node_d = Node("d")
node_i = Node("i")

root.children.extend([node_b, node_c, node_d])
node_b.children.extend([Node("e")])
node_c.children.extend([Node("f"), Node("g")])
node_d.children.extend([Node("h"), node_i, Node("k")])
node_i.children.extend([Node("l"), Node("m"), Node("n"), Node("o")])

result = direct(root)
print(result)
