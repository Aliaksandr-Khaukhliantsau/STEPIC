# Выведите таблицу размером n \times nn×n, заполненную целыми числами от 11 до n^2n
# 2
#   по спирали, выходящей из левого верхнего угла и закрученной по часовой стрелке, как показано в примере.
#
# Формат ввода:
# Одна строка, содержащая одно целое число nn, n > 0n>0.
#
# Формат вывода:
# Таблица из nn строк, значения в строках разделены пробелом.
#
# Sample Input:
#
# 5
# Sample Output:
#
# 1 2 3 4 5
# 16 17 18 19 6
# 15 24 25 20 7
# 14 23 22 21 8
# 13 12 11 10 9

def func():
    # len_lst = [i for i in range(1, (int(input())) ** 2 + 1)]
    # print(len_lst)


    lst = []
    inp = int(input())

    # for i in range(inp):
    #     for q in range(i):
    #         lst.append([])

    # print(lst)

    _result = [[1, 2, 3, 4, 5], [6, 7, 8, 9], [10, 11, 12, 13], [14, 15, 16], [17, 18, 19], [20, 21], [22, 23], [24], [25]]

    p = 0

    while p < inp * 2 - 1:
        lst.append([])
        p += 1

    print(lst)


        # [] * p + [] * (p - 1) + [] * (p - 1) + [] * (p - 2) + [] * (p - 2) + [] * (p - 3) + [] * (p - 3) + [] * (p - 4) + [] * (p - 4)




func()
