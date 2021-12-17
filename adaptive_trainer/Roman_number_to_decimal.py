# В римской системе счисления для обозначения чисел используются следующие символы (справа записаны числа,
# которым они соответствуют в десятичной системе счисления):
#
# I = 1 V = 5 X = 10 L = 50 C = 100 D = 500 M = 1000 Будем использовать вариант, в котором числа 4, 9, 40, 90,
# 400 и 900 записываются как вычитание из большего числа меньшего: IV, IX, XL, XC, CD и CM, соответственно.
#
# Напишите программу, которая переводит число из римской в десятичную систему счисления.
#
# Формат ввода:
# Строка, содержащая число, закодированное в римской системе счисления. Гарантируется, что число меньше 4000.
#
# Формат вывода:
# Строка, содержащая число в десятичной системе счисления, соответствующее введённому.
#
# Sample Input 1:
#
# MCMLXXXIV
# Sample Output 1:
#
# 1984
# Sample Input 2:
#
# IX
# Sample Output 2:
#
# 9
# Sample Input 3:
#
# III
# Sample Output 3:
#
# 3

def func():
    rom = 'III'
    # rom = input()
    # rom = ','.join(input())
    # rom = ','.join(input()).split(',')
    rom_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    dec_rom = {'1': 'I', '2': 'II', '3': 'III', '4': 'IV',
           '5': 'V', '6': 'VI', '7': 'VII', '8': 'VIII', '9': 'IX',
           '10': 'X', '20': 'XX', '30': 'XXX', '40': 'XL',
           '50': 'L', '60': 'LX', '70': 'LXX', '80': 'LXXX', '90': 'XC',
           '100': 'C', '200': 'CC', '300': 'CCC', '400': 'CD',
           '500': 'D', '600': 'DC', '700': 'DCC', '800': 'DCCC', '900': 'CM',
           '1000': 'M', '2000': 'MM', '3000': 'MMM'}


    # rom = reversed(rom)
    # rom = reversed(rom)
    # rom.reverse()


    res = []
    for r in rom:
        for k, v in rom_dict.items():
            if k == r:
                res.append(int(v))

    print(res)


    result = 0
    for i in range(len(res)):
        if i == 0:
            if res[i] > res[i + 1]:
                result += res[i]
            elif res[i] >= res[i + 1]:
                result += res[i]
        elif i < len(res) - 1:
            if res[i] > res[i - 1]:
                result += (res[i] - res[i - 1])
            elif res[i] < res[i + 1]:
                continue
            elif res[i] >= res[i + 1]:
                result += res[i]
            else:
                pass

        else:
            if res[i] > res[i - 1]:
                result += (res[i] - res[i - 1])
            elif res[i] <= res[i - 1]:
                result += res[i]




    print(result)

func()