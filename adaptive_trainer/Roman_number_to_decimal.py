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


# первый способ

# def func():
#     rom = input()
#     buff = []
#     result = 0
#     rom_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
#
#     for numb in rom:
#         for k, v in rom_dict.items():
#             if k == numb:
#                 buff.append(int(v))
#
#     for i in range(len(buff)):
#         if i == 0:
#             if len(buff) == 1 or buff[i] >= buff[i + 1]:
#                 result += buff[i]
#         elif i < len(buff) - 1:
#             if buff[i] > buff[i - 1]:
#                 result += buff[i] - buff[i - 1]
#             elif buff[i] >= buff[i + 1]:
#                 result += buff[i]
#
#         else:
#             if buff[i] > buff[i - 1]:
#                 result += buff[i] - buff[i - 1]
#             else:
#                 result += buff[i]
#
#     print(result)
#
#
# func()


# второй способ

rom = input()
rom_dec = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
result = 0

for i in range(len(rom) - 1):
    if rom_dec[rom[i]] < rom_dec[rom[i + 1]]:
        result -= rom_dec[rom[i]]
    else:
        result += rom_dec[rom[i]]

result += rom_dec[rom[len(rom) - 1]]
print(result)