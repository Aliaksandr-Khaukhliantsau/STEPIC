# string_input = input()
# word_input = input()

string_input = 'QLGNAEKIRLRNGEAE'
word_input = 'KING'

print(string_input)
print(word_input)

sqrt = len(string_input) ** .5
print(sqrt)

is_int = sqrt.is_integer()

if sqrt.is_integer():
    sqrt = int(sqrt)

matrix = []
print(len(matrix))

a = 0
b = sqrt
for _ in range(sqrt):
    matrix.append(string_input[a:a + sqrt])
    a += sqrt

print(matrix)


def func_1(i):
    for k in matrix:
        for z in k:
            if i == z:
                w = matrix.index(k)
                q = k.index(i)
                return w, q


result = ()
for i in word_input:
    result += (func_1(i),)

print(result)
