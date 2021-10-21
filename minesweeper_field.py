net = input().split()

if len(net) != 2:
    print('нужно указать именно два числа')

if net[0].isdigit() is False or net[1].isdigit() is False:
    print('нужно вводить только числа')

# print(net)

n, m = int(net[0]), int(net[1])

# print(n, m)

if n < 1 or n > 100 or m < 1 or m > 100:
    print('числа n и m должны быть не меньше 1 и не больше 100')

number_of_lines = ()

for _ in range(m):
    a = input()
    a = list(a)
    print(a)
    if len(a) != n:
        print(f'кол-во вводимых элементов должно быть равно {n}')
        break
    number_of_lines += (a,)

# number_of_cells = n * m

# print(number_of_lines)
# print(number_of_lines[-1])
# print(number_of_lines[-1][-1])

for i in number_of_lines:
    # ??????????????????????????????
    print(i)
    for z in range(len(i)):
        print(z)
        print(number_of_lines[i][z])
        if z == 0:
            # print('ноль')
            if i[z] == '.':
                x = 0
                # print('.')
                if number_of_lines[i + 1][z] == '*':
                    x += 1
                if number_of_lines[i + 1][z + 1] == '*':
                    x += 1
                print(x)

        elif z == len(i) - 1:
            # print('минус 1')
            if i[z] == '.':
                x = 0
                # print('.')
                if number_of_lines[i + 1][z] == '*':
                    x += 1
                if number_of_lines[i + 1][z - 1] == '*':
                    x += 1
                print(x)

        else:
            if i[z] == '.':
                x = 0
                # print('другое')
                if number_of_lines[i + 1][z] == '*':
                    x += 1
                    # print('.')
                if number_of_lines[i + 1][z - 1] == 'x':
                    x += 1
                if number_of_lines[i + 1][z + 1] == 'x':
                    x += 1
                    print(x)








if number_of_lines[-1]:
    pass