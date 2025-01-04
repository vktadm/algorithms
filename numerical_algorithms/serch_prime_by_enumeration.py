from math import sqrt, ceil

def is_prime(value):
    """
    Проверка числа на простоту методом перебора.
    """
    # Все числа от 1 до 3-х простые
    if value <= 3:
        return True

    # Проверяем на четность
    if value % 2 == 0:
        return False

    end = ceil(sqrt(value))

    for mult in range(3, end + 1, 2):
        if value % mult == 0:
            return False
    return True

q = False
value = None
print('Для выхода нажмите "q/Q"')

while not q:
    value = input('Введите значение для проверки на простоту? ')
    if value.lower() == 'q':
        q = True
    else:
        print("Простое" if is_prime(int(value)) else "Составное")