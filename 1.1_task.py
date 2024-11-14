# Задание 1
# Вариант 4

# month = int(input("Введите номер месяца: "))
#
# if month in [12, 1, 2]:
#     print("Зима")
# elif month in [3, 4, 5]:
#     print("Весна")
# elif month in [6, 7, 8]:
#     print("Лето")
# elif month in [9, 10, 11]:
#     print("Осень")
# else:
#     print("Нет такого месяца")

# Задание 2
# Вариант 3 О каждом учащемся класса известны его пол, год рождения, рост и вес.
# Определить, сколько в классе мальчиков и сколько девочек.
# Найти средний возраст мальчиков и девочек. Определить, верно ли,
# что самый высокий мальчик весит больше всех в классе,
# а самая маленькая девочка является самой юной среди девочек.
# children = [
#     {"gender": "male", "birth_year": 2005, "height": 170, "weight": 65},
#     {"gender": "female", "birth_year": 2007, "height": 160, "weight": 55},
#     {"gender": "male", "birth_year": 2004, "height": 180, "weight": 75},
#     {"gender": "female", "birth_year": 2006, "height": 150, "weight": 50},
#     {"gender": "male", "birth_year": 2006, "height": 175, "weight": 70},
#     {"gender": "female", "birth_year": 2005, "height": 155, "weight": 60}
# ]

# 1. Подсчет мальчиков и девочек
# boys = 0
# girls = 0
# for child  in children:
#     if child["gender"] == "male":
#         boys += 1
#     else:
#         girls += 1
#
# print("Количество мальчиков: " + str(boys))
# print("Количество девочек: " + str(girls))

# 2. Средний возраст мальчиков и девочек
# current_year = 2024
# boys_age = 0
# girls_age = 0
#
# for child in children:
#     if child["gender"] == "male":
#         boys_age += current_year - child["birth_year"]
#     else:
#         girls_age += current_year - child["birth_year"]
# average_boys_age = boys_age / boys
# average_girls_age = girls_age / boys
# if boys > 0:
#     print("Средний возраст мальчиков: " + str(round(average_boys_age, 2)))
# else:
#     print("Средний возраст мальчиков: 0")
#
# if girls > 0:
#     print("Средний возраст девочек: " + str(round(average_girls_age, 2)))
# else:
#     print("Средний возраст девочек: 0")
# 3. Проверки
# Самый высокий мальчик весит больше всех?

# tallest_boy =children[0]
# for child in children:
#         if child["gender"] == "male" and child["height"] > tallest_boy["height"]:
#             tallest_boy = child
# print("самый высокий мальчик: " + str(tallest_boy))
# if tallest_boy:
#     if tallest_boy["weight"] >= max(child["weight"] for child in children):
#         print("Самый высокий мальчик весит больше всех в классе.")
#     else:
#         print("Самый высокий мальчик не весит больше всех в классе.")

# 2. Находим самую низкую девочку и проверяем, является ли она самой юной среди девочек
# shortest_girl =children[0]
# for child in children:
#         if child["gender"] == "female" and child["height"] < shortest_girl["height"]:
#             shortest_girl = child
# print("самая низкая девочка: " + str(shortest_girl))
# if shortest_girl:
#     if shortest_girl["weight"] == min(child["birth_year"] for child in children):
#         print("самая низкая девочка младше всех в классе.")
#     else:
#         print("самая низкая девочка не младше всех в классе.")

# Задача 3
#Вариант 2
#Сформировать одномерный список целых чисел A, используя генератор случайных чисел (диапазон от 0 до 99).
# Размер списка n ввести с клавиатуры.
# В соответствии со своим вариантом написать программу по условию, представленному в таблице ниже:
# Все четные по значению элементы исходного списка A поместить в новый список B.

import random

# Вводим размер списка n
n = int(input("Введите кол-во элементов в списке n: "))

# Формируем список A с
A = []
for i in range(n):
    a = random.randint(0, 99)
    A.append(a)

# Создаем новый список B, включающий только четные элементы из A
B = [x for x in A if x % 2 == 0]

# Выводим результаты
print("Список A:", A)
print("Список B (четные элементы):", B)