import matplotlib.pyplot as plt
import numpy as np

x = np.random.rand(5)  # массив из 5 случайных чисел
y = np.random.rand(5)  # массив из 5 случайных чисел

plt.scatter(x, y)

plt.xlabel("ось Х")
plt.ylabel("ось Y")
plt.title("Диаграмма рассеяния для случайных чисел")

plt.show()