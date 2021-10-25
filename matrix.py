import sys


def result_output(result_tuple):
    result = ''
    for i in range(len(result_tuple)):
        if i == 0:
            result += f'[{result_tuple[i][0]},{result_tuple[i][1]}]'
        else:
            result += f' -> [{result_tuple[i][0]},{result_tuple[i][1]}]'
    print(result)


def filling_a_result_tuple(letter, matrix):
    for element in matrix:
        for symbol in element:
            if letter == symbol:
                return matrix.index(element), element.index(letter)
    print(f'Буквы \'{letter}\' нет в матрице')
    sys.exit()


def creating_a_result_tuple(matrix, word_input):
    result_tuple = ()
    for letter in word_input:
        result_tuple += (filling_a_result_tuple(letter, matrix),)
    result_output(result_tuple)


def matrix_creation(word_input, string_input, square_root):
    matrix = []
    line_slice = 0
    for _ in range(square_root):
        matrix.append(string_input[line_slice:line_slice + square_root])
        line_slice += square_root
    creating_a_result_tuple(matrix, word_input)


def word_validation(word_input, string_input, square_root):
    if len(word_input) == 0:
        print('Вы не ввели слово')
        return
    if word_input.isalpha():
        matrix_creation(word_input, string_input, square_root)
    else:
        print('Слово должно содержать только символы алфавита')
        return


def word_input_function(string_input, square_root):
    print('Введите слово: ')
    word_input = input()
    word_validation(word_input, string_input, square_root)


def square_root_extraction(string_input):
    square_root = len(string_input) ** .5
    if square_root.is_integer():
        square_root = int(square_root)
        word_input_function(string_input, square_root)
    else:
        print('Строка должна описывать квадратную матрицу')
        return


def string_validation(string_input):
    if len(string_input) < 4:
        print('Минимальное количество символов крадратной матрицы должно быть 2 * 2')
        return
    if string_input.isalpha():
        square_root_extraction(string_input)
    else:
        print('Строка должна содержать только символы алфавита')
        return


def line_input_function():
    print('Введите строку: ')
    string_input = input()
    string_validation(string_input)


line_input_function()
