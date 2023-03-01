import math
import random
list_1 = [1, 2, 3, 4, 5, 6, 7, ]
print(len(list_1))
list_1.append(11)
print(list_1)
list_1.remove(2)
print(list_1)
dict = {'left': '12', 'right': "234"}

for item in dict:
    print('{}, {}'.format(item, dict[item]))

for (k, v) in dict.items():
    print(k, v)

list_2 = [2, 7, 8, 9, 14, 1, 12, ]
print(list_2)
list_2.sort()
print(list_2)

list_3 = [(i, i*i) for i in range(101) if i % 2 == 0]
print(list_3)
