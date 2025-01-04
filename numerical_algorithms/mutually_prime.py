"""Определить взаимно простые ли числа?"""
def gcd(a, b):
    # Наибольший общий делитель
    while b:
        a, b = b, a % b
    return a


number1 = int(input('Введите первое число? '))
number2 = int(input('Введите второе число? '))

# Если НОД двух чисел нравен 1, то эти числа взаимно простые.
print("1" if gcd(number1, number2) == 1 else "0")

# Запарный способ

# def find_factors(number):
#     factors = []
#
#     # Проверяем делимость на 2.
#     while number % 2 == 0:
#         factors.append(2)
#         number = number // 2
#
#     i = 3
#     max_factor = number ** .5
#     while i <= max_factor:
#         # Проверяем делимость на i.
#         # Используем while, так как number
#         # может иметь несколько одинаковых простых делителей,
#         while number % i == 0:
#             factors.append(i)
#             number = number // i
#             max_factor = number ** .5
#
#         # Увеличиваем на 2, так как рассматриваем только нечетные числа.
#         i += 2
#
#     if number > 1:
#         factors.append(number)
#
#     return factors
#
# def check_factors(first_number, second_number):
#     first_factors, second_factors = find_factors(first_number), find_factors(second_number)
#     for value in first_factors:
#         if value in second_factors:
#             return False
#     return True
#
#
# first_number = int(input('Введите первое число? '))
# second_number = int(input('Введите второе число? '))
#
# print(1 if check_factors(first_number, second_number) else 0)