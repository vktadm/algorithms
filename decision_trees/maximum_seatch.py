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

def max_search(cities, city, path, distance):
    """
    Размещения без повторений.
    """
    global calls, iters, best_path, best_path_distance

    calls += 1

    # Считаем дистанцию между текущим городом и последним.
    distance += cities_table[path[-1]][city] if path else 0

    path = path.copy()
    path.append(city)

    new_cities = cities[:]
    new_cities.remove(city)

    # Если городов не осталось, то значит мы в конце пути и можно делать расчет.
    if not new_cities:

        # Добавляем Калининград
        path.append(0)

        # Считаем финальную дистанцию
        distance += cities_table[path[-2]][path[-1]]

        if distance < best_path_distance:
            best_path_distance = distance
            best_path = path

        return

    # Выбираем не случайный город, а ближайший.
    near_city = None
    near_city_distance = float("inf")

    # Перебираем потенциальные города
    for city_try in new_cities:
        iters += 1
        # Смотрим дистанцию
        distance_try = cities_table[city][city_try]
        if distance_try < near_city_distance:
            # Если она меньше, то это кандидат
            near_city = city_try
            near_city_distance = distance_try

    max_search(new_cities, near_city, path, distance)
