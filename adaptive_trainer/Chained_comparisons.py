# Имеется следующий код:
#
# def t():
#     print('t')
#     return True
#
# def f():
#     print('f')
#     return False
#
# x = 0
# if f() < t() < f():
#     x += 1
#
# if f() < t() and t() < f(): x += 1 Не используя интерпретатор, напишите через пробел то, что выведет программа,
# после чего через пробел значение переменной x, например, t f f 0 если считаете, что строки f и t будут выведены в
# таком порядке и в таком количестве, и что значение переменной x равно нулю.


def t():
    print('t')
    return True

def f():
    print('f')
    return False

x = 0
if f() < t() < f():
    x += 1

if f() < t() and t() < f():
    x += 1