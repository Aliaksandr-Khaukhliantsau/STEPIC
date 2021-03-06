# Когда Антон прочитал «Войну и мир», ему стало интересно, сколько слов и в каком количестве используется в этой книге.
#
# Помогите Антону написать упрощённую версию такой программы, которая сможет подсчитать слова, разделённые пробелом и
# вывести получившуюся статистику.
#
# Программа должна выводить для каждого уникального слова число его повторений (без учёта регистра).
#
# Формат ввода:
# Одна строка, содержащая последовательности символов через пробел
#
# Формат вывода: Набор строк, каждая из которых содержит слово и, через пробел, число -− количество раз,
# которое слово использовалось во входной строке. Регистр слов не важен, слова в выводе не должны повторяться,
# порядок слов произвольный.
#
# Sample Input:
#
# a aa abC aa ac abc bcd a
# Sample Output:
#
# bcd 1
# ac 1
# aa 2
# a 2
# abc 2


#  первый вариант
# def input_field():
#     my_input = input().lower().split()
#     my_dict = {}
#     for word in my_input:
#         if word not in my_dict:
#             my_dict[word] = 1
#         else:
#             my_dict[word] = my_dict.get(word) + 1
#
#     for x, v in my_dict.items():
#         # print('%s %d' % (x, v))  # можно так
#         print(f'{x} {v}')  # а можно и так
#
#
# input_field()


#  второй вариант
from collections import Counter

for key, value in Counter(input().lower().split()).items():
    print(key, value)
