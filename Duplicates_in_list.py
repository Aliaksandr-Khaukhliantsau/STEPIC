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


def func():
    my_list = []
    a = 0
    numb = input().split()
    for i in numb:
        my_list.append(int(i))
    my_list.sort()
    for i in my_list:
        if i == a:




print(func())