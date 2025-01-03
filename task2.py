import matplotlib.pyplot as plt
import numpy as np

# Параметры нормального распределения
mean = 0       # Среднее значение
std_dev = 1    # Стандартное отклонение
num_samples = 1000  # Количество образцов

# Генерация случайных чисел, распределенных по нормальному распределению
# Используем numpy для создания массива из 1000 случайных чисел
# с нормальным распределением, заданным средним и стандартным отклонением.
data = np.random.normal(mean, std_dev, num_samples)

# Построение гистограммы для визуализации распределения данных
# 'bins=6' означает, что данные будут сгруппированы в 6 интервалов.
plt.hist(data, bins=6)

# Подписи для осей и заголовок графика
plt.xlabel("x ось")  # Подпись для оси x
plt.ylabel("y ось")  # Подпись для оси y
plt.title("Гистограма для случайных чисел")  # Заголовок графика

# Отображение графика
plt.show()