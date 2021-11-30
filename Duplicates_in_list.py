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

# def func():
#     my_list = []
#     result = []
#     a = int
#     numb = input().split()
#     for i in numb:
#         my_list.append(int(i))
#     my_list.sort()
#     for i in my_list:
#         if i == a:
#             result.append(str(i))
#         a = i
#     result = set(result)
#     return ' '.join(result)
#
#
# print(func())


# второй вариант

import collections


# def func():
#     result = []
#     my_collection = collections.Counter()
#     numb = input().split()
#     for i in numb:
#         my_collection[i] += 1
#     for i, k in my_collection.most_common():
#         if k > 1:
#             result.append(i)
#     return ' '.join(result)
#
#
# print(func())


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
