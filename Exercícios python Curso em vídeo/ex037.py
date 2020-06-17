print('Conversão de decimal para binário, octal ou hexadecimal')
n = int(input('Digite um número inteiro: '))
print("""Escolha uma base de conversão:
1 - para binário
2 - para octal
3 - para hexadecimal""")
e = int(input('Digite a base de conversão escolhida: '))
if e == 1:
    conv = bin(n)[2:]
    print('O número {} convertido em binário é igual a {}'.format(n, conv))
elif e == 2:
    conv = oct(n)[2:]
    print('O número {} convertido em binário é igual a {}'.format(n, conv))
elif e == 3:
    conv = hex(n)[2:]
    print('O número {} convertido em binário é igual a {}'.format(n, conv))
else:
    print('Opção inválida! Tente novamente.')