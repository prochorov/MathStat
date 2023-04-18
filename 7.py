import numpy as np
from scipy.stats import chisquare

# Задаем выборочное среднее, несмещенную дисперсию и количество наблюдений
sample_mean = 168.28
sample_variance = 18.47
n = 10

# Ожидаемые значения для нормального распределения с такими параметрами
expected_values = np.full(n, sample_mean)

# Вычисляем статистику критерия Пирсона и p-значение
chi2_stat, p_value = chisquare(f_obs=expected_values, f_exp=expected_values)

# Задаем уровень значимости
alpha = 0.1

# Проводим проверку основной гипотезы
if p_value > alpha:
    print("Основная гипотеза (H0) не отвергается.")
else:
    print("Основная гипотеза (H0) отвергается в пользу конкурирующей гипотезы (H1).")
