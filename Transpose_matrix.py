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


def func_2(matrix):
    answer = ''
    for i in range(len(matrix[0])):
        for k in range(len(matrix)):
            answer += f'{str(matrix[k][i])} '
        answer = answer[:-1] + '\n'
    print(answer[:-1])


def func_1(n_m_list):
    matrix = []
    for i in range(int(n_m_list[0])):
        input_str = input().split()
        if len(input_str) != int(n_m_list[-1]):
            return
        matrix += [input_str]
    func_2(matrix)


n_m_list = input().split()

if len(n_m_list) == 2 and n_m_list[0] != '0':
    func_1(n_m_list)
