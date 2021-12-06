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
from pprint import pprint


def func():
    size = tuple(int(i) for i in input().split())
    inp_f = []

    for i in range(size[0]):
        inp_f.append(list(str(i) for i in input()))
        if len(inp_f[i]) != size[1]:
            return print(f'величина поля должна быть равна {size[1]}')


    out_f = inp_f
    buff = ''

    for i in range(len(inp_f)):
        for k in range(len(inp_f[i])):
            if i == 0 and k == 0:
                buff = buff + inp_f[i][k] + inp_f[i + 1][k] + inp_f[i + 1][k + 1]  # буфер для проверки
                if inp_f[i][k] == 'x' and inp_f[i + 1][k] == 'x' and inp_f[i + 1][k + 1] == 'x':
                    out_f[i][k] = 'x'
            elif i == 0 and k == len(inp_f[i]) - 1:
                if inp_f[i][k - 1] == 'x' and inp_f[i + 1][k] == 'x' and inp_f[i + 1][k - 1] == 'x':
                    out_f[i][k] = 'x'
            elif i == len(inp_f) - 1 and k == 0:
                if inp_f[i][k + 1] == 'x' and inp_f[i - 1][k] == 'x' and inp_f[i - 1][k + 1] == 'x':
                    out_f[i][k] = 'x'
            elif i == len(inp_f) - 1 and k == len(inp_f[i]) - 1:
                if inp_f[i][k - 1] == 'x' and inp_f[i - 1][k] == 'x' and inp_f[i - 1][k - 1] == 'x':
                    out_f[i][k] = 'x'
            elif i == 0:
                pass
            elif k == 0:
                pass
            elif i != 0:
                pass
            elif k != 0:
                pass
            else:
                pass

    for i in inp_f:
        print_str = ''
        for k in i:
            print_str += k
        print(print_str)


func()
