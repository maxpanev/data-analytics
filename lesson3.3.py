import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome()

url = "https://www.divan.ru/krasnodar/category/divany-i-kresla"

driver.get(url)

time.sleep(3)

divans = driver.find_elements(By.CLASS_NAME, '_Ud0k')

my_list = []

for divan in divans:
    try:
        price = divan.find_element(By.CSS_SELECTOR, 'span.ui-LD-ZU').text
        my_list.append([price])
    except NoSuchElementException:
        print("Произошла ошибка при парсинге")
        continue

driver.quit()

with open("homework.csv", 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Price'])
    writer.writerows(my_list)