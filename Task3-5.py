# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# *Пример:*
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def fibonacci(n):
    if n>=0:
       fib_list = [0, 1]
       for _ in range(1,n):
           fib_list.append(fib_list[-2] + fib_list[-1])
       return fib_list[n]
    else:
        negafib_list = [0, 1]
        for _ in range(1, -n):
            negafib_list.append(negafib_list[-2] - negafib_list[-1])
    return negafib_list[-1]

k = 8
result = []
for i in range(-k,k+1):
   result.append(fibonacci(i))
print("Для числа", k, "искомая последовательность Негафибоначчи будет такая:\n", result)