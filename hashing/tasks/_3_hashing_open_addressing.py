class DataItem:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return f"[{self.key:03d}:{self.value}]"


class HashTable:
    STEP = 1

    def __init__(self, size):
        self.size = size
        self.elements = 0
        # Создаем хэш-таблицу и заполняем её None.
        self.table = [None for i in range(self.size)]

    def _hash(self, key):
        return key % self.size

    def add(self, key, value):
        """
        Добавляем элемент в хэш-таблицу.
        Возбуждаем исключение, если элемент уже есть в таблице.

        item - уже существующий DataItem (например, для целей рехэширования, чтобы не пересоздавать объекты)
        """

        # Проверяем заполненность хэш-таблицы.
        if self.elements == self.size:
            raise OverflowError

        # Рассчитываем начальный индекс для вставки.
        probe = self._hash(key)

        while True:
            # Проверяем, не пуст ли текущий элемент.
            if self.table[probe] is None:
                # Вставляем элемент в хэш-таблицу.
                self.table[probe] = DataItem(key, value)
                self.elements += 1
                return

            # Проверяем, нет ли элемента с переданным ключом в таблице.
            if self.table[probe].key == key:
                raise ValueError(f"Ключ {key} уже находится в таблице под индексом {probe}.)")

            # Переходим к следующей ячейке.
            probe = self._hash(probe + HashTable.STEP)

    def find(self, key):
        """
        Ищет элемент по ключу.
        Возвращает None если элемента нет в таблице.
        """
        probe = self._hash(key)
        num_probes = 0

        while True:
            num_probes += 1

            # Проверяем, не пуст ли очередной элемент.
            if self.table[probe] is None:
                return None

            # Проверяем, не находится ли в ячейке целевой элемент.
            if self.table[probe].key == key:
                return self.table[probe]

            # Проверяем, не прошли ли мы уже по кругу.
            if num_probes == self.size:
                return None

            # Переходим к следующей ячейке.
            probe = self._hash(probe + HashTable.STEP)

    def change_size(self, new_size):
        # Создаем новую таблицу с новым размером
        new_table = [None for _ in range(new_size)]

        # Обнуляем количество элементов в текущей таблице
        self.elements = 0

        # Переносим элементы из старой таблицы в новую
        for item in self.table:
            if item is not None:
                # Вставляем элемент в новую таблицу
                probe = item.key % new_size

                while True:
                    if new_table[probe] is None:
                        new_table[probe] = item  # Перемещаем ссылку на существующий объект
                        self.elements += 1
                        break

                    probe = (probe + HashTable.STEP) % new_size

        # Обновляем размер и таблицу хэш-таблицы
        self.size = new_size
        self.table = new_table

    def __str__(self):
        """
        Выводит все ячейки хэш-таблицы.
        """
        text = []
        for i in range(self.size):
            if self.table[i] is None:
                text.append(f"{i: 3d}: [---]")
            else:
                text.append(f"{i: 3d}: {self.table[i]}")

        return "\n".join(text)


if __name__ == "__main__":
    ht = HashTable(5)
    ht.add(617, "a")
    ht.add(313, "b")
    ht.add(254, "c")
    ht.add(123, "d")
    ht.add(637, "e")
    print(ht)

    ht.change_size(10)
    print(ht)