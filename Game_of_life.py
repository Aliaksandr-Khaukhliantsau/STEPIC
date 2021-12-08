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


# from copy import deepcopy
#
#
# def result_print(out_f):
#     for y in out_f:
#         print_str = ''
#         for x in y:
#             print_str += x
#         print(print_str)
#
#
# def output_fields(inp_f, out_f, buff, y, x):
#     x = 0
#     for j in buff:
#         if j == 'X':
#             x += 1
#
#     if inp_f[y][x] == '.':
#         if x == 3:
#             out_f[y][x] = 'X'
#         else:
#             out_f[y][x] = '.'
#     elif inp_f[y][x] == 'X':
#         if x == 3 or x == 2:
#             out_f[y][x] = 'X'
#         else:
#             out_f[y][x] = '.'
#     return out_f[y][x]
#
#
# def input_field():
#     # size = tuple(int(y) for y in input().split())
#     #
#     size = [5, 6]
#     # size = [5, 5]
#
#     if size[0] == 0 or size[1] == 0:
#         return
#
#     inp_f = []
#
#
#     # for y in range(size[0]):
#     #     inp_f.append(list(str(y) for y in input()))
#     #     if len(inp_f[y]) != size[1]:
#     #         return print(f'величина поля должна быть равна {size[1]}')
#
#     inp_f = [['.', '.', '.', 'X', 'X', '.'],
#              ['.', 'X', 'X', '.', '.', '.'],
#              ['.', '.', 'X', '.', '.', '.'],
#              ['X', 'X', '.', '.', '.', '.'],
#              ['X', '.', '.', 'X', 'X', '.']]
#
#     # inp_f = [['.', '.', '.', '.', '.'],
#     #          ['.', '.', 'X', '.', '.'],
#     #          ['.', '.', 'X', '.', '.'],
#     #          ['.', '.', 'X', '.', '.'],
#     #          ['.', '.', '.', '.', '.']]
#
#     for y in inp_f:
#         print_str = ''
#         for x in y:
#             print_str += x
#         print(print_str)
#     print('')
#
#     out_f = deepcopy(inp_f)
#     buff = ''
#
#     # if size[0] == 1 and size[1] == 1:
#     #     result_print(out_f)
#     #     return
#     #
#     # if size[0] == 1:
#     #     pass
#     #
#     # if size[1] == 1:
#     #     pass
#
#     if size[0] < 2 or size[1] < 2:
#         return
#
#
#
#     for y in range(size[0]):
#         for x in range(size[1]):
#             if y == 0 and x == 0:
#                 buff += inp_f[0][-1] + inp_f[1][-1] + inp_f[1][0] + inp_f[1][1] + \
#                         inp_f[0][1] + inp_f[-1][1] + inp_f[-1][0] + inp_f[-1][-1]
#             elif y == 0 and x == size[1] - 1:
#                 buff += inp_f[0][x - 1] + inp_f[1][x - 1] + inp_f[1][x] + inp_f[1][0] + \
#                         inp_f[0][0] + inp_f[-1][0] + inp_f[-1][x] + inp_f[-1][x - 1]
#             elif y == size[0] - 1 and x == 0:
#                 buff += inp_f[y][-1] + inp_f[0][-1] + inp_f[0][0] + inp_f[0][1] + \
#                         inp_f[y][1] + inp_f[y - 1][1] + inp_f[y - 1][0] + inp_f[y - 1][-1]
#             elif y == size[0] - 1 and x == size[1] - 1:
#                 buff += inp_f[y][x - 1] + inp_f[0][x - 1] + inp_f[0][x] + inp_f[0][0] + \
#                         inp_f[y][0] + inp_f[y - 1][0] + inp_f[y - 1][x] + inp_f[y - 1][x - 1]
#             elif y == 0:
#                 buff += inp_f[0][x - 1] + inp_f[1][x - 1] + inp_f[1][x] + inp_f[1][x + 1] + \
#                         inp_f[0][x + 1] + inp_f[-1][x + 1] + inp_f[-1][x] + inp_f[-1][x - 1]
#             elif y == size[0] - 1:
#                 buff += inp_f[y][x - 1] + inp_f[0][x - 1] + inp_f[0][x] + inp_f[0][x + 1] + \
#                         inp_f[y][x + 1] + inp_f[y - 1][x + 1] + inp_f[y - 1][x] + inp_f[y - 1][x - 1]
#             elif x == 0:
#                 buff += inp_f[y][-1] + inp_f[y + 1][-1] + inp_f[y + 1][0] + inp_f[y + 1][1] + \
#                         inp_f[y][1] + inp_f[y - 1][1] + inp_f[y - 1][0] + inp_f[y - 1][-1]
#             elif x == size[1] - 1:
#                 buff += inp_f[y][x - 1] + inp_f[y + 1][x - 1] + inp_f[y + 1][x] + inp_f[y + 1][0] + \
#                         inp_f[y][0] + inp_f[y - 1][0] + inp_f[y - 1][x] + inp_f[y - 1][x - 1]
#             else:
#                 buff += inp_f[y][x - 1] + inp_f[y + 1][x - 1] + inp_f[y + 1][x] + inp_f[y + 1][x + 1] + \
#                         inp_f[y][x + 1] + inp_f[y - 1][x + 1] + inp_f[y - 1][x] + inp_f[y - 1][x - 1]
#             output_fields(inp_f, out_f, buff, y, x)
#             buff = ''
#
#     result_print(out_f)
#
#
# input_field()


