# Из файла ДЗ2 
# Задание 1
# вариант 2 Введите одномерный целочисленный список.
# Найдите наибольший нечетный элемент.
# Найдите минимальный по модулю элемент списка.

# num_list = []
# numbers = input("Введите список чисел (через пробел): ").split()
# for i in numbers:
#     num_list.append(int(i))
#
# max_num = -999999999  # Просто задаем очень маленькое значение для начала
# for x in num_list:
#     if x % 2 != 0 and x > max_num:
#         max_num = x
# if max_num != -999999999:
#     print("Наибольший нечетный элемент:", max_num)
# else:
#     print("Нет нечетных элементов.")
#
# min_mod = num_list[0]
# for y in num_list:
#     if abs(y) < abs(min_mod):
#         min_mod = y
# print("Минимальный по модулю элемент:", min_mod)

# Вариант 4
# Найдите произведение элементов списка с нечетными номерами.
# Найдите наибольший элемент списка, затем удалите его и выведите новый список.

num_list1 = []
numbers = input("Введите список чисел (через пробел): ").split()
for i in numbers:
    num_list1.append(int(i))
odd_num = 1
for i in range(1, len(num_list1), 2):  # Идем через один (нечетные индексы)
    odd_num *= num_list1[i]
print("Произведение элементов списка с нечетными номерами:", odd_num)

max_num = max(num_list1)
num_list1.remove(max_num)
print("Новый список после удаления наибольшего элемента:", num_list1)

# Задание 2
# вариант 1

# import numpy as np
#
# matrix = np.array([
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ])
#
# sum_max = matrix[0].sum()
# row = 0
# for i in range(1, len(matrix)):
#     row_sum = matrix[i].sum()
#     if row_sum > sum_max:
#         sum_max = row_sum
#         row = i
# print("номер строки, сумма чисел в которой максиальна:",row+1)
