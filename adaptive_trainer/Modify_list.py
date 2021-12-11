# Напишите функцию modify_list(l), которая принимает на вход список целых чисел, удаляет из него все нечётные
# значения, а чётные нацело делит на два. Функция не должна ничего возвращать, требуется только изменение переданного
# списка, например:
#
# lst = [1, 2, 3, 4, 5, 6]
# print(modify_list(lst))  # None
# print(lst)               # [1, 2, 3]
# modify_list(lst)
# print(lst)               # [1]
#
# lst = [10, 5, 8, 3]
# modify_list(lst)
# print(lst)               # [5, 4]
# Также функция не должна осуществлять ввод/вывод информации.

# первый вариант
# def modify_list(l):
#     buf = []
#     for y in range(len(l)):
#         if l[y] % 2:
#             buf.append(l[y])
#         else:
#             l[y] = l[y] // 2
#     for x in buf:
#         l.remove(x)
#
#
# lst = [1, 2, 3, 4, 5, 6]
# modify_list(lst)

# второй вариант
def modify_list(l):
    buf = []
    for i in range(len(l)):
        if not l[i] % 2:
            buf.append(l[i] // 2)
    l[:] = buf  # делаем l[:] потому что через [:] изменяется текущий список (так требуется по условию),
    # в не создается новый


lst = [1, 2, 3, 4, 5, 6]
modify_list(lst)
