# Функция для составления вариационного ряда
def create_variational_series(data):
    # Удаляем повторяющиеся значения
    unique_data = list(set(data))
    # Сортируем уникальные данные по возрастанию
    unique_data.sort()
    # Создаем словарь, где ключом является число, а значением - его количество
    variational_series = {number: data.count(number) for number in unique_data}
    # Возвращаем вариационный ряд в виде словаря
    return variational_series

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
