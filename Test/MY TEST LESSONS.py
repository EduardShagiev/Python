# import math
# import random
# list_1 = [1, 2, 3, 4, 5, 6, 7, ]
# print(len(list_1))
# list_1.append(11)
# print(list_1)
# list_1.remove(2)
# print(list_1)
# dict = {'left': '12', 'right': "234"}

# for item in dict:
#     print('{}, {}'.format(item, dict[item]))

# for (k, v) in dict.items():
#     print(k, v)

list_2 = [2, 0, 2, 0, 1, 1, 1, 3]
# print(list_2)
# list_2.sort()
# print(list_2)
#

# list_3 = [(i, i*i) for i in range(101) if i % 2 == 0]
# count = 0
# j = 0
# max_value = max(list_2)
# # print(max_value)
# for i in range(max_value+1):
#     if i in list_2:
#         count += 1
# print(count)
# print(len(set(list_2)))

# Сдвиг вперед и сдвиг назад
# list_4 = [1, 2, 3, 4, 5, ]
# k = int(input("Введите K - число сдвигов"))
# i = 0
# b = [0]*len(list_4)
# print(b)
# print(list_4)
# while (i != k):
#     list_4 = list_4[1:]+list_4[:1]
#     i += 1
# print(list_4)
# j = 0
# while (j != k):
#     list_4 = list_4[-1:]+list_4[:-1]
#     j += 1
# print(list_4)

dic = {"1": "10", "2": "20", "3": "30", "4": "40",
       "5": "50", "6": "40", "7": "30", "8": "20"}
list5 = []
for (k, v) in dic.items():
    print(v)
    list5.append(dic[k])
print(set(list5))
