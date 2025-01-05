class Cell:
    def __init__(self, key, value, next_node):
        self.key = key
        self.value = value
        self.next = next_node

    def __str__(self):
        return f"{self.key}:{self.value}"


class HashTable:
    def __init__(self, size):
        """
        Создаем массив и заполняем его связными списками.
        """
        self.size = size
        self.elements = 0

        # Заполняем пустой ячейкой (вершиной связного списка).
        self.buckets = [Cell(None, None, None) for i in range(self.size)]

    def _hash(self, key, size=None):
        """
        Вычисляем хэш (индекс элемента массива).
        """
        return key % (size or self.size)

    def _find_cell_before(self, key):
        """
        Возвращает элемент связного списка, который стоит до искомого.
        Или None если искомого элемента нет.
        """

        # Получаем индекс элемента массива, используя хэширование.
        bucket_num = self._hash(key)
        # Получаем вершину подходящего связного списка.
        top = self.buckets[bucket_num]

        # Ищем элемент связного списка по ключу.
        cell = top
        while cell.next is not None:
            if cell.next.key == key:
                # Возвращаем предшествующий элемент.
                return cell
            cell = cell.next

        # Если элемента нет, то возвращаем None.
        return None

    def get(self, key):
        """
        Возвращает элемент по его ключу.
        Или None если элемента нет.
        """

        # Получаем элемент предшествующий искомому.
        cell_before = self._find_cell_before(key)

        if cell_before is None:
            return None

        # Возвращаем ячейку связного списка.
        return cell_before.next

    def insert(self, key, value):
        """
        Вставляем новое значение в хэш-таблицу.
        """
        current = self.get(key)
        if current is not None:
            current.value = value
            return

        # Получаем подходящий связный список для вставки нового элемента.
        bucket_num = self._hash(key)
        linked_list = self.buckets[bucket_num]

        # Добавляем новую ячейку в начало связного списка.
        new_cell = Cell(key, value, linked_list.next)
        linked_list.next = new_cell

        # Увеличиваем счетчик элементов хэш-таблицы.
        self.elements += 1

    def delete(self, key):
        """
        Удаляет элемент из хэш-таблицы по ключу.
        Возбуждает исключение, если элемента в хэш-таблице нет.
        """

        # Получаем элемент, который стоит перед тем, который нужно удалить.
        cell_before = self._find_cell_before(key)

        # Если такого нет, то возбуждаем исключение.
        if cell_before is None:
            raise ValueError(f"Ключа {key} нет в хэш-таблице.")

        # Удаляем элемент из связного списка.
        cell_before.next = cell_before.next.next

        # Обновляем количество элементов в хэш-таблице.
        self.elements -= 1
        return None

    def __str__(self):
        """
        Возвращает текстовое представление хэш таблицы
        """
        text = ""
        for _, cell in enumerate(self.buckets):
            text += f"{_}->"
            cell = cell.next
            cells = []
            while cell is not None:
                cells.append(f"{cell}")
                cell = cell.next
            text += "[{}] ".format(";".join(cells))
        return text.strip()

if __name__ == "__main__":
    ht = HashTable(3)
    ht.insert(617, 'a')
    ht.insert(313, 'b')
    ht.insert(254, 'c')
    ht.insert(123, 'd')
    ht.insert(637, 'e')
    print(ht)

    ht.insert(313, 't')
    print(ht)
