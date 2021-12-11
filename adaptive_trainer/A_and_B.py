# Задача на работу со строками.
#
# Многим знакома детская загадка:
#
# А и Б сидели на трубе.
# А упало, Б пропало.
# Что осталось на трубе?
#
# Перевод, (какой я смог найти):
#
# A and B sat in the tree.
# A had fallen, B was stolen.
# What's remaining in the tree?
#
# Напишите программу, которая считывает два имени и выводит стихотворение, в котором вместо A и B используются эти
# имена.
#
# Формат ввода:
# Два имени, разделённых переносом строки. Первое имя должно заменять A, второе -− B.
#
# Формат вывода:
# Три строки стихотворения с заменёнными A и B.
#
# Sample Input:
#
# X
# Y
# Sample Output:
#
# X and Y sat in the tree.
# X had fallen, Y was stolen.
# What's remaining in the tree?


def func(puzzle, x, y):
    puzzle_split = puzzle.split()

    for i in range(len(puzzle_split)):
        if puzzle_split[i] == 'A':
            puzzle_split[i] = x
        elif puzzle_split[i] == 'B':
            puzzle_split[i] = y
    puzzle_split = ' '.join(puzzle_split)
    result = puzzle_split.replace('. ', '.\n')
    print(result)


puzzle = 'A and B sat in the tree.\nA had fallen, B was stolen.\nWhat\'s remaining in the tree?'

x = input()
y = input()

func(puzzle, x, y)
