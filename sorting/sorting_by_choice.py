def sorting_by_choice(values):
    """Сортировка выбором."""
    for i in range(len(values) - 1):
        min_idx = i
        for j in range(i + 1, len(values)):
            if values[min_idx] > values[j]:
                min_idx = j
        # Условие, чтобы не менялось итак наименьшее значение.
        if i != min_idx:
            values[min_idx], values[i] = values[i], values[min_idx]

data = [7, 4, 1, 10, 15, 3, 2]
sorting_by_choice(data)
print(data)