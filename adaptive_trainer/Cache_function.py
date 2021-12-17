# Имеется реализованная функция f(x), принимающая на вход целое число x, которая вычисляет некоторое
# целочисленое значение и возвращает его в качестве результата работы.
#
# Функция вычисляется достаточно долго, ничего не выводит на экран, не пишет в файлы и зависит только от переданного
# аргумента x.
#
# Напишите программу, которая вычисляет значение этой функции для n чисел.
#
# Для ускорения вычисления необходимо сохранять уже вычисленные значения функции при известных аргументах.
#
# Обратите внимание, что в этой задаче установлено достаточно сильное ограничение в две секунды по времени исполнения
# кода на тесте.
#
# Формат ввода: На первой строке находится число n -− количество значений, на которых нужно посчитать функцию. После
# этого следует n строк, на каждой строке по одному целому числу.
#
# Формат вывода:
# n строк, в каждой из которой результат вычисления функции на соответствующем аргументе.
#
# Sample Input:
#
# 5
# 5
# 12
# 9
# 20
# 12
# Sample Output:
#
# 11
# 41
# 47
# 61
# 41


def f(x):
    return x * 2


count = int(input())
my_tuple = ()
my_dict = {}

for i in range(count):
    my_tuple += (input(),)

for i in my_tuple:
    if i not in my_dict:
        my_dict[i] = f(int(i))
    print(my_dict[i])