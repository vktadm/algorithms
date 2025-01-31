class BinaryNode:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def __str__(self):
        return str(self.value)


# Создаем вершины.
root = BinaryNode(8)
node1 = BinaryNode(3)
node2 = BinaryNode(10)
node3 = BinaryNode(2)
node4 = BinaryNode(6)
node5 = BinaryNode(9)
node6 = BinaryNode(11)
node7 = BinaryNode(1)
node8 = BinaryNode(4)
node9 = BinaryNode(7)


# Связываем вершины.
root.left_child = node1
root.right_child = node2

node1.left_child = node3
node1.right_child = node4

node2.left_child = node5
node2.right_child = node6

node3.left_child = node7

node4.left_child = node8
node4.right_child = node9