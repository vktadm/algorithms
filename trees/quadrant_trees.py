# Минимальный размер ячейки.
MIN_LENGTH = 2.5


def get_elements(q, x, y):
    """
    Возвращает все элементы в заданой области.
    """
    for side in [q.nw, q.ne, q.se, q.sw]:

        if side and (side.x <= x < (side.x + side.length)) and (side.y <= y < (side.y + side.length)):
            return get_elements(side, x, y)

    return q.elements


def add_element(q, x, y, value):
    """
    Добавляет элемент в квадрант.
    x, y - координаты элемента.
    value - значение.
    """

    # Если размер текущего квадранта равен минимальному размеру,
    # то значит мы достигли нужного уровня и можно добавлять элемент.
    if q.length == MIN_LENGTH:
        q.elements.append(value)
        return

    # Иначе начинаем искать квадрант для добавления.
    # Перебираем стороны: с-з, с-в, ю-в, ю-з.
    for side in ['nw', 'ne', 'se', 'sw']:
        # Получаем непосредственно элемент-потомок, который соответствует стороне.
        child = getattr(q, side)

        # Если потомка нет.
        if child is None:
            # Вычисляем длину потомка.
            new_length = q.length / 2

            # Сбрасываем координаты потомка.
            new_x = new_y = None

            # Проверяем каждую сторону и рассчитываем начальные координаты потомка.
            # Северо-запад.
            if side == "nw":
                new_x, new_y = q.x, q.y + new_length
            # Северо-восток.
            elif side == "ne":
                new_x, new_y = q.x + q.length / 2, q.y + q.length / 2
            # Юго-восток.
            elif side == "se":
                new_x, new_y = q.x + q.length / 2, q.y
            # Юго-запад.
            elif side == "sw":
                new_x, new_y = q.x, q.y

            # Проверяем, если координаты вставляемого объекта попадают в диапазон координаты потомка.
            if new_x is not None and new_y is not None and (new_x <= x < (new_x + new_length)) and (new_y <= y < (new_y + new_length)):
                # Если попадают, то создаем потомка.
                child = Q(new_x, new_y, new_length)
                # Привязываем потомка к правильной стороне родителя.
                setattr(q, side, child)

        # Если потомок уже есть (или мы его только что создали), то смотрим на диапазоны координат.
        if child and (child.x <= x < (child.x + child.length)) and (child.y <= y < (child.y + child.length)):
            add_element(child, x, y, value)


class Q:

    def __init__(self, x=0.0, y=0.0, length=10.0):
        self.x = x
        self.y = y
        self.length = length

        self.elements = []

        self.nw = None  # Северо-запад
        self.ne = None  # Северо-восток
        self.se = None  # Юго-восток
        self.sw = None  # Юго-запад

    def __str__(self):
        return f"[{self.x}, {self.y}]"


root = Q()


add_element(root, 2.8, 8.3, "Вектор")
add_element(root, 4.5, 7.6, "Снежинка")
add_element(root, 4.9, 7.5, "Ромашка")


print(get_elements(root, 2.8, 8.3))
print(get_elements(root, 2.5, 7.5))
print(get_elements(root, 3.0, 9.1))
print(get_elements(root, 0.0, 0.0))
