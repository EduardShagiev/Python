# # Подготовка папки ко воторому ДЗ
# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть
# import math
# n = int(input("Введите n километров:  "))
# m = int(input("Введите m километров:  "))
# k = int(input("Введите m километров:  "))
# # result = math.ceil(n/2) + math.ceil(m/2) + math.ceil(k/2)
# result = (n+1)//2 + (m+1)//2 + (k+1)//2
# print(result)
coins = int(input("ВВЕДИТЕ КОЛ-ВО МОНЕТ: "))
count_heads = 0
count_tails = 0
while(coins!=0):
    side = int(input("Введите сторону монеты 1 - решка,  0 - орёл: "))
    if side == 0:
        count_heads += 1
        coins-=1
    else:
        count_tails += 1  
        coins -= 1 
if count_heads < count_tails:
    print(count_heads)
else:
    print(count_tails)
