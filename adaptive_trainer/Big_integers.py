# Напишите программу, которая получает от пользователя два числа a и b и выводит значение выражения a ^ ba
# b
#  . Для возведения в степень в Python используется оператор **.
#
# Так как Python может работать с целыми числами произвольной длины, то никаких затруднений с этой задачей не
# возникает.  В языках, не имеющих встроенной поддержки так называемой длинной арифметики подобная задача решается
# гораздо сложнее.
#
# Формат ввода:
# Числа a и b, разделённые переводом строки.
#
# Формат вывода:
# Искомое число -− результат вычисления выражения.
#
# Sample Input:
#
# 16
# 64
# Sample Output:
#
# 115792089237316195423570985008687907853269984665640564039457584007913129639936

#  первый способ
# def input_field():
#     return int(input()) ** int(input())
#
#
# print(input_field())

#  второй способ
print(int(input()) ** int(input()))
