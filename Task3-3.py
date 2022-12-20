# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# 
# *Пример:*
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# Технически, в примере ошибка. У пятерки дробная часть 0, значит она минимальная должна быть. Но сделал так, как в примере.

# импортируем модули рандомизатора 
from random import random, randint

# устанавливаем точность задаваемых вещественных чисел (кол-во цифр после запятой)
accuracy = 4

# функция герерирования случайного списка из n элементов в диапазоне от -10 до 9 с прибавлением рандомной дробной части
def generate_list(n):
    generated_list = []
    for _ in range(n):
        generated_list.append(round(randint(-10,9)+random(),accuracy))
    return generated_list

# определяем количество элементов списка
k = 7
# генерируем список случайных чисел
my_list = generate_list(k)
# вывод исходного списка
print("Исходный список:", my_list)

# функция нахождения максимальной дроной части
def findMaxFrac(flist):
    # по умолчанию - максимум 0
    maxFloatNum = 0
    # бежим по всему списку
    for f in flist:
        #если число целое - пропускаем его
        if f == int(f):
            continue
        # вычисляем дробную часть и если она больше максимума, то переприсваиваем
        if (abs(round(f-int(f), accuracy))) > maxFloatNum:
            maxFloatNum = abs(round(f-int(f), accuracy))
    return round(maxFloatNum,accuracy)

# функция нахождения минимальной дроной части
def findMinFrac(flist):
    # по умолчанию - минимум 1
    minFloatNum = 1
    # бежим по всему списку
    for f in flist:
        #если число целое - пропускаем его
        if f == int(f):
            continue
        # вычисляем дробную часть и если она меньше минимума, то переприсваиваем
        if (abs(round(f-int(f), accuracy))) < minFloatNum:
            minFloatNum = abs(round(f-int(f), accuracy))
    return round(minFloatNum,accuracy)

# находим Максимум, Минимум и выводим результат
print("Максимальная дробная часть: ", findMaxFrac(my_list))
print("Минимальная дробная часть: ", findMinFrac(my_list))
print("Разница между максимальной и минимальной дробной частью =", round(findMaxFrac(my_list)-findMinFrac(my_list),accuracy))
