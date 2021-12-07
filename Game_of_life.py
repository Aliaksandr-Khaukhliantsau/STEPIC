# Напишите программу, вычисляющую следующее состояние поля для Game of life.
#
# Поле представляет собой прямоугольник, причём для крайних клеток поля соседними являются клетки с противоположного
# конца (поле представляет собой тор).
#
# Формат ввода:
#
# На первой строке указаны два целых числа через пробел -- высота и ширина поля.
# В следующих строках подаётся состояние поля. Точка "." обозначает мёртвую клетку, символ "X" − живую.
#
# Формат вывода:
# Следующее состояние поля, используя те же обозначения, что использовались на вводе.
#
# Sample Input 1:
#
# 5 5
# .....
# ..X..
# ...X.
# .XXX.
# .....
# Sample Output 1:
#
# .....
# .....
# .X.X.
# ..XX.
# ..X..
# Sample Input 2:
#
# 5 5
# .....
# .....
# .XXX.
# .....
# .....
# Sample Output 2:
#
# .....
# ..X..
# ..X..
# ..X..
# .....
# Sample Input 3:
#
# 5 6
# ...XX.
# .XX...
# ..X...
# XX....
# X..XX.
# Sample Output 3:
#
# .X..XX
# .XX...
# X.X...
# XXXX.X
# XXXXX.


from copy import deepcopy


def func_2(inp_f, out_f, buff, i, k):
    x = 0
    for j in buff:
        if j == 'X':
            x += 1

    if inp_f[i][k] == '.':
        if x == 3:
            out_f[i][k] = 'X'
        else:
            out_f[i][k] = '.'
    elif inp_f[i][k] == 'X':
        if x == 3 or x == 2:
            out_f[i][k] = 'X'
        else:
            out_f[i][k] = '.'
    return out_f[i][k]


def func():
    # size = tuple(int(i) for i in input().split())
    # inp_f = []

    size = [5, 6]
    # size = [5, 5]


    # for i in range(size[0]):
    #     inp_f.append(list(str(i) for i in input()))
    #     if len(inp_f[i]) != size[1]:
    #         return print(f'величина поля должна быть равна {size[1]}')

    inp_f = [['.', '.', '.', 'X', 'X', '.'], ['.', 'X', 'X', '.', '.', '.'], ['.', '.', 'X', '.', '.', '.'], ['X', 'X', '.', '.', '.', '.'], ['X', '.', '.', 'X', 'X', '.']]
    # inp_f = [['.', '.', '.', '.', '.'], ['.', '.', 'X', '.', '.'], ['.', '.', 'X', '.', '.'], ['.', '.', 'X', '.', '.'],
    #          ['.', '.', '.', '.', '.']]

    for i in inp_f:
        print_str = ''
        for k in i:
            print_str += k
        print(print_str)
    print('')

    out_f = deepcopy(inp_f)
    buff = ''

    for i in range(len(inp_f)):
        for k in range(len(inp_f[i])):
            if i == 0 and k == 0:
                buff += inp_f[0][-1] + inp_f[1][-1] + inp_f[1][0] + inp_f[1][1] + inp_f[0][1] + inp_f[-1][1] + inp_f[-1][0] + inp_f[-1][-1]  # буфер для проверки
            elif i == 0 and k == len(inp_f[i]) - 1:
                buff += inp_f[0][k - 1] + inp_f[1][k - 1] + inp_f[1][k] + inp_f[1][0] + inp_f[0][0] + inp_f[-1][0] + inp_f[-1][k] + inp_f[-1][k - 1]
            elif i == len(inp_f) - 1 and k == 0:
                buff += inp_f[i][-1] + inp_f[0][-1] + inp_f[0][0] + inp_f[0][1] + inp_f[i][1] + inp_f[i - 1][1] + inp_f[i - 1][0] + inp_f[i - 1][-1]
            elif i == len(inp_f) - 1 and k == len(inp_f[i]) - 1:
                buff += inp_f[i][k - 1] + inp_f[0][k - 1] + inp_f[0][k] + inp_f[0][0] + inp_f[i][0] + inp_f[i - 1][0] + inp_f[i - 1][k] + inp_f[i - 1][k - 1]
            elif i == 0:
                buff += inp_f[0][k - 1] + inp_f[1][k - 1] + inp_f[1][k] + inp_f[1][k + 1] + inp_f[0][k + 1] + inp_f[-1][k + 1] + inp_f[-1][k] + inp_f[-1][k - 1]
            elif i == len(inp_f) - 1:
                buff += inp_f[i][k - 1] + inp_f[0][k - 1] + inp_f[0][k] + inp_f[0][k + 1] + inp_f[i][k + 1] + inp_f[i - 1][k + 1] + inp_f[i - 1][k] + inp_f[i - 1][k - 1]
            elif k == 0:
                buff += inp_f[i][-1] + inp_f[i + 1][-1] + inp_f[i + 1][0] + inp_f[i + 1][1] + inp_f[i][1] + inp_f[i - 1][1] + inp_f[i - 1][0] + inp_f[i - 1][-1]
            elif k == len(inp_f[i]) - 1:
                buff += inp_f[i][k - 1] + inp_f[i + 1][k - 1] + inp_f[i + 1][k] + inp_f[i + 1][0] + inp_f[i][0] + inp_f[i - 1][0] + inp_f[i - 1][k] + inp_f[i - 1][k - 1]
            else:
                buff += inp_f[i][k - 1] + inp_f[i + 1][k - 1] + inp_f[i + 1][k] + inp_f[i + 1][k + 1] + inp_f[i][k + 1] + inp_f[i - 1][k + 1] + inp_f[i - 1][k] + inp_f[i - 1][k - 1]
            func_2(inp_f, out_f, buff, i, k)
            buff = ''

    for i in out_f:
        print_str = ''
        for k in i:
            print_str += k
        print(print_str)


