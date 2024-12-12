class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def __str__(self):
        return str(self.value)

node1 = Node(75)

node2 = Node(12)
node1.next_node = node2

node3 = Node(28)
node2.next_node = node3

node4 = Node(6)
node3.next_node = node4

print(node1.value)
print(node1.next_node.value)