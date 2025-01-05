class DataItem:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.deleted = False

    def __str__(self):
        return f"[{self.key:02d}:{self.value}]"

    def delete(self):
        self.deleted = True
        self.key = None
        self.value = None


class HashTable:
    STEP = 1

    def __init__(self, size):
        self.size = size
        self.elements = 0
        self.deleted_items = 0
        # Создаем хэш-таблицу и заполняем её None.
        self.table = [None for i in range(self.size)]

    def _hash(self, key):
        return key % self.size

    def add(self, key, value):
        """
        Добавляем элемент в хэш-таблицу.
        Возбуждаем исключение, если элемент уже есть в таблице.
        """

        # Проверяем заполненность хэш-таблицы.
        if self.elements == self.size:
            raise OverflowError

        # Рассчитываем начальный индекс для вставки.
        probe = self._hash(key)

        while True:
            # Проверяем, не пуст ли текущий элемент.
            if self.table[probe] is None or self.table[probe].deleted:
                # Если запись в удаленный элемент, то увеличиваем счетчик удаленных эл-в на 1
                if self.table[probe] is not None:
                    if self.table[probe].deleted:
                        self.deleted_items -= 1

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
            if self.table[probe].key == key and not self.table[probe].deleted:
                return self.table[probe]

            # Проверяем, не прошли ли мы уже по кругу.
            if num_probes == self.size:
                return None

            # Переходим к следующей ячейке.
            probe = self._hash(probe + HashTable.STEP)

    def delete(self, key):
        item = self.find(key)
        if item:
            item.delete()
            self.elements -= 1
            self.deleted_items += 1

            # Проверяем количество удаленных элементов и инициируем рехэширование при необходимости
            if (self.deleted_items / self.size) > 0.3:
                # print(f"Рехэширование из-за превышения {self.deleted_items} удаленных элементов.")
                self.rehash()

    def rehash(self):

        old_table = self.table.copy()
        self.elements = 0
        self.deleted_items = 0
        self.table = [None for i in range(self.size)]

        # Переносим элементы из старой таблицы в новую
        for item in old_table:
            if item is not None and not item.deleted:
                # Добавляем элемент в новую таблицу
                self.add(item.key, item.value)

        # Обновляем ссылку на новую таблицу
        del old_table

    def __str__(self):
        """
        Выводит все ячейки хэш-таблицы.
        """
        text = ""
        values = []
        for i in range(self.size):
            if self.table[i] is None:
                values.append(f"EMPTY")
            elif self.table[i].deleted:
                values.append(f"DELETED")
            else:
                values.append(f"{self.table[i]}")

        return " ".join(values)

if __name__ == "__main__":
    ht = HashTable(7)

    ht.add(47, 'A')
    ht.add(13, 'B')
    ht.add(5, 'C')
    ht.add(15, 'D')
    ht.add(25, 'E')
    print(ht)

    ht.delete(15)
    print(ht)

    ht.add(35, 'F')
    print(ht)

    ht.add(22, 'G')
    print(ht)

    ht.delete(25)
    print(ht)

    ht.delete(13)
    print(ht)