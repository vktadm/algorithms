class DataItem:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.deleted = False

    def __str__(self):
        return f"[{self.key:03d}:{self.value}]"

    def delete(self):
        self.deleted = True
        self.key = None
        self.value = None


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

        # Расчитываем начальный индекс для вставки.
        probe = self._hash(key)

        while True:
            # Проверяем, не пуст ли текущий элемент.
            if self.table[probe] is None or self.table[probe].deleted:
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
        """
        Удаляем элемент из хэш-таблицы.
        """
        item = self.find(key)
        if item:
            self.elements -= 1
            item.delete()

    def __str__(self):
        """
        Выводит все ячейки хэш-таблицы.
        """
        text = ""
        for i in range(self.size):
            if self.table[i] is None:
                text += f"{i: 3d}: [--------]\n"
            elif self.table[i].deleted:
                text += f"{i: 3d}: deleted\n"
            else:
                text += f"{i: 3d}: {self.table[i]}\n"

        return text


if __name__ == "__main__":
    ht = HashTable(5)

    for key, value in map(lambda x: [int(x[1:4]), x],
                          ["B617KM39RUS", "B398AB39RUS", "C254HE39RUS", "E123OK39RUS", "H637EA39RUS"]):
        ht.add(key, value)
    print(ht)

    ht.delete(617)
    ht.delete(637)
    print(ht)

    ht.add(557, "H557OP39RUS")
    print(ht)