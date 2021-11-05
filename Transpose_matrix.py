# Напишите программу, которая принимает на вход матрицу, выполняет её транспонирование и выводит результат.
#
# Формат ввода:
# В первой строке указываются два целых числа nn и mm, количество строк и столбцов, соответственно.
# Далее следуют nn строк, содержащих по mm целых чисел, разделённых пробелом.
#
# Формат вывода:
# Программа должна вывести mm строк содержимого транспонированной матрицы. Элементы матрицы стоит разделять пробелом.
#
# Sample Input 1:
#
# 2 3
# 1 2 3
# 4 5 6
# Sample Output 1:
#
# 1 4
# 2 5
# 3 6
# Sample Input 2:
#
# 2 2
# 1 2
# 3 4
# Sample Output 2:
#
# 1 3
# 2 4

nm_list = input().split()
print(nm_list)
my_list = []
for i in range(int(nm_list[0])):
    a = input().split()
    print(a)
    if len(a) != int(nm_list[1]):
        break
    my_list += [a]
    print(my_list)

for i in range(len(my_list)):
    for k in range(len(my_list[i])):
        if i == len(my_list) - 1:
            break
        print(my_list[i][k], my_list[i + 1][k])
