def merge(array1, array2):
    """
    Функция слияния двух отсортированных массивов в один.
    array1 и array2 - массивы представленные python-списками.
    """
    array = [None] * (len(array1) + len(array2))
    lenght = 0

    for i in range(0, len(array1)):
        array[i] = array1[i]
        lenght += 1

    for i in range(0, len(array2)):
        array[lenght] = array2[i]
        lenght += 1

    for i in range(0, lenght):
        for j in range(i+1, lenght):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
    return array

array1 = [3, 4, 7, 8]
array2 = [1, 5, 9]
print(merge(array1, array2))