# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# *Пример:*
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def IntToBinary(x):
    strBinary = ""
    if x == 0:
        return 0
    while x > 0:
        strBinary = str(x % 2)+strBinary
        x //= 2
    return strBinary

num = 45

print(IntToBinary(num))