import sys


def func_5(result_tuple):
    result = ''
    for y in range(len(result_tuple)):
        if y == 0:
            result += f'[{result_tuple[y][0]},{result_tuple[y][1]}]'
        else:
            result += f' -> [{result_tuple[y][0]},{result_tuple[y][1]}]'
    print(result)


def func_4(i, matrix):
    for k in matrix:
        for z in k:
            if i == z:
                w = matrix.index(k)
                q = k.index(i)
                return w, q
    print(f'Буквы \'{i}\' нет в матрице')
    sys.exit()


def func_3(matrix):
    result_tuple = ()
    for i in word_input:
        result_tuple += (func_4(i, matrix),)
    print(result_tuple)
    func_5(result_tuple)


def func_2(sqrt):
    matrix = []
    a = 0
    b = sqrt
    for _ in range(sqrt):
        matrix.append(string_input[a:a + sqrt])
        a += sqrt
    print(matrix)
    func_3(matrix)


def func_1():
    sqrt = len(string_input) ** .5
    print(sqrt)
    if sqrt.is_integer():
        sqrt = int(sqrt)
        func_2(sqrt)
    else:
        print('Строка должна описывать квадратную матрицу')
        return





def line_input_function():
    print('Введите строку: ')
    string_input = input()
    # checking_a_string_for_the_alphabet()
    if len(string_input) < 4:
        print('Минимальное количество символов крадратной матрицы должно быть 2 * 2')
        return
    if string_input.isalpha():
        print('string is alpha')
        print('Введите слово: ')
        word_input = input()
        if len(word_input) == 0:
            print('Вы не ввели слово')
            return
        if word_input.isalpha():
            print('word is alpha')
            func_1()
        else:
            print('Слово должно содержать только символы алфавита')
            return
    else:
        print('Строка должна содержать только символы алфавита')
        return


# string_input = input()
# word_input = input()

# string_input = 'OMNZ'
# string_input = 'CVBSYPLME'
# string_input = 'QLGNAEKIRLRNGEAE'
# string_input = 'WKDODJHFGHGKDDKJXOQTDNTES'
# string_input = 'LPOIUHBVFGGFGGBVVCCCFFDWQAZMJDTUIRSD'
# string_input = 'LPOIUHBVFFGGFGGBVVCCCFFDWQAZMJDTUIRSD'
# string_input = 'EPIBLKHHGDLWHLKWLRDWJDMNBMNBVTHQYUIWOSYONDQKXZPMA'
# string_input = 'LEHWLKHCNQIUUJNBZLALSKKJQKJQQQSBCNCGNBMBBZXBJHKJHMNBVQWJDYTAKOPR'
# string_input = 'QLGCAEKIRLRUGEA'
# string_input = 'QLGNAEK1ILRNGEAE'
# string_input = 'eQGNAEKrILRNGEAE'
# string_input = 'QLGNAEKI{LRNGEA'
# string_input = 'LG.NAEKILLRNGEA'
# string_input = 'LGNAEKIL LRNGEA'
# string_input = ''
# string_input = ''
# string_input = '      '
# string_input = 'W'
# string_input = 'WE'
# string_input = 'WEF'

# word_input = 'MZ'
# word_input = 'OMNZ'
# word_input = 'OMNZM'
# word_input = 'CSEV'
# word_input = 'KING'
# word_input = 'NOTES'
# word_input = 'REGKQ'
# word_input = ''
# word_input = ' '
# word_input = 'CQDJUOPSZXBOPD'
# word_input = 'QUICK'
# word_input = 'QUIC1'
# word_input = 'KING'
# word_input = 'KING'


# print(string_input)
# print(len(string_input))
# print(word_input)

line_input_function()
# func_1()
# func_2()


# if len(string_input) < 4:
#     print('Строка должна описывать квадратную матрицу с минимальным количеством символов 2 * 2')
#     if string_input.isalpha():
#         print('string is alpha')
#         # word_input = input()
#         if len(word_input) == 0:
#             print('Вы не ввели слово')
#         if word_input.isalpha():
#             print('word is alpha')
#         else:
#             print('word isn\'t alpha')
#             # return
#     else:
#         print('string is\'t alpha')
#         # return


# sqrt = len(string_input) ** .5
# print(sqrt)

# if sqrt.is_integer():
#     sqrt = int(sqrt)

# matrix = []
#
# a = 0
# b = sqrt
# for _ in range(sqrt):
#     matrix.append(string_input[a:a + sqrt])
#     a += sqrt
#
# print(matrix)


# def func_4(i):
#     for k in matrix:
#         for z in k:
#             if i == z:
#                 w = matrix.index(k)
#                 q = k.index(i)
#                 return w, q
#
#     print('Такой буквы нет в матрице')
#     return


# result_tuple = ()
# for i in word_input:
#     result_tuple += (func_4(i),)
#
# print(result_tuple)


# result = ''
# for i in range(len(result_tuple)):
#     if i == 0:
#         result += f'[{result_tuple[i][0]},{result_tuple[i][1]}]'
#     else:
#         result += f' -> [{result_tuple[i][0]},{result_tuple[i][1]}]'
#
# print(result)
