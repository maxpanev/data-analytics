import csv
import matplotlib.pyplot as plt

# Имя файла с обработанными данными
filename = "processed_homework.csv"

# Чтение данных из CSV
prices = []
with open(filename, 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader)  # Пропускаем заголовок
    for row in reader:
        try:
            price = int(row[0])  # Преобразуем строку в число
            prices.append(price)
        except ValueError as e:
            print(f"Ошибка преобразования для строки {row}: {e}")

# Построение гистограммы
plt.figure(figsize=(10, 6))
plt.hist(prices, bins=20, color='skyblue', edgecolor='black')
plt.title('Распределение цен')
plt.xlabel('Цена (в рублях)')
plt.ylabel('Количество')
plt.grid(axis='y', alpha=0.75)

# Показать гистограмму
plt.show()