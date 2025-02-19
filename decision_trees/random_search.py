from datetime import datetime
from random import choice


# Города
# Калиниград, Москва, Санкт-Петербург, Казань, Воронеж, Тверь
cities_table = [
    [0,    1337, 1103, 2192, 1855, 1255],  # Калининград
    [1337 * 2, 0,    712,  825,  522,  192],   # Москва
    [1103, 712,  0,    1526, 1337, 531],   # Санкт-Петербург
    [2192, 825,  1526, 0,    1080, 1006],  # Казань
    [1855, 522,  1337, 1080, 0,    815],   # Воронеж
    [1255, 192,  531,  1006, 815,  0]      # Тверь
]

cities_names = ["Калининград", "Москва", "Санкт-Петербург", "Казань", "Воронеж", "Тверь"]

# Формируем индексы городов для перебора.
# [0, 1, 2, 3, 4, 5]
cities_idx = [i for i in range(len(cities_table))]

# Количество тестов
TESTS = 3 * (len(cities_idx) - 1) ** 3

calls = paths = 0

best_path = []
best_path_distance = float("inf")


def find_path(cities, city, path, distance):
    global calls, paths, best_path, best_path_distance
    calls += 1

    # Считаем дистанцию между текущим городом и последним.
    distance += cities_table[path[-1]][city] if path else 0

    path = path.copy()
    path.append(city)

    new_elements = cities[:]
    new_elements.remove(city)

    # Если городов не осталось, то значит мы в конце пути и можно делать расчет.
    if not new_elements:
        paths += 1

        # Добавляем Калининград
        path.append(0)

        # Считаем финальную дистанцию
        distance += cities_table[path[-2]][path[-1]]

        if distance < best_path_distance:
            best_path_distance = distance
            best_path = path

        return

    # Старый код
    # for e in new_cities:
    #    find_path(new_cities, e, path, distance)

    # Выбор случайного города и рекурсивный запуск функции
    new_city = choice(new_elements)
    find_path(new_elements, new_city, path, distance)


start = datetime.now()

for _ in range(TESTS):
    find_path(cities_idx, 0, [], 0)


print("Количество вызовов:", calls)
print("Количество путей:", paths)

print("Лучший путь:", best_path, best_path_distance)
print("Лучший путь (дистанция):", best_path_distance)


print("Время работы алгоритма:", datetime.now() - start)