# В какой-то момент вам надоело использовать имена файлов с пробелами и вы решили написать программу,
# которая переименовывает все файлы, содержащие пробелы в имени, заменив группы пробелов на символ подчёркивания "_".
#
# Для начала нужно написать программу, которая считывает строку и заменяет в ней группы пробельных символов на символ
# подчёркивания.
#
# Формат ввода:
# Одна строка, содержащая произвольные символы, в том числе и пробельные.
#
# Формат вывода:
# Преобразованная строка.
#
# Sample Input 1:
#
# my file name.txt
# Sample Output 1:
#
# my_file_name.txt
# Sample Input 2:
#
# string     with        multi spaces
# Sample Output 2:
#
# string_with_multi_spaces
# Sample Input 3:
#
# single
# Sample Output 3:
#
# single

def func(input_str):
    result = '_'.join(input_str)
    print(result)


input_1 = input().split()

func(input_1)
