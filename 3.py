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

# Количество участков
n = 10

# Вычисляем границы участков
step = (variational_series[-1] - variational_series[0]) / n
bins = np.arange(variational_series[0], variational_series[-1] + step, step)

# Построение полигона
plt.subplot(2, 1, 1)
plt.plot(variational_series, np.arange(1, len(variational_series) + 1) / len(variational_series), 'b-')
plt.xlabel('Значение')
plt.ylabel('Относительная частота')
plt.title('Полигон')

# Построение гистограммы
plt.subplot(2, 1, 2)
plt.hist(variational_series, bins=bins, density=True, alpha=0.75, color='b')
plt.xlabel('Интервалы участков')
plt.ylabel('Относительная частота')
plt.title('Гистограмма')

# Отображение графиков
plt.tight_layout()
plt.show()
