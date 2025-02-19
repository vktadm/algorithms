from binary_tree import root


def direct(node):
    print(node.value, end="  ")
    if node.left_child:
        direct(node.left_child)
    if node.right_child:
        direct(node.right_child)

def symmetric(node):
    if node.left_child:
        symmetric(node.left_child)
    print(node.value, end="  ")
    if node.right_child:
        symmetric(node.right_child)

def reverse(node):
    if node.left_child:
        reverse(node.left_child)
    if node.right_child:
        reverse(node.right_child)
    print(node.value, end="  ")

if __name__ == '__main__':
    print('----Обход в прямом порядке----')
    direct(root)
    print('\n----Симметричный обход----')
    symmetric(root)
    print('\n----Обход в обратном порядке----')
    reverse(root)

