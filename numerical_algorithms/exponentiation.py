def exp(value, p):
    # Результат возведения в степень (умножения).
    result = 1

    # Множитель.
    factor = value

    while p:
        # Если степень нечетная.
        if p % 2 == 1:
            result *= factor

        # Возводим множитель в квадрат, а степень уменьшаем в 2 раза.
        factor *= factor
        p //= 2

    return result


print(exp(9, 11))
print(9 ** 11)