# Ханойская башня -- одна из широко известных головоломок,
# условие которой состоит в следующем:
#
# Имеется три стержня (пронумеруем их числами 1, 2 и 3).
# На первом стержне находится nn колец с радиусами от 1 до nn.
# Кольца отсортированы по радиусу, и наибольшее кольцо лежит ниже всех.
#
# Вам требуется найти и записать алгоритм переноса всех nn колец с первого стержня
# на третий по следующим правилам:
# за один ход можно переносить только одно кольцо;
# нельзя класть большее кольцо на меньшее.
#
# Программа должна вывести на экран кратчайшую последовательность действий,
# необходимую для того, чтобы перенести все кольца с первого стержня на третий.
#
# Формат ввода:
# Строка, содержащая положительное целое число nn.
#
# Формат вывода: Порядок действий для решения головоломки. Каждое действие записывается на отдельной строке. Действие
# записывается в формате "номер стержня, с которого снимаем кольцо" - "номер стержня, на который надеваем кольцо" (
# см. пример работы программы).
#
# Sample Input 1:
#
# 2
# Sample Output 1:
#
# 1 - 2
# 1 - 3
# 2 - 3
# Sample Input 2:
#
# 1
# Sample Output 2:
#
# 1 - 3


def hanoi(c, first, third):
    if c == 1:
        print(f'{first} - {third}')
    else:
        hanoi(c - 1, first, 6 - first - third)
        print(f'{first} - {third}')
        hanoi(c - 1, 6 - first - third, third)


rings = int(input())

first, third = 1, 3

hanoi(rings, first, third)