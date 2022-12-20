# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# 
# *Пример:*
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# Технически, в примере ошибка. У пятерки дробная часть 0, значит она минимальная должна быть. Но сделал так, как в примере.


from random import random, randint
from math import floor

accuracy = 4

def generate_list(n):
    generated_list = []
    for _ in range(n):
        generated_list.append(round(randint(-10,9)+random(),accuracy))
    return generated_list

my_list = generate_list(7)
# my_list = [1.1, 1.2, 3.1, 5, 10.01]
print("Исходный список:", my_list)

def findMaxFrac(flist):
    maxFloatNum = 0
    for f in flist:
        if f == int(f):
            continue
        # print(abs(round(f-int(f), accuracy)))
        if (abs(round(f-int(f), accuracy))) > maxFloatNum:
            maxFloatNum = abs(round(f-int(f), accuracy))
    return round(maxFloatNum,4)

def findMinFrac(flist):
    minFloatNum = 1
    for f in flist:
        if f == int(f):
            continue
        # print(abs(round(f-int(f), accuracy)))
        if (abs(round(f-int(f), accuracy))) < minFloatNum:
            minFloatNum = abs(round(f-int(f), accuracy))
    return round(minFloatNum,accuracy)

print("Максимальная дробная часть: ", findMaxFrac(my_list))
print("Минимальная дробная часть: ", findMinFrac(my_list))
print("Разница между максимальной и минимальной дробной частью =", round(findMaxFrac(my_list)-findMinFrac(my_list),accuracy))
