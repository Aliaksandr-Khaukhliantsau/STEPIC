net = input().split()

if len(net) != 2:
    print('нужно указать именно два числа')

if net[0].isdigit() is False or net[1].isdigit() is False:
    print('нужно вводить только числа')

n, m = int(net[0]), int(net[1])

if n < 1 or n > 100 or m < 1 or m > 100:
    print('числа n и m должны быть не меньше 1 и не больше 100')

number_of_lines = ()

for _ in range(n):
    a = input()
    a = list(a)
    if len(a) != m:
        print(f'кол-во вводимых элементов должно быть равно {n}')
        break
    number_of_lines += (a,)

for i in range(len(number_of_lines)):
    result = ''
    for z in range(len(number_of_lines[i])):
        if i == 0:
            if z == 0:
                if number_of_lines[i][z] == '.' and n == 1:
                    x = 0
                    if m != 1:
                        if number_of_lines[i][z + 1] == '*':
                            x += 1
                            result += str(x)
                        else:
                            result += '0'
                    else:
                        result += '0'
                        break

                elif number_of_lines[i][z] == '.' and n != 1:
                    x = 0
                    if m != 1:
                        if number_of_lines[i][z + 1] == '*':
                            x += 1
                        if number_of_lines[i + 1][z] == '*':
                            x += 1
                        if number_of_lines[i + 1][z + 1] == '*':
                            x += 1
                        result += str(x)
                    else:
                        if number_of_lines[i + 1][z] == '*':
                            x += 1
                        result += str(x)
                else:
                    result += '*'

            elif z == len(number_of_lines[i]) - 1:
                if number_of_lines[i][z] == '.' and n == 1:
                    x = 0
                    if m != 1:
                        if number_of_lines[i][z - 1] == '*':
                            x += 1
                            result += str(x)
                        else:
                            result += '0'
                    else:
                        result += '0'

                elif number_of_lines[i][z] == '.' and n != 1:
                    x = 0
                    if number_of_lines[i][z - 1] == '*':
                        x += 1
                    if number_of_lines[i + 1][z] == '*':
                        x += 1
                    if number_of_lines[i + 1][z - 1] == '*':
                        x += 1
                    result += str(x)
                else:
                    result += '*'

            else:
                if number_of_lines[i][z] == '.' and n == 1:
                    x = 0
                    if m != 1:
                        if number_of_lines[i][z + 1] == '*':
                            x += 1
                        if number_of_lines[i][z - 1] == '*':
                            x += 1
                    else:
                        result += '0'
                        break
                    result += str(x)

                elif number_of_lines[i][z] == '.' and n != 1:
                    x = 0
                    if number_of_lines[i][z - 1] == '*':
                        x += 1
                    if number_of_lines[i][z + 1] == '*':
                        x += 1
                    if number_of_lines[i + 1][z] == '*':
                        x += 1
                    if number_of_lines[i + 1][z + 1] == '*':
                        x += 1
                    if number_of_lines[i + 1][z - 1] == '*':
                        x += 1
                    result += str(x)
                else:
                    result += '*'

        elif i == len(number_of_lines) - 1:
            if z == 0:
                if number_of_lines[i][z] == '.' and n != 1:
                    x = 0
                    if m != 1:
                        if number_of_lines[i][z + 1] == '*':
                            x += 1
                        if number_of_lines[i - 1][z] == '*':
                            x += 1
                        if number_of_lines[i - 1][z + 1] == '*':
                            x += 1
                        result += str(x)
                    else:
                        if number_of_lines[i - 1][z] == '*':
                            x += 1
                        result += str(x)
                else:
                    result += '*'

            elif z == len(number_of_lines[i]) - 1:
                if number_of_lines[i][z] == '.' and n != 1:
                    x = 0
                    if number_of_lines[i][z - 1] == '*':
                        x += 1
                    if number_of_lines[i - 1][z] == '*':
                        x += 1
                    if number_of_lines[i - 1][z - 1] == '*':
                        x += 1
                    result += str(x)
                else:
                    result += '*'

            else:
                if number_of_lines[i][z] == '.' and n != 1:
                    x = 0
                    if number_of_lines[i][z - 1] == '*':
                        x += 1
                    if number_of_lines[i][z + 1] == '*':
                        x += 1
                    if number_of_lines[i - 1][z] == '*':
                        x += 1
                    if number_of_lines[i - 1][z + 1] == '*':
                        x += 1
                    if number_of_lines[i - 1][z - 1] == '*':
                        x += 1
                    result += str(x)
                else:
                    result += '*'

        else:
            if z == 0:
                if number_of_lines[i][z] == '.' and n != 1:
                    x = 0
                    if m != 1:
                        if number_of_lines[i][z + 1] == '*':
                            x += 1
                        if number_of_lines[i + 1][z] == '*':
                            x += 1
                        if number_of_lines[i + 1][z + 1] == '*':
                            x += 1
                        if number_of_lines[i - 1][z] == '*':
                            x += 1
                        if number_of_lines[i - 1][z + 1] == '*':
                            x += 1
                        result += str(x)
                    else:
                        if number_of_lines[i + 1][z] == '*':
                            x += 1
                        if number_of_lines[i - 1][z] == '*':
                            x += 1
                        result += str(x)
                else:
                    result += '*'

            elif z == len(number_of_lines[i]) - 1:
                if number_of_lines[i][z] == '.' and n != 1:
                    x = 0
                    if number_of_lines[i][z - 1] == '*':
                        x += 1
                    if number_of_lines[i + 1][z] == '*':
                        x += 1
                    if number_of_lines[i + 1][z - 1] == '*':
                        x += 1
                    if number_of_lines[i - 1][z] == '*':
                        x += 1
                    if number_of_lines[i - 1][z - 1] == '*':
                        x += 1
                    result += str(x)
                else:
                    result += '*'

            else:
                if number_of_lines[i][z] == '.' and n != 1:
                    x = 0
                    if number_of_lines[i][z - 1] == '*':
                        x += 1
                    if number_of_lines[i][z + 1] == '*':
                        x += 1
                    if number_of_lines[i + 1][z] == '*':
                        x += 1
                    if number_of_lines[i + 1][z + 1] == '*':
                        x += 1
                    if number_of_lines[i + 1][z - 1] == '*':
                        x += 1
                    if number_of_lines[i - 1][z] == '*':
                        x += 1
                    if number_of_lines[i - 1][z + 1] == '*':
                        x += 1
                    if number_of_lines[i - 1][z - 1] == '*':
                        x += 1
                    result += str(x)
                else:
                    result += '*'

    print(result)
