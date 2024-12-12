def insertionsort(array):
    i = 1

    while i < len(array):
        j = i - 1
        while array[j + 1] < array[j] and j >= 0:
            array[j + 1], array[j] = array[j], array[j + 1]
            j -= 1
        i += 1

array = [8, 5, 6, 1, 12]
print(array)
insertionsort(array)
print(array)