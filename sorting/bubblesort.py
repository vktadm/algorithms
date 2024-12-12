def bubblesort(values):
    is_sorted = False
    n = 1
    while not is_sorted:
        is_sorted = True
        for i in range(len(values) - n):
            if values[i] > values[i + 1]:
                values[i], values[i + 1] = values[i + 1], values[i]
                is_sorted = False
        n += 1

def reverse_bubblesort(values):
    is_sorted = False
    n = 1
    while not is_sorted:
        is_sorted = True
        for i in range(len(values) - n):
            if values[i] < values[i + 1]:
                values[i], values[i + 1] = values[i + 1], values[i]
                is_sorted = False
        n += 1