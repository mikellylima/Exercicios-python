a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))
if a > b and a > c:
    if b > c:
        print('O maior número é {} e o menor número é {}'.format(a, c))
    else:
        print('O maior número é {} e o menor número é {}'.format(a, b))
if b > a and b > c:
    if a > c:
        print('O maior número é {} e o menor número é {}'.format(b, c))
    else:
        print('O maior número é {} e o menor número é {}'.format(b, a))
if c > a and c > b:
    if a > b:
        print('O maior número é {} e o menor número é {}'.format(c, b))
    else:
        print('O maior número é {} e o menor número é {}'.format(c, a))
if a == b or b == c or a == c:
    print('Um dos números é igual')