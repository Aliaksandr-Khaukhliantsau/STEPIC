# net = input().split()
net = ['4', '4']  # тест

if len(net) != 2:
    print('нужно указать именно два числа')

if net[0].isdigit() is False or net[1].isdigit() is False:
    print('нужно вводить только числа')

# print(net)

n, m = int(net[0]), int(net[1])

# print(n, m)

if n < 1 or n > 100 or m < 1 or m > 100:
    print('числа n и m должны быть не меньше 1 и не больше 100')

# number_of_lines = ()
#
# for _ in range(m):
#     a = input()
#     a = list(a)
#     # print(a)
#     if len(a) != n:
#         print(f'кол-во вводимых элементов должно быть равно {n}')
#         break
#     number_of_lines += (a,)

number_of_lines = (['.', '.', '*', '.'], ['*', '*', '.', '.'], ['.', '.', '*', '.'], ['.', '.', '.', '.'])  # тест


# number_of_cells = n * m

# print(number_of_lines)
# print(number_of_lines[-1])
# print(number_of_lines[-1][-1])

# for i in number_of_lines:
#     print(f'number_of_lines[i] = {i}')
#     print(f'индекс number_of_lines[i] = {number_of_lines.index(i)}')
#     for z in range(len(i)):
#         print(f'z = {z}')
#         print(f'number_of_lines[{number_of_lines.index(i)}][{z}] = {number_of_lines[number_of_lines.index(i)][z]}')
#         if z == 0:
#
#             if i[z] == '.':
#                 x = 0
#                 if number_of_lines.index(i) < len(number_of_lines):
#                     if number_of_lines[number_of_lines.index(i)][z + 1] == '*':
#                         x += 1
#                     if number_of_lines[number_of_lines.index(i) + 1][z] == '*':
#                         x += 1
#                     if number_of_lines[number_of_lines.index(i) + 1][z + 1] == '*':
#                         x += 1
#                     print(f'x = {x}')
#
#         elif z == len(i) - 1:
#
#             if i[z] == '.':
#                 x = 0
#                 if number_of_lines.index(i) < len(number_of_lines):
#                     if number_of_lines[number_of_lines.index(i)][z - 1] == '*':
#                         x += 1
#                     if number_of_lines[number_of_lines.index(i) + 1][z] == '*':
#                         x += 1
#                     if number_of_lines[number_of_lines.index(i) + 1][z - 1] == '*':
#                         x += 1
#                     print(f'x = {x}')
#
#         else:
#
#             if i[z] == '.':
#                 x = 0
#                 if number_of_lines.index(i) < len(number_of_lines):
#                     if number_of_lines[number_of_lines.index(i)][z - 1] == '*':
#                         x += 1
#                     if number_of_lines[number_of_lines.index(i)][z + 1] == '*':
#                         x += 1
#                     if number_of_lines[number_of_lines.index(i) + 1][z] == '*':
#                         x += 1
#                     if number_of_lines[number_of_lines.index(i) + 1][z - 1] == '*':
#                         x += 1
#                     if number_of_lines[number_of_lines.index(i) + 1][z + 1] == '*':
#                         x += 1
#
#                 if 0 < number_of_lines.index(i) < len(number_of_lines):
#                     if number_of_lines[number_of_lines.index(i) - 1][z] == '*':
#                         x += 1
#                     if number_of_lines[number_of_lines.index(i) - 1][z - 1] == '*':
#                         x += 1
#                     if number_of_lines[number_of_lines.index(i) - 1][z + 1] == '*':
#                         x += 1
#                     print(f'x = {x}')


for i in range(len(number_of_lines)):
    print(f'number_of_lines[{i}] = {number_of_lines[i]}')
    for z in range(len(number_of_lines[i])):
        print(f'number_of_lines[{i}][{z}] = {number_of_lines[i][z]}')
        if i == 0:
            if z == 0:
                if number_of_lines[i][z] == '.':
                    x = 0
                    if number_of_lines.index(number_of_lines[i]) < len(number_of_lines):
                        if number_of_lines[i][z + 1] == '*':
                            x += 1
                        if number_of_lines[i + 1][z] == '*':
                            x += 1
                        if number_of_lines[i + 1][z + 1] == '*':
                            x += 1
                    if 0 < number_of_lines.index(number_of_lines[i]) < len(number_of_lines):
                        if number_of_lines[i - 1][z] == '*':
                            x += 1
                        if number_of_lines[i - 1][z + 1] == '*':
                            x += 1
                    print(f'x = {x}')

            elif z == i - 1:
            # elif z == len(number_of_lines[i]) - 1:
                if number_of_lines[i][z] == '.':
                    x = 0
                    if number_of_lines.index(number_of_lines[i]) < len(number_of_lines):
                        if number_of_lines[i][z - 1] == '*':
                            x += 1
                        if number_of_lines[i + 1][z] == '*':
                            x += 1
                        if number_of_lines[i + 1][z - 1] == '*':
                            x += 1
                    if 0 < number_of_lines.index(number_of_lines[i]) < len(number_of_lines):
                        if number_of_lines[i - 1][z] == '*':
                            x += 1
                        if number_of_lines[i - 1][z - 1] == '*':
                            x += 1
                    print(f'x = {x}')

            else:
                if number_of_lines[i][z] == '.':
                    x = 0
                    if number_of_lines.index(number_of_lines[i]) < len(number_of_lines):
                        if number_of_lines[i][z - 1] == '*':
                            x += 1
                        if number_of_lines[i + 1][z] == '*':
                            x += 1
                        if number_of_lines[i + 1][z - 1] == '*':
                            x += 1

                    if 0 < number_of_lines.index(number_of_lines[i]) < len(number_of_lines):
                        if number_of_lines[i - 1][z] == '*':
                            x += 1
                        if number_of_lines[i - 1][z - 1] == '*':
                            x += 1
                    print(f'x = {x}')

