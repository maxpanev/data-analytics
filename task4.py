import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome()  # Запускаем Chrome браузер

url = "https://www.divan.ru/krasnodar/category/divany-i-kresla"
driver.get(url)  # Открываем URL в браузере

time.sleep(3)  # Ждем 3 секунды, чтобы страница полностью загрузилась

divans = driver.find_elements(By.CLASS_NAME, '_Ud0k')  # Находим все элементы с классом '_Ud0k'

my_list = []

for divan in divans:
    try:
        price = divan.find_element(By.CSS_SELECTOR, 'span.ui-LD-ZU').text  # Пытаемся получить текст элемента
        my_list.append([price])  # Добавляем цену в список
    except NoSuchElementException:
        print("Произошла ошибка при парсинге")  # Если элемент не найден, выводим сообщение об ошибке
        continue

driver.quit()  # Закрываем браузер

with open("homework.csv", 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Price'])  # Записываем заголовок
    writer.writerows(my_list)  # Записываем данные в CSV файл