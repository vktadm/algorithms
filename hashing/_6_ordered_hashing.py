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

            # Смотрим, если существующий элемент больше нового.
            if self.table[probe].key > key:
                # Меняем значения и делаем рехэширование.
                old_item = self.table[probe]

                # Вставляем на текущее место новое значение.
                self.table[probe] = DataItem(key, value)

                # Запоминаем ключ и значение.
                key = old_item.key
                value = old_item.value

            # Переходим к следующей ячейке.
            probe = self._hash(probe + HashTable.STEP)

    def find(self, key):
        """
        Ищет элемент по ключу.
        Возвращает None если элемента нет в таблице.
        """
        probe = self._hash(key)
        step = 1
        num_probes = 0

        while True:
            num_probes += 1

            # Проверяем, не пуст ли очередной элемент.
            # А также не больше ли ключ.
            if (self.table[probe] is None) or (self.table[probe].key > key):
                return None

            # Проверяем, не находится ли в ячейке целевой элемент.
            if self.table[probe].key == key:
                return self.table[probe]

            # Проверяем, не прошли ли мы уже по кругу.
            if num_probes == self.size:
                return None

            # Переходим к следующей ячейке.
            probe = self._hash(probe + step)

    def __str__(self):
        """
        Выводит все ячейки хэш-таблицы.
        """
        text = ""
        for i in range(self.size):
            if self.table[i] is None:
                text += f"{i: 3d}: [--------]\n"
            else:
                text += f"{i: 3d}: {self.table[i]}\n"

        return text