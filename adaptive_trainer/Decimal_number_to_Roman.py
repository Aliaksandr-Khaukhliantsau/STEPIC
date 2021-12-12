# В римской системе счисления для обозначения чисел используются следующие символы (справа записаны числа,
# которым они соответствуют в десятичной системе счисления):
#
# I = 1 V = 5 X = 10 L = 50 C = 100 D = 500 M = 1000 Будем использовать вариант, в котором числа 4, 9, 40, 90,
# 400 и 900 записываются как вычитание из большего числа меньшего: IV, IX, XL, XC, CD и CM, соответственно.
#
# Формат ввода:
# Строка, содержащая натуральное число nn, 0 < n < 40000<n<4000.
#
# Формат вывода:
# Строка, содержащая число, закодированное в римской системе счисления.
#
# Sample Input 1:
#
# 1984
# Sample Output 1:
#
# MCMLXXXIV
# Sample Input 2:
#
# 9
# Sample Output 2:
#
# IX
# Sample Input 3:
#
# 3
# Sample Output 3:
#
# III

def func():
    # dec_str = input()
    dec_str = '1984'
    dec_int = int(dec_str)
    dec_list = []
    for i in dec_str:
        dec_list += i

    dec_str_2 = ''.join(dec_list)

    res = int(dec_str)
    res_list = []
    i = 1
    for _ in range(len(dec_str)):
        buff = str(res)
        res_list.append(int(buff[len(buff) - i:]))
        res -= int(buff[len(buff) - i:])
        print(res)
        i += 1


    res_list.reverse()

    rom = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    # rom = {'1': 'I', '5': 'V', '10': 'X', '50': 'L', '100': 'C', '500': 'D', '1000': 'M'}

    print(res_list)

    result = ''
    for i in res_list:
        for k, v in rom:
            if i == v:
                result += v
            elif


func()