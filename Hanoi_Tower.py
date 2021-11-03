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

# kernel_1, kernel_2, kernel_3 = [], [], []

# for i in range(int(input())):
#     kernel_1.append(i + 1)

# print(kernel_1, kernel_2, kernel_3)


kernel_1, kernel_2, kernel_3 = [1, 2, 3, 4], [], []

# for x in kernel_1:
#     if x == 1:
#         kernel_1.remove(x)
#         kernel_3.append(x)
#         continue
#     kernel_1.remove(x)
#     kernel_2.append(x)

while True:
    if kernel_1[0] == 1:
        kernel_2.append(kernel_1[0])
        kernel_1.pop(0)
    else:
        kernel_3.append(kernel_1[0])
        kernel_1.pop(0)
        kernel_3.append(kernel_2[-1])
        kernel_2.pop(-1)
        kernel_2.append(kernel_1[0])
        kernel_1.pop(0)
        kernel_1.append(kernel_3[-1])
        kernel_3.pop(-1)
        kernel_2.append(kernel_3[-1])
        kernel_3.pop(-1)
        kernel_2.append(kernel_1[-1])
        kernel_1.pop(-1)
        kernel_3.append(kernel_1[-1])
        kernel_1.pop(-1)
        kernel_3.append(kernel_2[-1])
        kernel_2.pop(-1)
        kernel_1.append(kernel_2[-1])
        kernel_2.pop(-1)
        kernel_1.append(kernel_3[-1])
        kernel_3.pop(-1)



    # if kernel_1:
    #     continue
    # else:
    #     break