func()


# from copy import deepcopy
#
# def func_2(inp_f, out_f, buff, i, k):
#     x = 0
#     for j in buff:
#         if j == 'X':
#             x += 1
#
#     if inp_f[i][k] == '.':
#         if x == 3:
#             out_f[i][k] = 'X'
#         else:
#             out_f[i][k] = '.'
#     elif inp_f[i][k] == 'X':
#         if x == 3 or x == 2:
#             out_f[i][k] = 'X'
#         else:
#             out_f[i][k] = '.'
#     return out_f
#
#
# def func():
#     # size = tuple(int(i) for i in input().split())
#     # inp_f = []
#     size = [5, 5]
#
#
#     # for i in range(size[0]):
#     #     inp_f.append(list(str(i) for i in input()))
#     #     if len(inp_f[i]) != size[1]:
#     #         return print(f'величина поля должна быть равна {size[1]}')
#
#     inp_f = [['.', '.', '.', '.', '.'], ['.', '.', 'X', '.', '.'], ['.', '.', 'X', '.', '.'], ['.', '.', 'X', '.', '.'], ['.', '.', '.', '.', '.']]
#
#     for i in inp_f:
#         print_str = ''
#         for k in i:
#             print_str += k
#         print(print_str)
#     print('')
#
#     out_f = deepcopy(inp_f)
#     buff = ''
#
#     for i in range(len(inp_f)):
#         for k in range(len(inp_f[i])):
#             if i == 0 and k == 0:
#                 buff += inp_f[i][k + 1] + inp_f[i + 1][k] + inp_f[i + 1][k + 1]  # буфер для проверки
#             elif i == 0 and k == len(inp_f[i]) - 1:
#                 buff += inp_f[i][k - 1] + inp_f[i + 1][k] + inp_f[i + 1][k - 1]
#             elif i == len(inp_f) - 1 and k == 0:
#                 buff += inp_f[i][k + 1] + inp_f[i - 1][k] + inp_f[i - 1][k + 1]
#             elif i == len(inp_f) - 1 and k == len(inp_f[i]) - 1:
#                 buff += inp_f[i][k - 1] + inp_f[i - 1][k] + inp_f[i - 1][k - 1]
#             elif i == 0:
#                 buff += inp_f[i][k - 1] + inp_f[i][k + 1] + inp_f[i + 1][k] + inp_f[i + 1][k - 1] + inp_f[i + 1][k + 1]
#             elif i == len(inp_f) - 1:
#                 buff += inp_f[i][k - 1] + inp_f[i][k + 1] + inp_f[i - 1][k] + inp_f[i - 1][k - 1] + inp_f[i - 1][k + 1]
#             elif k == 0:
#                 buff += inp_f[i - 1][k] + inp_f[i - 1][k + 1] + inp_f[i][k + 1] + inp_f[i + 1][k] + inp_f[i + 1][k + 1]
#             elif k == len(inp_f[i]) - 1:
#                 buff += inp_f[i - 1][k] + inp_f[i - 1][k - 1] + inp_f[i][k - 1] + inp_f[i + 1][k] + inp_f[i + 1][k - 1]
#             else:
#                 buff += inp_f[i][k - 1] + inp_f[i + 1][k - 1] + inp_f[i + 1][k] + inp_f[i + 1][k + 1] + inp_f[i][k + 1] + inp_f[i - 1][k - 1] + inp_f[i - 1][k] + inp_f[i - 1][k + 1]
#             out_f = func_2(inp_f, out_f, buff, i, k)
#             buff = ''
#
#     for i in out_f:
#         print_str = ''
#         for k in i:
#             print_str += k
#         print(print_str)
#
#
# func()