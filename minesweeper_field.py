net = input().split()

if len(net) != 2:
    print('нужно указать именно два числа')

if net[0].isdigit() is False or net[1].isdigit() is False:
    print('нужно вводить только числа')

print(net)

n, m = int(net[0]), int(net[1])

print(n, m)

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
    number_of_lines += tuple(a)

# number_of_cells = n * m

print(number_of_lines)
