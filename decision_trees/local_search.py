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
TESTS = 3 * (len(cities_idx) - 1) ** 3

best_path = []
best_path_distance = float("inf")


def calc_distance(path):
    """
    Вычисляем расстояние между городами.
    """
    distance = 0
    prev_city = 0
    for city in path[1:]:
        distance += cities_table[prev_city][city]
        prev_city = city

    return distance


def init():
    """
    Инициализируем начальный маршрут, который будем улучшать.
    """
    global best_path, best_path_distance
    move_cities = cities_idx[1:]
    shuffle(move_cities)
    best_path = [0] + move_cities + [0]
    best_path_distance = calc_distance(best_path)


def improve(n):
    global best_path, best_path_distance

    for i in range(n):
        # Получаем текущий лучший путь (кроме Калининграда)
        move_path = best_path[1:-1]

        # Получаем первый город
        city_1 = choice(move_path)

        # Получаем второй город, чтобы он не был равен первому.
        city_2 = city_1
        while city_2 == city_1:
            city_2 = choice(move_path)

        # Делаем обмен
        city_1_index = move_path.index(city_1)
        city_2_index = move_path.index(city_2)

        move_path[city_1_index] = city_2
        move_path[city_2_index] = city_1

        # Генерируем новый путь и считаем его дистанцию.
        new_path = [0] + move_path + [0]
        new_path_distance = calc_distance(new_path)

        # Если новая дистанция лучше, то делаем замену.
        if new_path_distance < best_path_distance:
            best_path_distance = new_path_distance
            best_path = new_path


start = datetime.now()

init()
print("Начальный путь:", best_path, best_path_distance)
print("Начальный путь (дистанция):", best_path_distance)

improve(TESTS)
print("Лучший путь:", best_path, best_path_distance)
print("Лучший путь (дистанция):", best_path_distance)

print("Время работы алгоритма:", datetime.now() - start)
