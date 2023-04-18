import numpy as np

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

# Вычисляем выборочное среднее
sample_mean = np.mean(variational_series)

# Вычисляем несмещенную (исправленную) дисперсию
sample_variance = np.var(variational_series, ddof=1)

# Вычисляем среднеквадратическое отклонение
sample_std = np.sqrt(sample_variance)

# Выводим результаты
print("Выборочное среднее: {:.2f}".format(sample_mean))
print("Несмещенная (исправленная) дисперсия: {:.2f}".format(sample_variance))
print("Среднеквадратическое отклонение: {:.2f}".format(sample_std))
