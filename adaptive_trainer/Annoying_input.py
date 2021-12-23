# Напишите функцию get_int(start_message, error_message, end_message), принимающую три строки в качестве аргументов.
#
# Функция должна запрашивать у пользователя ввод до тех пор, пока не будет введено целое число (строка, принимаемая
# функцией int без ошибок).
#
# Перед первым запросом ввода должен быть выведен аргумент start_message, после каждого ошибочного ввода нужно
# выводить значение строки error_message и при удачном вводе нужно вывести строку end_message и вернуть полученное
# целое число из функции (см. пример работы). Каждое выводимое сообщение должно находиться на отдельной строке.
#
# Например, вызов
#
# x = get_int('Input int number:', 'Wrong value. Input int number:', 'Thank you.')
# Отработает следующим образом (каждая вторая строка описывает ввод пользователя):
#
# Input int number:
# ten
# Wrong value. Input int number:
# ten (10)
# Wrong value. Input int number:
# 10
# Thank you.
# После чего значение переменной x будет равно 10.
#
# Код решения не должен содержать вызова функции get_int. Гарантируется, что в какой-то момент пользователем будет
# введено целое число.

# способ 1
# def get_int(start_message, error_message, end_message):
#     print(start_message)
#     while True:
#         try:
#             x = int(input())
#             print(end_message)
#             return x
#         except:
#             print(error_message)
#
#
# x = get_int('Input int number:', 'Wrong value. Input int number:', 'Thank you.')
# print(x)

# способ 2
def get_int(start_message, error_message, end_message):
    print(start_message)
    try:
        x = int(input())
        print(end_message)
        return x
    except:
        return get_int(error_message, error_message, end_message)


x = get_int('Input int number:', 'Wrong value. Input int number:', 'Thank you.')
print(x)