from copy import deepcopy


def result_print(out_f):
    for cell in out_f:
        print_str = ''
        for k in cell:
            print_str += k
        print(print_str)


def output_fields(inp_f, out_f, buff, y, x):
    living_cell = 0
    for cell in buff:
        if cell == 'X':
            living_cell += 1

    if inp_f[y][x] == '.':
        if living_cell == 3:
            out_f[y][x] = 'X'
        else:
            out_f[y][x] = '.'
    elif inp_f[y][x] == 'X':
        if living_cell == 3 or living_cell == 2:
            out_f[y][x] = 'X'
        else:
            out_f[y][x] = '.'
    return out_f[y][x]


def check_field(size, inp_f, out_f, buff):
    for y in range(size[0]):
        for x in range(size[1]):

            if size[0] == 1 and size[1] == 1:
                buff += inp_f[0][0] + inp_f[0][0] + inp_f[0][0] + inp_f[0][0] + \
                        inp_f[0][0] + inp_f[0][0] + inp_f[0][0] + inp_f[0][0]
            elif size[0] == 1 and size[1] == 2:
                buff += inp_f[0][x - 1] + inp_f[0][x - 1] + inp_f[0][x] + inp_f[0][x - 1] + \
                        inp_f[0][x - 1] + inp_f[0][x - 1] + inp_f[0][x] + inp_f[0][x - 1]
            elif size[0] == 1 and x == size[1] - 1:
                buff += inp_f[0][x - 1] + inp_f[0][x - 1] + inp_f[0][x] + inp_f[0][0] + \
                        inp_f[0][0] + inp_f[0][0] + inp_f[0][x] + inp_f[0][x - 1]
            elif size[0] == 1:
                buff += inp_f[0][x - 1] + inp_f[0][x - 1] + inp_f[0][x] + inp_f[0][x + 1] + \
                        inp_f[0][x + 1] + inp_f[0][x + 1] + inp_f[0][x] + inp_f[0][x - 1]
            elif size[0] == 2 and size[1] == 1:
                buff += inp_f[y][0] + inp_f[y - 1][0] + inp_f[y - 1][0] + inp_f[y - 1][0] + \
                        inp_f[y][0] + inp_f[y - 1][0] + inp_f[y - 1][0] + inp_f[y - 1][0]
            elif y == size[0] - 1 and size[1] == 1:
                buff += inp_f[y][0] + inp_f[0][0] + inp_f[0][0] + inp_f[0][0] + \
                        inp_f[y][0] + inp_f[y - 1][0] + inp_f[y - 1][0] + inp_f[y - 1][0]
            elif size[1] == 1:
                buff += inp_f[y][0] + inp_f[y + 1][0] + inp_f[y + 1][0] + inp_f[y + 1][0] + \
                        inp_f[y][0] + inp_f[y - 1][0] + inp_f[y - 1][0] + inp_f[y - 1][0]
            elif y == 0 and x == 0:
                buff += inp_f[0][-1] + inp_f[1][-1] + inp_f[1][0] + inp_f[1][1] + \
                        inp_f[0][1] + inp_f[-1][1] + inp_f[-1][0] + inp_f[-1][-1]
            elif y == 0 and x == size[1] - 1:
                buff += inp_f[0][x - 1] + inp_f[1][x - 1] + inp_f[1][x] + inp_f[1][0] + \
                        inp_f[0][0] + inp_f[-1][0] + inp_f[-1][x] + inp_f[-1][x - 1]
            elif y == size[0] - 1 and x == 0:
                buff += inp_f[y][-1] + inp_f[0][-1] + inp_f[0][0] + inp_f[0][1] + \
                        inp_f[y][1] + inp_f[y - 1][1] + inp_f[y - 1][0] + inp_f[y - 1][-1]
            elif y == size[0] - 1 and x == size[1] - 1:
                buff += inp_f[y][x - 1] + inp_f[0][x - 1] + inp_f[0][x] + inp_f[0][0] + \
                        inp_f[y][0] + inp_f[y - 1][0] + inp_f[y - 1][x] + inp_f[y - 1][x - 1]
            elif y == 0:
                buff += inp_f[0][x - 1] + inp_f[1][x - 1] + inp_f[1][x] + inp_f[1][x + 1] + \
                        inp_f[0][x + 1] + inp_f[-1][x + 1] + inp_f[-1][x] + inp_f[-1][x - 1]
            elif y == size[0] - 1:
                buff += inp_f[y][x - 1] + inp_f[0][x - 1] + inp_f[0][x] + inp_f[0][x + 1] + \
                        inp_f[y][x + 1] + inp_f[y - 1][x + 1] + inp_f[y - 1][x] + inp_f[y - 1][x - 1]
            elif x == 0:
                buff += inp_f[y][-1] + inp_f[y + 1][-1] + inp_f[y + 1][0] + inp_f[y + 1][1] + \
                        inp_f[y][1] + inp_f[y - 1][1] + inp_f[y - 1][0] + inp_f[y - 1][-1]
            elif x == size[1] - 1:
                buff += inp_f[y][x - 1] + inp_f[y + 1][x - 1] + inp_f[y + 1][x] + inp_f[y + 1][0] + \
                        inp_f[y][0] + inp_f[y - 1][0] + inp_f[y - 1][x] + inp_f[y - 1][x - 1]
            else:
                buff += inp_f[y][x - 1] + inp_f[y + 1][x - 1] + inp_f[y + 1][x] + inp_f[y + 1][x + 1] + \
                        inp_f[y][x + 1] + inp_f[y - 1][x + 1] + inp_f[y - 1][x] + inp_f[y - 1][x - 1]
            output_fields(inp_f, out_f, buff, y, x)
            buff = ''

    result_print(out_f)


def input_field():
    size = tuple(int(i) for i in input().split())
    inp_f = []

    for i in range(size[0]):
        inp_f.append(list(str(i) for i in input()))
        if len(inp_f[i]) != size[1]:
            return print(f'ширина поля должна быть равна {size[1]}')

    out_f = deepcopy(inp_f)
    buff = ''

    check_field(size, inp_f, out_f, buff)


input_field()
