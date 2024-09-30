import matplotlib.pyplot as plt
import numpy as np

# Параметры нормального распределения
mean = 0       # Среднее значение
std_dev = 1    # Стандартное отклонение
num_samples = 1000  # Количество образцов

# Генерация случайных чисел, распределенных по нормальному распределению
data = np.random.normal(mean, std_dev, num_samples)
plt.hist(data, bins=6)

plt.xlabel("x ось")
plt.ylabel("y ось")
plt.title("Гистограма для случайных чисел")

plt.show()

