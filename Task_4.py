# 4'. Напишите программу, которая будет преобразовывать десятичное число
# в двоичное.

# *Пример:*

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def ordinary_bin(n: int) -> str:
    '''Возвращает привычную двоичную запись числа'''
    return bin(n)[2::]

def binar(number):
    number_bin_manual = ''
    temp = number
    while temp > 0:
        number_bin_manual = str(temp % 2) + number_bin_manual
        temp = temp // 2
    number_bin_manual = '0b' + number_bin_manual

print(ordinary_bin(2))