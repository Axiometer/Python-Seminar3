# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# *Пример:*
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# можно было бы вынести поиск первого и последнего элемента в функции и удалять поочередно элементы из списка,
# но показалось, что изменять начальный список не очень хорошая идея

from random import randint

def generate_list(n):
    generated_list = []
    for _ in range(n):
        generated_list.append(randint(-10,10))
    return generated_list

my_list = generate_list(7)
print("Исходный список:", my_list)

mult_list = []

i = len(my_list)

while i>int((len(my_list)+1)/2):
    # mult_list.append()
    print("Перемножаем пару", my_list[len(my_list)-i], "и", my_list[i-1])
    mult_list.append(my_list[len(my_list)-i] * my_list[i-1])
    i -= 1

print("Получаемый результат:", mult_list)