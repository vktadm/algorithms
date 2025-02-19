from datetime import datetime
from random import choice, shuffle

# Города
# Калиниград, Москва, Санкт-Петербург, Казань, Воронеж, Тверь
cities_table = [
    [0, 1337, 1103, 2192, 1855, 1255],  # Калининград
    [1337 * 2, 0, 712, 825, 522, 192],  # Москва
    [1103, 712, 0, 1526, 1337, 531],  # Санкт-Петербург
    [2192, 825, 1526, 0, 1080, 1006],  # Казань
    [1855, 522, 1337, 1080, 0, 815],  # Воронеж
    [1255, 192, 531, 1006, 815, 0]  # Тверь
]

cities_names = ["Калининград", "Москва", "Санкт-Петербург", "Казань", "Воронеж", "Тверь"]

# Формируем индексы городов для перебора.
# [0, 1, 2, 3, 4, 5]
cities_idx = [i for i in range(len(cities_table))]

# Количество тестов
TESTS = (len(cities_idx) - 1) ** 3

calls = paths = 0

best_path = []
best_path_distance = float("inf")


def calc_distance(path):
    distance = 0
    prev_city = 0
    for city in path[1:]:
        distance += cities_table[prev_city][city]
        prev_city = city

    return distance


def init():
    global best_path, best_path_distance
    move_cities = cities_idx[1:]
    shuffle(move_cities)
    best_path = [0] + move_cities + [0]
    best_path_distance = calc_distance(best_path)


def improve(n, temperature=3):
    global best_path, best_path_distance

    # Общий цикл.
    for i in range(n):
        # Создаем копию пути для тестов
        move_path_variant = best_path[1:-1]

        # Зафиксированные города
        fixed_cities = set()

        # Локальные перестановки с фиксацией городов.
        for j in range(temperature):
            # Выбираем город из оставшихся.
            variants_for_choice = list(set(move_path_variant) - fixed_cities)
            city_1 = choice(variants_for_choice)

            # Отмечаем выбранный город.
            fixed_cities.add(city_1)

            # Выбор второго города.
            city_2 = city_1
            while city_2 == city_1:
                city_2 = choice(variants_for_choice)

            # Отмечаем второй город (быстрое остывание).
            fixed_cities.add(city_2)

            # Обмен городов.
            city_1_index = move_path_variant.index(city_1)
            city_2_index = move_path_variant.index(city_2)

            move_path_variant[city_1_index] = city_2
            move_path_variant[city_2_index] = city_1

        # Добавляем Калининград в начало и конец
        new_path = [0] + move_path_variant + [0]

        # Вычисляем дистанцию.
        new_path_distance = calc_distance(new_path)

        # Сравниваем с лучшим маршрутом.
        if new_path_distance < best_path_distance:
            best_path = new_path
            best_path_distance = new_path_distance


start = datetime.now()

init()
print("Начальный путь:", best_path)
print("Начальный путь (дистанция):", best_path_distance)

improve(TESTS, 3)
print("Лучший путь:", best_path)
print("Лучший путь (дистанция):", best_path_distance)

print("Время работы алгоритма:", datetime.now() - start)
