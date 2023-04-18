import matplotlib.pyplot as plt
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

# Вычисляем значения эмпирической функции распределения
x = variational_series
y = np.arange(1, len(x) + 1) / len(x)

# Построение графика эмпирической функции распределения
plt.plot(x, y, 'b-')
plt.xlabel('Значение')
plt.ylabel('Эмпирическая функция распределения')
plt.title('Эмпирическая функция распределения')

# Отображение графика
plt.show()
