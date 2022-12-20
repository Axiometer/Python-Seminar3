# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
from random import randint

def generate_list(n):
    generated_list = []
    for _ in range(n):
        generated_list.append(randint(-10,10))
    return generated_list

my_list = generate_list(6)

sum = 0

for i in range(len(my_list)):
    if i % 2 != 0:
        sum+=my_list[i]

print("Сгенерирован случайный список: ", my_list)
print("Сумма всех элементов на нечетных позициях: ", sum)