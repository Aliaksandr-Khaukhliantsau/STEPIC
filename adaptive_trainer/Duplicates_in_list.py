# Напишите программу, которая принимает на вход список целых чисел и выводит на экран значения, которые повторяются в
# нём более одного раза.
#
# Для решения задачи может пригодиться метод sort списка.
#
# Формат ввода:
# Одна строка с целыми числами, разделёнными пробелом.
#
# Формат вывода:
# Строка, содержащая числа, разделённые пробелом. Числа не должны повторяться, порядок вывода может быть произвольным.
#
# Sample Input:
#
# 4 8 0 3 4 2 0 3
# Sample Output:
#
# 0 3 4


# первый вариант

# def input_field():
#     my_list = []
#     result = []
#     a = int
#     numb = input().split()
#     for y in numb:
#         my_list.append(int(y))
#     my_list.sort()
#     for y in my_list:
#         if y == a:
#             result.append(str(y))
#         a = y
#     result = set(result)
#     return ' '.join(result)
#
#
# print(input_field())


# второй вариант

import collections


# def input_field():
#     result = []
#     my_collection = collections.Counter()
#     numb = input().split()
#     for y in numb:
#         my_collection[y] += 1
#     for y, x in my_collection.most_common():
#         if x > 1:
#             result.append(y)
#     return ' '.join(result)
#
#
# print(input_field())


# третий вариант
def func():
    numb = input().split()
    buff = set()
    result = set()
    for i in numb:
        if i in buff:
            result.add(i)
        else:
            buff.add(i)
    print(*result)


func()
