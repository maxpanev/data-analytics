import csv
from statistics import mean

input_filename = "homework.csv"
output_filename = "processed_homework.csv"

# Чтение данных из CSV и их обработка
with open(input_filename, 'r', encoding='utf-8') as infile:
    reader = csv.reader(infile)
    header = next(reader)  # Считываем заголовок
    processed_data = []

    for row in reader:
        try:
            price_str = row[0]
            price_number = int(price_str.replace('руб.', '').replace(' ', ''))  # Преобразуем строку в число
            processed_data.append([price_number])  # Добавляем цену в обработанный список
        except ValueError as e:
            print(f"Ошибка преобразования для строки {row}: {e}")  # Сообщение об ошибке
            continue

# Запись обработанных данных в новый CSV файл
with open(output_filename, 'w', newline='', encoding='utf-8') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(['Price'])  # Записываем заголовок
    writer.writerows(processed_data)  # Записываем обработанные данные

# Вычисление средней цены
def calculate_average_price(file_path):
    prices = []

    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            try:
                price = int(row['Price'])
                prices.append(price)  # Добавляем цену в список
            except ValueError:
                continue

    if prices:
        average_price = mean(prices)  # Вычисляем среднюю цену
        print(f"Средняя цена: {average_price:.2f} руб.")  # Выводим среднюю цену
    else:
        print("Цены не найдены или все значения некорректны.")

# Вывод средней цены из processed_homework.csv
calculate_average_price(output_filename)