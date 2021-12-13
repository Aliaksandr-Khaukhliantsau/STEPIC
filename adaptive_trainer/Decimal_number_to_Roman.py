# В римской системе счисления для обозначения чисел используются следующие символы (справа записаны числа,
# которым они соответствуют в десятичной системе счисления):
#
# I = 1 V = 5 X = 10 L = 50 C = 100 D = 500 M = 1000 Будем использовать вариант, в котором числа 4, 9, 40, 90,
# 400 и 900 записываются как вычитание из большего числа меньшего: IV, IX, XL, XC, CD и CM, соответственно.
#
# Формат ввода:
# Строка, содержащая натуральное число nn, 0 < n < 4000
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
    dec_str = input()

    res = int(dec_str)
    res_list = []
    i = 0

    for _ in dec_str:
        i += 1
        res_list.append(str(res)[len(dec_str) - i:])
        res -= int(str(res)[len(dec_str) - i:])

    res_list.reverse()

    rom = {'1': 'I', '2': 'II', '3': 'III', '4': 'IV',
           '5': 'V', '6': 'VI', '7': 'VII', '8': 'VIII', '9': 'IX',
           '10': 'X', '20': 'XX', '30': 'XXX', '40': 'XL',
           '50': 'L', '60': 'LX', '70': 'LXX', '80': 'LXXX', '90': 'XC',
           '100': 'C', '200': 'CC', '300': 'CCC', '400': 'CD',
           '500': 'D', '600': 'DC', '700': 'DCC', '800': 'DCCC', '900': 'CM',
           '1000': 'M', '2000': 'MM', '3000': 'MMM'}

    result = ''
    for i in res_list:
        for k, v in rom.items():
            if i == k:
                result += v
                continue

    print(result)


func()
