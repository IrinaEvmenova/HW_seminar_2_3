# 2'. Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# *Пример:*

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# num = [2, 3, 4, 5, 6]
# result = []

# for i in range(0, len(num), 2):
#     result.append(num[i] * num[i + 1])

# print(str(result))

nums = [1, 5, 7, 2, 4, 9, 8, 6]
def pair_multi(nums: list[int]) -> list[int]:
    '''Возвращает список произведений пар элементов'''
    pairs = []
    iterations = int(round((len(nums)+1)/2))
    print(iterations)
    for i in range(iterations):
        pairs.append(nums[i] * nums[-1-i])
    return pairs

print(pair_multi(nums))