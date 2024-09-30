import csv

input_filename = "homework.csv"
output_filename = "processed_homework.csv"

# Чтение данных из CSV и их обработка
with open(input_filename, 'r', encoding='utf-8') as infile:
    reader = csv.reader(infile)
    header = next(reader)  # Считываем заголовок
    processed_data = []

    for row in reader:
        try:
            # Предполагается, что цена находится в первой колонке
            price_str = row[0]
            # Удаляем 'руб.' и пробелы, затем преобразуем в число
            price_number = int(price_str.replace('руб.', '').replace(' ', ''))
            processed_data.append([price_number])
        except ValueError as e:
            print(f"Ошибка преобразования для строки {row}: {e}")
            continue

# Запись обработанных данных в новый CSV файл
with open(output_filename, 'w', newline='', encoding='utf-8') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(header)  # Записываем заголовок
    writer.writerows(processed_data)