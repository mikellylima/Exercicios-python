print('Ler um número inteiro e dizer se é número primo')
n = int(input('Digite um número: '))
i = 0
for c in range(1, n+1):
    if n % c == 0:
        i = i + 1
if i == 2:
    print(f'O número {n} é primo!')
else:
    print(f'O número {n} não é primo!')
