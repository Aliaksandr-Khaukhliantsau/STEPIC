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
    n = int(input())
    matrix = []

    for i in range(n):
        matrix.append([])
        for k in range(n):
            matrix[i].append(None)

    x, y = 0, 0
    move_x, move_y = 1, 0  # если 1 то двигаемся вправо или вниз, если -1 то влево или вверх

    for i in range(n ** 2):
        matrix[y][x] = i + 1
        if move_x:
            test = x + move_x
        else:
            test = y + move_y
        if test < 0 or test == n or matrix[y + move_y][x + move_x] is not None:  # проверка на выход за пределы матрицы
            move_x, move_y = -move_y, move_x  # меняем направление движения по матрице
        x += move_x  # двигаемся по x b y
        y += move_y

    for y in range(n):
        print(*matrix[y])


func()
