print('Comparação maior ou igual entre 2 número inteiros')
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
if n1 > n2:
    print('O número {} é maior que {}.'.format(n1, n2))
elif n2 > n1:
    print('O número {} é maior que {}.'.format(n2, n1))
else:
    print('Os números são iguais.')
