#Задача 2: Найдите сумму цифр трехзначного числа.
#*Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

n= int(input("Input value n: "))
summa=0
while n>0:  
    x=n%10
    summa+=x
    n=n//10
print("",summa)
