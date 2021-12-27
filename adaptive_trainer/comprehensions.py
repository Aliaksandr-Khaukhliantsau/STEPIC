# Не используя интерпретатор, отметьте все однозначно неправильные утверждения о содержимом переменных после
# выполнения этого кода:

dict1 = dict(zip(('a', 'b', 'c'), (1, 2, 3)))
range5 = list(range(5))
lst1 = [i
        for i in range5
        if i in dict1]
dict2 = {i: i*i for i in range5}
lst2 = [dict1[value] for value in dict1]
lst3 = [i
        for i in range5
        if i in lst2]

print(f'dict1 {dict1}\nrange5 {range5}\nlst1 {lst1}\ndict2 {dict2}\nlst2 {lst2}\nlst3 {lst3}')
