def binary_search(value, array):
    min_index = 0
    max_index = len(array) - 1
    rez = -1

    # Цикл до тех пор, пока min и max не встретятся
    while min_index <= max_index:

        # Вычисляем средний элемент.
        middle_index = (min_index + max_index) // 2

        # Меняем max_index и min_index.
        if value < array[middle_index]:
            max_index = middle_index - 1
        elif value > array[middle_index]:
            min_index = middle_index + 1
        else:
            rez = middle_index
            min_index = middle_index + 1
    return rez

val = int(input())
values = list(map(int, input().split()))
print(binary_search(val, values))

print(binary_search(8, [1, 1, 1, 2, 2, 2, 3, 4, 5, 5, 6, 6, 8, 8]))