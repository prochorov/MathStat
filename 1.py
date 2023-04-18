# Функция для составления вариационного ряда
def create_variational_series(data):
    # Сортируем данные по возрастанию
    data.sort()
    # Возвращаем отсортированный список данных
    return data

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

# Выводим вариационный ряд на экран
print("Вариационный ряд: ", variational_series)
