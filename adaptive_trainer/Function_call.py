# Есть функция f, которая определена следующим образом:
#
# def f(n):
#     return n * 2 + 1
# Не используя интерпретатор посчитайте, чему будет равно значение выражения:
#
# f(f(f(3)))


def f(n):
    return n * 2 + 1


print(f(f(f(3))))