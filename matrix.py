import sys


def result_output(result_tuple):
    result = ''
    for y in range(len(result_tuple)):
        if y == 0:
            result += f'[{result_tuple[y][0]},{result_tuple[y][1]}]'
        else:
            result += f' -> [{result_tuple[y][0]},{result_tuple[y][1]}]'
    print(result)


def filling_a_result_tuple(i, matrix):
    for k in matrix:
        for z in k:
            if i == z:
                # w = matrix.index(k)
                # q = k.index(i)
                return matrix.index(k), k.index(i)
    print(f'Буквы \'{i}\' нет в матрице')
    sys.exit()


def creating_a_result_tuple(matrix, word_input):
    result_tuple = ()
    for i in word_input:
        result_tuple += (filling_a_result_tuple(i, matrix),)
    print(result_tuple)
    result_output(result_tuple)


def matrix_creation(word_input, string_input, sqrt):
    matrix = []
    a = 0
    b = sqrt
    for _ in range(sqrt):
        matrix.append(string_input[a:a + sqrt])
        a += sqrt
    print(matrix)
    creating_a_result_tuple(matrix, word_input)


def square_root_extraction(word_input, string_input):
    sqrt = len(string_input) ** .5
    # print(sqrt)
    if sqrt.is_integer():
        sqrt = int(sqrt)
        matrix_creation(word_input, string_input, sqrt)
    else:
        print('Строка должна описывать квадратную матрицу')
        return


def word_validation(word_input, string_input):
    if len(word_input) == 0:
        print('Вы не ввели слово')
        return
    if word_input.isalpha():
        # print('word is alpha')
        square_root_extraction(word_input, string_input)
    else:
        print('Слово должно содержать только символы алфавита')
        return


def word_input_function(string_input):
    print('Введите слово: ')
    word_input = input()
    word_validation(word_input, string_input)


def string_validation(string_input):
    if len(string_input) < 4:
        print('Минимальное количество символов крадратной матрицы должно быть 2 * 2')
        return
    if string_input.isalpha():
        # print('string is alpha')
        word_input_function(string_input)
    else:
        print('Строка должна содержать только символы алфавита')
        return


def line_input_function():
    print('Введите строку: ')
    string_input = input()
    string_validation(string_input)


line_input_function()

# 'OMNZ' 'MZ' [0,1] -> [1,1]
# 'QLGNAEKIRLRNGEAE' 'KING' [1,2] -> [1,3] -> [0,3] -> [0,2]
# 'WKDODJHFGHGKMDKJXOQTDNTES' 'OMNO' [0,3] -> [2,2] -> [4,1] -> [0,3]
# 'LPOIUHBVFGGFGGBVVCCCFFDWQAZMJDTUIRSD' 'OMWZM' [0,2] -> [4,3] -> [3,5] -> [4,2] -> [4,3]
# 'EPIBLKHHGDLWHLKWLRDWJDMNBMNBVTHQYUIWOSYONDQKXZPMA' 'NOTES' [3,2] -> [5,1] -> [4,1] -> [0,0] -> [5,2]
# 'LPOIUHBVFGGFGGBVVCCCFFDWQAZMJDTUIRSD' 'OMwZM' Буквы 'w' нет в матрице
# 'LEHWLKHCNQIUUJNBZLALSKKJQKJQQQSBCNCGNBMBBZXBJHKJHMNBVQWJDYTAKOPR' 'REGKQ' [7,7] -> [0,1] -> [4,3] -> [0,5] -> [1,1]
# 'QLGCAEKIRLRUGEA' 'REGKQ' Строка должна описывать квадратную матрицу
# 'QLGNAEK1ILRNGEAE' 'REGKQ' Строка должна содержать только символы алфавита
# 'eQGNAEKrILRNGEAE' 'REGKQ' [2,2] -> [1,1] -> [0,2] -> [1,2] -> [0,1]
# 'QLGNAEKI{LRNGEA' 'REGKQ' Строка должна содержать только символы алфавита
# 'LG.NAEKILLRNGEA' 'REGKQ' Строка должна содержать только символы алфавита
# 'LGNAEKIL LRNGEA' 'REGKQ' Строка должна содержать только символы алфавита
# 'WKDODJHFGHGKMDKJXOQTDNTES' '' Вы не ввели слово
# 'WKDODJHFGHGKMDKJXOQTDNTES' ' ' Слово должно содержать только символы алфавита
# 'WKDODJHFGHGKMDKJXOQTDNTES' '      ' Слово должно содержать только символы алфавита
# 'WKDODJHFGHGKMDKJXOQTDNTES' 'QUIC1' Слово должно содержать только символы алфавита
# 'W' 'W' Минимальное количество символов крадратной матрицы должно быть 2 * 2
# 'W' 'OMNZ' Минимальное количество символов крадратной матрицы должно быть 2 * 2
# 'WE' 'OMNZ' Минимальное количество символов крадратной матрицы должно быть 2 * 2
# 'WEF' 'OMNZ' Минимальное количество символов крадратной матрицы должно быть 2 * 2
# '' 'OMNZ' Минимальное количество символов крадратной матрицы должно быть 2 * 2
# ' ' 'OMNZ' Минимальное количество символов крадратной матрицы должно быть 2 * 2
# '          ' 'OMNZ' Строка должна содержать только символы алфавита
