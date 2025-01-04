"""Организация хэш-таблицы методом прямого связывания."""
class Cell:
    def __init__(self, key, value, next_node):
        self.key = key
        self.value = value
        self.next = next_node

    def __str__(self):
        return f"[{self.key}:{self.value}]"


class HashTable:
    def __init__(self, size):
        """
        Создаем массив и заполняем его связными списками.
        """
        self.size = size
        self.elements = 0

        # Заполняем пустой ячейкой (вершиной связного списка).
        self.buckets = [Cell(None, None, None) for i in range(self.size)]

    def _hash(self, key):
        """
        Вычисляем хэш (индекс элемента массива).
        """
        return key % self.size

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

        # Ищем значение в хэш-таблице, если оно уже есть, то вызываем исключение.
        if self.get(key) is not None:
            raise ValueError("Ключ {key} уже находится в хэш-таблице.".format(key=key))

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
        Возвращает текстовое представление хэш таблицы.
        """
        text = ""
        for _, cell in enumerate(self.buckets):
            text += f"{_}:"
            cell = cell.next
            while cell is not None:
                text += f" {cell}"
                cell = cell.next
            text += "\n"
        return text

    def change_size(self, new_size):
        """
        Изменяет размер хэш таблицы и делает рехэширование.
        """
        # Создаем новый массив.
        # Делаем рехэширование.
        # Заменяем старый массив новым.


if __name__ == "__main__":
    ht = HashTable(10)
    for key, value in map(lambda x: [int(x[1:4]), x],
                          ["B617KM39RUS", "B313AB39RUS", "C254HE39RUS", "E123OK39RUS",
                           "H637EA39RUS", "O129BA39RUS", "T765KP39RUS", "E389BT39RUS",
                           "B204BA39RUS", "M001EC39RUS", "A973AA39RUS", "C349EP39RUS",
                           "C166OK39RUS", "H555HH39RUS", "K675KH39RUS", "E746OP39RUS",
                           "T162BA39RUS", "C130BE39RUS", "B498BE39RUS", "B516MK39RUS"]):
        ht.insert(key, value)
    print(ht)
