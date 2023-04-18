# Функция для составления вариационного ряда
def create_variational_series(data):
    # Сортируем данные по возрастанию
    data.sort()
    # Возвращаем отсортированный список данных
    return data

# Функция для нахождения минимального значения
def find_min(data):
    return min(data)

# Функция для нахождения максимального значения
def find_max(data):
    return max(data)

# Функция для нахождения моды
def find_mode(data):
    mode = max(data, key=data.count)
    return mode

# Функция для нахождения медианы
def find_median(data):
    n = len(data)
    if n % 2 == 0:
        median = (data[n//2 - 1] + data[n//2]) / 2
    else:
        median = data[n//2]
    return median

# Имя файла с данными
file_name = "64.txt"

# Чтение данных из файла
with open(file_name, "r") as file:
    # Читаем данные из файла и разделяем их по пробелам
    data = file.read().split()
    # Преобразуем строки в числа
    data = [int(number) for number in data]

# Вызываем функцию составления вариационного ряда
variational_series = create_variational_series(data)

# Находим минимальное и максимальное значения
xmin = find_min(variational_series)
xmax = find_max(variational_series)

# Находим моду
mode = find_mode(variational_series)

# Находим медиану
median = find_median(variational_series)

# Выводим результаты на экран
print("xmin: ", xmin)
print("xmax: ", xmax)
print("Мода: ", mode)
print("Медиана: ", median)
