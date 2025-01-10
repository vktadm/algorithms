def factorial(n, result=1):
    """
    Алгоритм с хвостовой рекурсией.
    При каждом вызове мы передаем результат.
    """
    if n == 0:
        return result
    # Расчет результата, как результат прошлого вычисления умноженный на n.
    result = result * n
    return factorial(n - 1, result)


def factorial_loop(n):
    """
    Итеративный алгоритм.
    """
    result = 1
    while n != 0:
        # Результат изменяем на каждой итерации.
        # Фактически итерация тут заменяет рекурсивный вызов.
        result = result * n
        # Шаг цикла - это шаг рекурсии.
        n = n - 1
    return result


print(factorial(5))
print(factorial_loop(5))