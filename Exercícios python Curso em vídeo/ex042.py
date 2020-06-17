print('Saber se valores formam triângulo equilátero, isósceles ou escaleno')
a = int(input('Digite o lado a: '))
b = int(input('Digite o lado b: '))
c = int(input('Digite o lado c: '))

if (a < b + c) and (b < a + c) and (c < a + b):
    print('As retas podem fomar um triângulo ', end='')
    if a == b == c:
        print('equilátero!')
    elif a == b or b == c or c == a:
        print('isósceles!')
    else:
        print('escaleno!')
else:
    print('As retas não podem formar um triângulo.')
