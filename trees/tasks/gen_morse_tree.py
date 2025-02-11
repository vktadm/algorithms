class MorseBinaryNode:
    def __init__(self, char):
        self.char = char
        self.dot_child = None
        self.dash_child = None
        self.root = False

    def set_children(self, dot=None, dash=None):
        self.dot_child = dot
        self.dash_child = dash

    def __str__(self):
        return str(self.char)


class MorseTree:

    def __init__(self):
        # Создаём корень дерева
        self.morse = MorseBinaryNode(None)
        self.morse.root = True

    def insert_char(self, morse_code, char):
        """
        Вставляет символ char с кодом morse_code в дерево self.morse
        """
        current = self.morse
        for itm in morse_code:
            if itm == '.':
                if not current.dot_child:
                    current.dot_child = MorseBinaryNode(None)
                current = current.dot_child
            elif itm == '-':
                if not current.dash_child:
                    current.dash_child = MorseBinaryNode(None)
                current = current.dash_child

        current.char = char

    def get_nodes(self, node=None, result=None):
        """
        Симметричный обход с выводом всех узлов.
        Не изменяйте этот метод, он нужен для тестирования.
        """

        if result is None:
            result = []
            node = self.morse

        if node.dot_child:
            self.get_nodes(node.dot_child, result)

        if not node.root:
            result.append(node.char)

        if node.dash_child:
            self.get_nodes(node.dash_child, result)

        return ",".join(map(lambda x: "" if x is None else x, result))


mt = MorseTree()
lst_in = ['.-,A', '.,E', '..,I', '--,M', '-.,N', '-,T']

for itm in lst_in:
    mt.insert_char(*itm.split(','))

