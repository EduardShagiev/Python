# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества.
# m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.
import random
n = int(input("Введите длинну первого массива"))
m = int(input("Введите длинну вторго массива"))
lst_1 = []
lst_2 = []
for i in range(n):
    lst_1.append(
        int(input("Ввдеите занчение для первого списка :")))

for i in range(m):
    lst_2.append(
        int(input("Ввдеите занчение для второго списка :")))
print(lst_1)
print(lst_2)

set_1 = set(lst_1)
set_2 = set(lst_2)

lst_3 = list(set_1 & set_2)
print(sorted(lst_3))
