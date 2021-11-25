# Суть задачи та же, что и Caesar cipher, с одним отличием: кодируются символы из интервала 1F600—1F64F таблицы
# символов Юникода. Используется кодировка UTF-8.
#
# Для всех символов сдвиг один и тот же. Сдвиг циклический, т.е. если к последнему символу алфавита применить
# единичный сдвиг, то он заменится на первый символ, и наоборот.
#
# Напишите программу, которая шифрует текст шифром Цезаря.
#
# Формат ввода: На первой строке указывается используемый сдвиг шифрования: целое число. Положительное число
# соответствует сдвигу вправо. На второй строке указывается непустая фраза для шифрования.
#
# Не обращайте внимания, если у вас отображаются прямоугольники вместо некоторых символов. Это значит, что ваш шрифт
# не содержит этих символов. Для решения задачи это не имеет никакого значения.
#
# Формат вывода: Единственная строка, в которой записана фраза: Result: "..." , где вместо многоточия внутри кавычек
# записана зашифрованная последовательность.
#
# Sample Input 1:
#
# 1
# 😀🙏😇
# Sample Output 1:
#
# Result: "😁😀😈"
# Sample Input 2:
#
# 1
# 😀😁😂😃😄😅😆😇😈😉😊😋😌😍😎😏😐😑😒😓😔😕😖😗😘😙😚😛😜😝😞😟😠😡😢😣😤😥😦😧😨😩😪😫😬😭😮😯😰😱😲😳😴😵😶😷😸😹😺😻😼😽😾😿🙀🙁🙂🙃🙄🙅🙆🙇🙈🙉🙊🙋🙌🙍🙎🙏
# Sample Output 2:
#
# Result: "😁😂😃😄😅😆😇😈😉😊😋😌😍😎😏😐😑😒😓😔😕😖😗😘😙😚😛😜😝😞😟😠😡😢😣😤😥😦😧😨😩😪😫😬😭😮😯😰😱😲😳😴😵😶😷😸😹😺😻😼😽😾😿🙀🙁🙂🙃🙄🙅🙆🙇🙈🙉🙊🙋🙌🙍🙎🙏😀"


def func(alpha, input_str, shift):
    result = ''
    i = 0
    while i <= len(input_str) - 1:
        symbol = (alpha.index(input_str[i]) + shift) % len(alpha)  # остаток от деления (например 100 % 80 = 20)
        result += alpha[symbol]
        i += 1
    print(f'Result: "{result}"')


# my_alpha = '😁😂😃😄😅😆😇😈😉😊😋😌😍😎😏😐😑😒😓😔😕😖😗😘😙😚😛😜😝😞😟😠😡😢😣😤😥😦😧😨😩😪😫😬😭😮😯😰😱😲😳😴😵😶😷😸😹😺😻😼😽😾😿🙀🙁🙂🙃🙄🙅🙆🙇🙈🙉🙊🙋🙌🙍🙎🙏😀'
my_alpha = ''.join([chr(i) for i in range(int(0x1f600), int(0x1f64f) + 1)])
input_1 = int(input())
input_2 = input()

func(my_alpha, input_2, input_1)
