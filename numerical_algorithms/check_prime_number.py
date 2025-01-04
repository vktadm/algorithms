from random import randint

def is_prime(p, tests):
    """
    Функция для проверки является ли число p простым.
    Используется тест простоты Ферма.
    tests - количество тестов, которые нужно произвести.
    """
    for i in range(tests):
        # Получаем случайное a.
        a = randint(1, p - 1)

        # Проверка на простоту с помощью возведения в степень по модулю.
        # Аналог выражения, a ** (p - 1) % p, но работает гораздо быстрее.
        if pow(a, p - 1, p) != 1:
            return False

    return True


tests = 10

# Простые числа
print(3539, is_prime(3539, tests))
print(479001599, is_prime(479001599, tests))

# Составные числа
print(2856, is_prime(2856, tests))
print(3537, is_prime(3537, tests))

# Число Кармайкла (составное)
print(321197185, is_prime(321197185, tests))